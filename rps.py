import random
print('Basic Rock Paper Scissors Game\n')
try:
    rounds = int(input('How many times do you want to play?: '))
except:
    print('Invalid Number - Restart')
try:
    while rounds >= 0:
        def play():
            user = input("Whats your choice? 'r' for rock, 'p' for paper, 's' for scissors:\n")
            user = user.lower()
            if user in ('r' , 'p', 's'):
                bot = random.choice(['r', 'p', 's'])
                if user == bot:
                    return "You and the bot have chosen {}. Its a tie!!".format(bot)
                if you_win(user, bot): #rock beats scissors, scissors beats paper, paper beats rock (p>r, s>p, r>s)
                    return "You have chosen {} and the bot has chosen {}. You won!!!".format(user, bot)
                return "You have chosen {} and the bot has chosen {}. You lost".format(user, bot)
            else:
                print('Invalid Entry')
        def you_win(player, rival): #(p>r, s>p, r>s)
            if (player == 'r' and rival == 's') or (player == 'p' and rival == 'r') or (player == 's' and rival == 'p'):
                return True
            return False
        rounds = rounds - 1
        if int(rounds)== -1:
            print("\n\nProgram Terminated\nGo Check out my Github:github.com/abutalhaalam")
            break
        if __name__ == '__main__':
            print(play()) #github.com/abutalhaalam
except:
    print('Program will not work this way')
