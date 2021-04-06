from art import logo
import random

cards = [11,2,3,4,5,6,7,8,9,10,10,10]

def black_jack():
    print('\033c')
    print(logo)
    game_over = False
    player = [10,10,10]
    dealer = random.choices(cards, k=2)
    
    print(f"your cards: {player}, current score: {sum(cards)}")
    print(f"dealer's first card: {dealer[0]}")
    while not game_over:
        if sum(player) == 21:
            print(f"player final hand: {sum(player)}")
            print(f"dealer final hand: {sum(dealer)}")
            print("you win with blackjack")
            continue_game = input("wanna play a game of blackjack. type 'y' or 'n': ").lower()
            if continue_game == 'y':
                black_jack()
            else:
                exit()
        elif sum(player) > 21:
            if player.count(11) != 0 and ((sum(player)-10) <= 21):
                if (sum(player) - 10) == 21:
                    print(f"player final hand: {sum(player) -10}")
                    print(f"dealer final hand: {sum(dealer)}")
                    print("you win with blackjack")
                    continue_game = input("wanna play a game of blackjack. type 'y' or 'n': ").lower()
                    if continue_game == 'y':
                        black_jack()
                    else:
                        exit()
            else:
                print(f"player final hand: {sum(player)}")
                print(f"dealer final hand: {sum(dealer)}")
                print("you lose with bust")
                continue_game = input("wanna play a game of blackjack. type 'y' or 'n': ").lower()
                if continue_game == 'y':
                    black_jack()
                else:
                    exit()
                
black_jack()

def get_card(arr):
    arr.append(random.choice(cards))

