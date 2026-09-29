class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(b-a)
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            elif token == "/":
                a = stack.pop()
                b = stack.pop()
                stack.append(int((b/a))) # get decimal result, then remove decimal using int
            else:
                stack.append(int(token)) # convert string to int
        return stack[0] # only one last item in the stack
        