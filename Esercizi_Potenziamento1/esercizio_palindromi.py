def recursivePalindrome(word: str) -> bool:
    if len(word) <= 1:
        return True
    
    new_word = word.replace(" ", "").lower()

    if new_word[0] == new_word[-1]:

        return recursivePalindrome(new_word[1:-1])
    return False

word = "Roma e Amore"
print(recursivePalindrome(word))