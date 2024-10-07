import investpy
import time
import random


class DataFetcher:
    @staticmethod
    def get_stock_data(stock_symbol, country, from_date, to_date):
        max_retries = 5
        for i in range(max_retries):
            try:
                data = investpy.get_stock_historical_data(
                    stock=stock_symbol,
                    country=country,
                    from_date=from_date,
                    to_date=to_date,
                    as_json=False,
                    order="ascending",
                    interval="Daily",
                )
                return data.reset_index()
            except Exception as e:
                if i < max_retries - 1:
                    time.sleep(random.uniform(1, 5))
                    continue
                else:
                    raise e
