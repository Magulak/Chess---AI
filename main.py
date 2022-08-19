#  (type_of_piece)
class Chess:

    def move(self, board, x1, y1, x2, y2):
        """
        :param board: -  chess_board
        :param x1: - x coordinate of chess_piece that will be moved
        :param y1: - y coordinate of chess_piece that will be moved
        :param x2: - x coordinate of desired place
        :param y2: - y coordinate of desired place
        :return: return change chess_board to state after the move / deny if move is illegal
        """

        """  
        bishop movement is going to be represented by bishopmovement.png
        """

        def attack(self):
            print("attack")
        #If friendly piece encounters enemy piece on its move, the enemy piece gets destroyed

        print("if:"
              " \n - Desired spot is empty"
              " \n - Selected piece have move_set that allows him to move there"
              " \n - No checkmate")

    def move_set(self, type_of_piece, x, y):
        empty_board = \
            ((0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)), \
            ((0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)), \
            ((0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)), \
            ((0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)), \
            ((0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)), \
            ((0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)), \
            ((0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)), \
            ((0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)),

        """
        move_set()
        """

        """
                NEEDS FIXING
                :param y: y coordinate
                :param x: x coordinate
                :param type_of_piece: - e.g king(1) ,queen(6), pawn(2)
                :return:

                function will return move_set of specified chess_piece
                eg. king(1)

                current place = empty_board[x][y]

                return # this is stupid, i wrote it just to show the idea
                
                [x-1][y+1], [x][y+1], [x+1][y+1],
                [x-1][y],[x+1][y]
                [x-1][y-1], [x][y-1], [x+1][y-1],

                """



    # what board is better? chess_board or chess_board2 ?
    chess_board = \
        (5, 4, 3, 1, 6, 3, 4, 5), \
        (2, 2, 2, 2, 2, 2, 2, 2), \
        (0, 0, 0, 0, 0, 0, 0, 0), \
        (0, 0, 0, 0, 0, 0, 0, 0), \
        (0, 0, 0, 0, 0, 0, 0, 0), \
        (0, 0, 0, 0, 0, 0, 0, 0), \
        (2, 2, 2, 2, 2, 2, 2, 2), \
        (5, 4, 3, 6, 1, 3, 4, 5),

    chess_board2 = \
        ((5, 2), (4, 2), (3, 2), (1, 2), (6, 2), (3, 2), (4, 2), (5, 2)), \
        ((2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2)), \
        ((0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)), \
        ((0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)), \
        ((0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)), \
        ((0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)), \
        ((2, 1), (2, 1), (2, 1), (2, 1), (2, 1), (2, 1), (2, 1), (2, 1)), \
        ((5, 1), (4, 1), (3, 1), (6, 1), (1, 1), (3, 1), (4, 1), (5, 1)),

    #  (type_of_piece, Enemy/Ally)
    """
    The King == 1
    The Pawn == 2
    The Bishop == 3
    The Knight == 4
    The Rook == 5
    The Queen == 6
    
    (0 , 0) == empty
    (x , 1) == white
    (x , 2) == black
    """
