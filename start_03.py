from dotenv import load_dotenv
import os
import requests

from start_01 import get_token, BASE_URL

load_dotenv()

appkey = os.getenv("appkey_01")
appsecret = os.getenv("appsecret_01")
account = os.getenv("account_01")


def split_account():

    if account is None:
        raise Exception(
            "account_01이 .env에 없습니다."
        )

    cano = account

    acnt_prdt_cd = "01"

    return cano, acnt_prdt_cd


def get_balance():

    print("잔고조회 시작")

    token = get_token()

    cano, acnt_prdt_cd = split_account()

    url = (
        f"{BASE_URL}"
        "/uapi/domestic-stock/v1/trading/inquire-balance"
    )

    headers = {
        "content-type": "application/json",
        "authorization": f"Bearer {token}",
        "appkey": appkey,
        "appsecret": appsecret,
        "tr_id": "VTTC8434R"
    }

    params = {
        "CANO": cano,
        "ACNT_PRDT_CD": acnt_prdt_cd,
        "AFHR_FLPR_YN": "N",
        "OFL_YN": "",
        "INQR_DVSN": "02",
        "UNPR_DVSN": "01",
        "FUND_STTL_ICLD_YN": "N",
        "FNCG_AMT_AUTO_RDPT_YN": "N",
        "PRCS_DVSN": "01",
        "CTX_AREA_FK100": "",
        "CTX_AREA_NK100": ""
    }

    print("잔고조회 요청")

    try:

        res = requests.get(
            url,
            headers=headers,
            params=params,
            timeout=30
        )

    except Exception as e:

        print("잔고조회 요청 실패")

        print(e)

        return None

    print("잔고조회 응답 도착")

    print(
        "status :",
        res.status_code
    )

    if res.status_code != 200:

        print(res.text)

        return None

    data = res.json()

    if data.get("rt_cd") != "0":

        print(
            data.get("msg1")
        )

        return None

    return data


def get_samsung_qty():

    print("삼성전자 수량 조회")

    data = get_balance()

    if data is None:

        return 0

    holdings = data.get(
        "output1",
        []
    )

    for item in holdings:

        if item.get("pdno") == "005930":

            qty = int(
                item.get(
                    "hldg_qty",
                    0
                )
            )

            print(
                f"보유수량 : {qty}"
            )

            return qty

    print("보유수량 : 0")

    return 0


if __name__ == "__main__":

    print(
        get_samsung_qty()
    )