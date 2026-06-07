import art
import random as rnd
import game_data

SPACING = 15
overall_score = 0
people = game_data.people
game_over = False


def clear():
    print("\n" * SPACING)

def start():
    global overall_score
    global people
    global game_over

    item_a = rnd.choice(people)
    item_b = rnd.choice(people)

    is_item_a_higher = item_a['followers'] > item_b['followers']
    are_items_draw = item_a['followers'] == item_b['followers']

    print(art.logo)
    print(f"Your current score is: {overall_score}\n")
    print(f"{item_a["name"]} from {item_a['country']}")
    print(item_a["description"])
    print(art.vs)
    print(f"{item_b["name"]} from {item_b['country']}")
    print(item_b["description"])

    answer = input("Who has more followers in instagram? 'A' or 'B', or 'C' for draw: ")

    if answer.lower() == "c" and are_items_draw:
        overall_score += 1
    elif answer.lower() == "a" and is_item_a_higher:
        overall_score += 1
    elif answer.lower() == "b" and not is_item_a_higher:
        overall_score += 1
    else:
        clear()
        game_over = True
        print(art.game_over)
        print(f"\nYour total score is: {overall_score}")

    clear()

while not game_over:
    start()