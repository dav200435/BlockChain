import MySQLdb
from hash import Hash
import time

class DbUtils:
    
    def __init__(self):
        self.__ip='127.0.0.1'
        self.__name='votaciones'
        self.__user="root"
        self.__passwd=""
        self.database=self.connect()

    def connect(self):
        try:
            self.db = MySQLdb.connect(self.__ip, self.__user, self.__passwd, self.__name)
            print(f"Connecting to {self.__name}")
        except MySQLdb.Error as e:
            print(e)
            return None

    def getLogIn(self, dni):
        cursor = self.db.cursor()
        sql = f"SELECT * FROM users WHERE dni = '{dni}'"
        try:
            cursor.execute(sql)
            user = cursor.fetchone()
            return user
        except MySQLdb.Error as e:
            print(e)
        finally:
            cursor.close()


    def voted(self, user):
        cursor = self.db.cursor()
        sql = f"UPDATE users SET voted = TRUE WHERE id = {user.id}"
        try:
            cursor.execute(sql)
            self.db.commit()
            return "Enhorabuena, ya se ha emitido su voto"
        except MySQLdb.Error as e:
            return e
        finally:
            cursor.close()
    
    def getLastVoteHash(self):
        cursor = self.db.cursor()
        sql = "SELECT hash FROM votes ORDER BY id DESC LIMIT 1"
        try:
            cursor.execute(sql)
            result = cursor.fetchone()
            if result:
                return result[0]
            else:
                return None
        except MySQLdb.Error as e:
            return e
        finally:
            cursor.close()
    
    def vote(self, partido):
        cursor = self.db.cursor()
        prehash = self.getLastVoteHash()
        if prehash is None:
            prehash = ''
        timeStamp=str(time.time())
        data = f"{partido}-{timeStamp}-{prehash}"
        current_hash = Hash.convHash(data)
        
        sql = f"INSERT INTO votes (partido, fecha, hash, prehash) VALUES ('{partido}', '{timeStamp}', '{current_hash}', '{prehash}')"
        try:
            cursor.execute(sql)
            self.db.commit()
            return "Voto registrado con éxito"
        except MySQLdb.Error as e:
            return e
        finally:
            cursor.close()

    def getVotes(self):
        cursor = self.db.cursor()
        sql = "SELECT * FROM votes"
        try:
            cursor.execute(sql)
            values = cursor.fetchall()
            previous_hash = ''
            for value in values:
                id, partido, fecha, hash_value, prehash_value = value
                data = f"{partido}-{fecha}-{prehash_value}"
                calculated_hash = Hash.convHash(data)
                if calculated_hash != hash_value or prehash_value != previous_hash:
                    return f"Error de integridad en el voto con ID {id}"
                previous_hash = hash_value
            
            voteCounts = {}
            for value in values:
                partido = value[1]
                if partido in voteCounts:
                    voteCounts[partido] += 1
                else:
                    voteCounts[partido] = 1
            return voteCounts
        except MySQLdb.Error as e:
            return e
        finally:
            cursor.close()
        
        # Verificar la integridad de los hashes
        
