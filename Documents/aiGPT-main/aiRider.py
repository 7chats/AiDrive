
class AiRider:
    def __init__(self, rider_name):
        self.rider_name = rider_name
        self.deliveries = []

    def add_delivery(self, customer_name, address):
        self.deliveries.append({"customer": customer_name, "address": address})
        print(f"Added delivery to {customer_name} at {address} for {self.rider_name}.")

    def process_deliveries(self):
        if not self.deliveries:
            print(f"{self.rider_name}, you have no deliveries.")
            return

        print(f"Processing {self.rider_name}'s deliveries using AI delivery system:")
        for index, delivery in enumerate(self.deliveries, start=1):
            print(f"{index}. Deliver to {delivery['customer']} at {delivery['address']}")

def main():
    rider_name = "AI Rider 1"
    ai_rider = AiRider(rider_name)

    ai_rider.add_delivery("John Doe", "123 Main St")
    ai_rider.add_delivery("Jane Smith", "456 Oak St")
    ai_rider.add_delivery("Bob Johnson", "789 Maple St")

    ai_rider.process_deliveries()

if __name__ == "__main__":
    main()
