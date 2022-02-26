import pyupbit
import numpy as np

# ohlcv 7일치 데이터 불러오기
df = pyupbit.get_ohlcv("KRW-BTC", count=7)
# 변동성 돌파기준 범위계산 (고가-저가) * k값 // 전략
df['range'] = (df['high'] - df['low']) * 0.5
# range 컬럼을 한칸씩 밑으로 내리기(.shift(1)) // 전략
df['target'] = df['open'] + df['range'].shift(1)
# 수수료 비율
fee = 0.005
# np.where(조건문, 참일때 값, 거짓일때 값)
df['ror'] = np.where(df['high'] > df['target'],
                     df['close'] / df['target'] - fee,
                     1)
# 누적 곱 계산 (cumprod) => 누적 수익률
df['hpr'] = df['ror'].cumprod()
# Draw Down 계산 (누적 최대값과 현재 hpr 차이 / 누적 최대값 * 100)
df['dd'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100
# MDD 계산
print("MDD(%): ", df['dd'].max())
# 엑셀로 출력
df.to_excel("dd.xlsx")
# 엑셀에 나오는 용어 정리
# open = 시가 / high = 고가 / low = 저가 / close = 종가 
# volume = 거래량 / range = 변동폭 / target = 매수가 / ror = 수익률 / hpt = 누적 수익률 / dd = 낙폭