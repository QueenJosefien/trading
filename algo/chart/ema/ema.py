import time
import pyupbit
from datetime import *
import openpyxl

class EMA:
    def __init__(self, open, close, count, rolling):
        self.open = open
        self.close = close
        self.count = count
        self.rolling = rolling
 # 1분당       
    def get_emam17(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="minute1", count=200)
        dp = df['open']+df['close']
        ds = dp / 2
        emam17 = ds.rolling(7).mean().iloc[-1]
        return emam17
    def get_emam114(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="minute1", count=200)
        dp = df['open']+df['close']
        ds = dp / 2
        emam114 = ds.rolling(14).mean().iloc[-1]
        return emam114
    def get_emam121(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="minute1", count=200)
        dp = df['open']+df['close']
        ds = dp / 2
        emam121 = ds.rolling(21).mean().iloc[-1]
        return emam121
    def get_emam134(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="minute1", count=200)
        dp = df['open']+df['close']
        ds = dp / 2
        emam134 = ds.rolling(34).mean().iloc[-1]
        return emam134
    def get_emam160(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="minute1", count=200)
        dp = df['open']+df['close']
        ds = dp / 2
        emam160 = ds.rolling(60).mean().iloc[-1]
        return emam160
    def get_emam1120(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="minute1", count=200)
        dp = df['open']+df['close']
        ds = dp / 2
        emam1120 = ds.rolling(120).mean().iloc[-1]
        return emam1120
    def get_emam1180(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="minute1", count=200)
        dp = df['open']+df['close']
        ds = dp / 2
        emam1180 = ds.rolling(180).mean().iloc[-1]
        return emam1180
    def get_emam1200(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="minute1", count=200)
        dp = df['open']+df['close']
        ds = dp / 2
        emam1200 = ds.rolling(200).mean().iloc[-1]
        return emam1200

# 5분당   
    def get_emam57(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="minute5", count=200)
        dp = df['open']+df['close']
        ds = dp / 2
        emam57 = ds.rolling(7).mean().iloc[-1]
        return emam57
    def get_emam514(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="minute5", count=200)
        dp = df['open']+df['close']
        ds = dp / 2
        emam514 = ds.rolling(14).mean().iloc[-1]
        return emam514
    def get_emam521(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="minute5", count=200)
        dp = df['open']+df['close']
        ds = dp / 2
        emam521 = ds.rolling(21).mean().iloc[-1]
        return emam521
    def get_emam534(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="minute5", count=200)
        dp = df['open']+df['close']
        ds = dp / 2
        emam534 = ds.rolling(34).mean().iloc[-1]
        return emam534
    def get_emam560(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="minute5", count=200)
        dp = df['open']+df['close']
        ds = dp / 2
        emam560 = ds.rolling(60).mean().iloc[-1]
        return emam560
    def get_emam5120(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="minute5", count=200)
        dp = df['open']+df['close']
        ds = dp / 2
        emam5120 = ds.rolling(120).mean().iloc[-1]
        return emam5120
    def get_emam5180(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="minute5", count=200)
        dp = df['open']+df['close']
        ds = dp / 2
        emam5180 = ds.rolling(180).mean().iloc[-1]
        return emam5180
    def get_emam5200(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="minute5", count=200)
        dp = df['open']+df['close']
        ds = dp / 2
        emam5200 = ds.rolling(200).mean().iloc[-1]
        return emam5200

# 15분당   
    def get_emam157(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="minute15", count=200)
        dp = df['open']+df['close']
        ds = dp / 2
        emam157 = ds.rolling(7).mean().iloc[-1]
        return emam157
    def get_emam1514(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="minute15", count=200)
        dp = df['open']+df['close']
        ds = dp / 2
        emam1514 = ds.rolling(14).mean().iloc[-1]
        return emam1514
    def get_emam1521(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="minute15", count=200)
        dp = df['open']+df['close']
        ds = dp / 2
        emam1521 = ds.rolling(21).mean().iloc[-1]
        return emam1521
    def get_emam1534(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="minute15", count=200)
        dp = df['open']+df['close']
        ds = dp / 2
        emam1534 = ds.rolling(34).mean().iloc[-1]
        return emam1534
    def get_emam1560(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="minute15", count=200)
        dp = df['open']+df['close']
        ds = dp / 2
        emam1560 = ds.rolling(60).mean().iloc[-1]
        return emam1560
    def get_emam15120(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="minute15", count=200)
        dp = df['open']+df['close']
        ds = dp / 2
        emam15120 = ds.rolling(120).mean().iloc[-1]
        return emam15120
    def get_emam15180(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="minute15", count=200)
        dp = df['open']+df['close']
        ds = dp / 2
        emam15180 = ds.rolling(180).mean().iloc[-1]
        return emam15180
    def get_emam15200(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="minute15", count=200)
        dp = df['open']+df['close']
        ds = dp / 2
        emam15200 = ds.rolling(200).mean().iloc[-1]
        return emam15200

# 30분당   
    def get_emam307(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="minute30", count=200)
        dp = df['open']+df['close']
        ds = dp / 2
        emam307 = ds.rolling(7).mean().iloc[-1]
        return emam307
    def get_emam3014(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="minute30", count=200)
        dp = df['open']+df['close']
        ds = dp / 2
        emam3014 = ds.rolling(14).mean().iloc[-1]
        return emam3014
    def get_emam3021(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="minute30", count=200)
        dp = df['open']+df['close']
        ds = dp / 2
        emam3021 = ds.rolling(21).mean().iloc[-1]
        return emam3021
    def get_emam3034(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="minute30", count=200)
        dp = df['open']+df['close']
        ds = dp / 2
        emam3034 = ds.rolling(34).mean().iloc[-1]
        return emam3034
    def get_emam3060(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="minute30", count=200)
        dp = df['open']+df['close']
        ds = dp / 2
        emam3060 = ds.rolling(60).mean().iloc[-1]
        return emam3060
    def get_emam30120(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="minute30", count=200)
        dp = df['open']+df['close']
        ds = dp / 2
        emam30120 = ds.rolling(120).mean().iloc[-1]
        return emam30120
    def get_emam30180(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="minute30", count=200)
        dp = df['open']+df['close']
        ds = dp / 2
        emam30180 = ds.rolling(180).mean().iloc[-1]
        return emam30180
    def get_emam30200(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="minute30", count=200)
        dp = df['open']+df['close']
        ds = dp / 2
        emam30200 = ds.rolling(200).mean().iloc[-1]
        return emam30200

 # 1시간당   
    def get_mah17(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="hour1", count=200)
        dp = df['open']+df['close']
        ds = dp / 2
        mah17 = ds.rolling(7).mean().iloc[-1]
        return mah17
    def get_mah114(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="hour1", count=200)
        dp = df['open']+df['close']
        ds = dp / 2
        mah114 = ds.rolling(14).mean().iloc[-1]
        return mah114
    def get_mah121(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="hour1", count=200)
        dp = df['open']+df['close']
        ds = dp / 2
        mah121 = ds.rolling(21).mean().iloc[-1]
        return mah121
    def get_mah134(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="hour1", count=200)
        dp = df['open']+df['close']
        ds = dp / 2
        mah134 = ds.rolling(34).mean().iloc[-1]
        return mah134
    def get_mah160(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="hour1", count=200)
        dp = df['open']+df['close']
        ds = dp / 2
        mah160 = ds.rolling(60).mean().iloc[-1]
        return mah160
    def get_mah1120(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="hour1", count=200)
        dp = df['open']+df['close']
        ds = dp / 2
        mah1120 = ds.rolling(120).mean().iloc[-1]
        return mah1120
    def get_mah1180(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="hour1", count=200)
        dp = df['open']+df['close']
        ds = dp / 2
        mah1180 = ds.rolling(180).mean().iloc[-1]
        return mah1180
    def get_mah1200(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="hour1", count=200)
        dp = df['open']+df['close']
        ds = dp / 2
        mah1200 = ds.rolling(200).mean().iloc[-1]
        return mah1200
    
 # 4시간당   
    def get_mah47(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="hour4", count=200)
        dp = df['open']+df['close']
        ds = dp / 2
        mah47 = ds.rolling(7).mean().iloc[-1]
        return mah47
    def get_mah414(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="hour4", count=200)
        dp = df['open']+df['close']
        ds = dp / 2
        mah414 = ds.rolling(14).mean().iloc[-1]
        return mah414
    def get_mah421(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="hour4", count=200)
        dp = df['open']+df['close']
        ds = dp / 2
        mah421 = ds.rolling(21).mean().iloc[-1]
        return mah421
    def get_mah434(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="hour4", count=200)
        dp = df['open']+df['close']
        ds = dp / 2
        mah434 = ds.rolling(34).mean().iloc[-1]
        return mah434
    def get_mah460(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="hour4", count=200)
        dp = df['open']+df['close']
        ds = dp / 2
        mah460 = ds.rolling(60).mean().iloc[-1]
        return mah460
    def get_mah4120(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="hour4", count=200)
        dp = df['open']+df['close']
        ds = dp / 2
        mah4120 = ds.rolling(120).mean().iloc[-1]
        return mah4120
    def get_mah4180(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="hour4", count=200)
        dp = df['open']+df['close']
        ds = dp / 2
        mah4180 = ds.rolling(180).mean().iloc[-1]
        return mah4180
    def get_mah4200(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="hour4", count=200)
        dp = df['open']+df['close']
        ds = dp / 2
        mah4200 = ds.rolling(200).mean().iloc[-1]
        return mah4200
    
 # 일봉
    def get_emad7(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="day", count=200)
        dp = df['open']+df['close']
        ds = dp / 2
        emad7 = ds.rolling(7).mean().iloc[-1]
        return emad7
    def get_emad14(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="day", count=200)
        dp = df['open']+df['close']
        ds = dp / 2
        emad14 = ds.rolling(14).mean().iloc[-1]
        return emad14
    def get_emad21(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="day", count=200)
        dp = df['open']+df['close']
        ds = dp / 2
        emad21 = ds.rolling(21).mean().iloc[-1]
        return emad21
    def get_emad34(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="day", count=200)
        dp = df['open']+df['close']
        ds = dp / 2
        emad34 = ds.rolling(34).mean().iloc[-1]
        return emad34
    def get_emad60(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="day", count=200)
        dp = df['open']+df['close']
        ds = dp / 2
        emad60 = ds.rolling(60).mean().iloc[-1]
        return emad60
    def get_emad120(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="day", count=200)
        dp = df['open']+df['close']
        ds = dp / 2
        emad120 = ds.rolling(120).mean().iloc[-1]
        return emad120
    def get_emad180(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="day", count=200)
        dp = df['open']+df['close']
        ds = dp / 2
        emad180 = ds.rolling(180).mean().iloc[-1]
        return emad180
    def get_emad200(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="day", count=200)
        dp = df['open']+df['close']
        ds = dp / 2
        emad200 = ds.rolling(200).mean().iloc[-1]
        return emad200
    
 # 주봉
    def get_emaw7(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="week", count=200)
        dp = df['open']+df['close']
        ds = dp / 2
        emaw7 = ds.rolling(7).mean().iloc[-1]
        return emaw7
    def get_emaw14(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="week", count=200)
        dp = df['open']+df['close']
        ds = dp / 2
        emaw14 = ds.rolling(14).mean().iloc[-1]
        return emaw14
    def get_emaw21(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="week", count=200)
        dp = df['open']+df['close']
        ds = dp / 2
        emaw21 = ds.rolling(21).mean().iloc[-1]
        return emaw21
    def get_emaw34(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="week", count=200)
        dp = df['open']+df['close']
        ds = dp / 2
        emaw34 = ds.rolling(34).mean().iloc[-1]
        return emaw34
    def get_emaw60(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="week", count=200)
        dp = df['open']+df['close']
        ds = dp / 2
        emaw60 = ds.rolling(60).mean().iloc[-1]
        return emaw60
    def get_emaw120(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="week", count=200)
        dp = df['open']+df['close']
        ds = dp / 2
        emaw120 = ds.rolling(120).mean().iloc[-1]
        return emaw120
    def get_emaw180(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="week", count=200)
        dp = df['open']+df['close']
        ds = dp / 2
        emaw180 = ds.rolling(180).mean().iloc[-1]
        return emaw180
    def get_emaw200(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="week", count=200)
        dp = df['open']+df['close']
        ds = dp / 2
        emaw200 = ds.rolling(200).mean().iloc[-1]
        return emaw200

 # 월봉
    def get_emamo7(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="month", count=200)
        dp = df['open']+df['close']
        ds = dp / 2
        emamo7 = ds.rolling(7).mean().iloc[-1]
        return emamo7
    def get_emamo14(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="month", count=200)
        dp = df['open']+df['close']
        ds = dp / 2
        emamo14 = ds.rolling(14).mean().iloc[-1]
        return emamo14
    def get_emamo21(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="month", count=200)
        dp = df['open']+df['close']
        ds = dp / 2
        emamo21 = ds.rolling(21).mean().iloc[-1]
        return emamo21
    def get_emamo34(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="month", count=200)
        dp = df['open']+df['close']
        ds = dp / 2
        emamo34 = ds.rolling(34).mean().iloc[-1]
        return emamo34
    def get_emamo60(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="month", count=200)
        dp = df['open']+df['close']
        ds = dp / 2
        emamo60 = ds.rolling(60).mean().iloc[-1]
        return emamo60
    def get_emamo120(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="month", count=200)
        dp = df['open']+df['close']
        ds = dp / 2
        emamo120 = ds.rolling(120).mean().iloc[-1]
        return emamo120
    def get_emamo180(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="month", count=200)
        dp = df['open']+df['close']
        ds = dp / 2
        emamo180 = ds.rolling(180).mean().iloc[-1]
        return emamo180
    def get_emamo200(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="month", count=200)
        dp = df['open']+df['close']
        ds = dp / 2
        emamo200 = ds.rolling(200).mean().iloc[-1]
        return emamo200
