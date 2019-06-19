# TWP280 Strings - TWP282 Strings Palíndromes
#verifique se uma palavra é palindrome
palavra = input("Palavra: ")
if palavra == palavra[::-1]:
    print ("%s é palindrome" %palavra)
else:
    print ("%s não é palindrome" %palavra)
