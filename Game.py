https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder

class Faller:
    """
    class for faller object
    """

    def __init__(self, jewels, col):

        self.jewels = jewels
        self.col = col
        self.row = 0

    def rotate(self):

        self.jewels = self.jewels[2:] + self.jewels[:2]

    def getFallerPos(self):

        h = {}
        for i in range(3):

            h[(self.row - i, self.col)] = self.jewels[2 - i]

        return h


class State:
    """
    class for game state
    """
    def __init__(self, grid):

        self.rows = len(grid)

        self.cols = len(grid[0])

        self.grid = self.fallDown(grid)

        self.faller = None

        self.gameover = False

        # matched positions
        self.matched = self.findAllMatch()

    def getFallerPos(self):
        """
        :return: {faller position -> character}
        """

        if self.faller is not None:

            return self.faller.getFallerPos()

        else:

            return {}


    def fallDown(self, grid):
        """

        :param grid:
        :return: a new grid with jewel falling down
        """

        newGrid = [0] * self.rows

        for i in range(self.rows):

            newGrid[i] = [' '] * self.cols


        for j in range(self.cols):

            c = ''

            for i in range(self.rows-1, -1, -1):


                if grid[i][j] != ' ':

                    c += grid[i][j]

            if len(c) < self.rows:

                c += ' ' * (self.rows - len(c))

            for i in range(self.rows):


                newGrid[self.rows - i - 1][j] = c[i]


        return newGrid


    def validCoord(self, row, col):
        """

        :param row:
        :param col:
        :return: whether coordinate valid
        """

        if row >= self.rows or row < 0:

            return False

        if col >= self.cols or col < 0:
            return False


        return True


    def findAllMatch(self):

        """
        :return: all matched positions
        """

        dirs = [(0, 1),  (1, 0), (-1, 1), (1, 1)]

        matched = []

        for i in range(self.rows):
            for j in range(self.cols):

                for di, dj in dirs:

                    matched.extend(self.findMatch(i, j, di, dj))


        return matched




    def findMatch(self, i, j, di, dj):
        """

        :param i:
        :param j:
        :param di:
        :param dj:
        :return: matched positions found starting from i, j
        """

        # x = i
        # y = j

        color = self.grid[i][j]

        if color == ' ':

            return []

        matched = [(i, j)]

        for k in range(1, 3):

            i += di

            j += dj

            # if x == 3 and y == 0:
            #
            #     print(i, j)

            if not self.validCoord(i, j):

                return []

            if self.grid[i][j] != color:


                return []

            matched.append((i, j))

        # if x == 3 and y == 0:
        #
        #     print(matched)

        return matched


    def createFaller(self, j1, j2, j3, col):
        """
        create a faller
        :param j1:
        :param j2:
        :param j3:
        :param col:
        :return: None
        """

        if self.faller is  None:

            self.faller = Faller([j1, j2, j3], col)

            # print("create faller")
            #
            # print(self.faller)

        # else:
        #
        #
        #     print("77777")
        #
        #     print(self.faller)

    def rotate(self):
        """
        rotate the faller
        :return:
        """
        if self.faller is not None:
            self.faller.rotate()


    def canFallerIn(self, row, col):
        """

        :param row:
        :param col:
        :return: whether faller can move into row, col
        """
        # if row >= self.rows or row < 0:
        #
        #     return False
        #
        # if col >= self.grid or col < 0:
        #     return False

        if not self.validCoord(row, col):

            return False

        if self.grid[row][col] != ' ':
            return False

        if row - 1 >= 0 and self.grid[row - 1][col] != ' ':
            return False

        if row - 2 >= 0 and self.grid[row - 2][col] != ' ':
            return False

        return True

    def right(self):
        """
        move right
        :return:
        """

        if self.faller is not None:

            if self.canFallerIn(self.faller.row, self.faller.col + 1):

                self.faller.col += 1

    def left(self):
        """
        move left
        :return:
        """

        if self.faller is not None:

            if self.canFallerIn(self.faller.row, self.faller.col - 1):

                self.faller.col -= 1


    def isLanded(self):
        """
        whether faller landed
        :return:
        """
        if self.faller is None:

            return False

        return not self.canFallerIn(self.faller.row + 1, self.faller.col)


    def removeMatch(self):
        """
        remove matched jewels
        :return:
        """
        for i, j in self.matched:

            self.grid[i][j] = ' '

        self.grid = self.fallDown(self.grid)

    def step(self):
        """
        run one step
        :return:
        """
        if self.matched:

            self.removeMatch()

            self.matched = self.findAllMatch()

        if self.faller is not None:

            if self.isLanded():


                if self.faller.row - 2  < 0:

                    self.gameover = True

                for i in range(self.faller.row, max(self.faller.row - 3,-1), -1):

                    self.grid[i][self.faller.col] = self.faller.jewels[2 - (self.faller.row - i)]


                self.faller = None

                self.matched = self.findAllMatch()

            else:
                self.faller.row += 1


