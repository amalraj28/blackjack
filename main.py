import random
from replit import clear
from colorama import Fore, init
from art import logo

init()
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def result(user, comp):
    # Based on the rules of the game, scores are compared and outcome is obtained here
    score_of_user = sum(user)
    score_of_comp = sum(comp)

    if score_of_user > 21:
        outcome = Fore.GREEN + 'You went over. You lose 😭'

    elif score_of_user == 21 and len(user) == 2:
        outcome = Fore.BLUE + 'Win with a Blackjack 😎'

    elif score_of_comp == 21 and len(comp) == 2:
        outcome = Fore.GREEN + 'Lose, opponent has Blackjack 😱'

    elif score_of_comp > 21:
        outcome = Fore.BLUE + 'Opponent went over. You win 😁'

    elif score_of_user == score_of_comp:
        outcome = 'Draw 🙃'

    elif score_of_user > score_of_comp:
        outcome = Fore.BLUE + 'You win 😃'

    else:
        outcome = Fore.GREEN + 'You lose 😤'

    print(f'Your final hand: {user}, final score: {score_of_user}')
    print(f'Computer\'s final hand: {comp}, final score: {score_of_comp}')
    print(outcome + Fore.RESET)


def check_for_11_in_list(lst):
    # If the sum of scores exceeds 21 and 11 is present, then all 11's are replaced by 1 one by one till sum is lower than 21
    while lst.count(11):
        if sum(lst) > 21:
            lst.remove(11)
            lst.append(1)
        else:
            break


def modify_comp_score(user_scores, comp_scores):
    # First, the computer scores are chosen till count of scores of user and  computer is same
    comp_scores.extend(random.choices(cards, k=len(user_scores)-1))

    while True:
        # Computer scores are checked whether they have gone over and have 11 in them simultaneously
        check_for_11_in_list(comp_scores)

        sum_comp = sum(comp_scores)

        # If sum of computer scores is less than 17, then it has to choose another card. This is a rule of the game.
        if sum_comp < 17:
            comp_scores.append(random.choice(cards))
        else:
            break

    # After all the list modifications, scores are compared and result is obtained
    result(user_scores, comp_scores)


def modify_user_score(user, comp):

    print(f'User: {user}, User score: {sum(user)}')
    print(f'Computer: {comp}')
    choice = input(f'Type \'y\' to play and \'n\' to pass: ').lower()

    if choice == 'y':
        user.append(random.choice(cards))   # If user wants to play on, another card is randomly chosen

        # The user scores are now added and if the sum is greater than 21, then if 11 is there, it's replaced by 1
        check_for_11_in_list(user)
        # If after modification, sum is greater than 21, then the user has gone over and hence lost.
        if sum(user) > 21:
            result(user, comp)
        else:
            # If sum is not greater than 21, then recursion is made to occur till user decides to pass
            modify_user_score(user, comp)

    elif choice == 'n':
        modify_comp_score(user, comp)   # Once user passes, then computer score is decided


def main():     # Game begins here

    choice = input(f'Do you want to play a game of Blackjack? Type \'y\' or \'n\': ').lower()

    if choice == 'y':
        clear()
        print(Fore.CYAN + logo + Fore.RESET)

        # 2 cards are randomly picked for user and 1 card for computer
        user_scores = random.choices(cards, k=2)
        comp_scores = random.choices(cards, k=1)

        # Now user score is modified based on whether the user wants to play or pass
        modify_user_score(user_scores, comp_scores)

    else:
        raise KeyboardInterrupt


while True:     # Program will be endless until user interrupts it or if they refuse to play the game
    try:
        if __name__ == '__main__':  # Program begins here
            main()
    except KeyboardInterrupt:
        print(Fore.RED + '\nGame stopped by user!!!' + Fore.RESET)
        break
