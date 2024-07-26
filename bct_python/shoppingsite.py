class product:
    def __init__(self, product_id, name, price, description):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.description = description
    def display_product_info(self):
        print(f"Product: {self.name} ID: {self.product_id}")
        print(f"Price: ${self.price}")
        print(f"Description: {self.description}")
        print("")
class customer:
    def __init__(self,customer_id,name,email):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.shopping_cart = ShoppingCart()
    def add_to_cart(self,product):
        self.shopping_cart.add_product(product)
    def view_cart(self):
        self.shopping_cart.display_cart()
    def checkout(self):
        order = Order(self.shopping_cart)
        self.shopping_cart.clear_cart()
        return order
class Order:
    customer_id = 0
    def __init__(self,cart):
        Order.order_id += 1
        self.order_id = Order.order_id
        self.products = cart.products
        self.total_amount = cart.calculate_total()
    def display_order_display(self):
        print(f"Order ID: {self.order_id}")
        print("Product purchased: ")
        for produuct in self.products:
            print(f" - {product.name}")
        print(f"Total amount : ${self.total_amount}")
        print("")
class shoppingcart:
    def __init(self):
        self.products = []
    def add_products(self,product):
        self.products.append(product)
    def display_cart(self):
        if not self.products:
            print("Your shopping cart is empty")
        else:
            print("Your shopping cart: ")
            for product in self.products:
                product.display_product_info()
    def clear_cart(self):
        self.products = []
class EcomerceSite:
    def __init__(self):
        self.products = [
            product(1, "Laptop",1200,"Powerful laptop with high-performance specs"),
            product(2,"Phone",800,"Smart with advanced features"),
            product(3,"Headphones", 150, "Noice-cancelling headphones with great sound quality")
        ]
        self.customers = []
        self.orders = []
    def add_customer(self, customer):
        self.customer.append(customer)
    def list_products(self):
        print("Available Products: ")
        for product in self.products:
            product.display_product_info()
    def process_order(self, customer):
        order = customer.checkout()
        self.orders.append(order)
        return order
if __name__ == "__main__":
    ecommerce_site = EcomerceSite()
    while True:
        print("\nWelcome to the E-Comerce site!")
        print("1. List products")
        print("2. Add products to cart")
        print("3. View cart")
        print("4. Checkout")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")
        if choice == '1':
            ecommerce_site.list_products()
        elif choice == '2':
            product_id = int(input("ENTER THE ID OF THE PRODUCT YOU WANT TO ADD TO CART: "))
            product = next((p for p in ecommerce_site.products if p.product_id == product_id), None)
            if product:
                customer_id = int(input("Enter your customer ID: "))
                customer = next((c for c in ecommerce_site.customers if c.customer_id == customer_id),None)
                if customer:
                    customer.add_to_cart(product)
                    print(f"{product.name} added to your cart")
                else:
                    print("Customer not found.Please add yourself as a customer first.")
            else:
                print("Product not found.")
        elif choice == '3':
            customer_id = int(input("Enter your customer ID to view your cart: "))
            customer = next((c for c in ecommerce_site.customers if c.customer_id == customer_id),None)
            if customer:
                customer.view_cart()
            else:
                print("Customer not found.")
        elif choice == '4':
            customer_id = int(input("Enter your customer ID to checkout: "))
            customer = next((c for c in ecommerce_site.customers if c.customer_id == customer_id),None)
            if customer:
                order = ecommerce_site.process_order(customer)
                print(f"Order placed successfully. order ID: {order.order_id}")
                order.display_order_details()
            else:
                print("Customer not found")
        elif choice == '5':
            print("Thank you for visiting. GoodBye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5")
