def decor(func):
    def inner(n):
        if n == "ram":
            func(n)
        elif n == "shyam":
            print("u shyam")
        elif n == "abdul":
            print("fuck uo")
        else:
            print("good bye")
    return inner

@decor
def wish(name):
    print(f"hello {name} good morning")
wish("ram")
wish("shyam")
wish("abdul")
wish("xyz")
