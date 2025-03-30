# PyMySQL - um cliente MySQL feito em Python Puro
# Doc: https://pymysql.readthedocs.io/en/latest/
# Pypy: https://pypi.org/project/pymysql/
# GitHub: https://github.com/PyMySQL/PyMySQL
import os

import dotenv 
import pymysql
import pymysql.cursors

TABLE_NAME = 'customers'

dotenv.load_dotenv()

connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor,
)

with connection:
    with connection.cursor() as cursor:
        cursor.execute(
            f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ('
            'id INT NOT NULL AUTO_INCREMENT, '
            'nome VARCHAR(50) NOT NULL, '
            'idade INT NOT NULL, '
            'PRIMARY KEY (id)'
            ') '
        )

        # Cuidado isso limpa a TABELA
        cursor.execute(f'TRUNCATE TABLE {TABLE_NAME} ')
    connection.commit()

    # Manipulação de dados a partir daqui

    # Inserindo um valor com apenas o placeholder
    with connection.cursor() as cursor:
        # cursor.execute(
        #     f'INSERT INTO {TABLE_NAME} '
        #     '(nome, idade) VALUES ("Luiz", 25) '
        # )
        # cursor.execute(
        #     f'INSERT INTO {TABLE_NAME} '
        #     '(nome, idade) VALUES ("Luiz", 25) '
        # )
        sql = (
            f'INSERT INTO {TABLE_NAME} (nome, idade) '
            'VALUES (%s, %s) '
            )
        data= ('Luiz', 18)
        result = cursor.execute(sql, data) # Precisa de um valor
        # print(sql)
        # print(result)
    
    connection.commit()

    # Inserindo um valor com dicionário e placeholder
    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) '
            'VALUES (%(name)s, %(age)s) '
            )
        data2 = {
            "name": "Ane",
            "age": 25,
        }
        result = cursor.execute(sql, data2) # Precisa de um valor
        # print(sql)
        # print(data2)
        # print(result)

    # Inserindo vários valores com tupla, dicionário e placeholder
    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) '
            'VALUES (%(name)s, %(age)s) '
            )
        data3 = (
            {"name": "Jef", "age": 33,},
            {"name": "Juh", "age": 64,},
            {"name": "Rose", "age": 45,}
            )
        result = cursor.executemany(sql, data3) # Precisa ser um valor iterável
        # print(sql)
        # print(data3)
        # print(result)

    connection.commit()
    
    # Inserindo vários valores sem dicionário só com placeholder e com tupla de tuplas
    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) '
            'VALUES (%s, %s) '
            )
        data4 = (
            ("Helena", 22),
            ("Cortana", 15),
            ("Luiz", 18)
            )
        result = cursor.executemany(sql, data4) # Precisa ser um valor iterável
        # print(sql)
        # print(data4)
        # print(result)

    connection.commit()

    # Lendo valores com SELECT (CONSULTA)
    with connection.cursor() as cursor:
        # menor_id = int(input('Digite o menor ID: '))
        # maior_id = int(input('Digite o maior ID: '))
        menor_id = 2
        maior_id = 4
        # coluna = 'id'
        sql = (
            f'SELECT * FROM {TABLE_NAME} '
            f'WHERE id BETWEEN %s AND %s ' 
            )
        
        cursor.execute(sql, (menor_id, maior_id))
        # print(cursor.mogrify(sql, (menor_id, maior_id)))
        data5 = cursor.fetchall() # Busca todos os valores
        
        # for row in data5:
        #     print(row)

    # Excluindo valores com DELETE, WHERE e placeholders
    with connection.cursor() as cursor:
        sql = (
            f'DELETE FROM {TABLE_NAME} '
            # 'WHERE id = %s'
            'WHERE id BETWEEN %s AND %s'
            )
        
        cursor.execute(sql, (4, 6)) # Executa o arquivo SQL com os valores em uma tupla para os placeholder
        # print(cursor.execute(sql, (4, 6))) # Print exibe quantas linhas foram afetadas

        cursor.execute(f'SELECT * FROM {TABLE_NAME} ')
        
        # for row in cursor.fetchall():
        #     print(row)

    connection.commit()

    # Editando/Atualizando com UPDATE, WHERE e placeholders
    with connection.cursor() as cursor:
        sql = (
            f'UPDATE {TABLE_NAME} '
            'SET nome = %s, idade = %s '
            'WHERE id = %s'
            )
        
        cursor.execute(sql, ('Felipe', 75, 7)) # Executa o arquivo SQL com os valores em uma tupla para os placeholder
        # cursor.execute(f'SELECT * FROM {TABLE_NAME} ')
        resultFromSelect = cursor.execute(f'SELECT * FROM {TABLE_NAME} ')# Print exibe quantas linhas foram afetadas
        
        # for row in cursor.fetchall():
        #     _id, nome, idade = row # Desempacotamento
        #     print(_id, nome, idade)        

        data6 = cursor.fetchall() # É possível chamar essa var várias vezes

        for row in data6:
        # for row in cursor.fetchall(): 
            print(f'ID:', row['id'],'|','Nome:', f"{row.get('nome', '')[:6]:<6}",'|','Idade:',row['idade'],'|')
            # print(f"{row.get('nome', '')[:5]:<5}")
            # print(row)
        
        print('resultFromSelect', resultFromSelect) # Linhas iteradas
        print('len(data6)', len(data6)) # Quantos dados tem em data6
        print('rowcount', cursor.rowcount) # Última operação do cursor
     
        sql = (
            f'INSERT INTO {TABLE_NAME} (nome, idade) '
            'VALUES (%s, %s) '
            )
        data= ('ultimo_valor', 18)
        cursor.execute(sql, data)    
     
        print('lastrowid', cursor.lastrowid) # Retorna a id do último valor (com exceção do primeiro valor adicionado caso seja executado com executemany)

        cursor.execute(
            f'SELECT id FROM {TABLE_NAME} ORDER BY id DESC LIMIT 1'
        ) # Retorna o ultimo valor da tabela
        lastIdFromSelect = cursor.fetchone()

        print('lastrowid script proprio', lastIdFromSelect)

        cursor.execute(f'SELECT * FROM {TABLE_NAME} ') # Seleciona toda as colunas da tabela
        cursor.scroll(3) # Rola 3 iteração a frente
        print('rownumber', cursor.rownumber) # Retorna a posição do cursor
        for row in cursor.fetchall():
            print(row)

    connection.commit()
        
    
        