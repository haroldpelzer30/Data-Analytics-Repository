import yfinance as yf
import pandas as pd
import numpy as np

# --- CONFIGURATION ---
# Note: Using yfinance for public demonstration. 
# For live trading, credentials should be stored in environment variables.
TICKERS = ["EURUSD=X", "GBPUSD=X", "USDJPY=X", "USDCHF=X", "AUDUSD=X", "USDCAD=X", "NZDUSD=X"]

def calculate_indicators(df):
    """Calculates RSI and ATR to avoid the previous 'stuck at 99' error."""
    # 1. Calculate RSI (Relative Strength Index)
    window = 14
    delta = df['Close'].diff()
    up = delta.clip(lower=0)
    down = -1 * delta.clip(upper=0)
    ema_up = up.ewm(com=window-1, adjust=False).mean()
    ema_down = down.ewm(com=window-1, adjust=False).mean()
    rs = ema_up / ema_down
    df['RSI'] = 100 - (100 / (1 + rs))

    # 2. Calculate ATR (Average True Range) for Risk Management
    high_low = df['High'] - df['Low']
    high_close = np.abs(df['High'] - df['Close'].shift())
    low_close = np.abs(df['Low'] - df['Close'].shift())
    ranges = pd.concat([high_low, high_close, low_close], axis=1)
    true_range = np.max(ranges, axis=1)
    df['ATR'] = true_range.rolling(14).mean()
    
    return df

def scan_market():
    print(f"--- FlyGuy AeroSniper: High-Probability Scanner ---")
    print(f"Targeting Main 7 Majors | Strategy: 80/20 RSI + ATR Risk\n")
    
    for symbol in TICKERS:
        # Fetching 15m intervals for day trading precision
        df = yf.download(symbol, period="2d", interval="15m", progress=False)
        
        if len(df) > 14:
            df = calculate_indicators(df)
            current_rsi = df['RSI'].iloc[-1]
            current_atr = df['ATR'].iloc[-1]
            price = df['Close'].iloc[-1]

            # Strategy Logic
            status = "NEUTRAL"
            if current_rsi >= 80:
                status = "⚠️ OVERBOUGHT - SELL SIGNAL"
            elif current_rsi <= 20:
                status = "⚠️ OVERSOLD - BUY SIGNAL"

            print(f"{symbol:8} | Price: {price:.4f} | RSI: {current_rsi:.2f} | ATR: {current_atr:.4f} | {status}")
        else:
            print(f"Insufficient data for {symbol}")

if __name__ == "__main__":
    scan_market()
