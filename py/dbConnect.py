import MySQLdb

conn = MySQLdb.connect("AdSkipper.mysql.pythonanywhere-services.com","AdSkipper","cozad123","AdSkipper$default")

c = conn.cursor()

c.execute("SELECT * FROM UserDetails")

rows = c.fetchall()

for eachRow in rows:
    print (eachRow)
