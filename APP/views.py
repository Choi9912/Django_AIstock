import investpy
import matplotlib.pyplot as plt
import mpld3
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from keras.layers import LSTM, Dense
from keras.models import Sequential
from keras.callbacks import EarlyStopping
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# DataFetcher Class
class DataFetcher:
    @staticmethod
    def get_stock_data(stock_symbol, country, from_date, to_date):
        return investpy.get_stock_historical_data(stock_symbol, country=country, from_date=from_date, to_date=to_date)


# StockPlotter Class
class StockPlotter:
    @staticmethod
    def plot_stock_data(df):
        plt.figure(figsize=(18, 9))
        plt.plot(df.index, (df['Low'] + df['High']) / 2.0)
        plt.xticks(df.iloc[::50, :].index, rotation=45)
        plt.xlabel('Date', fontsize=18)
        plt.ylabel('Mid Price', fontsize=18)

    @staticmethod
    def plot_predictions(y_test_df, y_pred_df):
        ax1 = y_test_df.plot()
        y_pred_df.plot(ax=ax1)
        plt.legend(['테스트', '예측'])
        mpld3.show()


# DataPreparer Class
class DataPreparer:
    def __init__(self, x5_short, x5_long):
        self.x5_short = x5_short
        self.x5_long = x5_long
        self.scaler = MinMaxScaler()

    def prepare_data(self, stock_data, split_date):
        stock_price_close = stock_data[['Close']]
        train_data = pd.DataFrame(stock_price_close.loc[:split_date, ['Close']])
        test_data = pd.DataFrame(stock_price_close.loc[split_date:, ['Close']])

        train_data_sc = self.scaler.fit_transform(train_data)
        test_data_sc = self.scaler.transform(test_data)

        train_sc_df = pd.DataFrame(train_data_sc, columns=['Scaled'], index=train_data.index)
        test_sc_df = pd.DataFrame(test_data_sc, columns=['Scaled'], index=test_data.index)

        for i in range(1, (max(self.x5_short, self.x5_long) + 1)):
            train_sc_df['Scaled_{}'.format(i)] = train_sc_df['Scaled'].shift(i)
            test_sc_df['Scaled_{}'.format(i)] = test_sc_df['Scaled'].shift(i)

        x_train_short = train_sc_df.dropna().drop('Scaled', axis=1).iloc[:, :self.x5_short].values
        y_train_short = train_sc_df.dropna()[['Scaled']].values
        x_test_short = test_sc_df.dropna().drop('Scaled', axis=1).iloc[:, :self.x5_short].values
        y_test_short = test_sc_df.dropna()[['Scaled']].values

        x_train_long = train_sc_df.dropna().drop('Scaled', axis=1).iloc[:, :self.x5_long].values
        y_train_long = train_sc_df.dropna()[['Scaled']].values
        x_test_long = test_sc_df.dropna().drop('Scaled', axis=1).iloc[:, :self.x5_long].values
        y_test_long = test_sc_df.dropna()[['Scaled']].values

        x_train_short_t = x_train_short.reshape(x_train_short.shape[0], self.x5_short, 1)
        x_test_short_t = x_test_short.reshape(x_test_short.shape[0], self.x5_short, 1)

        x_train_long_t = x_train_long.reshape(x_train_long.shape[0], self.x5_long, 1)
        x_test_long_t = x_test_long.reshape(x_test_long.shape[0], self.x5_long, 1)

        return (x_train_short_t, y_train_short, x_test_short_t, y_test_short,
                x_train_long_t, y_train_long, x_test_long_t, y_test_long, test_sc_df)


# LSTMModel Class
class LSTMModel:
    def __init__(self, x5):
        self.model = Sequential()
        self.model.add(LSTM(64, return_sequences=True, input_shape=(x5, 1)))
        self.model.add(LSTM(32, return_sequences=False))
        self.model.add(Dense(1, activation='linear'))
        self.model.compile(loss='mean_squared_error', optimizer='adam')

    def train(self, x_train_t, y_train, epochs=50, batch_size=20):
        early_stop = EarlyStopping(monitor='loss', patience=5, verbose=1)
        self.model.fit(x_train_t, y_train, epochs=epochs, batch_size=batch_size, verbose=1, callbacks=[early_stop])

    def predict(self, x_test_t):
        return self.model.predict(x_test_t)


# Django Views
@login_required
def maker(request):
    return render(request, 'maker.html')


@login_required
def index(request):
    return render(request, 'index.html')


@login_required
def predict(request):
    x1 = request.GET.get('x1', '0')
    x2 = request.GET.get('x2', '0')
    x3 = request.GET.get('x3', '0')
    x4 = request.GET.get('x4', '0')
    x5_short = int(request.GET.get('x5_short', '0'))
    x5_long = int(request.GET.get('x5_long', '0'))
    prediction_type = request.GET.get('prediction_type', 'short')

    stock_data = DataFetcher.get_stock_data(x1, x2, x3, x4)
    StockPlotter.plot_stock_data(stock_data)

    split_date = pd.Timestamp('01-01-2019')
    data_preparer = DataPreparer(x5_short, x5_long)
    (x_train_short_t, y_train_short, x_test_short_t, y_test_short,
     x_train_long_t, y_train_long, x_test_long_t, y_test_long, test_sc_df) = data_preparer.prepare_data(stock_data, split_date)

    if prediction_type == 'short':
        lstm_model = LSTMModel(x5_short)
        x_train_t = x_train_short_t
        y_train = y_train_short
        x_test_t = x_test_short_t
    else:
        lstm_model = LSTMModel(x5_long)
        x_train_t = x_train_long_t
        y_train = y_train_long
        x_test_t = x_test_long_t

    lstm_model.train(x_train_t, y_train)
    y_pred = lstm_model.predict(x_test_t)

    t_df = test_sc_df.dropna()
    y_test_df = pd.DataFrame(y_train, columns=['close'], index=t_df.index)
    y_pred_df = pd.DataFrame(y_pred, columns=['close'], index=t_df.index)

    StockPlotter.plot_predictions(y_test_df, y_pred_df)

    return render(request, 'predict.html')
