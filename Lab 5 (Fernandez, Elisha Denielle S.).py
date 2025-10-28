
def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    stack = []      
    output = []     

    for token in expression:
        if token.isalnum():  
            output.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  
        else:
            
            while (stack and stack[-1] != '(' and
                   precedence.get(token, 0) <= precedence.get(stack[-1], 0)):
                output.append(stack.pop())
            stack.append(token)

    
    while stack:
        output.append(stack.pop())

    return ' '.join(output)



print("🔹 Infix to Postfix Converter (Shunting Yard Algorithm) 🔹")
infix = input("Enter an infix expression (e.g., A+B*C or (A+B)*C): ")

infix = infix.replace(" ", "")

postfix = infix_to_postfix(infix)
print("Postfix Expression:", postfix)

