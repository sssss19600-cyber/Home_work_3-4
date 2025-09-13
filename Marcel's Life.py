import random

class House:
    def __init__(self):
        self.food = 50

class Marcel:
    def __init__(self, name="Marcel", home=None):
        self.name = name
        self.gladness = 50
        self.satiety = 50
        self.home = home
    #Дім
    def get_home(self):
        self.home = House()
    #Показник їжі вдома
    def buy_food(self):
        self.home.food += 20
        print(f"Owner bought food! Now food = {self.home.food}")
    #Показник Їжі
    def eat(self):
        if self.home.food <= 0:
            self.buy_food()
        eat_amount = min(5, self.home.food)
        self.satiety += eat_amount
        self.home.food -= eat_amount
        if self.satiety > 100:
            self.satiety = 100
        print(f"{self.name} ate {eat_amount} food. Satiety = {self.satiety}")
    #Показник радості(коли гуляє)
    def walk(self):
        self.gladness += 15
        if self.gladness > 100:
            self.gladness = 100
        print(f"{self.name} went for a walk. Gladness = {self.gladness}")
    #Показник радості(при відпочинку)
    def rest(self):
        self.gladness += 10
        if self.gladness > 70:
            self.gladness = 70
        print(f"{self.name} rested. Gladness = {self.gladness}")
    #Показник радість, ситість тд
    def days_indexes(self, day):
        print(f"\n{'='*10} Day {day} {'='*10}")
        print(f"Satiety: {self.satiety}")
        print(f"Gladness: {self.gladness}")
        print(f"Food at home: {self.home.food}")
    #Кінцівки гри
    def is_alive(self):
        if self.gladness <= 0:
            print(f"{self.name} is in depression... Game over.")
            return False
        if self.satiety <= 0:
            print(f"{self.name} died of hunger... Game over.")
            return False
        return True

    def live(self, day):
        if not self.is_alive():
            return False

        self.days_indexes(day)

        # Основні дії
        #Марсель починає їсти, якщо голод менше ніж 20
        if self.satiety < 20:
            print(f"{self.name} is hungry, going to eat.")
            self.eat()
        #Марсель починає відпочивати/гуляти, якщо радість менше ніж 20
        if self.gladness < 20:
            print(f"{self.name} is sad, needs rest.")
            self.rest()
        else:
            #Вибір, Марсель буде гуляти чи відпочивати
            dice = random.randint(1, 2)
            if dice == 1:
                self.walk()
            else:
                self.rest()

        self.satiety -= 5
        #Тут саме 14 цифра тому, що якщо 15, то він завжди вмирав на 15 дні, а коли 13 то завжди жив до 30 дня. А я хотів щоб Марсель або недоходив до 20 дня або дойшов(а не одне з них)
        self.gladness -= 14

        return True


marcel = Marcel("Marcel")
marcel.get_home()

for day in range(1, 31):
    if not marcel.live(day):
        break

#Хочу додати трішки підтексту до кода, я майже весь код робив сам. Чому майже? Тому що я буквально без ніяких підсказок або рішень до коду не зробив би нічого.
#Якщо говорити честно, я брав половину коду з коду, який ми робили на парі, а другу половину сам робив тому, що в коді якій ми на парі робили там не було того що я хотів.
#А потім коли в мене були не технічні помилки(ну помилки в самому коді) то були помилки що наприклод в Марселя завжди була депресия, або наоборот, він недоїдав і вмирал
#Тому всі ці помилки які не в самому коді були я виправлял через ШІ. Але я зробив саме головне - зрозумів цей код. Може я його і копіював з пар, може я його виправлял через ШІ
#Але саме головне - розумання кода та можливе використання його в майбутньому. Як ви бачите я дуже посторався і зробив до кожного модуля коментар, який пише що робить кожний модуль
#Я дуже старався, тому можно будь ласка за таку роботу велику 12?