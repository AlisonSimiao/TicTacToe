from GColor import print_color, print_error,print_elemento, print_success, rows,clear

TicTacToe = [ 0,  0,  0,
              0,  0,  0,
              0,  0,  0]

players = ["O", "X"]
Time = 0

def value(v, p=False):
    if p:
        return players[v]

    if v == 0:
        print_color(0, 114, 187, "   ")
    elif v == 1:
        print_color(143, 201, 58, " X ")
    else:
        print_color(0, 114, 187, " O ")

def printTable():
    for i in range(0, 9):
        if i % 3 == 0:
            rows(13)
            print_elemento("\n|")

        value(TicTacToe[i])

        print_elemento("|")
    rows(13)
    print()


def win():
    Status = 0
    for i in range(0, 3):
        row_win = TicTacToe[i*3] == TicTacToe[i*3 +
                                              1] == TicTacToe[i*3+2] and not TicTacToe[i*3] == 0
        if row_win:
            clear()
            printTable()
            print_success("o jogador {jogador} ganhou".format(
                jogador=value(TicTacToe[i*3], True)))
            Status = TicTacToe[i*3]
            break

        col_win = TicTacToe[i] == TicTacToe[i +
                                            3] == TicTacToe[6+i] and not TicTacToe[i] == 0
        if col_win:
            clear()
            printTable()
            print_success("o jogador {jogador} ganhou".format(
                jogador=value(TicTacToe[i], True)))
            Status = TicTacToe[i]
            break

    diag_main = TicTacToe[0] == TicTacToe[4] == TicTacToe[8] and not TicTacToe[0] == 0
    if diag_main:
        clear()
        printTable()
        print_success("o jogador {jogador} ganhou".format(jogador=value(TicTacToe[i], True)))
        return TicTacToe[0]
    diag_second = TicTacToe[2] == TicTacToe[4] == TicTacToe[6] and not TicTacToe[2] == 0
    if diag_second:
        clear()
        printTable()
        print_success("o jogador {jogador} ganhou".format(jogador=value(TicTacToe[2], True)))
        return TicTacToe[2]
        
    return Status


def jogar(row, col):
    pos = (row - 1)*3+(col - 1)

    if row > 3 or row < 1:
        print_error("valor linha entre 1 e 3")
        return False
    if col > 3 or col < 1:
        print_error("valor coluna entre 1 e 3")
        return False

    table_value = TicTacToe[pos]
    if table_value == 0:
        TicTacToe[pos] = Time if Time else -1
        return True
    else:
        print_error("posição ({row},{col}) ja ocupada por {jogada}".format(
            row=row, col=col, jogada=value(table_value, True)))


def game():
    global Time
    for i in range(0, 9):
        clear()
        print("Vez do jogador {jogador}".format(jogador=value(Time, True)))
        printTable()

        while(True):
            row, col = input("linha coluna ").split()
            if jogar(int(row), int(col)):
                Time = (Time + 1) % 2
                break
        if win():
            input("pressione ENTER")
            break
        if(i == 8):
            clear()
            printTable()
            print_error("deu velha")
            input("VOLTAR MENU [ENTER]")
def menu():
    op = 0
    while(True):
        clear()
        print_color(250,250,200," jogo da velha ".center(50, '*').upper())
        print_elemento("\n\t1 -")
        print_success("P1 vs P2")
        print_elemento("\t\t2 -")
        print_success("P1 vs CPU")
        print_elemento("\t\t\t3 -")
        print_success("intruções")
        print_elemento("\t\t\t\toutros -")
        print_success("Sair")
        op = int(input("opcao => "))
        if(op == 1):
            game()
            
        else:
            print_success( "Ate mais tarde" )
            break
        
    
def main():
    menu()
    
if __name__ == '__main__':
    main()
