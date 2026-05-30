import requests
import time

coins = ["BTC", "ETH", "BNB", "SOL", "XRP", "LTC", "BCH", "ADA", "TRX"]

print("💰 Binance Prices | Ctrl+C для выхода\n" + "="*50)

while True:
    prices = {}
    for coin in coins:
        url = f"https://api.binance.com/api/v3/ticker/price?symbol={coin}USDT"
        data = requests.get(url).json()
        prices[coin] = float(data['price'])
    
    # Сортируем по цене (от дорогих к дешёвым)
    sorted_coins = sorted(prices.items(), key=lambda x: x[1], reverse=True)
    
    print(f"\n⏰ {time.strftime('%H:%M:%S')}")
    for coin, price in sorted_coins:
        # Визуальный индикатор объёма (простой ASCII-бар)
        bar_length = min(30, int(price / max(prices.values()) * 30))
        bar = "█" * bar_length + "░" * (30 - bar_length)
        print(f"{coin:<5} ${price:>10,.2f} {bar}")
    
    print("="*50)
    time.sleep(5)  # Обновление каждые 5 секунд
