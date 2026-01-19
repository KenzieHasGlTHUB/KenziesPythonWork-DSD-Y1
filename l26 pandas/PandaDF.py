import pandas as pd
 
data = {
    "Name": ["Alex", "Jamie", "Sam"],
    "Attendance": [92, 85, 78],
    "Grade": ["B", "C", "D"]
}
data["Name"].append(str("Kenzie"))
data["Attendance"].append(int(88))
data["Grade"].append(str("C"))
 
df = pd.DataFrame(data)
df = data
print(df)
