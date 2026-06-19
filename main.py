import time
from datetime import datetime

from start_02 import get_current_price
from start_03 import get_samsung_qty
from start_04 import buy_order
from start_05 import sell_order
from excel import save_trade

print("자동매매 시작")

while True:

    print("\n======================")
    print(datetime.now())
    print("======================")

    price = get_current_price("005930")

    if price is None:

        print("현재가 조회 실패")

        time.sleep(30)

        continue

    qty = get_samsung_qty()

    print(
        f"현재 보유 수량 : {qty}"
    )

    save_trade(
        stock_code="005930",
        price=price,
        qty=qty,
        action="조회"
    )

    if qty == 0:

        buy_price = price - 1000

        print(
            f"\n매수 주문가 : {buy_price}"
        )

        buy_order(
            stock_code="005930",
            price=buy_price,
            qty=1
        )

        qty_after = get_samsung_qty()

        save_trade(
            stock_code="005930",
            price=buy_price,
            qty=qty_after,
            action="매수주문"
        )

        print(
            f"주문 후 보유 수량 : {qty_after}"
        )

    else:

        sell_price = price + 1000

        print(
            f"\n매도 주문가 : {sell_price}"
        )

        sell_order(
            stock_code="005930",
            price=sell_price,
            qty=1
        )

        qty_after = get_samsung_qty()

        save_trade(
            stock_code="005930",
            price=sell_price,
            qty=qty_after,
            action="매도주문"
        )

        print(
            f"주문 후 보유 수량 : {qty_after}"
        )

    print("\n30초 대기")

    time.sleep(30)