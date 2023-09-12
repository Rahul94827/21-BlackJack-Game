############### Blackjack Project #####################
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#generating random cards
def deal_card():
  return random.choice(cards)
#calculating the score and finding of blackjack
def calculate_score(cards):
  if 11 in cards and 10 in cards and len(cards)==2:
    return 0
  if 11 in cards and sum(cards)>21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)
#comparing user and computer card
def compare(user_score,comp_score):
    if user_score==comp_score:
      return "Draw"
    elif comp_score==0:
      return "Lose,opponent has Blackjack"
    elif user_score==0:
      return "Win with a Blackjack"
    elif user_score>21:
      return "You went over.Y0u lose"
    elif comp_score>21:
      return "Opponent went over,You won"
    elif user_score>comp_score:
      return "You Win"
    else:
      return "You lose"

def playgame():
  user_cards = []
  computer_cards = []
  is_game_over=False

  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  
  while not is_game_over:
    user_score=calculate_score(user_cards)
    comp_score=calculate_score(computer_cards)
    print(f"Your cards : {user_cards},current score: {user_score}")
    print(f"Computer first cards : {computer_cards[0]}")
    if user_score==0 or comp_score==0 or user_score>21:
      is_game_over=True
    else:
      user_should_deal=input("Type 'y' for getting another card,type 'n' to pass")
      if user_should_deal=='y':
        user_cards.append(deal_card())
      else:
        is_game_over=True
 
  while comp_score!=0 and comp_score<17:
    computer_cards.append(deal_card())
    comp_score=calculate_score(computer_cards)
  
  print(f"Your final cards:{user_cards},final_score:{user_score}")
  print(f"Computer final cards:{computer_cards},final_score:{comp_score}")
  print(compare(user_score,comp_score))

while input("Do you want to play Blackjack game?Type 'y' or 'n'")=='y':
  playgame()
