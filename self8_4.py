class Game:
    def __init__(self,title,price,rating):
        self._title = title
        self._price = price
        self._rating = rating

    def print_game(self):
        print(f"{self._title} is a {self._price} game that has a rating of {self._rating}")

Purchase = Game("Hollow Knight","7,49$","10/10")
Purchase.print_game()