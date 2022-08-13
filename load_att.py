import  sqlalchemy
import pandas as pd
import pyexpat

engine = sqlalchemy.create_engine('mysql+mysqldb://root:Rajbhatta1!#$@localhost/bulk_uploadfile')
#data_sales = pd.read_excel(r'C:\Users\Samsung\Downloads\data fsds -20220812T084946Z-001\data fsds_\Dress Sales.xlsx')
#df = pd.DataFrame(data=data_sales)

#df.to_sql(con=engine,name='data_sales',if_exists='append',index= False)
#q1 = 'SELECT Dress_data.Dress_ID, data_sales.Dress_ID FROM Dress_data LEFT JOIN data_sales ON Dress_data.Dress_ID = data_sales.Dress_ID'
#q2 = "select Dress_Id from data_sales"
#data_ljoin = pd.read_sql(q1,engine)
#df = pd.DataFrame(data=data_ljoin)
#df.to_sql(name= 'data_ljoin', con= engine,if_exists='append',index= False)
#Write a sql query to find out how many unique dress that we have based on dress id
#q1 = 'select  count(distinct Dress_ID) from dress_data'
#df = pd.read_sql(q1,engine)
#print(df)
#Try to find out how mnay dress is having recommendation 0
#q2 = "select count(*)from dress_data where recommendation  = 0"
#print(pd.read_sql(q2,engine))
q3 = "SHOW COLUMNS FROM Dress_data"

df = pd.read_sql(q3,engine)
print(df)




















