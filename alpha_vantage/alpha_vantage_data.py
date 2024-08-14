import requests
import pandas as pd

# Your Alpha Vantage API key
api_key = "1OCSQFFNESRUHIUK"

# Ticker symbol for United Health Group
ticker = "UNH"

# Function to retrieve financial data
def get_financial_data(function, ticker, api_key):
    url = f"https://www.alphavantage.co/query?function={function}&symbol={ticker}&apikey={api_key}"
    response = requests.get(url)
    data = response.json()
    
    if function == "BALANCE_SHEET":
        key = "annualReports"
    elif function == "CASH_FLOW":
        key = "annualReports"
    elif function == "INCOME_STATEMENT":
        key = "annualReports"
    
    # Convert the data to a DataFrame
    df = pd.DataFrame(data[key])
    
    # Convert the date columns to datetime
    df['fiscalDateEnding'] = pd.to_datetime(df['fiscalDateEnding'])
    
    return df

# Retrieve balance sheet, cash flow, and income statement data
balance_sheet_df = get_financial_data("BALANCE_SHEET", ticker, api_key)
cash_flow_df = get_financial_data("CASH_FLOW", ticker, api_key)
income_statement_df = get_financial_data("INCOME_STATEMENT", ticker, api_key)

# Save the data to CSV files
balance_sheet_df.to_csv("UHG_Balance_Sheet.csv", index=False)
cash_flow_df.to_csv("UHG_Cash_Flow.csv", index=False)
income_statement_df.to_csv("UHG_Income_Statement.csv", index=False)

print("Data has been successfully retrieved and saved.")