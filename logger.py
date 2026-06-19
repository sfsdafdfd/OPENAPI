import csv
import os
from datetime import datetime

LOG_FILE = "trade_log.csv"


def write_log(action, stock, price, qty, result):

    file_exists = os.path.exists(LOG_FILE)

    with open(
        LOG_FILE,
        "a",
        newline="",
        encoding="utf-8-sig"
    ) as f:

        writer = csv.writer(f)

        if not file_exists:
            writer.writerow([
                "time",
                "action",
                "stock",
                "price",
                "qty",
                "result"
            ])

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            action,
            stock,
            price,
            qty,
            result
        ])