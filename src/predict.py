from tensorflow.keras.models import load_model
import numpy as np

model = load_model("../models/heart_disease_model_v3.keras")

means = [53.87922210849539, 131.8229273285568, 211.94575230296826, 141.0348004094166, 0.9213920163766632, 1.7840327533265097
stds  = [9.327804604435439, 18.689447755500296
, 99.77518851245934, 24.986283466357058, 1.098304816588329, 0.5612403116764801]

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

# numeric features (normalized)
for i in range(6):
    while True:
        try:
            value = float(input(f"{feature_names[i]}: "))
            input_data.append((value - means[i]) / stds[i])
            break
        except ValueError:
            print("Invalid input!")

# categorical / one-hot features (raw)
for i in range(6, len(feature_names)):
    while True:
        try:
            value = float(input(f"{feature_names[i]} (0 or 1): "))
            input_data.append(value)
            break
        except ValueError:
            print("Invalid input!")

input_data = np.array(input_data).reshape(1, -1)

print("Input shape:", input_data.shape)

prediction = model.predict(input_data)
print("Prediction: ", prediction[0][0]*100, "%", sep="")