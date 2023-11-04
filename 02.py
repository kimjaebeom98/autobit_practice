# pyupbit로 마켓 코드 조회

# get_tickers 함수 : 마켓 코드를 파이썬 리스트 타입으로 리턴

import pyupbit

tickers = pyupbit.get_tickers(fiat="KRW")
print(tickers)
print(len(tickers))
