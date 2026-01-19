import requests
import time
from datetime import datetime

# ANSI Color Codes
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

def get_bitcoin_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd,inr"
    try:
        response = requests.get(url)
        data = response.json()
        return data['bitcoin']['usd'], data['bitcoin']['inr']
    except:
        return None, None

print("---------------------------------------")
print("💰 TRACKING LIVE BITCOIN MARKET...")
print("---------------------------------------")

last_price = 0

while True:
    usd, inr = get_bitcoin_price()
    
    if usd:
        now = datetime.now().strftime("%H:%M:%S")
        
        if last_price != 0:
            if usd > last_price:
                print(f"{GREEN}[{now}] ▲ UP   | ${usd} | ₹{inr}{RESET}")
            elif usd < last_price:
                print(f"{RED}[{now}] ▼ DOWN | ${usd} | ₹{inr}{RESET}")
            else:
                print(f"[{now}] = SAME | ${usd} | ₹{inr}")
        else:
            print(f"[{now}] Starting Price: ${usd}")
            
        last_price = usd
        
    time.sleep(30)
