# Terminal-based Supervised ML Program
# Predicts if a song is HAPPY (1) or SAD (0) based on tempo, energy, and positivity score

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# ===========================
# Custom dataset (unique)
# Features: [tempo_bpm, energy(0-10), positivity_score(0-10)]
# Label: 1 = Happy, 0 = Sad
# ===========================

X = [
    [120, 7, 8],
    [85, 3, 2],
    [140, 8, 9],
    [95, 4, 3],
    [160, 9, 7],
    [75, 2, 1],
    [132, 6, 6],
    [88, 3, 4],
    [150, 9, 5],
    [100, 5, 2],
]

y = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=21
)

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Evaluate accuracy
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print(f"Model trained. Accuracy on test set: {accuracy*100:.2f}%\n")

# ===========================
# Terminal input for interactive prediction
# ===========================

print("=== Music Mood Predictor ===")
print("Enter your song features:")

try:
    tempo = float(input("Tempo (BPM): "))
    energy = float(input("Energy (0-10): "))
    positivity = float(input("Positivity (0-10): "))
except ValueError:
    print("Invalid input! Please enter numbers only.")
    exit()

# Predict mood
new_song = [[tempo, energy, positivity]]
mood = model.predict(new_song)[0]

mood_text = "Happy 😀" if mood == 1 else "Sad 😢"
print(f"\nPrediction: {mood_text}")
