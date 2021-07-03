class check:
   def is_valid_parentheses(self, str1):
        stack, dic = [], {"(": ")", "{": "}", "[": "]"}
        for i in str1:
            if i in dic:
                stack.append(i)
            elif len(stack) == 0 or dic[stack.pop()] != i:
                return False
        return len(stack) == 0

print(check().is_valid_parentheses("(){}[]"))

