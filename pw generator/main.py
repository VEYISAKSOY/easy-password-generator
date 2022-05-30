import random
import time

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

all= list(letters + numbers + symbols)

print("welcome to the easy password generator")
time.sleep(1)


def pw_generate():

    user_question1 = int(input("how many characters password your password should contain?:\n"))

    print(f"Your pw will be consist of {user_question1} characters")
    print("we are working on it now..")
    time.sleep(2)

    pw =[]
    for i in range(user_question1):
        pw.append(random.choice(all))
    random.shuffle(pw)

    print(" ".join(pw))


pw_generate()