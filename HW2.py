# 6. Наследование: Создайте класс ElectricCar, который наследует от класса
# Car и имеет дополнительный атрибут battery_size.
class Car:
    def transmission(self, b):
        if b==0:
            self.tr = 'Transmission: mechanical'
        elif b==1:
            self.tr = 'Transmission: automatic'
        elif b==2:
            self.tr = 'Electric car'
        else:
            self.tr = 'unknown'
        return self.tr


class ElectricCar(Car):
    def batterySize(self, v):
        self.volume = v
        return v
    def start_engine(self):
        c = 'unknown'
        return c
print("Задача 6:")
BMW = Car()
print(BMW.transmission(1))
Tesla = ElectricCar()
print(Tesla.transmission(2), f", Battery: {Tesla.batterySize(100)} kW/h")

# 7. Переопределение метода: Переопределите метод start_engine в классе ElectricCar,
# чтобы он выводил "Тихий запуск двигателя!"

class ElectricCar2(ElectricCar):
    def start_engine(self):
        c = 'Тихий запуск двигателя!'
        return c
print("Задача 7:")
Tesla2 = ElectricCar2()
print(Tesla2.start_engine())

#8. Использование суперкласса: используйте функцию super() в методе __init__ класса ElectricCar

print("Задача 8:")
class ElectricCar3(ElectricCar):
    def __init__(self, v, type_batt):
        print(f'Battery size {v} kW/h')
        super().batterySize(v)
        if type_batt == 10:
            print('Lithium ion battery')
        elif type_batt == 20:
            print('Lithium phosphate battery')
        else:
            print('Unknown')

Audi = ElectricCar3(200, 10)