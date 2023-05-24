# Write a short Python function, is even(k), that takes an integer value and
# returns True if k is even, and False otherwise. However, your function
# cannot use the multiplication, modulo, or division operators.

def is_even(k):
    while k > 0:
        k = k - 2
        if k == 0:
            return True
    return False


print(is_even(62))
