import pandas as pd
import numpy as np
import os
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

CSV_FILE = "Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv"
LABEL_COL = "label"
OUTPUT_DIR = "dataset"

MAX_SAMPLES = 1000 #I have added limitation because running the code took time
IMG_H = 8
IMG_W = 10

os.makedirs(f"{OUTPUT_DIR}/benign", exist_ok=True)
os.makedirs(f"{OUTPUT_DIR}/malware", exist_ok=True)

print("Loading CSV File, DO Not Worry ... yet")
data = pd.read_csv(CSV_FILE)

data[LABEL_COL] = data[LABEL_COL].astype(str).str.lower()

label_map = {
    "benign": 0,
    "ddos": 1
}

data = data[data[LABEL_COL].isin(label_map)]
data[LABEL_COL] = data[LABEL_COL].map(label_map)

y = data[LABEL_COL]

X = data.drop(columns=[LABEL_COL])
X = X.select_dtypes(include=["int64", "float64"])

X = X.replace([np.inf, -np.inf], np.nan)
X = X.dropna(axis=0)
y = y.loc[X.index]

scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)


for i in range(min(len(X_scaled), MAX_SAMPLES)):

    img = X_scaled[i][:IMG_H * IMG_W].reshape(IMG_H, IMG_W)
    label = "malware" if y.iloc[i] == 1 else "benign"

    plt.imsave(
        f"{OUTPUT_DIR}/{label}/sample_{i}.png",
        img,
        cmap="gray"
    )

print("It Works! Images created successfully")
