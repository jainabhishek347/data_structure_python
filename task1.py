# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(S):
    """
    will follow below rules for return result
    stack[-1] last element of stack after string execution
    -1 is string is empty
    -1 if there is no element in stack for perform action duplicate and pop
    -1 if there is no element in stack for perform + and -
    -1 if string is not as per format
    """
    if not S:
        return -1
        
    strings = S.split()
    stack =[]
    for s in strings:
        if s.isdigit():
                stack.append(int(s))
        elif s == "DUP":
            if stack:
                stack.append(stack[-1])
            else:
                return -1
        elif s =="POP":
            if stack:
                stack.pop()
            else:
                return -1
        elif s == "+":
            try:
                last = stack.pop()
                second_last = stack.pop()
                stack.append(second_last+last)
            except Exception,e:
                return -1
        elif s == "-":
            try:
                last = stack.pop()
                second_last = stack.pop()
                stack.append(last-second_last)
            except Exception,e:
                return -1
        else:
            print s , "="
        #    return -1
    return stack[-1] if stack else -1

S="13 DUP 4 POP 5 DUP + DUP + -"
print solution(S)    
S="5 6 + -"
print solution(S)    
S="3 DUP 5 - -"
print solution(S)    
S=""
print solution(S)    
S="POP POP"
print solution(S)  
S="DUP DUP DUP"
print solution(S)  
S="DUP DUP DUP3"
print solution(S)  