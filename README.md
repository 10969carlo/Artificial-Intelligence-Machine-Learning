# Music Mood Classifier

## Overview
This project is a terminal-based supervised machine learning program that predicts the mood of a song as either **Happy** or **Sad**. 

The prediction is based on three features:

- Tempo (beats per minute)  
- Energy level (0–10)  
- Positivity score of lyrics (0–10)  

The dataset used is custom-made for this project, so it is unique. Users can enter new song features in the terminal to get an instant prediction.

---

## Goal
The goal of this project is to demonstrate **supervised learning**. The model is trained on labeled data (songs with known moods) and can predict the mood of new songs.

This can be useful for:

- Music recommendation  
- Mood-based playlists  
- Tagging music by emotion  

---

## Supervised Learning
Supervised learning uses labeled data, which means each song has input features and a correct label (Happy = 1, Sad = 0). The model learns the relationship between the inputs and labels to make predictions on new data.

---

## Dataset
The dataset is small and created for this project:

| Tempo | Energy | Positivity | Mood |
|-------|--------|------------|------|
| 120 | 7 | 8 | 1 |
| 85  | 3 | 2 | 0 |
| 140 | 8 | 9 | 1 |
| 95  | 4 | 3 | 0 |
| 160 | 9 | 7 | 1 |
| 75  | 2 | 1 | 0 |
| 132 | 6 | 6 | 1 |
| 88  | 3 | 4 | 0 |
| 150 | 9 | 5 | 1 |
| 100 | 5 | 2 | 0 |

---

## How the Program Works
1. The dataset is split into training and testing sets.  
2. A Logistic Regression model is trained on the training data.  
3. The model predicts moods for the test set and prints the accuracy.  
4. Users enter new song features in the terminal.  
5. The program outputs whether the song is Happy or Sad.  
6. The program waits for the user to press Enter before closing.

---

## Example Terminal Interaction

