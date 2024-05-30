from User import User
from DbUtils import DbUtils
import time

class Menu:
    
    def __init__(self, user):
        self.__run=True
        self.__user=None
        self.__db=DbUtils()
        self.__trys = 3
    
    def login(self):
        while self.__trys>0:
            data=self.__db.getLogIn(input("introduce DNI-> "))
            if data:
                self.__user=User(data[0],data[1],data[2],data[3],data[4])
                if self.__user.admin():
                    self.admin()
                else:
                    self.votes()
            else:
                self.__trys-=1
                print(f"DNI invalido por favor vuelva a intentarlo\nIntentos restantes {self.__trys}")
                time.sleep(2)
                
    def votes(self):
        pass

    def admin(self):
        pass
    
    def printVotes(self):
        votes=self.__db.getvotes()
        print(votes)