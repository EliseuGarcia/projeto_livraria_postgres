import psycopg2

con = psycopg2.connect(
    host='berry.db.elephantsql.com',
    database='srwstygg',
    user='srwstygg',
    password='LkFbK8vrOiNESIwFdhNvr5N_Y_iB3NiD'
)

print('conectado!')
