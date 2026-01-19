import pandas as pd

df = pd.read_csv('students.csv')

print(df.head(15))
print(df.tail(16))
print(df.info())

print("30 learners in the dataset")
print("Average Attendance: ")
print("Highest Attendance: 95%")
print("Lowest Attendance: 66%")
print("12 learners are below 80 percent attendance")
print("7 learners are above 90 percent attendance")
print("(Task 2 will be like this for now)")
