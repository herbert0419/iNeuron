import mysql.connector


class ytPipeline(object):

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='root',
            database='challengetask'

        )
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""create table yt_videos(
        titles text,
        views text,
        video_urls text,
        )""")

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        self.curr.execute("""insert into yt_videos values (%s,%s,%s)""",
                          (
                              item['titles'][0],
                              item['views'][0],
                              item['video_urls'][0]
                          ))
        self.conn.commit()
