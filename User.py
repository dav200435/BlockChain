class User:
    
    def __init__(self, id, dni, nombre, admin, voted):
        self.__id=id
        self.__dni = dni
        self.__nombre = nombre
        self.__admin = admin
        self.__voted = voted
        
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value
    
    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self, value):
        self.__dni = value

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, value):
        self.__nombre = value

    @property
    def admin(self):
        return self.__admin

    @admin.setter
    def admin(self, value):
        self.__admin = value
        
    @property
    def voted(self):
        return self.__voted
    
    @voted.setter
    def voted(self, value):
        self.__voted = value