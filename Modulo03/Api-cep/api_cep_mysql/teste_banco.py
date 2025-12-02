import mysql.connector

conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="sua_senha"
        )

cursor = conexao.cursor()

def criar_banco():

        cursor.execute("SHOW DATABASES LIKE 'cep';")
        existe_banco = cursor.fetchone()

        if not existe_banco:
            print("Banco 'cep' nao existe ")
            cursor.execute("CREATE DATABASE cep;")
            conexao.commit()
        else:
            print("Banco 'cep' já existe.")
        cursor.execute("USE cep;")

        cursor.execute("""
            SHOW TABLES LIKE 'endereco';
        """)
        existe_tabela = cursor.fetchone()

        if not existe_tabela:
            print("Tabela 'endereco' nao exite")
            cursor.execute("""
                CREATE TABLE endereco(
                    cep VARCHAR(10),
                    logradouro VARCHAR(100),
                    bairro VARCHAR(100),
                    localidade VARCHAR(100),
                    uf VARCHAR(2)
                );
            """)
            conexao.commit()
        else:
            print("Tabela 'endereco' já existe.")

        print("Banco e tabela prontos para uso!")

def inserir_valor(cep, logradouro, bairro, localidade, uf):
    sql = """
    INSERT INTO endereco (cep, logradouro, bairro, localidade, uf)
    VALUES (%s, %s, %s, %s, %s)
    """
    valores = (
        cep ,
        logradouro,
        bairro,
        localidade,
        uf
        )
    cursor.execute(sql, valores)
    conexao.commit()
        
def ver_banco():
    cursor.execute("SELECT * FROM endereco")
    resultado = cursor.fetchall()

    for linha in resultado:
        print(linha)

cursor.close()
conexao.close()


