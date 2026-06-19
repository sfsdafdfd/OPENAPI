#Korea Investment OpenAPI Auto Trading

# 프로젝트 소개

한국투자증권 OpenAPI를 이용한 삼성전자(005930) 자동매매 프로그램입니다.

모의투자 환경에서 REST API를 사용하여 현재가 조회, 보유 종목 조회, 매수/매도 주문을 수행하며 거래 내역을 Excel 파일에 저장했습니다.

# 주요 기능

* Access Token 발급 및 재사용
* 삼성전자(005930) 현재가 조회
* 보유 수량 조회
* 매수 주문
* 매도 주문
* 자동 반복 매매
* 거래 내역 Excel 저장

# 프로젝트 구조

* start_01.py : 토큰 발급 및 관리
* start_02.py : 현재가 조회
* start_03.py : 보유 종목 조회
* start_04.py : 매수 주문
* start_05.py : 매도 주문
* main.py : 자동매매 실행
* excel.py : Excel 저장 기능
* logger.py : 로그 관리

# 사용 기술

* Python
* Requests
* Python-dotenv
* Xlwings
* Korea Investment OpenAPI

# 실행 방법

1. 필요한 라이브러리 설치

pip install requests python-dotenv xlwings

2. .env 파일 생성

appkey_01=YOUR_APPKEY

appsecret_01=YOUR_APPSECRET

account_01=YOUR_ACCOUNT

3. 프로그램 실행

python main.py

## 매매

1. 삼성전자 현재가 조회
2. 보유 수량 조회
3. 보유 수량이 없으면 현재가 - 1000원에 매수 주문
4. 보유 수량이 있으면 현재가 + 1000원에 매도 주문
5. 결과를 Excel 파일에 저장
6. 반복 실행

# 참고

본 프로젝트는 한국투자증권 OpenAPI 모의투자 환경을 기준으로 작성되었습니다.
