"""
b = True;
if b : 
    print(b);

f = False;
"""
a = [1, 2, 3, 4, 5, 1, 7, 3, 1, 1, 1, 1]
if (n := len(a)) > 10:
    print(f"List is too long ({n} elements, expected <= 10)")
