'''
Problem: Find the factorial of a number using a loop (no recursion, no math library).

Input:  5   → Output: 120
Input:  0   → Output: 1
Input:  1   → Output: 1
'''


def find_factorial(num):

        total = 1
        for i in range(1, num + 1):
                total = total * i
        return total

print(find_factorial(5))
print(find_factorial(0))
print(find_factorial(1))




















































                                             [ New File ]
^G Help       ^O Write Out  ^F Where Is   ^K Cut        ^T Execute    ^C Location   M-U Undo
^X Exit       ^R Read File  ^\ Replace    ^U Paste      ^J Justify    ^/ Go To Line M-E Redo

