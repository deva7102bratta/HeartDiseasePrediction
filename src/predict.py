# from tensorflow.keras.models import load_model
# import numpy as np

# Load trained model
# model_version = input("Model Version: ")
# model = load_model("./models/heart_disease_model_v1.keras")
required_features = [
    "Age",
    "Sex (0=Female, 1=Male)",
    "Chest Pain Type (0=No Chest Pain, 1=Typical Angina, 2=Atypical Angina, 3=Non-anginal Pain, 4=Asymptomatic)",
    "Resting Blood Pressure (mm Hg)",
    "Serum Cholesterol (mg/dL)",
    "Fasting Blood Sugar (0=≤120 mg/dL, 1=>120 mg/dL)",
    "Resting ECG (0=Normal, 1=ST-T Abnormality, 2=LV Hypertrophy)",
    "Maximum Heart Rate Achieved",
    "Exercise Induced Angina (0=No, 1=Yes)",
    "ST Depression (Oldpeak)",
    "Slope of Peak Exercise ST Segment (1=Upsloping, 2=Flat, 3=Downsloping)",
    "Number of Major Vessels (0–3)",
    "Thalassemia (1=Normal, 2=Fixed Defect, 3=Reversible Defect)"
]
input_data = []

for feature in required_features:
    while True:
      try:
        value = float(input(f"{feature}: "))
        input_data.append(value)
        break
      except ValueError:
        print("Please Enter Valid Number!!")
        
        

# Convert to NumPy array with shape (1, 13)
input_data = np.array([input_data])

print(input_data)
print(input_data.shape)
# Predict
# prediction = model.predict(input_data)

# print(prediction)