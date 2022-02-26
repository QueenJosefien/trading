from pyupbit import WebSocketManager
import pyupbit
#로그인
access = "JG5PmRwtSp3emHMesXoVqRI5FoVIH6vGripDWbdE"          # 본인 값으로 변경
secret = "CnMdUobIlQxhfeKGaeEfRGKYjRmBcxHWlxuqsKi7"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

#잔고조회
print(upbit.get_balance("KRW-ATOM"))     # KRW-ATOM 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회
print(upbit.get_balances()) # 전체 잔고조회

# 매도
print(upbit.sell_limit_order("KRW-XRP", 600, 20)) # 리플을 600원에 20개 매도

# 매수
print(upbit.buy_limit_order("KRW-XRP", 613, 10)) # 리플을 613원에 10개 매수

#시장가
print(upbit.buy_market_order("KRW-XRP", 10000)) # 리플을 시장가로 1만원어치 구매
print(upbit.sell_market_order("KRW-XRP", 30)) # 리플을 시장가로 30개 매도

#미체결 주문조회
upbit.get_order("KRW-LTC") #라이트 코인 미체결 주문조회

#체결된 주문조회
print(upbit.get_order("KRW-LTC", state="done")) #라이트 코인 오더중 체결된 오더 리스트조회

# 체결/미체결 주문을 조회후 주문 상세 내역조회 
order = upbit.get_order('uuid')
print(order) #주문의 uuid를 입력하여 조회할 수 있음

# 미체결 오더취소
print(upbit.cancel_order('uuid')) # 미체결 주문의 uuid를 입력해서 취소한다.

# 현재가, 호가, 체결가 불러오기

if __name__ == "__main__":
    wm = WebSocketManager("ticker", ["KRW-BTC"])
    for i in range(10):
        data = wm.get()
        print(data)
    wm.terminate()

# 현재 가격
print(pyupbit.get_current_price("KRW-BTC"))
print(pyupbit.get_current_price(["KRW-BTC", "KRW-XRP"]))

# 고가/시가/저가/종가/거래량을 DataFrame으로 반환
# ohlcv 란 : open, high, low, close, volume 을 요약한 말임
df = pyupbit.get_ohlcv("KRW-BTC")
print(df.tail())
# 예 : 2021-03-25 09:00:00  64777000.0  65305000.0  63319000.0  64257000.0   2770.703203 고/시/저/종/거래량 순으로 정렬
df = pyupbit.get_ohlcv("KRW-BTC", count=5) # 최근 5일까지로 출력 날짜 갯수 지정
df = pyupbit.get_ohlcv("KRW-BTC", count=600, period=1) # 기본 200개이며 그 이상일경우 갯수를 지정해준다. 1은 1초단위라는 뜻
print(len(df))

#캔들 조회단위 지정
print(pyupbit.get_ohlcv("KRW-BTC", interval="day"))              # 일봉 데이터 (5일)
print(pyupbit.get_ohlcv("KRW-BTC", interval="minute1"))         # 분봉 데이터
print(pyupbit.get_ohlcv("KRW-BTC", interval="week"))            # 주봉 데이터

#이전 캔들 데이터 얻기
print(pyupbit.get_ohlcv("KRW-BTC", to="20201010")) # 2020년 10월 9일까지 데이터 수집함, 별도 설정없으면 일봉기준
print(pyupbit.get_ohlcv("KRW-BTC", interval="minute1", to="20201010")) # (2020-10-09 23:59:00)까지의 200개 데이터를 출력

# 호가창 불러오기
print(pyupbit.get_orderbook(ticker="KRW-BTC"))
# market : 암호화폐 티커
# timestamp : 조회시간 (단위 ms)
# orderbook_units : 매도호가/매수호가 정보
print(pyupbit.get_orderbook(tickers=["KRW-BTC", "KRW-XRP"])) # 비트랑 리플 둘다 조회하기











