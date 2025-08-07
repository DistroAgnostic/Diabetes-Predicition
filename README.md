# 🩺 Diabetes Prediction App

A lightweight **Streamlit** web app that estimates the likelihood of diabetes based on eight common medical indicators.

---

## 🚀 Quick Start

1. **Install dependencies**

   ```bash
   pip install streamlit numpy
   ```

2. **Place the model file**  
   Make sure `db_log_model.pkl` (your pre-trained logistic-regression model) is in the same folder as `diabetes.py`.

3. **Launch the app**

   ```bash
   streamlit run diabetes.py
   ```

4. **Open the browser**  
   Navigate to `http://localhost:8501`.

---

## 📊 Input Features

| Field | Widget | Range | Description |
|-------|--------|-------|-------------|
| **Pregnancies** | Slider | 0 – 17 | Number of times pregnant |
| **Glucose** | Slider | 0 – 199 | Plasma glucose concentration |
| **BloodPressure** | Slider | 0 – 122 | Diastolic BP (mm Hg) |
| **SkinThickness** | Slider | 0 – 99 | Triceps skin-fold thickness (mm) |
| **BMI** | Number input | 0.0 – 67.1 | Body-mass index |
| **DiabetesPedigreeFunction** | Number input | 0.0 – 2.42 | Diabetes pedigree function |
| **Age** | Slider | 0 – 81 | Age in years |
| **Insulin** | Slider | 0 – 846 | 2-hour serum insulin (mu U/ml) |

---

## 🔮 Prediction Output

After clicking **Predict**, the app returns:

- **Survived** + probability → if the model predicts **positive** for diabetes  
- **Not Survived** + probability → if the model predicts **negative**

*(The wording “Survived / Not Survived” is reused from a previous template—feel free to change it to “Diabetic / Not Diabetic” inside the code.)*

---

## 📁 Project Structure

```
.
├── diabetes.py          # Streamlit app
├── db_log_model.pkl     # Trained logistic-regression model
└── README.md            # This file
```

---

## 🤝 Contributing

Pull requests, feature ideas, and bug reports are welcome!

---

## 📄 License

This project is open-source under the [MIT License](LICENSE).
