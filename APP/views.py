import pandas as pd
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from datetime import datetime
from sklearn.metrics import mean_squared_error, mean_absolute_error
from .data_fetcher import DataFetcher
from .stock_plotter import StockPlotter
from .data_preparer import DataPreparer
from .lstm_model import LSTMModel


def convert_date_format(date_string):
    date_object = datetime.strptime(date_string, "%d/%m/%Y")
    return date_object.strftime("%d/%m/%Y")


@login_required
def predict(request):
    x1 = request.GET.get("x1", "0")
    x2 = request.GET.get("x2", "0")
    x3 = convert_date_format(request.GET.get("x3", "0"))
    x4 = convert_date_format(request.GET.get("x4", "0"))
    x5_short = int(request.GET.get("x5_short", "0"))
    x5_long = int(request.GET.get("x5_long", "0"))
    prediction_type = request.GET.get("prediction_type", "short")

    try:
        stock_data = DataFetcher.get_stock_data(x1, x2, x3, x4)
        data_preparer = DataPreparer(x5_short, x5_long)
        prepared_data = data_preparer.prepare_data(stock_data, split_date)

        lstm_model = LSTMModel(
            input_shape=(
                x5_short if prediction_type == "short" else x5_long,
                prepared_data[0].shape[2],
            )
        )
        lstm_model.train(prepared_data[0], prepared_data[1])

        y_pred = lstm_model.predict(prepared_data[2])
        y_pred_original = data_preparer.scaler.inverse_transform(y_pred)

        actual_df = stock_data[stock_data["Date"] > split_date].set_index("Date")
        train_df = stock_data[stock_data["Date"] <= split_date].set_index("Date")
        pred_df = pd.DataFrame(
            y_pred_original,
            columns=["Close"],
            index=actual_df.index[: len(y_pred_original)],
        )

        plot_html = StockPlotter.plot_predictions_with_actual(
            actual_df, train_df, pred_df
        )

        context = {
            "plot_html": plot_html,
            "mse": mean_squared_error(
                actual_df["Close"][: len(y_pred_original)], y_pred_original
            ),
            "mae": mean_absolute_error(
                actual_df["Close"][: len(y_pred_original)], y_pred_original
            ),
        }

        return render(request, "predict.html", context)

    except Exception as e:
        error_message = str(e)
        return render(request, "error.html", {"error_message": error_message})


@login_required
def maker(request):
    return render(request, "maker.html")


@login_required
def index(request):
    return render(request, "index.html")
