def main():
    say("Hello, World")
    mezera()
    plus(1, 5)
    mezera()
    condition(5)

def say(text):
    print(text)

def plus(x, y):
    print(x + y)

def condition(x):
    if x > 4:
        print(x + " is greater than 4")
    elif x < 4:
        print(x + " is less than 4")
    else:
        print(x + " is equal to 4")

def mezera():
    print("--------------")

if __name__ == "__main__":
    main()