# ==================================================
#          STOCK PORTFOLIO TRACKER
#             CODEALPHA - TASK 2
# ==================================================

# Predefined stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 420,
    "AMZN": 190
}

# Store portfolio information
portfolio = []

# Total investment
total_investment = 0

# Display heading
print()
print("==============================================")
print("           STOCK PORTFOLIO TRACKER")
print("==============================================")
print("Available Stocks:")
print("AAPL  - $180")
print("TSLA  - $250")
print("GOOGL - $150")
print("MSFT  - $420")
print("AMZN  - $190")
print("==============================================")
print()

# Main loop
while True:

    # Ask user for stock name
    stock = input(
        "Enter stock name (or type 'done' to finish): "
    ).upper().strip()

    # Stop entering stocks
    if stock == "DONE":
        break

    # Check whether stock exists
    if stock not in stock_prices:
        print()
        print("❌ Invalid stock name!")
        print("Please select a stock from the available list.")
        print()
        continue

    # Ask for quantity
    quantity_input = input("Enter quantity: ").strip()

    # Check quantity
    if not quantity_input.isdigit():
        print()
        print("❌ Invalid quantity!")
        print("Please enter a positive whole number.")
        print()
        continue

    quantity = int(quantity_input)

    # Check for zero
    if quantity <= 0:
        print()
        print("❌ Quantity must be greater than zero.")
        print()
        continue

    # Get stock price
    price = stock_prices[stock]

    # Calculate investment
    investment = price * quantity

    # Add to total investment
    total_investment += investment

    # Store portfolio information
    portfolio.append({
        "stock": stock,
        "price": price,
        "quantity": quantity,
        "investment": investment
    })

    # Display successful entry
    print()
    print("✅ Stock added successfully!")
    print("Stock:", stock)
    print("Price: $", price)
    print("Quantity:", quantity)
    print("Investment: $", investment)
    print()


# ==================================================
#              FINAL PORTFOLIO
# ==================================================

if len(portfolio) == 0:

    print()
    print("==============================================")
    print("No stocks were added to the portfolio.")
    print("==============================================")

else:

    print()
    print("==============================================")
    print("               YOUR PORTFOLIO")
    print("==============================================")

    print("Stock\tPrice\tQuantity\tInvestment")
    print("----------------------------------------------")

    # Display each stock
    for item in portfolio:
        print(
            item["stock"],
            "\t$" + str(item["price"]),
            "\t" + str(item["quantity"]),
            "\t\t$" + str(item["investment"])
        )

    print("----------------------------------------------")

    # Display total
    print("Total Investment: $", total_investment)

    print("==============================================")

    # ==================================================
    #             SAVE RESULT TO FILE
    # ==================================================

    with open("portfolio_result.txt", "w") as file:

        file.write("==============================================\n")
        file.write("           STOCK PORTFOLIO TRACKER\n")
        file.write("==============================================\n\n")

        file.write("Stock\tPrice\tQuantity\tInvestment\n")
        file.write("----------------------------------------------\n")

        for item in portfolio:

            file.write(
                item["stock"]
                + "\t$"
                + str(item["price"])
                + "\t"
                + str(item["quantity"])
                + "\t\t$"
                + str(item["investment"])
                + "\n"
            )

        file.write("----------------------------------------------\n")
        file.write(
            "Total Investment: $"
            + str(total_investment)
            + "\n"
        )

        file.write("==============================================\n")

    print()
    print("✅ Portfolio result saved successfully!")
    print("📄 File created: portfolio_result.txt")
    print()