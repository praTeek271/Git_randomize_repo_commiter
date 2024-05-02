import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    result= employee['salary'].drop_duplicates().sort_values(ascending=False).iloc[1]

    if result:
        return  pd.DataFrame( data = {"SecondHighestSalary":[result]}) 
    else:
        return  pd.DataFrame( data = {"SecondHighestSalary":[None]}) 



data = [[1, 100], [2, 200], [3, 300], [4, 400], [5, 500], [6, 600], [7, 700], [8, 800], [9, 900], [10, 1000]]
employee = pd.DataFrame(data, columns=['id', 'salary']).astype({'id':'int64', 'salary':'int64'})

print(second_highest_salary(employee))