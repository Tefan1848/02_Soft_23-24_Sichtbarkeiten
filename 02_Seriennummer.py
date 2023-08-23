class ElektronicProduct:
    def __init__(self):
        self.serial_number = 0

    def __generate_serial_number(self, serial_number):
        if 0 < serial_number <= 1000:
            self.serial_number = serial_number

    def get_serial_number(self):
        return self.serial_number

my_product = ElektronicProduct()
my_product.generate_serial_number(1)
print(my_product.get_serial_number())
my_product.generate_serial_number(2)
print(my_product.get_serial_number())

# Output: