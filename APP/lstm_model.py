from keras.layers import LSTM, Dense
from keras.models import Sequential
from keras.callbacks import EarlyStopping


class LSTMModel:
    def __init__(self, input_shape):
        self.model = Sequential(
            [
                LSTM(64, return_sequences=True, input_shape=input_shape),
                LSTM(32, return_sequences=False),
                Dense(16, activation="relu"),
                Dense(1, activation="linear"),
            ]
        )
        self.model.compile(loss="mean_squared_error", optimizer="adam")

    def train(self, x_train_t, y_train, epochs=50, batch_size=20):
        early_stop = EarlyStopping(monitor="loss", patience=5, verbose=1)
        self.model.fit(
            x_train_t,
            y_train,
            epochs=epochs,
            batch_size=batch_size,
            verbose=1,
            callbacks=[early_stop],
        )

    def predict(self, x_test_t):
        return self.model.predict(x_test_t)
