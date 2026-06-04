import art
import random

cards= {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11  # Or 1 if total is pass 21, dynamically handled in logic
}

def start_game():
    print(art.logo)

    your_cards = get_cards(2)
    computer_cards = get_cards(2)
    your_score = calculate(your_cards)
    computer_score = calculate(computer_cards)

    print(f"Your cards: [{your_cards[0]}, {your_cards[1]}], current score: {your_score}")
    print(f"Dealer's first card: {computer_cards[0]}\n\n")

    will_draw = input("Type 'y' to get another card, type 'n' to pass: ")
    if will_draw.lower() == 'y':
        your_cards.extend(get_cards(1))
        your_score = calculate(your_cards)

        if computer_score <= 16:
            computer_cards.extend(get_cards(1))
            computer_score = calculate(computer_cards)

        show_cards(your_cards, computer_cards)
        process_winner(your_score, computer_score)
    else:
        if computer_score <= 16:
            computer_cards.extend(get_cards(1))
            computer_score = calculate(computer_cards)

        show_cards(your_cards, computer_cards)
        process_winner(your_score, computer_score)

def process_winner(your_score, computer_score):
    print(f"Your final score: {your_score} vs Dealer's final score: {computer_score}")
    if your_score > computer_score and your_score <= 21:
        print(art.win)
    elif your_score > computer_score and your_score > 21:
        print(art.lose)
    elif computer_score > your_score and computer_score <= 21:
        print(art.lose)
    elif computer_score > your_score and computer_score > 21:
        print(art.win)
    else:
        print(art.goodbye)

    will_continue = input("\nType 'y' to continue or 'n' to stop: ")
    if will_continue.lower() == 'y':
        print("\n" * 15)
        start_game()
    else:
        print(art.goodbye)

def get_cards(draw_number: int = 1):
    on_hand = []
    for x in range(draw_number):
        card = random.choice(list(cards))
        on_hand.append(card)
    return on_hand

def calculate(on_hand_cards):
    list_of_cards = []
    for on_hand in on_hand_cards:
        list_of_cards.append(cards[on_hand])

    total = sum(list_of_cards)
    if total > 21:
        if "A" in on_hand_cards:
            total -= 10

    return total

def show_cards(deck1, deck2):
    print(f"\nYour cards are: {deck1}")
    print(f"Dealer cards are: {deck2}\n")