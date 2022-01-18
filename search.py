import cx_Oracle
con = cx_Oracle.connect("SFWGEC", "SFWGEC", "localhost/ORCL")
cursor = con.cursor()
print("Database version:", con.version)

sql = """SELECT *
         FROM TESTE
         """
cursor.execute(sql)

for row in cursor:
    print(row)
#AQUI VOCÊ TEM QUE USAR O INTERPRETADOR PYTHON DE 32 BITS POR CAUSA DO BANCO DE DADOS