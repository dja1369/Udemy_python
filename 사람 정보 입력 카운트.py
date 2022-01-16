class person:

    def __init__(self ,*argList):

     
        #정보은닉
        self.__name = argList[0]
        if len(argList) == 2:
            self.__age = 20
            self.__tel = argList[1]
        else:
            self.__age = argList[1]
            self.__tel = argList[2]
    #설정자 setter
    def setname(self, name):
        self.__name = name
    def setage(self, age):
        self.__age = age
    def settel(self, tel):
        self.__tel = tel

    #접근자 getter
    def getname(self):
        return self.__name
    def getage(self):
        return self.__age
    def gettel(self):
        return self.__tel

    def show(self):
        print(self.__name,'',self.__age,'',self.__tel)

argList = []
argList.append(input('이름:'))
argList.append(int(input('나이:')))
argList.append(input('번호:'))

myperson1 = person(*argList)
myperson1.show()

argList.clear()

argList.append(input('이름:'))
argList.append(input('번호:'))

myperson2 =person(*argList)
myperson2.show()

print('총',len(argList),'명 등록되었습니다.')



