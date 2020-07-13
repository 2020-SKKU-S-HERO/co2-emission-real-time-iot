import pymysql

host = 'localhost'
user = 'shero'
password = 'shero'
db = 'sheroDB'
table = 'co2_emissions'
column1 = 'date_time'
column2 = 'emissions'


class Data:

    def __init__(self, date_time: str, emissions: float):
        self._date_time = date_time
        self._emissions = emissions

    @property
    def date_time(self) -> str:
        return self._date_time

    @property
    def emissions(self) -> float:
        return self._emissions


def insert_into_db(data: Data) -> None:
    """ db에 데이터를 저장한다.

    Args:
        data: db에 저장할 배출량 데이터
    """
    connection = pymysql.connect(host=host, user=user, password=password, db=db, charset='utf8')
    curs = connection.cursor()
    curs.execute(f"INSERT INTO {table}({column1}, {column2}) VALUES ('{data.date_time}', {data.emissions})")
    connection.commit()
    connection.close()
