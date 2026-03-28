import prisoner as prs

prs.current_output("Hello! Lets' play a prisoner's dilemma game?")
prs.current_output("You can choose a bot")
prs.current_output("1 - always yes bot")
prs.current_output("2 - always no bot")
prs.current_output("3 - random bot")
prs.current_output("4 - tit_for_tat")

bot_choice = prs.current_input()

if bot_choice == '1':
    player2 = prs.always_yes_bot
elif bot_choice == '2':
    player2 = prs.always_no_bot
elif bot_choice == '3':
    player2 = prs.random_bot
elif bot_choice == '4':
    player2 = prs.tit_for_tat
else:
    prs.current_output("Invalid choice")
    exit()

logs = prs.make_game(
    player1=prs.human_control, 
    player2=player2
    )