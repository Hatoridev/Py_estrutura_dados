import sqlite3

class TransactionObject:
    database = "clientes.db"
    conn = None
    cur = None
    connected = False

    def connect(self):
        self.conn = sqlite3.connect(self.database)
        self.cur = self.conn.cursor()
        self.connected = True

    def disconnect(self):
        self.conn.close()
        self.connected = False

    def execute(self, sql, parms=None):
        if self.connected:
            if parms is None:
                self.cur.execute(sql)
            else:
                self.cur.execute(sql, parms)
            return True
        else:
            return False

    def fetchall(self):
        return self.cur.fetchall()

    def persist(self):
        if self.connected:
            self.conn.commit()
            return True
        else:
            return False

def initDB():
    trans = TransactionObject()
    trans.connect()
    trans.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY,
            nome TEXT,
            sobrenome TEXT,
            email TEXT,
            cpf TEXT
        )
    """)
    trans.persist()
    trans.disconnect()

def insert(nome, sobrenome, email, cpf):
    trans = TransactionObject()
    trans.connect()
    trans.execute("INSERT INTO clientes VALUES (NULL, ?, ?, ?, ?)", (nome, sobrenome, email, cpf))
    trans.persist()
    trans.disconnect()

def view():
    trans = TransactionObject()
    trans.connect()
    trans.execute("SELECT * FROM clientes")
    rows = trans.fetchall()
    trans.disconnect()
    return rows

def search(nome="", sobrenome="", email="", cpf=""):
    trans = TransactionObject()
    trans.connect()
    trans.execute("SELECT * FROM clientes WHERE nome=? OR sobrenome=? OR email=? OR cpf=?", (nome, sobrenome, email, cpf))
    rows = trans.fetchall()
    trans.disconnect()
    return rows

def delete(id):
    trans = TransactionObject()
    trans.connect()
    trans.execute("DELETE FROM clientes WHERE id=?", (id,))
    trans.persist()
    trans.disconnect()

def update(id, nome, sobrenome, email, cpf):
    trans = TransactionObject()
    trans.connect()
    trans.execute("UPDATE clientes SET nome=?, sobrenome=?, email=?, cpf=? WHERE id=?", (nome, sobrenome, email, cpf, id))
    trans.persist()
    trans.disconnect()

initDB()

# Este arquivo define a classe TransactionObject para gerenciar operações no banco de dados SQLite.

# Funções auxiliares (initDB, insert, view, search, delete, update) interagem com a classe TransactionObject para realizar operações específicas no banco de dados.

# initDB é chamado no final para garantir que a tabela clientes seja criada se ainda não existir.

