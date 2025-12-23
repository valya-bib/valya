class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Order:
    def __init__(self, order_number):
        self.order_number = order_number
        self.products = []
    
    def add_product(self, product):
        self.products.append(product)
    
    def get_total_price(self):
        total = 0
        for product in self.products:
            total += product.price
        return total
    
    def display_order(self):
        print("заказ " + str(self.order_number))
        print("список товаров:")
        
        for product in self.products:
            print(product.name + " : " + str(product.price) + " руб")
        
        print("общая сумма: " + str(self.get_total_price()) + " руб")


if __name__ == "__main__":
    p1 = Product("чипсы", 150)
    p2 = Product("яйца", 90)
    
    order = Order(1)
    
    order.add_product(p1)
    order.add_product(p2)
    
    order.display_order()
    

   