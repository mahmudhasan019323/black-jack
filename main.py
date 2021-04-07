from art import logo
import random

cards = [11,2,3,4,5,6,7,8,9,10,10,10]
def get_card(arr):
    arr.append(random.choice(cards))

def black_jack():
    print('\033c')
    print(logo)
    game_over = False
    player = random.choices(cards, k=2)
    # player = [10,4]
    dealer = random.choices(cards, k=2)
    while not game_over:
        print(f"your cards: {player}, current score: {sum(player)}")
        print(f"dealer's first card: {dealer[0]}")
        if sum(player) == 21:
            print(f"player final hand  {player}: {sum(player)}")
            print(f"dealer final hand  {dealer}: {sum(dealer)}")
            print("you win with blackjack")
            continue_game = input("wanna play a game of blackjack. type 'y' or 'n': ").lower()
            if continue_game == 'y':
                black_jack()
            else:
                exit()
        elif sum(player) > 21:
            if player.count(11) != 0 and ((sum(player)-10) <= 21):
                if (sum(player) - 10) == 21:
                    print(f"player final hand  {player}: {sum(player) -10}")
                    print(f"dealer final hand  {dealer}: {sum(dealer)}")
                    print("you win with blackjack")
                    continue_game = input("wanna play a game of blackjack. type 'y' or 'n': ").lower()
                    if continue_game == 'y':
                        black_jack()
                    else:
                        exit()
                else:
                    player[player.index(11)] = 1
            else:
                print(f"player final hand  {player}: {sum(player)}")
                print(f"dealer final hand  {dealer}: {sum(dealer)}")
                print("you lose with bust")
                continue_game = input("wanna play a game of blackjack. type 'y' or 'n': ").lower()
                if continue_game == 'y':
                    black_jack()
                else:
                    exit()
        else:
            hit = input("get another card? type 'y' or 'n': ").lower()
            # hit = 'n'
            if hit == 'y':
                get_card(player)
            else:
                if sum(dealer)< 16:
                    while sum(dealer)< 16:
                        get_card(dealer)
                if sum(dealer) > 21:
                    if dealer.count(11) != 0 and ((sum(dealer)-10) <= 21):
                        if (sum(dealer) - 10) == 21:
                            print(f"player final hand  {player}: {sum(player) -10}")
                            print(f"dealer final hand  {dealer}: {sum(dealer)}")
                            print("you win with blackjack")
                            continue_game = input("wanna play a game of blackjack. type 'y' or 'n': ").lower()
                            if continue_game == 'y':
                                black_jack()
                            else:
                                exit()
                    else:
                        print(f"player final hand  {player}: {sum(player)}")
                        print(f"dealer final hand  {dealer}: {sum(dealer)}")
                        print("you lose with bust")
                        continue_game = input("wanna play a game of blackjack. type 'y' or 'n': ").lower()
                        if continue_game == 'y':
                            black_jack()
                        else:
                            exit()
                else:
                    if sum(player) > sum(dealer):
                        print(f"player final hand  {player}: {sum(player)}")
                        print(f"dealer final hand  {dealer}: {sum(dealer)}")
                        print("you WIN!")
                        continue_game = input("wanna play a game of blackjack. type 'y' or 'n': ").lower()
                        if continue_game == 'y':
                            black_jack()
                        else:
                            exit()
                    elif sum(player) < sum(dealer):
                        print(f"player final hand  {player}: {sum(player)}")
                        print(f"dealer final hand  {dealer}: {sum(dealer)}")
                        print("you lose!")
                        continue_game = input("wanna play a game of blackjack. type 'y' or 'n': ").lower()
                        if continue_game == 'y':
                            black_jack()
                        else:
                            exit()
                    else:
                        print(f"player final hand  {player}: {sum(player)}")
                        print(f"dealer final hand  {dealer}: {sum(dealer)}")
                        print("it's a draw")
                        continue_game = input("wanna play a game of blackjack. type 'y' or 'n': ").lower()
                        if continue_game == 'y':
                            black_jack()
                        else:
                            exit()
black_jack()



