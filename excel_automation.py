import pandas as pd

# Excel file read
df = pd.read_excel("employees.xlsx")

# 10% salary hike
df["Updated Salary"] = df["Salary"] * 1.10

# Average salary
print("Average Salary:", df["Salary"].mean())

# Save updated file
df.to_excel("updated_employees.xlsx", index=False)

print("Automation Completed Successfully!")
