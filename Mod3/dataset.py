import pandas as pd
# from sklearn.preprocessing import LabelEncoder

d = pd.read_excel('diabetes.xlsx')

d.plot(kind = 'scatter', x = 'Pregnancies', y = 'BloodPressure')

#Transforming outcome to binary: 0 = "alive" 1 = "dead"
# label_encoder = LabelEncoder()
# label_encoder.fit(d["Outcome"])


# Drop columns that are not part of four descriptive features
df = d.drop(columns=(["BloodPressure", "SkinThickness", "Insulin", "DiabetesPedigreeFunction"]), axis =1)

# Save new datafram to csv file
df.to_csv('modified.csv')

dfD2 = df[["Pregnancies", "Glucose", "BMI", "Age"]].mean()
dfD2.to_csv('modified2.csv')

dfD3 = df[["Outcome"]].mode()


print(dfD2)
# print(dfD3)












