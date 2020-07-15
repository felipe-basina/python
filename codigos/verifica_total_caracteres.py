# Verifica o total de caracteres diferentes
# para que seja possivel criar um anagrama, a partir de duas metades,
# de uma determinada palavra
from collections import Counter
s = "hhpddlnnsjfoyxpciioigvjqzfbpllssuj"
if len(s)%2 == 1:
 print "-1"
print Counter(s[0:len(s)/2])
print Counter(s[len(s)/2:])
temp = Counter(s[0:len(s)/2]) - Counter(s[len(s)/2:])
print temp
print sum(temp.values())
