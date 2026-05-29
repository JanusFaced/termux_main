import requests

coins = [
	"BTC", "ETH", "BNB",
	"SOL", "XRP", "LTC",
	"BCH", "ADA", "TRX"
]

print("💰 Текущие цены на Binance")
print("=" * 40)

for coin in coins:
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={coin}USDT"
    response = requests.get(url)
    data = response.json()
    price = float(data['price'])
    print(f"{coin}: ${price:,.2f}")
