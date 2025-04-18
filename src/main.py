def main():
    say("Hello, World")
    mezera()
    plus(1, 5)
    mezera()
    condition(5)
    mezera()
    forloop()
    mezera()
    whileloop()
    mezera()

def say(text):
    print(text)

def plus(x, y):
    print(x + y)

def condition(x):
    if x > 4:
        print(f"{x} is greater than 4")
    elif x < 4:
        print(f"{x} is less than 4")
    else:
        print(f"{x} is equal to 4")

def forloop():
    for i in range(5):
        print(i)

def whileloop():
    x = 10
    while x > 1:
        print(x)
        x = x - 1


def mezera():
    print("--------------")

if __name__ == "__main__":
    main()