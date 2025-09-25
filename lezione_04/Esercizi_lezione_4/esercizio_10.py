
    # Create a function that checks whether two given strings are anagrams of each other.
    # Convert both strings to lowercase and remove any non-alphabetic characters.
    # Sort the characters of each string and compare the sorted strings for equality.
    # Indicate whether the strings are anagrams or not.


def anagram_checker(string1: str, string2: str) -> bool:

    new_string1 = ""
    new_string2 = ""

    no_alpha = ""
    
    for i in string1.lower():
        if i.isalpha():
            new_string1 += i
            return sorted(new_string1)
        else:
            no_alpha += i

    for i in string2.lower():
        if i.isalpha():
            new_string2 += i
            return sorted(new_string2)
        else:
            no_alpha += i
    
        print(new_string1, new_string2)

anagram_checker("canebau", "cane")