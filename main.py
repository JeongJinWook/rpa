import pywinmacro as pw
import time
import random

location1 = (354, 54) #주소창
location2 = (843, 96) #종목 검색창
location3 = (1525, 777) #일자별 시세 +버튼
location4 = (1519, 335) #다운로드 버튼
location5 = (1319, 443) #엑셀 버튼
location6 = (1902, 1009) #크롬 다운로드창 끄는 버튼


#보유종목 리스트
stocks = ["강원랜드", "리노공업", "에스에프에이", "NHN한국사이버결제"]


#크롬 열려있는 상태에서 KRX 정보데이터시스템 접속 함수
def go_to_krx_data():
    #주소창 클릭
    pw.click(location1)
    time.sleep(1)
    #한국거래소 정보데이터 시스템 주소 입력
    pw.type_in("http://data.krx.co.kr/contents/MDC/MAIN/main/index.cmd")
    time.sleep(0.5)
    #엔터키
    pw.key_press_once('enter')
    time.sleep(3)


#주가 정보를 다운받는 함수
def price(ticker):
    #검색창 클릭
    pw.click(location2)
    time.sleep(random.randint(3, 5))
    #티커코드 입력
    pw.type_in(ticker)
    time.sleep(random.randint(3, 5))
    #엔터
    pw.key_press_once('enter')
    time.sleep(random.randint(5, 7))
    #일자별 시세 + 버튼 클릭
    pw.click(location3)
    time.sleep(random.randint(3, 5))
    #Download 버튼 클릭
    pw.click(location4)
    time.sleep(random.randint(1, 3))
    #엑셀 버튼 클릭
    pw.click(location5)
    time.sleep(random.randint(2, 3))
    pw.click(location6)
    time.sleep(random.randint(1, 3))


# 보유종목 리스트에 저장된 종목들의 주가 조회
def get_price_data(stocks):
    for stock in stocks:
        #개별종목 주가 조회
        price(stock)
        time.sleep(random.randint(3, 5))


go_to_krx_data()
get_price_data(stocks)