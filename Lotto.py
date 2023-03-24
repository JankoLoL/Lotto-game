import random


def lotto(user: list[int], win_num: list[int]):
    if len(user) != 6:
        print("Please give six numbers separated by space!")
    else:
        try:
            user = [int(i) for i in user]
            if any(i < 1 or i > 49 for i in user):
                print("Please give the numbers between 1 and 49!")
            elif any(user.count(i) > 1 for i in user):
                print("You gave the same values!")
            else:
                user.sort()
                print("Your numbers:", user)
                print("Winning numbers:", sorted(win_num))
                no_guessed_num = 0
                for num in user:
                    if num in win_num:
                        no_guessed_num += 1
                if no_guessed_num == 0:
                    print("You have zero numbers guessed...")
                elif no_guessed_num < 3:
                    print("Sorry, you did not win, you guessed only:", no_guessed_num)
                else:
                    print("You win!!! You have guessed", no_guessed_num, "numbers")
        except ValueError:
            print("Those are not numbers!")


if __name__ == '__main__':
    print("Welcome in LOTTO game! Remember numbers are between 1 and 49!")
    win_num = random.sample(range(1, 50), 6)
    user = input("Please, type your 6 numbers separated by space:")
    user = user.split()
    lotto(user, win_num)
