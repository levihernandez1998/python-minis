import art
import random as rnd
import game_data

overall_score = 0
people = game_data.people
game_over = False
item_a = rnd.choice(people)
item_b = None

def description(person):
    print(f"{person["name"]} from {person['country']}")
    print(person["description"])

def clear():
    print("\n" * 15)

def start():
    global overall_score
    global game_over
    global item_a
    global item_b

    item_b = rnd.choice(people)
    is_item_a_higher = item_a['followers'] > item_b['followers']
    are_items_draw = item_a['followers'] == item_b['followers']

    print(art.logo)
    print(f"Your current score is: {overall_score}\n")
    description(item_a)
    print(art.vs)
    description(item_b)

    answer = input("Who has more followers in instagram? 'A' or 'B', or 'C' for draw: ")

    if answer.lower() == "c" and are_items_draw:
        overall_score += 1
        item_b = rnd.choice(people)
    elif answer.lower() == "a" and is_item_a_higher:
        overall_score += 1
        item_b = rnd.choice(people)
    elif answer.lower() == "b" and not is_item_a_higher:
        overall_score += 1
        item_a = item_b
        item_b = rnd.choice(people)
    else:
        clear()
        game_over = True
        print(art.game_over)
        print(f"\nYour total score is: {overall_score}")

    clear()

while not game_over:
    start()