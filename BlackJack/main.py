import art
import card

cards = card.cards

will_play = input("Do you want to play BlackJack? 'y' for yes or 'n' for no: ")
if will_play.lower() == "y":
    card.start_game()
else:
    print(art.goodbye)