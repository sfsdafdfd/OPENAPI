from dotenv import load_dotenv
import os
import requests

from start_01 import get_token, BASE_URL

load_dotenv()

appkey = os.getenv("appkey_01")
appsecret = os.getenv("appsecret_01")


def get_current_price(stock_code="005930"):

    token = get_token()

    url = f"{BASE_URL}/uapi/domestic-stock/v1/quotations/inquire-price"

    headers = {
        "content-type": "application/json",
        "authorization": f"Bearer {token}",
        "appkey": appkey,
        "appsecret": appsecret,
        "tr_id": "FHKST01010100"
    }

    params = {
        "FID_COND_MRKT_DIV_CODE": "J",
        "FID_INPUT_ISCD": stock_code
    }

    res = requests.get(
        url,
        headers=headers,
        params=params,
        timeout=10
    )

    print("status :", res.status_code)

    if res.status_code != 200:
        print(res.text)
        return None

    data = res.json()

    print("\n응답 데이터:")
    print(data)

    try:
        price = int(data["output"]["stck_prpr"])

        print(f"\n삼성전자 현재가 : {price}원")

        return price

    except Exception as e:
        print("\n현재가 파싱 실패")
        print(e)
        print(data)

        return None


if __name__ == "__main__":
    get_current_price("005930")