#CS191 Assignment 2
#Student : Pavlos Eikospentakis id: 20240206
#Instructor : Vaggelis Chatzistavrou
# Graduation Party program
#This program demonstrates a small database for my graduation party
#Basic OOP implementations


import json

drink_prices = {
    "vodka": 12,
    "whiskey": 9,
    "gin": 10,
    "redbull": 5
}

food_prices = {
    "pizza": 8,
    "pasta": 7,
    "burger": 9,
    "salad": 5
}

club_prices = {
    "casper": 15,
    "vog": 20,
    "partytura": 10,
    "eightball": 5,
    "mabel": 10
}


class PartyGuest:


    def __init__(self, name, surname, drink_preference, food_preference,club_price,cake_portion):
        self.name = name
        self.surname = surname
        self.drink_preference = drink_preference
        self.food_preference = food_preference
        self.club_price = club_price
        self.cake_portion = cake_portion


    def to_dict(self):
        return {
            "Name": self.name,
            "Surname": self.surname,
            "Drink Preference": self.drink_preference,
            "Food Preference": self.food_preference,
            "Cake Portion": self.cake_portion,
            "Club Fee" :self.club_price
        }

    def __str__(self):
        return (
            f"Name: {self.name}\n"
            f"Surname: {self.surname}\n"
            f"Drink Preference: {self.drink_preference}\n"
            f"Food Preference: {self.food_preference}\n"
            f"Cake Portion: {self.cake_portion}\n"
            f"Club Fee:  {self.club_price} € ""\n"
        )


guest_list = []

total_drink_cost = 0
total_food_cost = 0
total_cake_portions = 0

print("\n---- CLUB CHOICES ----\n")
print(list(club_prices.keys()))

club_fee = input(
    "Enter club for the party: "
).strip().casefold()

club_price = club_prices.get(club_fee, 0)

print("\n----- FOOD MENU -----")
print(list(food_prices.keys()))

print("\n----- DRINK MENU -----")
print(list(drink_prices.keys()))
print()

decision = int(input("Enter number of guests: ").strip())

print()
print("Cake portions go by 150 grams per person each portion costs 4€ ")
print()
for i in range(decision):

    name = input("Enter Name: ").strip()
    surname = input("Enter Surname: ").strip()
    drink_preference = input("Enter Drink Preference: ").strip().casefold()
    food_preference = input("Enter Food Preference: ").strip().casefold()
    cake_portion = int(input("Enter Cake Portion: ").strip())

    print()

    guest = PartyGuest(
        name,
        surname,
        drink_preference,
        food_preference,
        club_price,cake_portion

    )

    guest_list.append(guest)

    total_drink_cost += drink_prices.get(drink_preference, 0)
    total_food_cost += food_prices.get(food_preference, 0)
    club=club_price * decision
    total_cake_cost = 4 * decision

def Total_party_expenses(total_drink_cost, total_food_cost,club,total_cake_cost):
    return total_drink_cost + total_food_cost + club + total_cake_cost

print("---- PARTY GUEST LIST ----\n")

for guest in guest_list:
    print(guest)

guest_data = [guest.to_dict() for guest in guest_list]

with open("guests.json", "w") as file:
    json.dump(guest_data, file, indent=4)



    print("\n---- PARTY BILL ----\n")
    print(f"Total Drink Cost: {total_drink_cost}€")
    print(f"Total Food Cost: {total_food_cost}€")
    print(f"Total Cake Cost: {total_cake_cost}€")
    print(f"Club Cost: {club}€")
    print(f"Total Party Cost: {Total_party_expenses(total_drink_cost, total_food_cost,club,total_cake_cost)}€")
    print()
    print(f"Guest data saved to guests.json")