import cx_Oracle
import time

def conn():
    db = cx_Oracle.connect('�˴���oracle�˺�/�˴���oracle����@�˴���oracle��ַ:�˴���˿�/�˴���oracle����')
# ��('ABC2019/ABC20191QAZ@100.10.100.10:8017/xe')
    return db

def insert(db,cr):
    cr = db.cursor()
    cr.execute('select * from hyl_table_a')
    rs = cr.fetchall()
    cr.close()
    return rs

if __name__ == '__main__':
    start = time.process_time()
    db = conn()
    cr = db.cursor
    result = insert(db,cr)
    print(list(result))
    end = time.process_time()
    print("final is in ", end - start)