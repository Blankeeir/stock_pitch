import yfinance as yf
import pandas as pd

# Define the ticker for United Health Group (UHG)
ticker = "UNH"

# Download historical stock prices for the last 10 years
uhg_data = yf.download(ticker, start="2013-01-01", end="2023-01-01")

# Save the historical stock prices to a CSV file
uhg_data.to_csv("UHG_Historical_Stock_Prices.csv")

# Download financial data for United Health Group
uhg_financials = yf.Ticker(ticker).financials
uhg_balance_sheet = yf.Ticker(ticker).balance_sheet
uhg_cashflow = yf.Ticker(ticker).cashflow

# Save the financial data to CSV files
uhg_financials.to_csv("UHG_Financials.csv")
uhg_balance_sheet.to_csv("UHG_Balance_Sheet.csv")
uhg_cashflow.to_csv("UHG_Cash_Flow.csv")

print("Data has been successfully retrieved and saved.")