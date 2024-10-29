class Game:
    def __init__(self,title,price,rating):
        self.title = title
        self.price = price
        self.rating = rating

    def print_game(self):
        print(f"{self.title} is a {self.price} game that has a rating of {self.rating}")

Purchase = Game("Hollow Knight","7,49$","10/10")
Purchase.print_game()