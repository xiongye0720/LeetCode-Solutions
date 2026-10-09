class Solution:
    def isValid(self, s: str) -> bool:
        # A valid sequence must contain an even number of brackets.
        if len(s)%2 == 1:
            return False
        else:
            # Store unmatched opening brackets.
            ops = []
            for char in s:
                if char=='(' or char=='[' or char=='{':
                    ops.append(char)
                else:
                    # Match each closing bracket with the most recent opening bracket.
                    if char == ')':
                        if len(ops)==0 or ops[-1]!='(':
                            return False
                        else:
                            ops.pop()
                    elif char == ']':
                        if len(ops)==0 or ops[-1]!='[':
                            return False
                        else:
                            ops.pop()
                    else:
                        if len(ops)==0 or ops[-1]!='{':
                            return False
                        else:
                            ops.pop()
            
            # All opening brackets must have been matched.
            if len(ops) == 0:
                return True
            else:
                return False
        