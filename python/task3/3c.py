# ///Modular Python Application (3 files)
# students.csv
# Name,Age,Math,Science,English
# Alice,20,85,78,92
# Bob,21,90,88,84
# Charlie,20,72,65,70
# David,22,95,92,96
# Eva,21,88,90,85///

# dataloader.py
# import pandas as pd
# def load_data():
    # df = pd.read_csv("students.csv")
    # return df

# statshelper.py
# import numpy as np
# from scipy import stats
# def subject_mean(df, subject):
    # return np.mean(df[subject])
# def subject_std(df, subject):
    # return np.std(df[subject])
# def subject_mode(df, subject):
    # return stats.mode(df[subject], keepdims=True).mode[0]

# main.py
from dataloader import load_data
from statshelper import subject_mean, subject_std, subject_mode
import pandas as pd
df = load_data()
subjects = ["Math", "Science", "English"]
results = []
for subj in subjects:
    mean_val = subject_mean(df, subj)
    std_val = subject_std(df, subj)
    mode_val = subject_mode(df, subj)
    results.append([subj, mean_val, std_val, mode_val])
results_df = pd.DataFrame(results, columns=["Subject", "Mean", "Standard Deviation", "Mode"])
print(results_df)