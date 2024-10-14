#Создайте приложение которое позволит оценивать работу таксистов
from pprint import pprint

my_rating = {}

def form_rater(**kwargs):
    my_rating.update(**kwargs)

form_rater(name=input(),rating = input())
pprint(my_rating)