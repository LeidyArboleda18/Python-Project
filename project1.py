# Interactive Python Variables Tutorial with Topics

def topic_1():
    print("\n🚀 **Topic 1: What is a Variable?** 🚀\n")
    print("Welcome to the first topic! In Python, a variable is like a box where you can store information. Think of it as a label for a value.")
    print("\nFor example, if you want to store someone's age, you would create a variable and assign the value to it.")
    
    print("\nHere’s an example:\n")
    print('''# Create a variable called 'age' and assign the value 25 to it
age = 25
print(age)  # Output: 25
    ''')

    # Ask the user a question to reinforce the concept
    answer = input("\n🎯 Can you create a variable with the syntax 'age = 25'? (yes/no): ").lower()
    if answer == "yes":
        print("✅ Correct! You've created your first variable!")
    else:
        print("❌ Nope! The syntax 'age = 25' is correct for creating a variable in Python.")
    
    print("\n🎉 You're off to a great start! Let's move on to the next topic!")

def topic_2():
    print("\n💡 **Topic 2: Understanding Different Data Types** 💡\n")
    print("Now that you know how to create a variable, let's explore the different types of data you can store in your variables.")
    print("In Python, a variable can hold many types of values:")
    print("\n1. **Integers (int)**: Whole numbers like 10, -5, 42.")
    print("2. **Floating-point numbers (float)**: Numbers with decimals like 3.14, 0.99, -2.71.")
    print("3. **Strings (str)**: Text values, like 'Hello!', or 'Python'.")
    print("4. **Lists**: A collection of ordered items, like ['apple', 'banana', 'cherry'].")
    print("5. **Booleans (bool)**: True or False values, used for logical operations.")
    
    # Example of data types
    print("\nLet’s see an example of different data types:\n")
    print('''# Integer
num = 10
print(type(num))  # Output: <class 'int'>

# String
greeting = "Hello, world!"
print(type(greeting))  # Output: <class 'str'>
    ''')

    # Interactive question about data types
    answer = input("\n🌟 Can a variable store both numbers and text? (yes/no): ").lower()
    if answer == "yes":
        print("✅ Yes! Python allows variables to store all kinds of data.")
    else:
        print("❌ Actually, variables in Python are dynamic, meaning they can store any type of data!")

    print("\n🚀 You're doing great! Let’s dive into naming your variables in the next topic.")

def topic_3():
    print("\n📝 **Topic 3: Naming Your Variables** 📝\n")
    print("When you create a variable, you need to give it a name. But not just any name! There are a few rules you need to follow.")
    print("\nHere are the key rules for naming variables in Python:")
    print("1. The name must start with a letter (a-z, A-Z) or an underscore (_).")
    print("2. It can contain letters, numbers, and underscores, but no spaces or special characters.")
    print("3. Variable names are **case-sensitive**—'age' and 'Age' are different variables.")
    print("4. Avoid using Python reserved keywords (e.g., 'if', 'while', 'def').")
    
    # Example of valid and invalid variable names
    print("\nLet’s look at some examples:\n")
    print('''# Valid variable names
name = "John"
_age = 25
variable_123 = 100

# Invalid names (commented out)
# 1st_variable = "Error"  # Starts with a number
# my variable = "Oops"  # Contains a space
# def = 10  # 'def' is a reserved keyword
    ''')

    # Interactive question about variable names
    answer = input("\n🎯 Which of the following is a valid variable name?\n(a) 1st_variable\n(b) _age\n(c) my-variable\n").lower()
    if answer == "b":
        print("✅ Correct! '_age' is a valid name. Remember, no spaces or starting with numbers!")
    else:
        print("❌ Oops! The correct answer is (b) _age.")

    print("\n🎉 Nice work! Let’s continue by learning how to assign and modify variables.")

def topic_4():
    print("\n✏️ **Topic 4: Assigning and Modifying Variables** ✏️\n")
    print("In Python, once you create a variable, you can assign a value to it. You can even change that value later in your program!")
    print("\nYou assign a value to a variable using the equals sign (`=`), like so:")
    
    print('''# Assigning a value to a variable
x = 5
print(x)  # Output: 5
    ''')
    
    print("\nBut here's the cool part! You can modify the value of a variable by performing operations on it.")
    print('''# Modifying the value of 'x'
x = x + 10
print(x)  # Output: 15
    ''')

    # Interactive question about variable modification
    answer = input("\n🎯 If 'x' starts at 5, what will be the value of 'x' after 'x = x + 10'? (a) 5\n(b) 10\n(c) 15\n").lower()
    if answer == "c":
        print("✅ Correct! After adding 10 to x, the value becomes 15.")
    else:
        print("❌ Oops! The correct answer is (c) 15.")

    print("\n🎉 You’re mastering Python variables! Let’s finish with a quick look at constants.")

def topic_5():
    print("\n🔒 **Topic 5: Constants in Python** 🔒\n")
    print("In Python, there's no built-in constant type, but there’s a naming convention to indicate a constant.")
    print("We use **uppercase** letters to define constants, which are values that shouldn’t change once set.")
    
    print("\nHere’s an example of how to define a constant for the value of Pi:")
    print('''# Defining a constant
PI = 3.14159
print(PI)  # Output: 3.14159
    ''')

    # Interactive question about constants
    answer = input("\n🎯 Is 'PI = 3.14159' an example of using a constant in Python? (yes/no): ").lower()
    if answer == "yes":
        print("✅ Correct! 'PI' is a constant because it's a fixed value.")
    else:
        print("❌ Actually, yes! 'PI' is a constant, commonly used in Python.")

    print("\n🎉 Congratulations, you've completed the topics! Time for a quick quiz to check your understanding.")

def take_quiz():
    print("\n🎓 **Final Quiz: Test Your Knowledge!** 🎓\n")
    score = 0

    # Question 1
    answer1 = input("1. Can a variable store both integers and strings in Python? (yes/no): ").lower()
    if answer1 == "yes":
        print("✅ Correct!")
        score += 1
    else:
        print("❌ Actually, variables can store any type of data in Python, so yes!")

    # Question 2
    answer2 = input("\n2. Which of these is a valid variable name?\n(a) 2nd_variable\n(b) _myVariable\n(c) my-variable\n").lower()
    if answer2 == "b":
        print("✅ Correct!")
        score += 1
    else:
        print("❌ The correct answer is (b) _myVariable. Variable names can't start with numbers or contain dashes!")

    # Question 3
    answer3 = input("\n3. Can you modify the value of a variable in Python? (yes/no): ").lower()
    if answer3 == "yes":
        print("✅ Correct!")
        score += 1
    else:
        print("❌ Yes! You can modify the value of a variable at any time.")

    # Final score
    print(f"\nYour final score is: {score}/3")
    if score == 3:
        print("🎉 Excellent! You are a Python variable pro!")
    elif score == 2:
        print("👍 Good job! You’ve got the basics down.")
    else:
        print("📚 You might want to review some material and try again.")

# Main function to run the topics and quiz
def main():
    topic_1()
    topic_2()
    topic_3()
    topic_4()
    topic_5()
    take_quiz()

# Run the program
if __name__ == "__main__":
    main()
