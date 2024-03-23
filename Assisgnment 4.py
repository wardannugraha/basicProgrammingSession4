def calculate_selling_price(cost_price):
    selling_price = cost_price * 1.1  # 10% markup
    return selling_price

def main():
    print("Welcome to Siti's Cosmetic Shop!")
    while True:
        try:
            cost_price = float(input("Enter the cost price of the item (or '0' to exit): "))
            if cost_price == 0:
                print("Exiting...")
                break
            selling_price = calculate_selling_price(cost_price)
            print(f"Selling price: {selling_price}")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()
