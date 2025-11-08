# ================================================================
#  SCENARIO
#  You are asked to summarise marks from a quiz to display
#  the minimum, maximum and average.
#
#  LEARNING GOALS
#  • Numeric variables and type conversion
#  • Loop-based aggregation vs. built-ins
#
#  PROBLEM DESCRIPTION
#  Read N followed by N integers.  Compute:
#     - Minimum mark
#     - Maximum mark
#     - Average (rounded to 2 decimals)
#  Print the three values twice (manual and built-ins).
#
#  EXAMPLE
#     Input:
#       5
#       10 20 30 40 50
#     Output:
#       10 50 30.0
#       10 50 30.0
# ================================================================

n = int(input("Number of marks: "))
nums = list(map(int, input("Enter marks: ").split()))

# TODO 1 – Manual calculation using a loop.
min_manual = nums[0]
max_manual = nums[0]
total=0
for i in nums:
    if i<min_manual:
        min_manual=i
    if i>max_manual:
        max_manual=i
    total+=i
avg_manual=total/n
    



# HINT: initialize min/max to first element; accumulate total

# TODO 2 – Use built-ins min(), max(), sum(), len().
min_builtin = min(nums)
max_builtin = max(nums)
avg_builtin = sum(nums)/n


# TODO 3 – Print both results.
print(min_manual, max_manual, round(avg_manual, 2))
print(min_builtin, max_builtin, round(avg_builtin, 2))

# REFLECTION:
# How would you verify that both approaches match for any dataset?
