# Name: YAO Yao
# Assignment One
# ddl is 22/9/2026 23:59pm


# Task 1: Simple Calculator
def simple_calculator():
    print("\n----- Simple Calculator -----")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    op = input("Choose operation (+, -, *, /): ")

    if op == "+":
        print("Result:", num1 + num2)
    elif op == "-":
        print("Result:", num1 - num2)
    elif op == "*":
        print("Result:", num1 * num2)
    elif op == "/":
        if num2 == 0:
            print("Error: Cannot divide by zero.")
        else:
            print("Result:", num1 / num2)
    else:
        print("Invalid operation")


# Task 2: QA Bot
def qa_bot():
    print("\n----- Question Answering Bot -----")

    question = input("Ask me something: ").strip().lower()

    if question == "hello":
        print("Bot: Hello! Nice to meet you.")
    elif question == "python":
        print("Bot: Python is a language.")
    elif question == "jetson":
        print("Bot: Jetson Nano is an AI computer.")
    elif question == "ai":
        print("Bot: AI means Artificial Intelligence.")
    elif question == "name":
        print("Bot: My name is Python Bot.")
    else:
        print("Bot: Sorry, I don't understand.")


# Main selection menu
print("----- Welcome to Assignment One -----")

while True:
    choice = input(
        "\n---- Please select what you want to run:\n"
        " (1 for Simple Calculator, 2 for Question Answering Bot)\n"
        "Your selection is: "
    )

    if choice == "1":
        simple_calculator()
    elif choice == "2":
        qa_bot()
    else:
        print("Please input the value in [1, 2]")
