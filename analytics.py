import sqlite3
import matplotlib.pyplot as plt
import os

# Criar pasta output
os.makedirs("output", exist_ok=True)

# Conectar ao banco
conn = sqlite3.connect("qa_metrics.db")
cursor = conn.cursor()

# ==========================
# BUGS POR SPRINT
# ==========================

cursor.execute("""
SELECT sprint, COUNT(*)
FROM bugs
GROUP BY sprint
ORDER BY sprint
""")

dados_sprint = cursor.fetchall()

# ==========================
# BUGS POR SEVERIDADE
# ==========================

cursor.execute("""
SELECT severidade, COUNT(*)
FROM bugs
GROUP BY severidade
ORDER BY COUNT(*) DESC
""")

dados_severidade = cursor.fetchall()

# ==========================
# MÓDULOS COM MAIS DEFEITOS
# ==========================

cursor.execute("""
SELECT modulo, COUNT(*)
FROM bugs
GROUP BY modulo
ORDER BY COUNT(*) DESC
""")

dados_modulos = cursor.fetchall()

# ==========================
# TAXA DE RESOLUÇÃO
# ==========================

cursor.execute("""
SELECT
ROUND(
SUM(CASE WHEN status='Fechado' THEN 1 ELSE 0 END)*100.0
/ COUNT(*),
2
)
FROM bugs
""")

taxa_resolucao = cursor.fetchone()[0]

# ==========================
# RELATÓRIO TXT
# ==========================

relatorio = f"""
===== SQL ANALYTICS QA =====

Bugs por Sprint:
{dados_sprint}

Bugs por Severidade:
{dados_severidade}

Módulos com mais defeitos:
{dados_modulos}

Taxa de Resolução:
{taxa_resolucao}%
"""

with open("output/relatorio_sql.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write(relatorio)

# ==========================
# GRÁFICO 1
# Bugs por Sprint
# ==========================

sprints = [x[0] for x in dados_sprint]
total_sprint = [x[1] for x in dados_sprint]

plt.figure(figsize=(8,5))
plt.plot(sprints, total_sprint, marker="o")
plt.title("Bugs por Sprint")
plt.xlabel("Sprint")
plt.ylabel("Quantidade")
plt.tight_layout()
plt.savefig("output/bugs_por_sprint.png")
plt.close()

# ==========================
# GRÁFICO 2
# Bugs por Severidade
# ==========================

severidades = [x[0] for x in dados_severidade]
total_severidade = [x[1] for x in dados_severidade]

plt.figure(figsize=(8,5))
plt.bar(severidades, total_severidade)
plt.title("Bugs por Severidade")
plt.xlabel("Severidade")
plt.ylabel("Quantidade")
plt.tight_layout()
plt.savefig("output/bugs_por_severidade.png")
plt.close()

# ==========================
# GRÁFICO 3
# Módulos com Mais Bugs
# ==========================

modulos = [x[0] for x in dados_modulos]
total_modulos = [x[1] for x in dados_modulos]

plt.figure(figsize=(8,5))
plt.bar(modulos, total_modulos)
plt.title("Módulos com Mais Defeitos")
plt.xlabel("Módulo")
plt.ylabel("Quantidade")
plt.tight_layout()
plt.savefig("output/modulos_com_mais_bugs.png")
plt.close()

conn.close()

print("Relatório criado com sucesso!")
print("Gráficos gerados com sucesso!")