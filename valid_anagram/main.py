# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

# Example 1:

# Input: s = "anagram", t = "nagaram"

# Output: true

# Example 2:

# Input: s = "rat", t = "car"

# Output: false


class A:
    def checkvalid_anagram(self, s: str, t:str) -> bool:
        if (sorted(s) == sorted(t)):
            print ("The strings are anagrams of each other")
            return True
        else:
            print("The strings are not anagrams of each other")
            return False


if __name__ == "__main__":
    a =A()
    output = a.checkvalid_anagram("rat", "car")
    print(output)   