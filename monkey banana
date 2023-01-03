import random
class Monkey:
    def __init__(self,bananas):
        self.bananas = bananas
    def __repr__(self):
        return "Monkey with %d bananas."% self.bananas
monkeys = [Monkey(random.randint(0,50)) for i in range(5)]
print("Random monkeys:")
print(monkeys)
print
def number_of_bananas(monkey):
    """Returns number of bananas that monkey has."""
    return monkey.bananas
print("number_of_bananas(FIRST MONKEY):",number_of_bananas(monkeys[0]))
max_monkey=max(monkeys,key=number_of_bananas)
print("Max monkey: ",max_monkey)
