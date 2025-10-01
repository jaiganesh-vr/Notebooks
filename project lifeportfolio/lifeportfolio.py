import matplotlib.pyplot as plt

# Empty list to store user input
data = []

print("Enter your data points (Label, Importance, Time Spent, Satisfaction).")
print("Type 'done' when finished.\n")

# Input loop
while True:
    user_input = input("Enter data as label,importance,time_spent,satisfaction: ")
    if user_input.lower() == "done":
        break
    try:
        # Split input
        parts = user_input.split(",")
        label = parts[0].strip()
        i, t, s = map(int, parts[1:])  # importance, time_spent, satisfaction
        data.append((label, i, t, s))
    except:
        print("❌ Invalid format. Please enter like: Career,7,100,6")

# If no data entered, use defaults
if not data:
    print("\n⚠️ No data entered. Using default values.")
    data = [
        ("Career", 7, 100000, 6),
        ("Health", 9, 150, 8),
        ("Family", 5, 80, 7),
        ("Hobbies", 8, 40, 3),
        ("Finance", 6, 120, 9),
    ]

# Split data into lists
labels = [d[0] for d in data]
importance = [d[1] for d in data]
time_spent = [d[2] for d in data]
satisfaction = [d[3] for d in data]

# Bubble chart
plt.figure(figsize=(9, 7))
plt.scatter(satisfaction, importance, s=[ts/50 for ts in time_spent],
            c='red', alpha=0.6, edgecolors="w")

# Add labels to each bubble
for lbl, x, y in zip(labels, satisfaction, importance):
    plt.text(x+0.1, y+0.1, lbl, fontsize=9, weight="bold", color="black")

# Labels and formatting
plt.title("Strategic Life Portfolio", fontsize=16, weight="bold")
plt.xlabel("Satisfaction", fontsize=12)
plt.ylabel("Importance", fontsize=12)

# Axis ranges (0–10 scale for satisfaction and importance)
plt.xlim(0, 10)
plt.ylim(0, 10)

# Add quadrant lines
plt.axhline(y=5, color='gray', linestyle="--", alpha=0.7)
plt.axvline(x=5, color='gray', linestyle="--", alpha=0.7)

# Add faint quadrant labels
plt.text(2.5, 7.5, "HIGH", fontsize=30, color="gray", alpha=0.15,
         ha="center", va="center", weight="bold")
plt.text(7.5, 7.5, "HAPPY", fontsize=30, color="gray", alpha=0.15,
         ha="center", va="center", weight="bold")
plt.text(2.5, 2.5, "UNHAPPY", fontsize=30, color="gray", alpha=0.15,
         ha="center", va="center", weight="bold")
plt.text(7.5, 2.5, "HAPPY", fontsize=30, color="gray", alpha=0.15,
         ha="center", va="center", weight="bold")

plt.grid(alpha=0.3, linestyle="--")
plt.show()