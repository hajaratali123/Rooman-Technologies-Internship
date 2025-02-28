def add_cust():
    global total_cust
    total_cust = 0  # Initialize if not already defined
    total_cust += 1
    print(f"Customers added. Total customers: {total_cust}")

def process_cart(items):
    total_price = 0
    for item in items:
        total_price += item['price'] * item['quantity']
    print(f"Total price: {total_price}")

# Initialize customer count
total_cust = 0

# Add customers
add_cust()
add_cust()

# Define cart items properly
cart = [
    {"name": "book", "price": 10, "quantity": 2},
    {"name": "pen", "price": 1, "quantity": 2}
]

# Process cart
process_cart(cart)
