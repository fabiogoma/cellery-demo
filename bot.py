from tasks import extract
import time
import sqlite3

con = sqlite3.connect('origem.db')
cur = con.cursor()

cur.execute('SELECT RootDomain FROM top_domains')

resultados = []
lista_de_sites = cur.fetchall()

for site in lista_de_sites:
    resultados.append(extract.delay(f'https://{site[0]}'))

time.sleep(40)

pendentes = []
sucesso = 0
for resultado in resultados:
    if resultado.status == 'SUCCESS':
        print(resultado.get())
        sucesso += 1
    else:
        pendentes.append(resultado)

print(f"Total records in the database: { len(lista_de_sites) }")
print(f"Total succeded tasks : { sucesso }")
print(f"Total pending tasks : { len(pendentes) }")
