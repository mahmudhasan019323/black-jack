from art import logo
import random

cards = [11,2,3,4,5,6,7,8,9,10,10,10]
def get_card(arr):
    arr.append(random.choice(cards))

def show_result(player_list,dealer_list,msg):
    print(f"player final hand  {player_list}: {sum(player_list)}")
    print(f"dealer final hand  {dealer_list}: {sum(dealer_list)}")
    print(msg)
    continue_game = input("wanna play a game of blackjack. type 'y' or 'n': ").lower()
    if continue_game == 'y':
        black_jack()
    else:
        exit()

def black_jack():
    print('\033c')
    print(logo)
    game_over = False
    player = random.choices(cards, k=2)
    dealer = random.choices(cards, k=2)
    while not game_over:
        print(f"your cards: {player}, current score: {sum(player)}")
        print(f"dealer's first card: {dealer[0]}")
        if sum(player) == 21:
            show_result(player,dealer,'you won with blackjack')
            
        elif sum(player) > 21:
            if player.count(11) != 0 and ((sum(player)-10) <= 21):
                if (sum(player) - 10) == 21:
                    show_result(player,dealer, 'you won with blackjack')
                    
                else:
                    player[player.index(11)] = 1
            else:
                show_result(player,dealer, 'you lost with bust')
                
        else:
            hit = input("get another card? type 'y' or 'n': ").lower()
            if hit == 'y':
                get_card(player)
            else:
                if sum(dealer)< 16:
                    while sum(dealer)< 16:
                        get_card(dealer)
                if sum(dealer) > 21:
                    if dealer.count(11) != 0 and ((sum(dealer)-10) <= 21):
                        if (sum(dealer) - 10) == 21:
                            show_result(player,dealer, 'you won with blackjack')
                            
                    else:
                        show_result(player,dealer, 'you lost with bust')
                        
                else:
                    if sum(player) > sum(dealer):
                        show_result(player,dealer, 'you win')
                        
                    elif sum(player) < sum(dealer):
                        show_result(player,dealer, 'you lose')
                        
                    else:
                        show_result(player,dealer, "it's a draw" )
                        
black_jack()



