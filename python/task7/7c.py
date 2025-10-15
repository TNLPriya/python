# Recursive function to reverse a string
def reverse_string(s):
    if len(s) == 0:   # base case
        return s
    return reverse_string(s[1:]) + s[0]

# Test cases
print("Reverse of 'hello' =", reverse_string("hello"))
print("Reverse of 'python' =", reverse_string("python"))
print("Reverse of 'recursion' =", reverse_string("recursion"))

