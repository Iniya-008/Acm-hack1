# ================================================================
#  SCENARIO
#  The campus post-office receives novelty postcards printed backwards.
#  You are asked to create a small utility that reverses words so that
#  the clerk can instantly read them.
#
#  LEARNING GOALS
#  • String indexing and iteration
#  • Using slicing for quick reversals
#
#  PROBLEM DESCRIPTION
#  1. Read a single word (no spaces).
#  2. Print the reversed word twice:
#       - First line: produced manually using a loop.
#       - Second line: produced using slicing.
#
#  INPUT / OUTPUT EXAMPLE
#     Input:   hello
#     Output:  olleh
#              olleh
#
#  IMPLEMENTATION TASKS
#     TODO 1 – Read the word.
#     TODO 2 – Build the reverse manually by prepending characters.
#     TODO 3 – Use slicing to reverse quickly.
#     TODO 4 – Print both results.
# ================================================================

# TODO 1
word = input("Enter a word: ").strip()

# TODO 2
reverse_manual = ""
for ch in range(len(word)-1,-1,-1):
    reverse_manual+=word[ch]
#pushing code
# HINT: iterate over each character ch in word and set reverse_manual = ch + reverse_manual

# TODO 3
reverse_builtin = "" 
reverse_builtin=word[::-1] # HINT: use slicing word[::-1]

# TODO 4
print(reverse_manual)
print(reverse_builtin)

# REFLECTION (2–3 sentences):
# Which approach was easier to write and why?
