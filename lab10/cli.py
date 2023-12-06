# cli.py

from logic import Game, Human, Bot

def play_game():
    game = Game()
    human_player = Human()
    bot_player = Bot()
    available_moves = list(range(1, 10))
    first_move = None

    while not game.leaveLoop:
        if game.turnCounter % 2 == 0:
            game.print_board()
            number_picked = human_player.make_move(available_moves)
            if first_move is None:
                first_move = number_picked
            if number_picked in available_moves:
                available_moves.remove(number_picked)
                game.modify_array(number_picked)
                game.other_player()
            else:
                print("Invalid input. Please try again.")
            game.turnCounter += 1
        else:
            other_player_choice = bot_player.make_move(available_moves)
            print("\nOther Player's Choice:", other_player_choice)
            if other_player_choice in available_moves:
                available_moves.remove(other_player_choice)
            game.modify_array(other_player_choice)
            game.other_player()
            game.turnCounter += 1

        winner = game.get_winner()
        if winner != "N":
            game.print_board()
            print(f"{winner} won!")
            result = "Win"
            break
        elif game.turnCounter == 9:
            game.print_board()
            print("It's a draw!")
            result = "Draw"
            break

    winner = game.get_winner()
    player1 = "Human" if winner == "X" else "Bot"
    player2 = "Bot" if winner == "X" else "Human"
    moves = game.turnCounter

    game.log_game(winner, player1, player2, moves, first_move, result)


if __name__ == '__main__':
    play_game()