#mysql = MySQL(app)
 
#Creating a connection cursor
#cursor = mysql.connection.cursor()
 
#Executing SQL Statements
import mysql.connector
mydb = mysql.connector.connect(
    host = 'localhost',
    port = '3306',
    user = 'root',
    password = 'root123',
    database = 'mydatabase'
)


#Insert a record in the "customers" table:
#sql = "INSERT INTO Customers (name, address) VALUES (%s, %s)"
#var = ("John", "Highway 21")
#mycursor.execute(sql,var)
#mydb.commit()
#print(mycursor.rowcount, "record inserted")

def create_table():
    checktable_sql="""SELECT 
                    TABLE_SCHEMA, 
                    TABLE_NAME,
                    TABLE_TYPE
                    FROM 
                    information_schema.TABLES 
                    WHERE 
                    TABLE_SCHEMA='mydatabase' AND
                        TABLE_TYPE LIKE 'BASE TABLE' AND
                        TABLE_NAME = 'Employees';"""
    mycursor = mydb.cursor()
    mycursor.execute(checktable_sql)
    result=mycursor.fetchone()
    resp="Table created successfully"
    if len(result)==0:
        sql="CREATE TABLE Employees(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255),age INT, email VARCHAR(255), address VARCHAR(255),salary INT"
        mycursor.execute(sql)
        mydb.commit()
    else:
        resp="Table already exists"
    mycursor.close()
    return resp

def db_insert(val):
    sql = "INSERT INTO Employees(name, age, email, address, salary) VALUES (%s, %s, %s, %s, %s)"
    """
    val = [
    ('Peter', 30, 'peter@gmail.com,' 'Lowstreet 4', 10000),
    ('Amy',31,'amy@gmail.com', 'Apple st 652', 20000),
    ('Hannah', 'Mountain 21'),
    ('Michael', 'Valley 345'),
    ('Sandy', 'Ocean blvd 2'),
    ('Betty', 'Green Grass 1'),
    ('Richard', 'Sky st 331'),
    ('Susan', 'One way 98'),
    ('Vicky', 'Yellow Garden 2'),
    ('Ben', 'Park Lane 38'),
    ('William', 'Central st 954'),
    ('Chuck', 'Main Road 989'),
    ('Viola', 'Sideway 1633')
    ]
    """
    mycursor = mydb.cursor()
    mycursor.executemany(sql,val)
    mydb.commit()
    
    #Saving the Actions performed on the DB
    #mysql.connection.commit()
    
    #Closing the cursor
    mycursor.close()
def select_table_data(db_tablename):
    #if ";" in db_tablename:
        #return "Invalid Input"
    
    sql = "SELECT * FROM "+db_tablename
    mycursor = mydb.cursor()
    mycursor.execute(sql)
    result = mycursor.fetchall()
    mycursor.close()
    return result