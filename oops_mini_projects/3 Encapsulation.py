class Laptop:
    def __init__(self, name ,intel,version):
        self.name = name
        self.__intel = intel
        self.__version = version

    def get_intel(self):
        return self.__intel

    def get_version(self):
        return self.__version

    def set_intel(self,new_intel):
        self.__intel = new_intel

    def set_version(self,new_version):
        self.__version = new_version


L = Laptop("Hp","i3","windows11")
print(L.get_intel())
print(L.get_version())
L.set_intel("i5")
L.set_version("windows12")
print(L.get_intel())
print(L.get_version())