import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# Cria a tabela
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT,'
    'weight REAL'
    ')'
)
connection.commit()

# CRUD - Creat Read   Update Delete
# SQL - INSERT SELECT UPDATE DELETE

# CUIDADO: fazendo delete sem where
cursor.execute(
    f'DELETE FROM {TABLE_NAME}'
)

# DELETE mais seguro
cursor.execute(
    f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"'
)
# connection.commit()


# Registrar valores nas colunas da tabela
# cursor.execute(
#     f'INSERT INTO {TABLE_NAME} (id, name, weight)'
#     'VALUES'
#     '(NULL, "Helena", 6),'
#     '(NULL, "Eduardo", 9.6),'
#     '(NULL, "Luciano", 2)'
# )

sql = (
    f'INSERT INTO {TABLE_NAME} '
    '(name, weight) '
    'VALUES '
    '(:nome, :peso)'
)

# cursor.execute(sql, ['Joana', 4]) # Executa geralmente 1 valor
# cursor.executemany(sql, ( # Executa vários com
#     ('Joana', 4), ('Luiz', 5 )
#     )
# )

cursor.execute(sql, {'nome': 'Sem nome', 'peso': 4})
cursor.executemany(sql, (
                {'nome': 'Jason', 'peso': 96},
                {'nome': 'Maria', 'peso': 21},
                {'nome': 'Felipe', 'peso': 75},
                {'nome': 'João', 'peso': 45} 
            )
)

connection.commit()


if __name__ == '__main__':
    print(sql)

    cursor.execute(
        f'DELETE FROM {TABLE_NAME} '
        'WHERE id = "3"'
    )
    cursor.execute(
        f'DELETE FROM {TABLE_NAME} '
        'WHERE id = "1"'
    )
    connection.commit()
    
    cursor.execute(
        f'UPDATE {TABLE_NAME} '
        'SET name="QUALQUER", weight=67.53 '
        'WHERE id = "2"'
    )
    connection.commit()

    cursor.execute(
    f'SELECT * FROM {TABLE_NAME} '
    )

    for row in cursor.fetchall(): # Seleciona todas as linhas da tabela
        _id, name, weight = row
        print(_id, name, weight)


    cursor.close()
    connection.close()