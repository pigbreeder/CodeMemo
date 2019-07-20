import sqlite3
from log_init import Log
from init_sql import sql_file
conn = sqlite3.connect(sql_file)
cur = conn.cursor()
log = Log()
class Sql:

    @classmethod
    def insert_corpus(cls, jp, cn):
        sql = 'INSERT INTO jp2cn (`jp`, `cn` ) VALUES (?, ?)'
        try:
            cur.execute(sql,(jp,cn))
            conn.commit()
        except Exception as e:
            log.error('insert failed!,e='+str(e))
        return cur.rowcount
    @classmethod
    def insert_dd_chaptername(cls, xs_chaptername, xs_content, id_name, num_id, url):
        sql = 'INSERT INTO dd_chaptername (`xs_chaptername`, `xs_content`, `id_name`, `num_id`, `url`) \
                VALUES (%(xs_chaptername)s, %(xs_content)s, %(id_name)s, %(num_id)s, %(url)s)'
        value = {
            'xs_chaptername': xs_chaptername,
            'xs_content': xs_content,
            'id_name': id_name,
            'num_id': num_id,
            'url': url
        }
        cur.execute(sql, value)
        conn.commit()

    @classmethod
    def id_name(cls, xs_name):
        sql = 'SELECT id FROM dd_name WHERE xs_name=%(xs_name)s'
        value = {
            'xs_name': xs_name
        }
        cur.execute(sql, value)
        for name_id in cur:
            return name_id[0]

    @classmethod
    def select_name(cls, name_id):
        sql = "SELECT EXISTS(SELECT 1 FROM dd_name WHERE name_id=%(name_id)s)"
        value = {
            'name_id': name_id
        }
        cur.execute(sql, value)
        return cur.fetchall()[0]

    @classmethod
    def sclect_chapter(cls, url):
        sql = "SELECT EXISTS(SELECT 1 FROM dd_chaptername WHERE url=%(url)s)"
        value = {
            'url': url
        }
        cur.execute(sql, value)
        return cur.fetchall()[0]