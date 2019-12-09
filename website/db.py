import sqlite3

def insertResumo(name, resumo, arquivo):
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO resumo (id, nameUpload, resumoCriptografico, arquivo) VALUES (?,?,?,?)", (countResumo(), name, resumo, arquivo))
    conn.commit()
    conn.close()

def countResumo():
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) As total from resumo")
    return_value = cursor.fetchone()[0] + 1
    conn.close()
    return return_value

def insertChaves(tipo, n, e, p, q, d):
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO chaves (id, tipo, n, e, p, d, q) VALUES (?,?,?,?,?,?,?)", (countChaves(), tipo, n, e, p, q, d))
    conn.commit()
    conn.close()

def countChaves():
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) As total from chaves")
    return_value = cursor.fetchone()[0] + 1
    conn.close()
    return return_value