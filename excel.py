import xlwings as xw
from datetime import datetime


def save_trade(
    stock_code,
    price,
    qty,
    action
):

    wb = xw.Book("주식투자.xlsx")

    sheet = wb.sheets[0]

    if sheet.range("A1").value is None:

        sheet.range("A1").value = "시간"
        sheet.range("B1").value = "종목코드"
        sheet.range("C1").value = "현재가"
        sheet.range("D1").value = "보유수량"
        sheet.range("E1").value = "동작"

    last_row = sheet.used_range.last_cell.row

    next_row = last_row + 1

    sheet.range(f"A{next_row}").value = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    sheet.range(f"B{next_row}").value = stock_code

    sheet.range(f"C{next_row}").value = price

    sheet.range(f"D{next_row}").value = qty

    sheet.range(f"E{next_row}").value = action

    wb.save()

    print(
        f"[EXCEL 저장] {stock_code} {price} {qty} {action}"
    )