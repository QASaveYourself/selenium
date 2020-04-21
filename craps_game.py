from random import randint


def craps_game(money):
    while money > 0:
        print("NOW, you have money:", money)
        go_on = False
        while True:
            debt = int(input("Please enter money you want to debt:"))
            if debt > money:
                print("You only have $%d and have no enough money!" % money)
                continue
            elif debt == money:
                print("You have ALLIN!")
                break
            elif debt <= 0:
                print("Cannot debt this")
                continue
            else:
                print("You debt $%d" % debt)
                break

        first_point = randint(1, 6) + randint(1, 6)
        print("First time, you got %d point" % first_point)
        if first_point == 7 or first_point == 11:  # 丟出7 or 11 算贏
            print("you WIN!")
            money += debt
        elif first_point == 2 or first_point == 3 or first_point == 12:
            print("you LOSE!")
            money -= debt
        else:
            go_on = True

        while go_on is True:
            go_on = False
            point = randint(1, 6) + randint(1, 6)
            print("you got %d point" % point)
            if point == 7:
                print("you LOSE!")
                money -= debt
            elif point == first_point:
                print("you WIN!")
                money += debt
            else:
                go_on = True
    print("YOU HAVE NO ANY MONEY AND PLEASE GET OUT!!!")


if __name__ == '__main__':
    craps_game(500)
