from stack import Stack

def isBalanced(str):
    """Function to validate the balace of the expression """
    stack = Stack()
    for char in str:
        if char in ['(', '[']:
            stack.push(char)
        else:
            if stack.isEmpty():
                return False
            top = stack.pop()
            if (top == '[' and char != ']') or \
               (top == '(' and char != ')'):
                return False
    return stack.isEmpty()

def main():
    c = input("Type only '[]' and '()': ")
    if isBalanced(c) == True:
        print("This expression is balanced!\n")
    else:
        print("This expression is unbalanced!\n")

if __name__ == "__main__":
    main()
