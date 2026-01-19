# 📈 Live Crypto Price Tracker

### 🚀 Overview
This is a financial tracking tool built with Python. It connects to the **CoinGecko API** to fetch live cryptocurrency data in real-time. It monitors Bitcoin prices (USD & INR) and provides visual trend indicators (Green for UP, Red for DOWN) directly in the terminal.

### 🛠️ Technologies Used
* **Python 3.14**
* **REST APIs** (CoinGecko Public API)
* **Requests Library** (HTTP Data Fetching)
* **Colorama / ANSI** (Terminal UI formatting)

### ⚙️ How it Works
1.  **API Connection:** Sends a request to the server every 30 seconds.
2.  **Data Parsing:** Extracts raw JSON data into readable currency formats.
3.  **Trend Logic:** Compares current price vs. previous price to determine market direction.
4.  **Stealth Mode:** optimized to run in the background without getting rate-limited.

### 👨‍💻 Author
**Himal Singh** - Aspiring Python Developer
