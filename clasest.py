class Dog:
    def __init__(self,size,color,race,price):
        self.size=size
        self.color=color
        self.race=race
        self.price= price

Rufo=Dog("big","grey","Bulldog",500)
Kenai=Dog("medium","brown", "Shiba Inu", 1800)
Max=Dog("big","black", "pastor aleman ", 600)
Luna=Dog("small","beige", "labrador retriever",800)
ScoobyDoo=Dog("big","brown", " chandoso dog",200)



print(f"Rufo is a  {Rufo.size} {Rufo.race},  color {Rufo.color} and his price is  {Rufo.price} dollars")
print(f"Kenai is a  {Kenai.size} {Kenai.race},  color {Kenai.color} and his price is  {Kenai.price} dollars")
print(f"Max is a  {Max.size} {Max.race},  color {Max.color} and his price is  {Max.price} dollars")
print(f"Luna is a  {Luna.size} {Luna.race},  color {Luna.color} and his price is  {Luna.price} dollars")
print(f"ScoobyDoo is a  {ScoobyDoo.size} {ScoobyDoo.race},  color {ScoobyDoo.color} and his price is  {ScoobyDoo.price} dollars")


class cat:
    def __init__(self,size,color,race,price):
        self.size=size
        self.color=color
        self.race=race
        self.price= price

Silvestre=cat("small","grey","Siamés",800)
Nilo=cat("medium","grey","Abisinio",1000)
Orion=cat("big","white","Bombay",400)
Garfield=cat("huge", "orange","exótico",10000000000)
DonGato=cat("big", "yellow","abisinia",50000)


print(f"Silvetre is a  {Silvestre.size} {Silvestre.race} cat,  color {Silvestre.color} and his price is  {Silvestre.price} dollars")
print(f"Nilo is a  {Nilo.size} {Nilo.race} cat,  color {Nilo.color} and his price is  {Nilo.price} dollars")
print(f"Orion is a  {Orion.size} {Orion.race} cat,  color {Orion.color} and his price is  {Orion.price} dollars")
print(f"Garfield is a  {Garfield.size} {Garfield.race} cat,  color {Garfield.color} and his price is  {Garfield.price} dollars")
print(f"DonGato is a  {DonGato.size} {DonGato.race} cat,  color {DonGato.color} and his price is  {DonGato.price} dollars")


class Shoes:
    def __init__(self,size,color,brand,price):
        self.size=size
        self.color=color
        self.brand=brand
        self.price= price


Mocasínnegro=Shoes("small","black","mocasines",900)
Louboutin=Shoes("medium","grey","Louboutin",10000)
Nike_Air=Shoes("small","red","Nike",400)
Superstar=Shoes("medium", "black","Adidas",1000)
Yeezy=Shoes("small", "black","Adidad",500)

print(f"These shoes are{Mocasínnegro.color}, their size is{Mocasínnegro.size}, and they cost{Mocasínnegro.price}")
print(f"These shoes are{Louboutin.color}, their size is{Louboutin.size}, and they cost{Louboutin.price}")
print(f"These shoes are{Nike_Air.color}, their size is{Nike_Air.size}, and they cost{Nike_Air.price}")
print(f"These shoes are{Superstar.color}, their size is{Superstar.size}, and they cost{Superstar.price}")
print(f"These shoes are{Yeezy.color}, their size is{Yeezy.size}, and they cost{Yeezy.price}")

class Movie:
    def __init__(self, title, genre, duration, price):
        self.title = title
        self.genre = genre
        self.duration = duration
        self.price = price

# Movie objects
Shrek = Movie("Shrek", "Comedy", 90, 50)
Titanic = Movie("Titanic", "Romance", 195, 80)
SpiritedAway = Movie("Spirited Away", "Fantasy", 125, 70)
Avengers = Movie("Avengers: Endgame", "Action", 180, 100)
Coco = Movie("Coco", "Animation", 105, 60)

# Movie prints
print(f"{Shrek.title} is a {Shrek.genre} movie, it lasts {Shrek.duration} minutes and costs {Shrek.price} pesos")
print(f"{Titanic.title} is a {Titanic.genre} movie, it lasts {Titanic.duration} minutes and costs {Titanic.price} pesos")
print(f"{SpiritedAway.title} is a {SpiritedAway.genre} movie, it lasts {SpiritedAway.duration} minutes and costs {SpiritedAway.price} pesos")
print(f"{Avengers.title} is a {Avengers.genre} movie, it lasts {Avengers.duration} minutes and costs {Avengers.price} pesos")
print(f"{Coco.title} is a {Coco.genre} movie, it lasts {Coco.duration} minutes and costs {Coco.price} pesos")



class Food:
    def __init__(self, name, type, flavor, price):
        self.name = name
        self.type = type
        self.flavor = flavor
        self.price = price


Pizza = Food("Pizza", "Fast food", "salty", 150)
Taco = Food("Taco", "Mexican", "spicy", 30)
Apple = Food("Apple", "Fruit", "sweet", 10)
Pear = Food("Pear", "Fruit", "sweet", 12)
Sushi = Food("Sushi", "Japanese", "savory", 200)

# Food prints
print(f"{Pizza.name} is a {Pizza.type}, it's {Pizza.flavor} and costs {Pizza.price} pesos")
print(f"{Taco.name} is a {Taco.type}, it's {Taco.flavor} and costs {Taco.price} pesos")
print(f"{Apple.name} is a {Apple.type}, it's {Apple.flavor} and costs {Apple.price} pesos")
print(f"{Pear.name} is a {Pear.type}, it's {Pear.flavor} and costs {Pear.price} pesos")
print(f"{Sushi.name} is a {Sushi.type}, it's {Sushi.flavor} and costs {Sushi.price} pesos")











