# ================================================================
#  SCENARIO
#  A biology lab tracks bacterial growth at different temperatures.
#  Each class of bacteria thrives in specific ranges.
#
#  LEARNING GOALS
#  • Nested conditions and comparisons
#  • Dictionaries and lambda expressions
#
#  PROBLEM DESCRIPTION
#  Classes and Ranges:
#     Hyperthermophile (t ≥ 60)
#     Thermophile (45 ≤ t ≤ 122)
#     Mesophile (20 ≤ t ≤ 45)
#     Psychrotrophs (t ≥ 0)
#     Psychrophiles (-15 ≤ t ≤ 10)
#
#  Input: n then n temperatures.
#  Output:
#     For each temp → matching classes (| separated).
#     Then totals for each class (Name: count).
#  Print twice (manual and lambda list).
#
#  EXAMPLE
#     Input:
#       6
#       75 30 -10 25 0 50
#     Output (per temp + totals for both methods)
# ================================================================

n = int(input("Number of readings: "))
temps = list(map(int, input().split()))

# TODO 1 – Manual classification with if chains. Produce per-temp labels and totals.
per_manual = []   # list of strings like "Thermophile|Psychrotrophs"
totals_manual = {}  # dict of class -> count
for t in temps:
    l1=[]
    if t>=60:
        l1.append("Hyperthermophile")
    if t>=45 and t<=122:
        l1.append("Thermophile")
    if t>=20 and t<=45:
        l1.append("Mesophile")
    if t>=0:
        l1.append("Psychrotrophs")
    if t>=(-15) and t<=10:
        l1.append("Psychrophiles")
    per_manual.append("|".join(l1))
    for i in l1:
        totals_manual[i]=totals_manual.get(i,0)+1


# TODO 2 – Use list of (name, lambda) and dict.get() to replicate the same.
CLASSES = [
    ("Hyperthermophile", lambda t: t >= 60),
    ("Thermophile",      lambda t: 45 <= t <= 122),
    ("Mesophile",        lambda t: 20 <= t <= 45),
    ("Psychrotrophs",    lambda t: t >= 0),
    ("Psychrophiles",    lambda t: -15 <= t <= 10),
]
per_builtin = []
totals_builtin = {}
for t in temps:
   
    matched = [name for name, rule in CLASSES if rule(t)]
    per_builtin.append("|".join(matched))
    for name in matched:
        totals_builtin[name] = totals_builtin.get(name, 0) + 1




# TODO 3 – Print per-temp lines (manual), then totals (manual).
# Then print per-temp lines (built-in), then totals (built-in).
print("\n--- Manual Classification ---")
for t, label in zip(temps, per_manual):
    print(f"{t}: {label}")

print("Totals (manual):")
for k, v in totals_manual.items():
    print(f"{k}: {v}")

print("\n--- Lambda Classification ---")
for t, label in zip(temps, per_builtin):
    print(f"{t}: {label}")

print("Totals (lambda):")
for k, v in totals_builtin.items():
    print(f"{k}: {v}")
