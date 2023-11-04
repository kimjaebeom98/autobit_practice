# Rest API

import requests

url = "https://api.upbit.com/v1/market/all"
resp = requests.get(url)
data = resp.json()
print(len(data))


# isDetails 활용
# isDetails : 유의종목 필드과 같은 상세 정보 노출 여부(선택 파라미터)
# 유의 종목 여부 'market_warning' - > NONE (해당 사항 없음), CAUTION(투자유의)
params = {
    "isDetails": "true"
}
respIsDetails = requests.get(url, params=params)
dataIsDetails = respIsDetails.json()
print(dataIsDetails)
