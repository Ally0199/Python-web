import mysql.connector
import json

class DBMySQL():
    def __init__(self):
        self.conector = mysql.connector.connect(user='root', password='S', host='localhost',port=3306, database='employees',auth_plugin='mysql_native_password')
    
    def getAllDepartments(self):
        cursor = self.conector.cursor()
        sql = "SELECT * from departments"
        cursor.execute(sql)
        data = []
        for (dept_no, dept_name,fecha, anios) in cursor.fetchall():
            data.append({'id': dept_no, 'name': dept_name, 'fecha': fecha, 'anios': anios})
        return data
    
    def findByNameDepartment(self, dept_name):
        print(dept_name)
        cursor = self.conector.cursor()
        sql = "SELECT * from departments WHERE dept_name like '%" + dept_name + "%'"
        cursor.execute(sql, dept_name)
        data = cursor.fetchall()
        return json.dumps(data)
        
    def closeConnection(self):
        self.conector.close()