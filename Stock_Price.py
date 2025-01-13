print("hello world")
import yfinance as yf
import pandas as pd

# Define the stock ticker and date range
ticker = "YETI"  # Replace with your desired stock ticker
start_date = "2024-01-01"
end_date = "2025-01-07"

# Fetch stock data using yfinance
print("Downloading stock data...")
stock_data = yf.download(ticker, start=start_date, end=end_date)

# Check the first few rows of the stock data
print("Stock data preview:")
print(stock_data.head())

stock_data.dropna(inplace=True)  # Drop rows with missing values
data = stock_data[stock_data['Volume'] > 0]  # Remove rows with no trading activity

# Save the stock data to a CSV file
output_csv_file = "yeti_stock_data.csv"
stock_data.to_csv(output_csv_file)

print(f"Stock data successfully saved to {output_csv_file}")





