https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder


from Game import *

def printState(state):
    """
    print out the game
    :param state:
    :return:
    """
    landed = state.isLanded()

    for i in range(state.rows):

        rs = "|"

        for j in range(state.cols):

            # print(state.getFallerPos())

            if (i, j) in state.getFallerPos():

                if landed:

                    rs += '|' + state.getFallerPos()[(i, j)] + '|'

                else:

                     rs += '[' + state.getFallerPos()[(i, j)] + ']'

            else:


                chr = ' '

                if (i, j) in state.matched:

                    chr = '*'

                rs += chr + state.grid[i][j] + chr

        rs += "|"

        print(rs)

    print(' ' + '-' * (3 * state.cols) + ' ')



if __name__ == '__main__':

    DEBUG = False

    numrow = int(input())


    numcol = int(input())

    kind = input()

    if DEBUG:
        print(numrow)
        print(numcol)
        print(kind)


    grid = [0] * numrow

    for i in range(numrow):

        grid[i] = [' '] * numcol

    # if kind == "EMPTY":
    #
    #     for i in range(numrow + 1):
    #
    #         input()

    # print(grid)

    if kind == "CONTENTS":

        for i in range(numrow):

            l = input()

            if DEBUG:
                print(l)

            grid[i]  = l


    state = State(grid)

    while not state.gameover:

        printState(state)

        # read command
        command = input()


        if DEBUG:
            print(command)

        # run the command
        if command == '':


            state.step()


        elif command.startswith("F"):

            # print("faller")

            args = command.split()

            col = int(args[1]) - 1

            # jewls = args[2:5]

            state.createFaller(args[2], args[3], args[4], col)

            # print(state.faller)

        elif command == 'R':


            state.rotate()


        elif command == '>':

            state.right()

        elif command == '<':

            state.left()





        elif command == 'Q':

            break

    if state.gameover:

        printState(state)

        print('GAME OVER')






