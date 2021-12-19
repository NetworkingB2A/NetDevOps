class ConfigValues:
    
    __instance = None

    @staticmethod
    def getInstance():
        if ConfigValues.__instance == None:
            ConfigValues()
        return ConfigValues.__instance

    def __init__(self):
        if ConfigValues.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            ConfigValues.__instance = self

s = ConfigValues()
print(s)

print(type(s))

s = ConfigValues.getInstance()
print (s)

s = ConfigValues.getInstance()
print (s)

s = ConfigValues()
print(s)