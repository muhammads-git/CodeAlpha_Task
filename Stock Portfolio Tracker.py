import requests

class StockPortfolio:
    def __init__(self, api_key):
        self.api_key = api_key
        self.portfolio = {}

    def add_stock(self, symbol, quantity):
        if symbol in self.portfolio:
            self.portfolio[symbol]['quantity'] += quantity
        else:
            self.portfolio[symbol] = {'quantity': quantity}
        print(f'Added {quantity} shares of {symbol} to your portfolio.')

    def remove_stock(self, symbol, quantity):
        if symbol in self.portfolio:
            if self.portfolio[symbol]['quantity'] >= quantity:
                self.portfolio[symbol]['quantity'] -= quantity
                if self.portfolio[symbol]['quantity'] == 0:
                    del self.portfolio[symbol]
                print(f'Removed {quantity} shares of {symbol} from your portfolio.')
            else:
                print(f'Error: You cannot remove more shares than you own.')
        else:
            print(f'Error: {symbol} not found in your portfolio.')

    def get_stock_data(self, symbol):
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=1min&apikey={self.api_key}'
        response = requests.get(url).json()
        
        if 'Time Series (1min)' in response:
            # Get the latest stock price
            latest_time = sorted(response['Time Series (1min)'].keys())[0]
            stock_info = response['Time Series (1min)'][latest_time]
            return float(stock_info['1. open']), float(stock_info['4. close'])
        else:
            print(f"Error fetching data for {symbol}: {response.get('Note', response.get('Error Message', 'Unknown error'))}")
            return None, None

    def track_performance(self):
        total_investment = 0
        total_value = 0
        
        for symbol, data in self.portfolio.items():
            quantity = data['quantity']
            open_price, close_price = self.get_stock_data(symbol)
            if open_price and close_price:
                investment = quantity * open_price
                value = quantity * close_price
                total_investment += investment
                total_value += value
                print(f"{symbol}: Quantity: {quantity}, Investment (Open): ${investment:.2f}, Current Value (Close): ${value:.2f}")
        
        print(f"\nTotal Investment: ${total_investment:.2f}, Total Current Value: ${total_value:.2f}")
        
def main():
    api_key = 'dEyQWBhOMiHt3C9M2QD0oGZFpEYSJZzA'  # Replace with your Alpha Vantage API Key
    portfolio = StockPortfolio(api_key)

    while True:
        print("\nStock Portfolio Tracker")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. Track Performance")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            symbol = input("Enter stock symbol: ").upper()
            quantity = int(input("Enter quantity: "))
            portfolio.add_stock(symbol, quantity)
        elif choice == '2':
            symbol = input("Enter stock symbol: ").upper()
            quantity = int(input("Enter quantity: "))
            portfolio.remove_stock(symbol, quantity)
        elif choice == '3':
            portfolio.track_performance()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
