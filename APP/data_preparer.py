import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler


class DataPreparer:
    def __init__(self, x5_short, x5_long):
        self.x5_short = x5_short
        self.x5_long = x5_long
        self.scaler = MinMaxScaler()

    def add_technical_indicators(self, df):
        # 단순 이동평균 (SMA)
        df["SMA_20"] = df["Close"].rolling(window=20).mean()

        # 상대강도지수 (RSI)
        delta = df["Close"].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
        rs = gain / loss
        df["RSI"] = 100 - (100 / (1 + rs))

        # 이동평균수렴확산지수 (MACD)
        exp1 = df["Close"].ewm(span=12, adjust=False).mean()
        exp2 = df["Close"].ewm(span=26, adjust=False).mean()
        df["MACD"] = exp1 - exp2
        df["MACD_Signal"] = df["MACD"].ewm(span=9, adjust=False).mean()

        return df

    def prepare_data(self, stock_data, split_date):
        stock_data = self.add_technical_indicators(stock_data)
        stock_price_close = stock_data[["Close"]]
        train_data = pd.DataFrame(stock_price_close.loc[:split_date, ["Close"]])
        test_data = pd.DataFrame(stock_price_close.loc[split_date:, ["Close"]])

        train_data_sc = self.scaler.fit_transform(train_data)
        test_data_sc = self.scaler.transform(test_data)

        train_sc_df = pd.DataFrame(
            train_data_sc, columns=["Scaled"], index=train_data.index
        )
        test_sc_df = pd.DataFrame(
            test_data_sc, columns=["Scaled"], index=test_data.index
        )

        for i in range(1, (max(self.x5_short, self.x5_long) + 1)):
            train_sc_df[f"Scaled_{i}"] = train_sc_df["Scaled"].shift(i)
            test_sc_df[f"Scaled_{i}"] = test_sc_df["Scaled"].shift(i)

        x_train_short = (
            train_sc_df.dropna().drop("Scaled", axis=1).iloc[:, : self.x5_short].values
        )
        y_train_short = train_sc_df.dropna()[["Scaled"]].values
        x_test_short = (
            test_sc_df.dropna().drop("Scaled", axis=1).iloc[:, : self.x5_short].values
        )
        y_test_short = test_sc_df.dropna()[["Scaled"]].values

        x_train_long = (
            train_sc_df.dropna().drop("Scaled", axis=1).iloc[:, : self.x5_long].values
        )
        y_train_long = train_sc_df.dropna()[["Scaled"]].values
        x_test_long = (
            test_sc_df.dropna().drop("Scaled", axis=1).iloc[:, : self.x5_long].values
        )
        y_test_long = test_sc_df.dropna()[["Scaled"]].values

        x_train_short_t = x_train_short.reshape(
            x_train_short.shape[0], self.x5_short, 1
        )
        x_test_short_t = x_test_short.reshape(x_test_short.shape[0], self.x5_short, 1)

        x_train_long_t = x_train_long.reshape(x_train_long.shape[0], self.x5_long, 1)
        x_test_long_t = x_test_long.reshape(x_test_long.shape[0], self.x5_long, 1)

        return (
            x_train_short_t,
            y_train_short,
            x_test_short_t,
            y_test_short,
            x_train_long_t,
            y_train_long,
            x_test_long_t,
            y_test_long,
            test_sc_df,
        )
