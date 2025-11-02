# ================================================================
#  SCENARIO
#  Students copy notes from a classroom whiteboard into a text file.
#  The copied text contains random extra spaces and tabs.
#
#  LEARNING GOALS
#  • Loop control and flags
#  • Using split() and join() for string cleanup
#
#  PROBLEM DESCRIPTION
#  Clean the spacing in text:
#     1. Remove extra spaces and tabs.
#     2. Leave exactly one space between words.
#     3. No spaces at the beginning or end.
#     4. Print the result twice (manual and built-in methods).
#
#  INPUT / OUTPUT EXAMPLE
#     Input:   "  Data\t  structures   are   cool "
#     Output:  "Data structures are cool"
#              "Data structures are cool"
# ================================================================

# TODO 1
text = input("Enter text: ")

# TODO 2 – Manual cleanup using a loop and a flag variable.
clean_manual = ""
# HINT: iterate characters, treat ' ' and '\t' as whitespace; collapse multiples; trim ends

# TODO 3 – Use split() + " ".join() for the same task.
clean_builtin = ""

# TODO 4 – Print both results.
print(clean_manual)
print(clean_builtin)

# REFLECTION:
# What differences did you notice between your two versions?
