
class AiFoodOrder:
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.orders = []

    def add_order(self, dish_name, quantity):
        self.orders.append({"dish": dish_name, "quantity": quantity})
        print(f"Added {quantity} x {dish_name} to {self.customer_name}'s order.")

    def process_order(self):
        if not self.orders:
            print(f"{self.customer_name}, your order is empty.")
            return

        print(f"Processing {self.customer_name}'s order using AI food ordering system:")
        for index, order in enumerate(self.orders, start=1):
            print(f"{index}. {order['quantity']} x {order['dish']}")

def main():
    customer_name = "John Doe"
    ai_food_order = AiFoodOrder(customer_name)

    ai_food_order.add_order("Pizza Margherita", 2)
    ai_food_order.add_order("Spaghetti Carbonara", 1)
    ai_food_order.add_order("Caesar Salad", 1)

    ai_food_order.process_order()

if __name__ == "__main__":
    main()
