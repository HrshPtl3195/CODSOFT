class Calculator:
    def add(self, a, b):
        print(f"\n {a} + {b} = {(a+b):.2f}")
    def subtract(self, a, b):
        print(f"\n {a} - {b} = {(a-b):.2f}")
    def multiply(self, a, b):
        print(f"\n {a} x {b} = {(a*b):.2f}")
    def divide(self, a, b):
        print(f"\n {a} / {b} = {(a/b):.2f}")

c = Calculator()
while 1:
    choice = int(input("""
+--------------+
|  CALCULATOR  |
+--------------+
|  1) Add      |
|  2) Subtract |
|  3) Multiply |
|  4) Divide   |
|  5) Exit     |
+--------------+

Enter Operation:  """))
    if choice == 5:
        print("\n Thank You.\n")
        break
    
    a = eval(input("\nEnter 2 numbers:\n a = "))
    b = eval(input(" b = "))
    
    if choice == 1:
        c.add(a, b)
        
    elif choice == 2:
        c.subtract(a, b)
    
    elif choice == 3:
        c.multiply(a, b)
        
    elif choice == 4:
        c.divide(a, b)

    else:
        print("\n Some Internal Error Occured.\nPlease try again...\n")
        continue