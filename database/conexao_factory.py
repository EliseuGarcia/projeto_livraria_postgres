import psycopg2


class ConexaoFactory:

    def get_conexao(self):
        return psycopg2.connect(
            host='berry.db.elephantsql.com',
            database='srwstygg',
            user='srwstygg',
            password='LkFbK8vrOiNESIwFdhNvr5N_Y_iB3NiD'
        )
