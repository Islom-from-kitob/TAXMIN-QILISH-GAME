import random

GameOver = ValueError

def gess_number():
    return random.randint(10, 20)
def chek_namber(namber, gesse):
    message = "Men oylagan son"
    if namber<gesse:
        message = f"{message} {gesse} dan kichikroq."
        return message
    elif namber>gesse:
        message = f"{message} {gesse} dan kataaroq."
        return message
    else:
        raise GameOver

def main():
    namber = gess_number()
    print("men 10-20 oraligh`ida son o`yladim: ", namber)
    # gesse = int(input("taxminingizni kiriting"))

    bir = 1
    while True:
        if bir <= 3:
            try:
                gesse = int(input("taxminingizni kiriting"))
            except ValueError:
                print("int kriting")
                break
            try:
                message = chek_namber(namber, gesse)
                print(message)
            except GameOver:
                print (f"you found the correct answer on the {bir} try")
                break
            bir += 1
            print(bir)
        else:
            print("yutqazdingiz")
            print(f"correct answer {namber}")
            break
if __name__ == '__main__':
    main()