"""
https://leetcode.com/problems/basic-calculator/
Basic Calculator
Hard

Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ),
the plus + or minus sign -, non-negative integers and empty spaces .

Example 1:

Input: "1 + 1"
Output: 2

Example 2:

Input: " 2-1 + 2 "
Output: 3

Example 3:

Input: "(1+(4+5+2)-3)+(6+8)"
Output: 23

Note:
You may assume that the given expression is always valid.
Do not use the eval built-in library function.
"""


class Solution(object):
    def calculate2(self, s):
        """ O(N), O(N)
        :type s: str
        :rtype: int
        >>> fn = Solution().calculate2
        >>> fn("1 + 1")
        2
        >>> fn(" 2-1 + 2 ")
        3
        >>> fn("(1+(4+5+2)-3)+(6+8)")
        23
        >>> fn("(1-(4-5+2)+3)-(6+8)")
        -11
        >>> fn("2147483647")
        2147483647
        """
        op_stack, val_stack, i = [], [], len(s) - 1
        op_map = {"+": lambda x, y: x + y, "-": lambda x, y: x - y}
        while i >= 0:
            j = i - 1
            if s[i].isdigit():
                while j >= 0 and s[j].isdigit():
                    j -= 1
                val_stack.append(int(s[j+1:i+1]))
            elif s[i] in {"+", "-", ")"}:
                op_stack.append(s[i])
            elif s[i] == "(":
                while op_stack[-1] != ")":
                    op, x, y = op_stack.pop(), val_stack.pop(), val_stack.pop()
                    val_stack.append(op_map[op](x, y))
                op_stack.pop()
            i = j
        while op_stack:
            x, y = val_stack.pop(), val_stack.pop()
            val_stack.append(op_map[op_stack.pop()](x, y))
        return val_stack[0]

    def calculate1(self, s):
        """ O(N), O(N)
        :type s: str
        :rtype: int
        >>> fn = Solution().calculate1
        >>> fn("1 + 1")
        2
        >>> fn(" 2-1 + 2 ")
        3
        >>> fn("(1+(4+5+2)-3)+(6+8)")
        23
        >>> fn("(1-(4-5+2)+3)-(6+8)")
        -11
        >>> fn("2147483647")
        2147483647
        """
        postfix, op_stack, i, n = [], [], 0, len(s)
        op_map = {"+": lambda x, y: x + y, "-": lambda x, y: x - y}
        while i < n:
            ch, j = s[i], i + 1
            if ch.isdigit():
                while j < n and s[j].isdigit():
                    j += 1
                postfix.append(s[i:j])
            elif ch in {"+", "-"}:
                if op_stack and op_stack[-1] in {"+", "-"}:
                    postfix.append(op_stack.pop())
                op_stack.append(ch)
            elif ch == "(":
                op_stack.append(ch)
            elif ch == ")":
                while op_stack[-1] != "(":
                    postfix.append(op_stack.pop())
                op_stack.pop()
            i = j
        while op_stack:
            postfix.append(op_stack.pop())

        for s in postfix:
            if s.isdigit():
                op_stack.append(int(s))
            elif s in {"+", "-"}:
                y, x = op_stack.pop(), op_stack.pop()
                op_stack.append(op_map[s](x, y))

        return op_stack[0]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
