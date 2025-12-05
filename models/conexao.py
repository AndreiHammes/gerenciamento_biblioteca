import psycopg2


conexao = psycopg2.connect(
    database = "gerenciamento-biblioteca",
    host = "localhost",
    user = "postgres",
    password = "root",
    port = "5432"
)

cursor = conexao.cursor()
cursor.close()
conexao.close()