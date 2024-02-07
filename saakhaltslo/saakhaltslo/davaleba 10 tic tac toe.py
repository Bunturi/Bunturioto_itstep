import random

while True:
    def print_b(board):
        print(f"{board[0]}  {board[1]}  {board[2]}")
        print(f"{board[3]}  {board[4]}  {board[5]}")
        print(f"{board[6]}  {board[7]}  {board[8]}")

    def ch_win(board):
        for i in range(3):
            if board[i] == board[i + 3] == board[i + 6] != ' ':
                return True
            if board[i * 3] == board[i * 3 + 1] == board[i * 3 + 2] != ' ':
                return True
        if (board[0] == board[4] == board[8] != ' ' or
                board[2] == board[4] == board[6] != ' '):
            return True
        return False

    def game():
        board = [' '] * 9
        plyr = 'X'
        comp = 'O'
        choices = [0, 1, 2, 3, 4, 5, 6, 7, 8]

        while True:

            plyr_ch = None
            print_b(board)

            while plyr_ch not in choices:
                plyr_ch = int(input("შეიყვანე რიცხვი 1დან 9ის ჩათვლით: "))-1

            choices.remove(plyr_ch)
            board[plyr_ch] = plyr

            if ch_win(board):
                print_b(board)
                print("თქვენ მოიგეთ!")
                break
            elif len(choices) < 1:
                print_b(board)
                print("ფრე!")
                break

            comp_ch = random.choice(choices)
            board[comp_ch] = comp
            choices.remove(comp_ch)
            if ch_win(board):
                print_b(board)
                print("კომპიუტერმა მოიგო!")
                break
    game()

    # თავიდან თამაში და ვალიდურობა
    while True:
        again = input("ითამაშებ თავიდან? (yes/no): ").lower()
        if again == "yes" or again == "no":
            break
    if again != "yes":
        break
print('დროებით!')
