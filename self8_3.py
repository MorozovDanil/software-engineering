class Game:
    def __init__(self,title,price,rating):
        self.title = title
        self.price = price
        self.rating = rating

    def print_game(self):
        print(f"{self.title} is a {self.price} game that has a rating of {self.rating}")

class Expansion(Game):
    def __init__(self,title,price,expansion_title):
        super().__init__(self,title,price)
        self.title = title
        self.expansion_title = expansion_title

    def print_expansion(self):
        print (f"{self.expansion_title} is an expansion for {self.title}. Coming soon!")

Purchase = Game("Hollow Knight","7,49$","10/10")
Purchase.print_game()
PurchaseExpansion = Expansion("Hollow Knight","12,99$","Silksong")
PurchaseExpansion.print_expansion()