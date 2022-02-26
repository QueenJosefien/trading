import time
import pyupbit
from datetime import *
import openpyxl

class MA:
    def __init__(self, open, close, count, rolling):
        self.open = open
        self.close = close
        self.count = count
        self.rolling = rolling
 # 1분당       
    def get_mam17(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="minute1", count=200)
        mam17 = df['close'].rolling(7).mean().iloc[-1]
        return mam17
    def get_mam114(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="minute1", count=200)
        mam114 = df['close'].rolling(14).mean().iloc[-1]
        return mam114
    def get_emam121(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="minute1", count=200)
        mam121 = df['close'].rolling(21).mean().iloc[-1]
        return mam121
    def get_mam134(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="minute1", count=200)
        mam134 = df['close'].rolling(34).mean().iloc[-1]
        return mam134
    def get_mam160(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="minute1", count=200)
        mam160 = df['close'].rolling(60).mean().iloc[-1]
        return mam160
    def get_mam1120(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="minute1", count=200)
        mam1120 = df['close'].rolling(120).mean().iloc[-1]
        return mam1120
    def get_mam1180(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="minute1", count=200)
        mam1180 = df['close'].rolling(180).mean().iloc[-1]
        return mam1180
    def get_mam1200(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="minute1", count=200)
        mam1200 = df['close'].rolling(200).mean().iloc[-1]
        return mam1200

# 5분당   
    def get_mam57(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="minute5", count=200)
        mam57 = df['close'].rolling(7).mean().iloc[-1]
        return mam57
    def get_mam514(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="minute5", count=200)
        mam514 = df['close'].rolling(14).mean().iloc[-1]
        return mam514
    def get_mam521(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="minute5", count=200)
        mam521 = df['close'].rolling(21).mean().iloc[-1]
        return mam521
    def get_mam534(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="minute5", count=200)
        mam534 = df['close'].rolling(34).mean().iloc[-1]
        return mam534
    def get_mam560(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="minute5", count=200)
        mam560 = df['close'].rolling(60).mean().iloc[-1]
        return mam560
    def get_mam5120(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="minute5", count=200)
        mam5120 = df['close'].rolling(120).mean().iloc[-1]
        return mam5120
    def get_mam5180(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="minute5", count=200)
        mam5180 = df['close'].rolling(180).mean().iloc[-1]
        return mam5180
    def get_mam5200(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="minute5", count=200)
        mam5200 = df['close'].rolling(200).mean().iloc[-1]
        return mam5200

# 15분당   
    def get_mam157(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="minute15", count=200)
        mam157 = df['close'].rolling(7).mean().iloc[-1]
        return mam157
    def get_mam1514(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="minute15", count=200)
        mam1514 = df['close'].rolling(14).mean().iloc[-1]
        return mam1514
    def get_mam1521(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="minute15", count=200)
        mam1521 = df['close'].rolling(21).mean().iloc[-1]
        return mam1521
    def get_mam1534(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="minute15", count=200)
        mam1534 = df['close'].rolling(34).mean().iloc[-1]
        return mam1534
    def get_mam1560(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="minute15", count=200)
        mam1560 = df['close'].rolling(60).mean().iloc[-1]
        return mam1560
    def get_mam15120(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="minute15", count=200)
        mam15120 = df['close'].rolling(120).mean().iloc[-1]
        return mam15120
    def get_mam15180(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="minute15", count=200)
        mam15180 = df['close'].rolling(180).mean().iloc[-1]
        return mam15180
    def get_mam15200(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="minute15", count=200)
        mam15200 = df['close'].rolling(200).mean().iloc[-1]
        return mam15200

# 30분당   
    def get_mam307(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="minute30", count=200)
        mam307 = df['close'].rolling(7).mean().iloc[-1]
        return mam307
    def get_mam3014(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="minute30", count=200)
        mam3014 = df['close'].rolling(14).mean().iloc[-1]
        return mam3014
    def get_mam3021(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="minute30", count=200)
        mam3021 = df['close'].rolling(21).mean().iloc[-1]
        return mam3021
    def get_mam3034(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="minute30", count=200)
        mam3034 = df['close'].rolling(34).mean().iloc[-1]
        return mam3034
    def get_mam3060(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="minute30", count=200)
        mam3060 = df['close'].rolling(60).mean().iloc[-1]
        return mam3060
    def get_mam30120(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="minute30", count=200)
        mam30120 = df['close'].rolling(120).mean().iloc[-1]
        return mam30120
    def get_mam30180(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="minute30", count=200)
        mam30180 = df['close'].rolling(180).mean().iloc[-1]
        return mam30180
    def get_mam30200(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="minute30", count=200)
        mam30200 = df['close'].rolling(200).mean().iloc[-1]
        return mam30200

 # 1시간당   
    def get_mah17(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="hour1", count=200)
        mah17 = df['close'].rolling(7).mean().iloc[-1]
        return mah17
    def get_mah114(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="hour1", count=200)
        mah114 = df['close'].rolling(14).mean().iloc[-1]
        return mah114
    def get_mah121(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="hour1", count=200)
        mah121 = df['close'].rolling(21).mean().iloc[-1]
        return mah121
    def get_mah134(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="hour1", count=200)
        mah134 = df['close'].rolling(34).mean().iloc[-1]
        return mah134
    def get_mah160(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="hour1", count=200)
        mah160 = df['close'].rolling(60).mean().iloc[-1]
        return mah160
    def get_mah1120(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="hour1", count=200)
        mah1120 = df['close'].rolling(120).mean().iloc[-1]
        return mah1120
    def get_mah1180(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="hour1", count=200)
        mah1180 = df['close'].rolling(180).mean().iloc[-1]
        return mah1180
    def get_mah1200(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="hour1", count=200)
        mah1200 = df['close'].rolling(200).mean().iloc[-1]
        return mah1200
    
 # 4시간당   
    def get_mah47(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="hour4", count=200)
        mah47 = df['close'].rolling(7).mean().iloc[-1]
        return mah47
    def get_mah414(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="hour4", count=200)
        mah414 = df['close'].rolling(14).mean().iloc[-1]
        return mah414
    def get_mah421(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="hour4", count=200)
        mah421 = df['close'].rolling(21).mean().iloc[-1]
        return mah421
    def get_mah434(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="hour4", count=200)
        mah434 = df['close'].rolling(34).mean().iloc[-1]
        return mah434
    def get_mah460(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="hour4", count=200)
        mah460 = df['close'].rolling(60).mean().iloc[-1]
        return mah460
    def get_mah4120(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="hour4", count=200)
        mah4120 = df['close'].rolling(120).mean().iloc[-1]
        return mah4120
    def get_mah4180(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="hour4", count=200)
        mah4180 = df['close'].rolling(180).mean().iloc[-1]
        return mah4180
    def get_mah4200(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="hour4", count=200)
        mah4200 = df['close'].rolling(200).mean().iloc[-1]
        return mah4200
    
 # 일봉
    def get_mad7(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="day", count=200)
        mad7 = df['close'].rolling(7).mean().iloc[-1]
        return mad7
    def get_mad14(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="day", count=200)
        mad14 = df['close'].rolling(14).mean().iloc[-1]
        return mad14
    def get_mad21(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="day", count=200)
        mad21 = df['close'].rolling(21).mean().iloc[-1]
        return mad21
    def get_mad34(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="day", count=200)
        mad34 = df['close'].rolling(34).mean().iloc[-1]
        return mad34
    def get_mad60(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="day", count=200)
        mad60 = df['close'].rolling(60).mean().iloc[-1]
        return mad60
    def get_mad120(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="day", count=200)
        mad120 = df['close'].rolling(120).mean().iloc[-1]
        return mad120
    def get_mad180(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="day", count=200)
        mad180 = df['close'].rolling(180).mean().iloc[-1]
        return mad180
    def get_mad200(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="day", count=200)
        mad200 = df['close'].rolling(200).mean().iloc[-1]
        return mad200
    
 # 주봉
    def get_maw7(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="week", count=200)
        maw7 = df['close'].rolling(7).mean().iloc[-1]
        return maw7
    def get_maw14(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="week", count=200)
        maw14 = df['close'].rolling(14).mean().iloc[-1]
        return maw14
    def get_maw21(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="week", count=200)
        maw21 = df['close'].rolling(21).mean().iloc[-1]
        return maw21
    def get_maw34(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="week", count=200)
        maw34 = df['close'].rolling(34).mean().iloc[-1]
        return maw34
    def get_maw60(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="week", count=200)
        maw60 = df['close'].rolling(60).mean().iloc[-1]
        return maw60
    def get_maw120(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="week", count=200)
        maw120 = df['close'].rolling(120).mean().iloc[-1]
        return maw120
    def get_maw180(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="week", count=200)
        maw180 = df['close'].rolling(180).mean().iloc[-1]
        return maw180
    def get_maw200(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="week", count=200)
        maw200 = df['close'].rolling(200).mean().iloc[-1]
        return maw200

 # 월봉
    def get_mamo7(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="month", count=200)
        mamo7 = df['close'].rolling(7).mean().iloc[-1]
        return mamo7
    def get_mamo14(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="month", count=200)
        mamo14 = df['close'].rolling(14).mean().iloc[-1]
        return mamo14
    def get_mamo21(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="month", count=200)
        mamo21 = df['close'].rolling(21).mean().iloc[-1]
        return mamo21
    def get_mamo34(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="month", count=200)
        mamo34 = df['close'].rolling(34).mean().iloc[-1]
        return mamo34
    def get_mamo60(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="month", count=200)
        mamo60 = df['close'].rolling(60).mean().iloc[-1]
        return mamo60
    def get_mamo120(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="month", count=200)
        mamo120 = df['close'].rolling(120).mean().iloc[-1]
        return mamo120
    def get_mamo180(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="month", count=200)
        mamo180 = df['close'].rolling(180).mean().iloc[-1]
        return mamo180
    def get_mamo200(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="month", count=200)
        mamo200 = df['close'].rolling(200).mean().iloc[-1]
        return mamo200