from Restaurant import Restaurant

restaurant = Restaurant("Kostya's restaurant", 'universal')

print(f'Количество обслуженных гостей - {restaurant.number_served}')

restaurant.set_number_served(100)
restaurant.increment_number_served(500)