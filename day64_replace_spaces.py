'''
Day 64: Replace Spaces with Hyphens
Problem statement: Given a string, create a new string where every space is replaced by a hyphen (-). (Do this using a loop, not the .replace() function).
Input: "hello world" → Output: "hello-world"
'''

def replace_spaces(s):

        result = ""
        for i in s:
                if i == " ":
                        result = result + "-"
                else:
                        result = result + i
        return result

print(replace_spaces("hello world"))
print(replace_spaces("a b c"))
