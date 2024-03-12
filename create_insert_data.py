import pandas as pd


sqlLIST = []
CsidLIST = []
genderLIST = []
AgeLIST = []
AnnincomeLIST = []
SpenScoLIST = []
ProfLIST = []
WorkExpLIST = []
FamSizeLIST = []



table = f"CREATE TABLE IF NOT EXISTS Customers (CustomerID INT PRIMARY KEY,Gender VARCHAR(255),Age INT, AnnualIncome INT, SpendingScore INT, Profession VARCHAR(255), WorkExperience INT, FamilySize INT);"

sqlLIST.append(table)

#print(sqlLIST)


#extract and insert data from excel sheet
filepath = ("C:/Users/jorda/Desktop/School/Tertiary Education/Computer Science/2023-2024/Semester 2/COMP3161 - Introduction to Database Management Systems/Lab/Lab3/Customers.csv")

df = pd.read_csv(filepath)


#print(df['Gender'].head(5))

for id in df['CustomerID'].head(2000):
    CsidLIST.append(id)

for gender in df['Gender'].head(2000):
    genderLIST.append(gender)

for age in df['Age'].head(2000):
    AgeLIST.append(age)

for income in df['Annual Income ($)'].head(2000):
    AnnincomeLIST.append(income)

for score in df['Spending Score (1-100)'].head(2000):
    SpenScoLIST.append(score)

for profession in df['Profession'].head(2000):
    ProfLIST.append(profession)

for exp in df['Work Experience'].head(2000):
    WorkExpLIST.append(exp)

for famsize in df['Family Size'].head(2000):
    FamSizeLIST.append(famsize)

#print(CsidLIST)
#print(genderLIST)
#print(AgeLIST)
#print(AnnincomeLIST)
#print(SpenScoLIST)
#print(ProfLIST)
#print(WorkExpLIST)
#print(FamSizeLIST)

#print(len(CsidLIST))
#print(len(genderLIST))
#print(len(AgeLIST))
#print(len(AnnincomeLIST))
#print(len(SpenScoLIST))
#print(len(ProfLIST))
#print(len(WorkExpLIST))
#print(len(FamSizeLIST))

print_statement = []
   
for customer in range(len(CsidLIST)):
        insert_statement = f"INSERT INTO Customers (CustomerID, Gender, Age, AnnualIncome, SpendingScore, Profession, WorkExperience, FamilySize) VALUES ({CsidLIST[customer]}, '{genderLIST[customer]}' , {AgeLIST[customer]} , {AnnincomeLIST[customer]}, {SpenScoLIST[customer]}, '{ProfLIST[customer]}', {WorkExpLIST[customer]}, {FamSizeLIST[customer]});"
        print_statement.append(insert_statement)

#print(print_statement)
sqlLIST += print_statement


with open('create_insert_sql_LAB3.sql', 'w') as file:
    for statement in sqlLIST:
        file.write(statement + "\n")