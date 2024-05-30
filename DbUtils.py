import MySQLdb
import sys

class DbUtils:
    
    def __init__(self):
        self.__ip='127.0.0.1'
        self.__name='Temperatura'
        self.__user="root"
        self.__passwd=""
        self.database=self.connect()

    def connect(self):
        try:
            self.db=MySQLdb.connect(self.__ip, self.__user, self.__passwd, self.__name)
            print(f"connecting to {self.__name}")
        except MySQLdb.Error as e:
            return e
            sys.exit()

    def getLogIn(self,dni):
        cursor=self.db.cursor()
        sql=f"select * from users where dni = {dni}"
        try:
            cursor.execute(sql)
            return cursor.fetchall()
        except MySQLdb.Error as e:
            return e
        finally:
            cursor.close()
        
    def voted(self, user):
        cursor = self.db.cursor()
        sql = f"update users set voted = true where id = {user.id}"
        try:
            cursor.execute(sql)
            self.db.commit()
            print("Enhorabueno ya se ha emitido su voto")
        except MySQLdb.Error as e:
            return e
        finally:
            cursor.close()
            
    def vote(self, vote):
        cursor = self.db.cursor()
        sql = f"insert into votes (partido) values ('{vote}')"
        try:
            cursor.execute(sql)
            cursor.commit()
        except MySQLdb.Error as e:
            return e
            
    def getvotes(self):
        cursor = self.db.cursor()
        sql = f"select * from votes"
        try:
            cursor.execute(sql)
            values=cursor.fetchall()
        except MySQLdb.Error as e:
            return e
            
        voteCounts = {}
        for value in values:
            partido = value[1]
            if partido in voteCounts:
                voteCounts[partido] += 1
            else:
                voteCounts[partido] = 1
        return voteCounts