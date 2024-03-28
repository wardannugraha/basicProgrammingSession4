class Item:
    def __init__(self, name, cost_price, stock):
        self.name = name
        self.cost_price = cost_price
        self.stock = stock

    def calculate_selling_price(self):
        return self.cost_price * 1.1  # 10% markup

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Cost Price: {self.cost_price}")
        print(f"Selling Price: {self.calculate_selling_price()}")
        print(f"Stock: {self.stock}")


class CosmeticShop:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def display_items(self):
        print("Available Items:")
        for item in self.items:
            item.display_info()

    def make_purchase(self, item_name, quantity):
        for item in self.items:
            if item.name == item_name:
                if item.stock >= quantity:
                    total_cost = item.calculate_selling_price() * quantity
                    item.stock -= quantity
                    print(f"Purchase successful! Total cost: {total_cost}")
                    return total_cost
                else:
                    print("Insufficient stock!")
                    return 0
        print("Item not found!")
        return 0


def main():
    shop = CosmeticShop()

    # Adding some sample items
    shop.add_item(Item("Lipstick", 10, 20))
    shop.add_item(Item("Mascara", 15, 15))
    shop.add_item(Item("Foundation", 20, 10))

    print("Welcome to Siti's Cosmetic Shop!")
    while True:
        try:
            print("\n1. Display Available Items")
            print("2. Make a Purchase")
            print("3. Exit")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                shop.display_items()
            elif choice == 2:
                item_name = input("Enter the name of the item you want to purchase: ")
                quantity = int(input("Enter the quantity you want to purchase: "))
                shop.make_purchase(item_name, quantity)
            elif choice == 3:
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please enter a valid option.")
        except ValueError:
            print("Please enter a valid number.")


if __name__ == "__main__":
    main()
