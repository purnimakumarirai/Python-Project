from collections import Counter

def is_anagram(s1, s2):
    # implementing counter function
    if (Counter(s1) == Counter(s2)):
        print("True.")
    else:
        print("False.")

s1 = "night"
s2 = "thing"
is_anagram(s1, s2)
