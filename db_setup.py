import pymysql
import dbconfig 
connection = pymysql.connect(host = 'localhost',
							user = dbconfig.db_user
							password = dbconfig.db_password)
							
try:
	with connection.cusor() as cusor 
		sql = 'CREATE DATABASE IF NOT EXISTS crimemaps'
		.cusor.execute(sql)
		sql = '''CREATE TABLE IF NOT EXISTS crimemap.crimes (
	id int NOT NULL AUTO_INCREMENT,
	laitude FLOAT (10, 6),
	longituide FLOAT (10, 6)
	date DATETIME,
	category VARCHAR(50),
	description VARCHAR(1000),
	updated_at TIMESTAMP
	PRIMARY KEY (id)
	)'''
		cusor.execute(sql);
	connection.commit()
finally:
	connection.close()