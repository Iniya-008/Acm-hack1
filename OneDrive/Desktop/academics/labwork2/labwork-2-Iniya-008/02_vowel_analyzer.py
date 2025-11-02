# ================================================================
#  SCENARIO
#  The campus café posts a “Word of the Day.”  To gauge how
#  “vowel-heavy” a word is, they want a vowel-counting tool.
#
#  LEARNING GOALS
#  • Conditional statements and logical operators
#  • Introduction to sets and membership testing
#
#  PROBLEM DESCRIPTION
#  Build a program that counts vowels twice:
#     1. Using simple if checks for each character (manual).
#     2. Converting the string to lowercase and checking membership
#        in a set (built-ins).
#
#  INPUT / OUTPUT EXAMPLE
#     Input:  Apple strudel is AMAZING!
#     Output: 8
#             8
#
#  IMPLEMENTATION TASKS
#     TODO 1 – Read a sentence.
#     TODO 2 – Count vowels manually.
#     TODO 3 – Convert to lowercase and count again using a set.
#     TODO 4 – Print both counts.
# ================================================================

# TODO 1
sentence = input("Enter a sentence: ")

# TODO 2
vowel_count_manual = 0
# HINT: check ch in "aeiouAEIOU"

# TODO 3
vowels = set("aeiou")
vowel_count_builtin = 0
# HINT: for ch in sentence.lower(): if ch in vowels: increment

# TODO 4
print(vowel_count_manual)
print(vowel_count_builtin)

# REFLECTION:
# How did lowercase + set membership simplify your logic?
