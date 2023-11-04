# 시세 캔드 조회 API

import pyupbit

# o(open) : 시가
# h(high) : 고가
# l(low) : 저가
# c(close) : 종가
# v(volume) : 거래량
df = pyupbit.get_ohlcv("KRW-BTC", "minute1")


# 1분봉과 3분봉의 관계
# open : 3분으로 묶었을 때 그 중 젤 첫 번째 1분 봉 값
print(df['open'].resample('3T').first())
# high : 3분으로 묵었을 때 그 중 젤 큰 1분 봉 값
print(df['high'].resample('3T').max())
# low : 3분으로 묵었을 때 그 중 젤 작은 1분 봉 값
print(df['low'].resample('3T').min())
# close : 3분으로 묵었을 때 그 중 마지막 1분 봉 값
print(df['close'].resample('3T').last())
# volume : 3분으로 묵었을 때 1분 봉들 다 합한 값
print(df['volume'].resample('3T').sum())
