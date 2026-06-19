from dotenv import load_dotenv
import os
import json
import requests

from start_01 import get_token, BASE_URL

load_dotenv()

appkey = os.getenv("appkey_01")
appsecret = os.getenv("appsecret_01")
account = os.getenv("account_01")


def split_account():

    cano = account
    acnt_prdt_cd = "01"

    return cano, acnt_prdt_cd


def sell_order(stock_code, price, qty):

    token = get_token()

    cano, acnt_prdt_cd = split_account()

    url = f"{BASE_URL}/uapi/domestic-stock/v1/trading/order-cash"

    headers = {
        "content-type": "application/json",
        "authorization": f"Bearer {token}",
        "appkey": appkey,
        "appsecret": appsecret,
        "tr_id": "VTTC0801U"
    }

    body = {
        "CANO": cano,
        "ACNT_PRDT_CD": acnt_prdt_cd,
        "PDNO": stock_code,
        "ORD_DVSN": "00",
        "ORD_QTY": str(qty),
        "ORD_UNPR": str(price)
    }

    print("\n[매도 주문]")
    print(body)

    res = requests.post(
        url,
        headers=headers,
        data=json.dumps(body),
        timeout=10
    )

    print("status :", res.status_code)

    data = res.json()

    print("\n응답:")
    print(data)

    return data


if __name__ == "__main__":

    sell_order(
        stock_code="005930",
        price=363500,
        qty=1
    )