from dotenv import load_dotenv
import os
import json
import requests
from datetime import datetime

load_dotenv()

appkey = os.getenv("appkey_01")
appsecret = os.getenv("appsecret_01")
print("appkey:", appkey)
print("appsecret:", appsecret)

TOKEN_FILE = "token_cache.json"

# 모의투자 서버
BASE_URL = "https://openapivts.koreainvestment.com:29443"


def load_token():
    try:
        with open(TOKEN_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)

        today = datetime.now().strftime("%Y-%m-%d")

        if data.get("date") == today and data.get("access_token"):
            print("[TOKEN] 기존 토큰 사용")
            return data.get("access_token")

    except:
        pass

    return None


def save_token(token):
    data = {
        "access_token": token,
        "date": datetime.now().strftime("%Y-%m-%d")
    }

    with open(TOKEN_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def get_token():

    cached_token = load_token()

    if cached_token:
        return cached_token

    print("[TOKEN] 새 토큰 발급")

    url = f"{BASE_URL}/oauth2/tokenP"

    headers = {
        "content-type": "application/json"
    }

    body = {
        "grant_type": "client_credentials",
        "appkey": appkey,
        "appsecret": appsecret
    }

    res = requests.post(
        url,
        headers=headers,
        data=json.dumps(body),
        timeout=10
    )

    print("status :", res.status_code)

    if res.status_code != 200:
        print(res.text)
        raise Exception("토큰 발급 실패")

    data = res.json()
    token = data["access_token"]

    save_token(token)

    print("[TOKEN] 저장 완료")

    return token


if __name__ == "__main__":

    token = get_token()

    print("\n발급 토큰:")
    print(token)