
"""
Una frase es un palindromo si se lee igual de reversa. 

Dado un string s, determina si s es un palindromo, considerando solo los caracteres alfanuméricos incluyendo letras y numeros
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
"""

def palindromo(s):
    "retorna verdadero si S es un palindromo, retorna falso si no lo es"
    non_alphanumeric = [", ", ": ", " ", "!", "."]
    s_alpha_numeric = s.lower().replace([non_alphanumeric], "")
    s_alpha_numeric = s.lower().replace(" ", "").replace(",", "").replace(":", "").replace("!","").replace(".","")
    s_reversed = s_alpha_numeric[::-1]
    if s_alpha_numeric == s_reversed:
        return True
    return False

print(palindromo('sugus'))