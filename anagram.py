from collections import Counter

def check_anagram(s1, s2):
    """
    Checks if two strings are anagrams of each other.
    This function is case-insensitive and ignores spaces.
    """
    # 1. Normalize the strings:
    #    - Convert to lowercase
    #    - Remove spaces
    s1_processed = "".join(s1.lower().split())
    s2_processed = "".join(s2.lower().split())

    # If you want to ignore other punctuation as well, you could use:
    # import string
    # s1_processed = "".join(filter(str.isalnum, s1.lower()))
    # s2_processed = "".join(filter(str.isalnum, s2.lower()))
    # This would keep only alphanumeric characters.

    # 2. Check if lengths are different after processing.
    #    If they are, they can't be anagrams.
    if len(s1_processed) != len(s2_processed):
        return False

    # 3. Count character frequencies for both processed strings.
    #    The Counter object creates a dictionary-like structure
    #    where keys are items and values are their counts.
    #    e.g., Counter("apple") -> {'a': 1, 'p': 2, 'l': 1, 'e': 1}
    #
    # 4. Compare the frequency counts.
    #    If the counts of all characters are the same, the strings are anagrams.
    return Counter(s1_processed) == Counter(s2_processed)

# --- Main part of the program ---
if __name__ == "__main__":
    print("Anagram Checker Program")
    print("-----------------------")

    # Get the first string from the user
    string1 = input("Enter the first word or phrase: ")

    # Get the second string from the user
    string2 = input("Enter the second word or phrase: ")

    # Check if they are anagrams by calling the function
    if check_anagram(string1, string2):
        print(f"\nResult: '{string1}' and '{string2}' ARE anagrams.")
    else:
        print(f"\nResult: '{string1}' and '{string2}' are NOT anagrams.")

    print("\n-----------------------")
    print("Program finished.")