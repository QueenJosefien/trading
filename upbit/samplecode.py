import time
import pyupbit
import datetime
# 계정
access = ""
secret = "" 
# 200ma
def get_ma200mo(ticker):
    df = pyupbit.get_ohlcv(ticker, interval="month", count=15)
    ma200mo = df['close'].rolling(200).mean().iloc[-1]
    return ma200mo
def get_ma200w(ticker):
    df = pyupbit.get_ohlcv(ticker, interval="week", count=15)
    ma200w = df['close'].rolling(200).mean().iloc[-1]
    return ma200w
def get_ma200d(ticker):
    df = pyupbit.get_ohlcv(ticker, interval="day", count=15)
    ma200d = df['close'].rolling(200).mean().iloc[-1]
    return ma200d
def get_ma200h4(ticker):
    df = pyupbit.get_ohlcv(ticker, interval="hour4", count=15)
    ma200h4 = df['close'].rolling(200).mean().iloc[-1]
    return ma200h4
def get_ma200h1(ticker):
    df = pyupbit.get_ohlcv(ticker, interval="hour1", count=15)
    ma200h1 = df['close'].rolling(200).mean().iloc[-1]
    return ma200h1
def get_ma200m30(ticker):
    df = pyupbit.get_ohlcv(ticker, interval="minute30", count=15)
    ma200m30 = df['close'].rolling(200).mean().iloc[-1]
    return ma200m30
def get_ma200m15(ticker):
    df = pyupbit.get_ohlcv(ticker, interval="minute15", count=15)
    ma200m15 = df['close'].rolling(200).mean().iloc[-1]
    return ma200m15
def get_ma200m5(ticker):
    df = pyupbit.get_ohlcv(ticker, interval="minute5", count=15)
    ma200m5 = df['close'].rolling(200).mean().iloc[-1]
    return ma200m5
def get_ma200m3(ticker):
    df = pyupbit.get_ohlcv(ticker, interval="minute3", count=15)
    ma200m3 = df['close'].rolling(200).mean().iloc[-1]
    return ma200m3
def get_ma200m1(ticker):
    df = pyupbit.get_ohlcv(ticker, interval="minute1", count=15)
    ma200m1 = df['close'].rolling(200).mean().iloc[-1]
    return ma200m1

ma200 = [get_ma200m1, get_ma200m3, get_ma200m5, get_ma200m15, get_ma200m30, get_ma200h1, get_ma200h4, get_ma200d, get_ma200w, get_ma200mo]

#목표가 설정
def get_target_price(ticker):
    df = pyupbit.get_ohlcv(ticker, interval="minute1", count=2)
    target_price = df.iloc[0]['ma200']
    return target_price
# 시작 시간 설정
def get_start_time(ticker):
    """시작 시간 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=1)
    start_time = df.index[0]
    return start_time
# 잔고조회
def get_balance(ticker):
    """잔고 조회"""
    balances = upbit.get_balances()
    for b in balances:
        if b['currency'] == ticker:
            if b['balance'] is not None:
                return float(b['balance'])
            else:
                return 0
    return 0
# 현재 가격 조회
def get_current_price(ticker):
    """현재가 조회"""
    return pyupbit.get_orderbook(ticker=ticker)["orderbook_units"][0]["ask_price"]


# 로그인
upbit = pyupbit.Upbit(access, secret)
print("autotrade start")
