import requests
import pandas as pd

# Your Financial Modeling Prep API key
api_key = "OMGauZzS7pTNrJX8ZdCw5LRd9jLhejMA"

# Ticker symbol for United Health Group
ticker = "UNH"

# Base URL for the API
base_url = "https://financialmodelingprep.com/api/v3"

# Functions to retrieve balance sheet, cash flow, and income statement data
def get_financial_data(statement_type, ticker, api_key):
    url = f"{base_url}/{statement_type}/{ticker}?apikey={api_key}&limit=15"
    response = requests.get(url)
    data = response.json()
    
    # Convert the data to a DataFrame
    df = pd.DataFrame(data)
    
    # Convert the date columns to datetime
    df['date'] = pd.to_datetime(df['date'])
    
    return df

# Retrieve balance sheet, cash flow, and income statement data
balance_sheet_df = get_financial_data("balance-sheet-statement", ticker, api_key)
cash_flow_df = get_financial_data("cash-flow-statement", ticker, api_key)
income_statement_df = get_financial_data("income-statement", ticker, api_key)

# Save the data to CSV files
balance_sheet_df.to_csv("UHG_Balance_Sheet_15_Years.csv", index=False)
cash_flow_df.to_csv("UHG_Cash_Flow_15_Years.csv", index=False)
income_statement_df.to_csv("UHG_Income_Statement_15_Years.csv", index=False)

print("15 years of financial data has been successfully retrieved and saved.")


