import mysql.connector


dataBase = mysql.connector.connect(
    host="localhost",
    user = 'root',
    passwd = 'Bakomans24.',
)
cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE tomek")

print("all done !")