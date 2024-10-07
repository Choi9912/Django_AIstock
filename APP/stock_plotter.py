import matplotlib.pyplot as plt
import mpld3


class StockPlotter:
    @staticmethod
    def plot_predictions_with_actual(actual_df, train_df, pred_df):
        plt.figure(figsize=(18, 9))
        plt.plot(actual_df.index, actual_df["Close"], label="실제 가격")
        plt.plot(train_df.index, train_df["Close"], label="학습 데이터")
        plt.plot(pred_df.index, pred_df["Close"], label="예측 가격")
        plt.xlabel("날짜")
        plt.ylabel("주가")
        plt.title("주가 예측 결과")
        plt.legend()
        return mpld3.fig_to_html(plt.gcf())
