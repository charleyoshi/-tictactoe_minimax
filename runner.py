import tictactoe as ttt


while True:
    input('Press to Continue...')
    mode = input('Choose your opponent (1 - 4): '
                   '\n\t1. Easy (random)'
                   '\n\t2. Medium (hard-coded)'
                   '\n\t3. Boss (Artificial Intelligence Minimax)'
                   '\n\t4. Quit\n\t')
    try:
        mode = int(mode)
        if mode == 4:
            break
        elif mode in [1, 2, 3]:
            ttt.play(mode)
        else:
            print('Not in 1-4')
    except ValueError:
        print('Enter an Integer')

