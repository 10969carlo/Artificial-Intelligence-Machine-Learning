import pandas as pd
from sklearn.linear_model import LogisticRegression

# Load CSV
df = pd.read_csv("hw_200.csv")
# Clean column names
df.columns = df.columns.str.strip().str.replace('"', '')
df.rename(columns={"Height(Inches)": "Height", "Weight(Pounds)": "Weight"}, inplace=True)

# Label: Tall if height > median
median_height = df["Height"].median()
df["Tall"] = (df["Height"] > median_height).astype(int)

X = df[["Height", "Weight"]]
y = df["Tall"]

# Train model
model = LogisticRegression(max_iter=1000)
model.fit(X, y)

# Terminal interaction
print("=== Height Classifier ===")
print("Units: Height in inches, Weight in pounds\n")

height = float(input("Enter height (inches): "))
weight = float(input("Enter weight (pounds): "))

user_input = pd.DataFrame([[height, weight]], columns=["Height", "Weight"])
prediction = model.predict(user_input)[0]
label = "Tall" if prediction == 1 else "Short"

print(f"\nPrediction: {label}")
input("Press Enter to exit...")
