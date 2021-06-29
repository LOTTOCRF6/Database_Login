import mysql.connector


mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1', database='Hospital',auth_plugin='mysql_native_password')
mycursor = mydb.cursor()
sql = "INSERT INTO Login (username, password) Value(%s, %s)"
val = ("leto", "zet"), ()
mycursor.execute(sql, val)
mydb.commit()