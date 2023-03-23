# Subir datos de un archivo csv a una base de datos en MySQL

import mysql.connector
import pandas as pd

# Conexion a la base de datos MySQL
connect_mydb = mysql.connector.connect(host='localhost',
                               user='root',
                               database='twitter_db',
                               port='3306')
# Leer el archivo csv con los tweets del primer dataset
dataframe = pd.read_csv('GPT4.csv')

# Crear un cursor para ejecutar las consultas
cursor = connect_mydb.cursor()

# Crear una tabla en la base de datos MySQL donde se almacenaran los tweets del primer dataset 
cursor.execute('CREATE TABLE tweets_GPT4 (id INT AUTO_INCREMENT PRIMARY KEY, Date VARCHAR(255), Username VARCHAR(255), Tweet VARCHAR(255), Polarity VARCHAR(255), Subjectivity VARCHAR(255))')

# Insertar valores del dataframe en la tabla creada en la base de datos MySQL 
for i, row in dataframe.iterrows():
    sql = "INSERT INTO tweets_GPT4 (Date, Username, Tweet, Polarity, Subjectivity) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(sql, tuple(row))
    # Imprimir el numero de filas insertadas hasta el momento
    print("Filas insertadas: ",i, end='\r')
    connect_mydb.commit()