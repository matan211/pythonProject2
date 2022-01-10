from game_cards.CardGame import CardGame
name1 = input("enter player name: ")
name2 = input("enter player name: ")
game = CardGame(name1, name2)
for i in range(10):
    print("round", i+1)
    c1 = game.player1.get_card()
    c2 = game.player2.get_card()
    print(f"{game.player1.name}'s card is: {c1}")
    print(f"{game.player2.name}'s card is: {c2}")
    if c1 > c2:
        game.player1.add_card(c1)
        game.player1.add_card(c2)
        print(f"the winner in this round is: {game.player1.name}")
    else:
        game.player2.add_card(c2)
        game.player2.add_card(c1)
        print(f"the winner in this round is: {game.player2.name}")
    print()

if game.get_winner() is None:
    print("tie")
else:
    print(f"the winner is: {game.get_winner().name}")
