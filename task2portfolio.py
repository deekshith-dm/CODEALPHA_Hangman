# Stock Portfolio Tracker

def stock_portfolio_tracker():
    # Hardcoded stock prices
    stock_prices = {
        "AAPL": 180,
        "TSLA": 250,
        "GOOGL": 140,
        "AMZN": 130,
        "MSFT": 330
    }

    print("📊 Welcome to Stock Portfolio Tracker")
    print("Available stocks and prices (USD):")
    for stock, price in stock_prices.items():
        print(f"{stock}: ${price}")

    portfolio = {}
    total_investment = 0

    while True:
        stock = input("\nEnter stock symbol (or 'done' to finish): ").upper()

        if stock == "DONE":
            break

        if stock not in stock_prices:
            print("⚠️ Stock not available. Please choose from the list.")
            continue

        try:
            quantity = int(input(f"Enter quantity of {stock}: "))
            if quantity <= 0:
                print("⚠️ Quantity must be positive.")
                continue
        except ValueError:
            print("⚠️ Please enter a valid number.")
            continue

        # Add to portfolio
        cost = stock_prices[stock] * quantity
        portfolio[stock] = portfolio.get(stock, 0) + quantity
        total_investment += cost

        print(f"✅ Added {quantity} shares of {stock}. Investment: ${cost}")

    # Display summary
    print("\n===== Portfolio Summary =====")
    for stock, qty in portfolio.items():
        print(f"{stock}: {qty} shares @ ${stock_prices[stock]} each = ${stock_prices[stock] * qty}")

    print(f"\n💰 Total Investment Value: ${total_investment}")

    # Option to save result
    save_choice = input("\nDo you want to save the result in a file? (yes/no): ").lower()
    if save_choice == "yes":
        with open("portfolio_summary.txt", "w") as file:
            file.write("===== Portfolio Summary =====\n")
            for stock, qty in portfolio.items():
                file.write(f"{stock}: {qty} shares @ ${stock_prices[stock]} each = ${stock_prices[stock] * qty}\n")
            file.write(f"\nTotal Investment Value: ${total_investment}\n")
        print("📂 Portfolio summary saved as 'portfolio_summary.txt'.")


# Run program
if __name__ == "__main__":
    stock_portfolio_tracker()

