import random
import json
import time

def current_output(message):
    """
    Send the mesage to current output format (console, logs, telegram, browser, etc.)
    """
    print(message)

def current_input():
    """
    Get the message from current input format (console, logs, telegram, browser, etc.)
    """
    message = str(input())
    return message


def standart_tests(C, D, c, d):
    # firs check
    if D > C > d > c:
        current_output('First check: Ok')
    else:
        current_output('Houston:  D > C > d > c')

    # second check
    if 2*C > (D + c):
        current_output('Second check: Ok')
    else:
        current_output('Houston: 2C > D + c')



def make_round(player1, player2, C=3, D=5, c=0, d=1):
    """
    Prisoner's dilemma game round modulation.

    Parameters:
    C, D, c, d - game parameters
    player1, player2 - players choices (0 or 1)

    Returns:
    tuple of players choices
    """
    if player1 == 1 and player2 == 1:
        return C, C
    elif player1 == 0 and player2 == 1:
        return D, c
    elif player1 == 1 and player2 == 0:
        return c, D
    elif player1 == 0 and player2 == 0:
        return d, d

def always_yes_bot(logs):
    return 1

def always_no_bot(logs):
    return 0

def random_bot(logs):
    return random.randint(0, 1)


def make_game(bot=random_bot, is_save=0, C=3, D=5, c=0, d=1):
    """
    Make a game of prisoner's dilemma for random number of rounds.
    Every round new choices are made.
    Full log is avilable

    Parameters:
    bot - bot function
    is_save - save logs to file if 1
    C, D, c, d - game parameters

    """

    number_of_rounds = random.randint(3, 10)
    player1_score = 0
    player2_score = 0
    logs = []
    for i in range(number_of_rounds):
        current_output("Round {i}".format(i=i))
        current_output("Your move")
        player1 = current_input()
        if player1 not in ['0', '1']:
            current_output("Invalid move: {player1}".format(player1=player1))
            current_output("it meant 0 for us")
            player1 = '0'
        player1 = int(player1)
        player2 = bot(logs)

        now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        round_res = make_round(player1, player2)
        
        player1_score = player1_score + round_res[0]
        player2_score = player2_score + round_res[1]

        iter_log = {
            'timestamp': now,
            'round': i,
            'player1': player1,
            'player2': player2,
            'player1_round_score': round_res[0],
            'player2_round_score': round_res[1],
            'player1_total_score': player1_score,
            'player2_total_score': player2_score
        }
        logs.append(iter_log)
        print(logs)
        
    current_output("Game over")
    current_output("Player 1 total score: {player1_score}".format(player1_score=player1_score))
    current_output("Player 2 total score: {player2_score}".format(player2_score=player2_score))

    if player1_score > player2_score:
        current_output("Player 1 wins")
    elif player1_score < player2_score:
        current_output("Player 2 wins")
    else:
        current_output("Draw")

    if is_save:
        with open('logs_{now}.json'.format(now=str(now)), 'w') as f:
            json.dump(logs, f)

    return logs

make_game(is_save=1)