class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Store operands and intermediate results on a stack.
        ops = []
        for item in tokens:
            if item == '+':
                ops.append(int(ops.pop()) + int(ops.pop()))
            elif item == '-':
                # The right operand is popped first, so negate the difference.
                ops.append(-1 * (int(ops.pop())-int(ops.pop())))
            elif item == '*':
                ops.append(int(ops.pop()) * int(ops.pop()))
            elif item == '/':
                # Pop the divisor before the dividend.
                ops2 = ops.pop()
                ops1 = ops.pop()
                # Divide magnitudes, then negate to truncate toward zero.
                if (ops2>0 and ops1<0) or (ops2<0 and ops1>0):
                    ops.append(-1*(abs(ops1)//abs(ops2)))
                else:
                    ops.append(ops1//ops2)
            else:
                ops.append(int(item))

        return ops[0]
