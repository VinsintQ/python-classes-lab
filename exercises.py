class Game:

    def __init__(self):
        self.turn = True
        self.winer = False

        self.board = {
            "a1": None,
            "b1": None,
            "c1": None,
            "a2": None,
            "b2": None,
            "c2": None,
            "a3": None,
            "b3": None,
            "c3": None,
        }
        self.print_board()
        while not self.winer:
            self.userin = input("select a place")
            if self.userin in (  # valid inputs
                "a1",
                "a2",
                "a3",
                "b1",
                "b2",
                "b3",
                "c1",
                "c2",
                "c3",
            ):
                self.add(self.userin)
            else:
                print("invalid position")

    def add(self, position):
        self.used = []
        self.userin = position
        self.used += self.userin
        b = self.board

        if b[self.userin]:  # check if place is not taken
            print("place is taken")
        else:
            if self.turn:
                self.turn = False
                b[self.userin] = "X"
                if (
                    (b["a1"] == b["a2"] == b["a3"] == "X")
                    or (b["b1"] == b["b2"] == b["b3"] == "X")
                    or (b["c1"] == b["c2"] == b["c3"] == "X")
                    or (b["a1"] == b["b1"] == b["c1"] == "X")
                    or (b["a2"] == b["b2"] == b["c2"] == "X")
                    or (b["a3"] == b["b3"] == b["c3"] == "X")
                    or (b["a1"] == b["b2"] == b["c3"] == "X")
                    or (b["a3"] == b["b2"] == b["c1"] == "X")
                ):
                    print("--------")
                    print("Winner X")
                    self.winer = True
            else:
                self.turn = True
                b[self.userin] = "O"
                if (
                    (b["a1"] == b["a2"] == b["a3"] == "O")
                    or (b["b1"] == b["b2"] == b["b3"] == "O")
                    or (b["c1"] == b["c2"] == b["c3"] == "O")
                    or (b["a1"] == b["b1"] == b["c1"] == "O")
                    or (b["a2"] == b["b2"] == b["c2"] == "O")
                    or (b["a3"] == b["b3"] == b["c3"] == "O")
                    or (b["a1"] == b["b2"] == b["c3"] == "O")
                    or (b["a3"] == b["b2"] == b["c1"] == "O")
                ):
                    print("--------")
                    print("Winner O")
                    self.winer = True
            print(
                f"""
           A   B   C
        1)  {b['a1'] or ' '} | {b['b1'] or ' '} | {b['c1'] or ' '}
           ----------
        2)  {b['a2'] or ' '} | {b['b2'] or ' '} | {b['c2'] or ' '}
           ----------
        3)  {b['a3'] or ' '} | {b['b3'] or ' '} | {b['c3'] or ' '}
            """
            )

    def print_board(self):
        b = self.board
        print(
            f"""
           A   B   C
       1)  {b['a1'] or ' '} | {b['b1'] or ' '} | {b['c1'] or ' '}
           ----------
       2)  {b['a2'] or ' '} | {b['b2'] or ' '} | {b['c2'] or ' '}
           ----------
       3)  {b['a3'] or ' '} | {b['b3'] or ' '} | {b['c3'] or ' '}
         """
        )


newGame = Game()
