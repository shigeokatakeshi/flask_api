import requests

res = requests.get("https://zipcloud.ibsnet.co.jp/api/search?zipcode=7830060")

# print(res.text["status"])

json = res.json()
result01 = json["results"][0]
print(result01["address1"])
