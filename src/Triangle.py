from Node import *


class Triangle:

    def __init__(self, removed_node):
        self.board = []
        self.removed_node = removed_node
        for i in range(0, 10):
            self.board.append(Node(i+1))
        self.add_all_relations_by_hand()
        self.board[removed_node-1].toggle()

    def add_all_relations_by_hand(self):
        """
        hahaha I'm an idiot. There's so much symmetry here for which I just haven't optimized
        """
        # 1 hops over 2 to get to 4, 3 to get to 6
        self.board[0].add_relation(self.board[1], self.board[3])
        self.board[0].add_relation(self.board[2], self.board[5])
        # 2 hops over 4 to get to 7, 5 to get to 9
        self.board[1].add_relation(self.board[3], self.board[6])
        self.board[1].add_relation(self.board[4], self.board[8])
        # 3 hops over 5 to get to 8, 6 to get to 10
        self.board[2].add_relation(self.board[4], self.board[7])
        self.board[2].add_relation(self.board[5], self.board[9])
        # 4 hops over 2 to get to 1, 5 to get to 6
        self.board[3].add_relation(self.board[1], self.board[0])
        self.board[3].add_relation(self.board[4], self.board[5])
        # 5 hops over nothing
        # center
        # 6 hops over 5 to get to 4, 3 to get to 1
        self.board[5].add_relation(self.board[4], self.board[3])
        self.board[5].add_relation(self.board[2], self.board[0])
        # 7 hops over 4 to get to 2, 8 to get to 9
        self.board[6].add_relation(self.board[3], self.board[1])
        self.board[6].add_relation(self.board[7], self.board[8])
        # 8 hops over 5 to get to 3, 9 to get to 10
        self.board[7].add_relation(self.board[4], self.board[2])
        self.board[7].add_relation(self.board[8], self.board[9])
        # 9 hops over 5 to get to 2, 8 to get to 7
        self.board[8].add_relation(self.board[4], self.board[1])
        self.board[8].add_relation(self.board[7], self.board[6])
        # 10 hops over 6 to get to 3, 9 to get to 8
        self.board[9].add_relation(self.board[5], self.board[2])
        self.board[9].add_relation(self.board[8], self.board[7])

    def get_board(self):
        return self.board

    def display(self):
        print(self)

    def get_all_moves(self):
        result = []
        for node in self.board:
            result += node.get_valid_moves()
        return result

    def move(self, relation):
        """
        make a move
        :param relation: list of 3 numbers. 2 hops over 0 to reach 1.
        """
        for i in relation:
            self.board[i-1].toggle()

    def __str__(self):
        TRIANGE_ROWS = 4
        board = self.board
        board_location = 0
        result = ""
        for i in range(1, TRIANGE_ROWS + 1):
            printable = ""
            for j in range(0, TRIANGE_ROWS + 1 - i):
                printable += " "
            for j in range(0, i):
                printable += board[board_location].__str__() + " "
                board_location += 1
            result += printable+"\n"
        return result
