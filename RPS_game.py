import random

def get_bot_move(previous_moves):
    # Example of a bot that repeats its last move
    if len(previous_moves) == 0:
        return random.choice(['rock', 'paper', 'scissors'])
    else:
        return previous_moves[-1]

def get_winner(player_move, bot_move):
    # Determine winner based on moves
    if player_move == bot_move:
        return 'draw'
    elif (player_move == 'rock' and bot_move == 'scissors') or \
         (player_move == 'paper' and bot_move == 'rock') or \
         (player_move == 'scissors' and bot_move == 'paper'):
        return 'player'
    else:
        return 'bot'

def play_game(player_strategy, bot_type, rounds=100):
    player_wins = 0
    for _ in range(rounds):
        previous_moves = []
        for _ in range(10):  # Play 10 rounds against the same bot
            player_move = player_strategy(previous_moves)
            bot_move = get_bot_move(previous_moves)
            winner = get_winner(player_move, bot_move)
            if winner == 'player':
                player_wins += 1
            previous_moves.append(player_move)
    win_percentage = (player_wins / (rounds * 10)) * 100
    print(f"Against Bot {bot_type}: Player wins {win_percentage}% of the games.")

# Example of playing against different bots
play_game(lambda moves: 'rock', "Type 1")
play_game(lambda moves: random.choice(['rock', 'paper', 'scissors']), "Type 2")
# Implement more strategies for other bot types (Type 3, Type 4) based on observed behavior

