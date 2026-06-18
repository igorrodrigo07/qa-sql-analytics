import sqlite3

# Criar conexão com banco
conn = sqlite3.connect("qa_metrics.db")

cursor = conn.cursor()

# Criar tabela
cursor.execute("""
CREATE TABLE IF NOT EXISTS bugs (
    id INTEGER PRIMARY KEY,
    sprint TEXT,
    modulo TEXT,
    severidade TEXT,
    status TEXT
)
""")

# Inserir dados de exemplo
dados = [
    (1, "Sprint 1", "Login", "Crítica", "Aberto"),
    (2, "Sprint 1", "Carrinho", "Alta", "Fechado"),
    (3, "Sprint 1", "Checkout", "Média", "Fechado"),
    (4, "Sprint 1", "Perfil", "Baixa", "Aberto"),

    (5, "Sprint 2", "Login", "Alta", "Fechado"),
    (6, "Sprint 2", "Checkout", "Média", "Fechado"),
    (7, "Sprint 2", "Carrinho", "Crítica", "Aberto"),
    (8, "Sprint 2", "Perfil", "Baixa", "Fechado"),

    (9, "Sprint 3", "Login", "Alta", "Fechado"),
    (10, "Sprint 3", "Checkout", "Média", "Fechado"),
    (11, "Sprint 3", "Carrinho", "Alta", "Aberto"),
    (12, "Sprint 3", "Perfil", "Baixa", "Fechado"),

    (13, "Sprint 4", "Login", "Média", "Fechado"),
    (14, "Sprint 4", "Checkout", "Alta", "Fechado"),
    (15, "Sprint 4", "Carrinho", "Baixa", "Fechado"),
    (16, "Sprint 4", "Perfil", "Crítica", "Aberto"),

    (17, "Sprint 5", "Login", "Baixa", "Fechado"),
    (18, "Sprint 5", "Checkout", "Média", "Fechado"),
    (19, "Sprint 5", "Carrinho", "Alta", "Fechado"),
    (20, "Sprint 5", "Perfil", "Baixa", "Fechado")
]

cursor.executemany("""
INSERT OR REPLACE INTO bugs
(id, sprint, modulo, severidade, status)
VALUES (?, ?, ?, ?, ?)
""", dados)

conn.commit()
conn.close()

print("Banco criado com sucesso!")