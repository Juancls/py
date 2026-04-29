import sqlite3

def createDb(db):
    conn = sqlite3.connect(db) # criando a conexão com o DB
    c = conn.cursor() #criado o objeto cursor para manipular os dados
    c.execute(
        '''
            CREATE TABLE IF NOT EXISTS estoque (id integer, data text, transacao text, simbolo text, quant real, preco real)
        '''
    )
    conn.commit()
    compras = [
        (1, '2026-04-29', 'Compra', 'Tags', 1000, 45.00),
        (2, '2026-04-20', 'Compra', 'Ball', 5, 15.00),
        (3, '2026-04-02', 'Vendas', 'Tags', 20, 150.00)
    ]

    c.executemany('INSERT INTO estoque values (?, ?, ?, ?, ?, ?)', compras) # usado para inserir varios itens de uma vez só
    c.execute('INSERT INTO estoque VALUES(4, "2026-04-29", "Venda", "Tags", 500, 950.00)')
    conn.commit()
    conn.close()

#programa principal
if __name__ == "__main__":
    createDb("aulaDb.db")