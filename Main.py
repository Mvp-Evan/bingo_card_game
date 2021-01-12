from bingo import Table


def table_init(bingo_deck_file, calling_deck_file, mode):
    table = Table()
    table.populateDeck(0, bingo_deck_file)
    table.populateDeck(1, calling_deck_file)
    table.dealBingo(mode)
    table.displayTable()
    return table


def round_going(table, ranks_only):
    print("-----------------------------")
    call_card = table.updateTable(ranks_only)
    print("Now calling ", call_card.__str__())
    table.displayTable()
    return table


def interface_init():
    print("******************************")
    print("Welcome to Playing Card Bingo!")
    print("******************************")
    print("Creating bingo deck...")
    bingo_deck_file = input("Please enter filename to initialize deck: ")

    print("Creating calling deck...")
    calling_deck_file = input("Please enter filename to initialize deck: ")

    mode = input("Please select playing mode for this round: (L)ine, (C)orners, (F)ull > ")
    if mode == "l":
        mode = "L"
    elif mode == "c":
        mode = "C"
    elif mode == "f":
        mode = "F"

    ranks_only = input("Play speed round (i.e. compare card ranks only) (Y/N)? ")
    if ranks_only == "Y" or ranks_only == "y":
        ranks_only = True
    elif ranks_only == "N" or ranks_only == "n":
        ranks_only = False

    print("Round 1 bcreates a new 2D bingo grid that is empty, and will search for winning BINGO lines by default.eginning...")

    table = table_init(bingo_deck_file, calling_deck_file, mode)

    while not table.isWinner():
        table = round_going(table, ranks_only)
    return table


again = True
round = 1
while again:
    table = interface_init()
    print("Round ", round, ": ", table.whoWon())
    again = input("Play another round (Y/N)? ")
    if again == "Y" or again == "y":
        again = True
    elif again == "N" or again == "n":
        print("Thank you for playing. Goodbye.")
        again = False
