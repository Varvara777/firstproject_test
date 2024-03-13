class Human:
    def __init__(self):
        self.adress=''
        self.fio=''
        self.date=''
        self.__tel=''
        self.city=''
        self.country=''
    def getTel(self,a):
        return self.__tel
    def setTel(self,tel):
        self.__tel=tel
    def inputINFO(self):
        self.fio =input("Введите ФИО: ")
        self.adress = input("Введите Адрес: ")
        self.date = input("Введите дату рождения: ")
        tel = input("Введите теелфон: ")
        self.setTel(tel)
        self.city = input("Введите ваш город: ")
        self.country = input("Введите вашу страну: ")
    def __str__(self):
        return f"Данные человека: \n  {self.fio}\n  {self.adress}\n {self.date}\n {self.getTel()}\n {self.city}\n {self.country} \n "
listHuman=[Human() for i in range(1)]
for i in range(len(listHuman)):
    print('*'*11)
    print(f"Human {i}")
    listHuman[i].inputINFO()
    print(listHuman[i].__dict__)
    print(listHuman[i].country)
# human1=Human()
# human1.inputINFO()
# print(human1)

