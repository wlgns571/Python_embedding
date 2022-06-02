import cx_Oracle

class DBmanager:
    def __init__(self):
        self.conn = None
        self.get_connection()
    def __del__(self):
        try:
            print('소멸자')
            if self.conn:
                self.conn.close()
        except Exception as e:
            print('_del_ 오류', str(e))
    def get_connection(self):
        self.conn = cx_Oracle.connect("java", "oracle", "localhost:1521/XE", encoding="utf-8")
        return self.conn
    def fn_insert(self, query, param):
        cursor = self.conn.cursor()
        cursor.execute(query, param)
        self.conn.commit()
        cursor.close()

if __name__ == '__main__':
    print('conn test')
    try:
        manager = DBmanager()
        conn = manager.get_connection()
        print(conn.version)
    except Exception as e:
        print(str(e))
    finally:
        print('conn close')
