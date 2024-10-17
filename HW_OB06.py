import random


class Hero():
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 20

    def attack(self, other):
        other.health -= self.attack_power
        print(f"{self.name} атакует {other.name} и наносит {self.attack_power} урона!")
        print(f"У {other.name} осталось {other.health} здоровья.")

    def is_alive(self):
        return self.health > 0


class Game():
    def __init__(self, player, computer):
        self.player = Hero(player)
        self.computer = Hero(computer)

    def start(self):
        print("Игра началась!")
        while self.player.is_alive() and self.computer.is_alive():
            # Ход игрока
            self.player.attack(self.computer)
            if not self.computer.is_alive():
                print(f"{self.player.name} победил!")
                break

            # Ход компьютера
            self.computer.attack(self.player)
            if not self.player.is_alive():
                print(f"{self.computer.name} победил!")
                break


# Запуск игры
game = Game('Alex', 'Bob')
game.start()
