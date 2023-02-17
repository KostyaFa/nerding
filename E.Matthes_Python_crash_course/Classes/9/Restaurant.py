class Restaurant():
    def __init__(self, restaurant_name, cuisine_name):
        self.restaurant_name = restaurant_name
        self.cuisine_name = cuisine_name
        self.number_served = 0 # количество обслужженных посетителей

    def describe_restaurant(self):
        print(f'Ресторан {self.restaurant_name.title()} базируется на {self.cuisine_name.title()} кухне')

    def open_restaurant(self):
        print(f'Ресторан {self.restaurant_name.title()} открыт')

    def set_number_served(self, number):
        self.number_served = number
        print(f'{self.number_served} - количество обслуженных гостей')

    def increment_number_served(self, number):
        self.number_served += number
        print(f'По окончанию дня общее число обслуженных гостей составляет {self.number_served} человек')



        