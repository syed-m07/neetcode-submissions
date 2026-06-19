class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack =[]
        parsed_tokens = []
        for x in tokens:
            if x.lstrip('-').isdigit():
                parsed_tokens.append(int(x))
            elif isinstance(x, str):
                parsed_tokens.append(str(x))
        tokens = parsed_tokens

        for i in range(0, len(tokens)):
            if isinstance(tokens[i], int):
                stack.append(tokens[i])
            elif tokens[i] in ["+", "-", "*", "/"]:
                num1 = stack.pop()
                num2 = stack.pop()
                if tokens[i] == "+":
                    result = num1 + num2
                elif tokens[i] == "-":
                    result = num2 - num1
                elif tokens[i] == "*":
                    result = num1 * num2
                else:
                    result = int(num2 / num1)
                stack.append(result)
        return stack.pop()
