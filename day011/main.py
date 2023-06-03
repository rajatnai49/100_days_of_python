from art import logo
import random
import click


def blackJack_game():

    def deal_cards(cards):
        return random.choice(cards)

    def play_again():
        play_again = input("Do you want to play again y/n?: ")
        if play_again == 'y':
            click.clear()
            blackJack_game()
        else:
            print("Sayonara!!")

    def hit_action():
        hit = input("You want another card or not y/n?: ")
        if hit == 'n':
            done_playing()
        elif hit == 'y':
            keep_playing()

    def player_win():
        if sum(dealer_cards) > 21:
            return True
        elif sum(player_cards) != 21 and sum(dealer_cards) == 21:
            return False
        elif sum(player_cards) == 21 and sum(dealer_cards) == 21:
            return False
        elif sum(player_cards) == 21 and sum(dealer_cards) != 21:
            return True
        elif sum(player_cards) > 21:
            return False
        elif sum(player_cards) > sum(dealer_cards):
            return True
        return False

    def done_playing():
        print(
            f"Your hand is: {player_cards}, a total sum is {sum(player_cards)}")
        print(
            f"Dealer's hand is: {dealer_cards}, a total sum is {sum(dealer_cards)}")
        if player_win():
            print("You WON!!")
        elif sum(player_cards) == sum(dealer_cards):
            print("It's Draw!!")
        else:
            print("You LOSE!!")
        play_again()

    def keep_playing():
        player_cards.append(deal_cards(cards))
        dealer_cards.append(deal_cards(cards))
        if 11 in player_cards and sum(player_cards) >= 21:
            a = player_cards.index(11)
            player_cards[a] = 1
        print(f"Your hand is: {player_cards}, a total is {sum(player_cards)}")
        print(
            f"Dealer's hand is: {dealer_cards}, a total is {sum(dealer_cards)}")
        if sum(player_cards) > 21:
            print("You Lose!!")
            play_again()
        if sum(player_cards) <= 21:
            hit_action()

    click.clear()
    print(logo)
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    player_cards = []
    dealer_cards = []
    player_cards.append(deal_cards(cards))
    player_cards.append(deal_cards(cards))
    dealer_cards.append(deal_cards(cards))
    print(f"Your cards are: {player_cards}")
    print(f"Dealer cards are: {dealer_cards}")
    hit_action()


# start game
blackJack_game()
