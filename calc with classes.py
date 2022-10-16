#Building my calculator with classes

print("Hello World to my calculator!")
print("")
print("Please enter calculations in the following format: 2 + 2, with whitespace")

#performs the calculations with user input
class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def addition(self):
        return self.num1 + self.num2

    def subtraction(self):
        return self.num1 - self.num2

    def multiplication(self):
        return self.num1 * self.num2

    def division(self):
        return self.num1 / self.num2

    def choice(self, user_decision):
        if user_decision == '+':
            return self.addition()
        elif user_decision == "-":
            return self.subtraction()
        elif user_decision == "*":
            return self.multiplication()
        elif user_decision == "/":
            return self.division()
        else:
            print("Try again")


#use user input tp assign numbers and operators
user_input = input("Please enter your calculation!")
user_input = user_input.strip().split(" ") #strips input of whitespace and splits it when whitespace detected
number_1 = float(user_input[0])
number_2 = float(user_input[2])
user_decision = user_input[1]

#pass number 1 and number 2 into the class
calculation = Calculator(number_1, number_2)
result_num = calculation.choice(user_decision)

print(result_num)