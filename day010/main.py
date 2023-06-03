from art import logo


def add(n1, n2):
    return n1+n2


def sub(n1, n2):
    return n1-n2


def mul(n1, n2):
    return n1*n2


def div(n1, n2):
    return n1/n2


def mod(n1, n2):
    return n1 % n2


operations = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': div,
    '%': mod,
}


def calculator():
    print(logo)
    num1 = float(input("Input first number?: "))
    run = True
    ans = 0
    while (run):
        for e in operations:
            print(e)
        perforn = input("Math operation: ")
        num2 = float(input("Input second number?: "))
        if not (perforn == '/' and num2 == 0):
            calculation = operations[perforn]
            ans = calculation(num1, num2)
            print(f"{num1}{perforn}{num2} = {ans}")
        else:
            print("/ not possible.")
        print(
            f"Type 'y' to continue calculations with {ans}, type 'n' to exit and 'new' for new calculations")
        con_calc = input("type y/n/new: ")
        if con_calc == "y":
            run = True
            num1 = ans
        elif con_calc == 'n':
            run = False
            print("\nBye Bye!!")
        elif con_calc == 'new':
            calculator()
        else:
            print("Invalid response.")
            run = False
            print("\nBye Bye!!")


calculator()
