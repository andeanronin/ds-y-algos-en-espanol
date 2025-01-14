# reverse words

"""
Escribe una funcion que reversa las palabras en una string.

Input: "the sky is blue"
Output: "blue is the sky"
"""



def solve(s):
    words = s.split(" ")
    reversed = words[::-1]
    return " ".join(reversed)

