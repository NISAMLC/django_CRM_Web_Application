import mysql.connector

dataBase = mysql.connector.connect(
    host="localhost",
    user = "root",
    passwd = "158031",

)

#prepare a cursor
cursorObject = dataBase.cursor()


#create a database
cursorObject.execute("CREATE DATABASE crmCompany")

print("ALL Done")