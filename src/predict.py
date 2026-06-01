from tensorflow.keras.models import load_model
import numpy as np
import pandas as pd

model = load_model("./models/heart_disease_model_v3.keras")

# means = pd.read_csv("../data/means.csv")
# stds = pd.read_csv("../data/stds.csv")

# age_mean = 54.97
# trestbps_mean = 132.35
# chol_mean = 247.45
# thalach_mean = 147.62
# oldpeak_mean = 1.10
# slope_mean = 1.60

# age,8.885122458722824
# trestbps,18.186912785860557
# chol,49.54693487176298
# thalach,23.463325904851786
# oldpeak,1.183855640287323
# slope,0.6309776383383059

means = [54.97, 132.35, 247.45, 147.62, 1.10, 1.60]
stds = [8.885122458722824, 18.186912785860557, 49.54693487176298, 23.463325904851786, 1.183855640287323, 0.6309776383383059
]

feature_names = [
    "age","trestbps","chol","thalach","oldpeak","slope",
    "sex_0","sex_1",
    "cp_0","cp_1","cp_2","cp_3","cp_4",
    "fbs_0","fbs_1",
    "restecg_0","restecg_1","restecg_2",
    "exang_0","exang_1",
    "ca_0","ca_1","ca_2","ca_3",
    "thal_fixed","thal_normal","thal_reversible"
]

input_data = []

for i in range(6):
    while True:
        try:
            value = float(input(f"{feature_names[i]}: "))
            input_data.append((value-means[i])/stds[i])
            break
        except:
            print("Invalid input!")
for i in range(6:):
    while True:
        try:
            value = float(input(f"{feature_names[i]}: "))
            input_data.append(value)
            break
        except:
            print("Invalid input!")  
            
input_data = np.array(input_data).reshape(1, -1)
print(input_data)
print(input_data.shape)
# Predict
# prediction = model.predict(input_data)

# print(prediction)