# Height Classifier

## Description
This is a simple terminal-based machine learning program that predicts whether a person is **Tall** or **Short** based on their **height and weight**.  

The program uses a **public dataset** downloaded from Google/FSU:

- Dataset: [hw_200.csv](https://people.sc.fsu.edu/~jburkardt/data/csv/hw_200.csv)  
- Features: Height (inches), Weight (pounds)  
- Label: Tall (1) if height > median, Short (0) if height ≤ median  
- Model: Logistic Regression (simple supervised ML)

The program reads the dataset **directly**, cleans the column names in Python, trains a model, and then interacts with the user in the terminal.

---

## How to Run
1. Make sure Python 3 is installed.  
2. Install required packages:
3. Place the downloaded public Dataset file in the same folder as the script.  
4. Run the script in terminal:
5. Input **height (inches)** when prompted.  
6. Input **weight (pounds)** when prompted.  
7. The program will predict **Tall** or **Short**.  
8. Press Enter to exit.  

---

## Limitations
Only height and weight are used.  
Other factors like age or gender are ignored.  
Predictions are based on the dataset median height.  
Results may not generalize to all populations.  
The model is simple.  
More advanced ML models could improve accuracy.  
Accuracy depends on the training dataset.  
Small datasets may lead to less reliable predictions.  

---

## Notes
The program does not require editing the CSV file.  
Column names are handled automatically in Python.  
The dataset is publicly available.  
It can be downloaded from Google/FSU: [hw_200.csv](https://people.sc.fsu.edu/~jburkardt/data/csv/hw_200.csv)






