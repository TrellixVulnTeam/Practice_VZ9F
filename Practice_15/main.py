from factorial import factorial
from exp_root import exponentiation as exp, root
from logarithm import logarithm

def main():
    print("Welcome to The Greatest Program for Mathematical")
    print("Calculations of All Times! If you see None instead")
    print("of numeric result, the input data is incorrect.")
    print()
    print("Choose the package")
    print("1 - factorial")
    print("2 - exp_root")
    print("3 - logarithm")
    print()
    while True:
        choice = input("Your choice: ").strip()
        if choice in ['1', '2', '3']:
            break
        else:
            print("Nonexistent option! Try again.")

    if choice == '1':
        n = int(input("Enter an integer for fact: "))
        print("Result =", factorial.fact(n))
    if choice == '2':
        print("Choose the function")
        print("1 - exp2")
        print("2 - exp3")
        print("3 - root2")
        print("4 - root3")
        while True:
            subchoice = input("Your choice: ").strip()
            if subchoice in ['1', '2', '3', '4']:
                break
            else:
                print("Nonexistent option! Try again.")

        if subchoice == '1':
            x = float(input("Enter an argument for exp2: "))
            print("Result =", exp.exp2(x))
        if subchoice == '2':
            x = float(input("Enter an argument for exp3: "))
            print("Result =", exp.exp3(x))
        if subchoice == '3':
            x = float(input("Enter an argument for root2: "))
            print("Result =", root.root2(x))
        if subchoice == '4':
            x = float(input("Enter an argument for root3: "))
            print("Result =", root.root3(x))
    if choice == '3':
        print("Choose the function")
        print("1 - log")
        print("2 - ln")
        print("3 - lg")
        while True:
            subchoice = input("Your choice: ").strip()
            if subchoice in ['1', '2', '3']:
                break
            else:
                print("Nonexistent option! Try again.")

        if subchoice == '1':
            a = float(input("Enter the log base: "))
            b = float(input("Enter an argument: "))
            print("Result =", logarithm.log(a, b))
        if subchoice == '2':
            b = float(input("Enter an argument for ln: "))
            print("Result =", logarithm.ln(b))
        if subchoice == '3':
            b = float(input("Enter an argument for lg: "))
            print("Result =", logarithm.lg(b))


if __name__ == '__main__':
    main()
