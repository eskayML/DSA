import string


def cipher(word):
    # this challenge is a form of cyclic cipher
    group = string.ascii_letters
    
    res = ''
    for char in word:
        pos = group.index(char)
        
        rev = group[51-pos]

        res+=rev
    
    return res

print(cipher('abcd'))
print(cipher('Zabc'))
  
        