import time
import pyupbit
from datetime import *
import openpyxl

BTC = pyupbit.get_ohlcv("KRW-BTC")
ticker = "KRW-BTC"

class Volume:
    def __init__(self, volume):
        self.volume = volume
        
    def get_volm1(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="minute1", count=200)
        volm1 = df['volume']
        return volm1
    def get_volm1(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="minute1", count=200)
        volm1 = df['volume']
        return volm1
    def get_volm3(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="minute3", count=200)
        volm3 = df['volume']
        return volm3
    def get_volm5(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="minute5", count=200)
        volm5 = df['volume']
        return volm5
    def get_volm15(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="minute15", count=200)
        volm15 = df['volume']
        return volm15
    def get_volm30(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="minute30", count=200)
        volm30 = df['volume']
        return volm30
    
    def get_volh1(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="hour1", count=200)
        volh1 = df['volume']
        return volh1
    def get_volh4(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="hour4", count=200)
        volh4 = df['volume']
        return volh4

    def get_vold(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="day", count=200)
        vold = df['volume']
        return vold
    def get_volw(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="week", count=200)
        volw = df['volume']
        return volw
    def get_volmo(ticker):
        df = pyupbit.get_ohlcv(ticker, interval="month", count=200)
        volmo = df['volume']
        return volmo





