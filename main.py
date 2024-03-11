# работа  с файлами
file='C:/Users/Little/PycharmProjects/pythonProject17/text.txt'
#name='C:|dir|file'
string=''
try:
    stream=open(file,mode='r',encoding=None)
# r: чтение

# w: запись
# a: редактирование\дозапись
#  r+: чтение и дополнение
# w+: запись и обновление
    for i in stream:
        string+=i
        print(f'Строки в файле:\n{string}')
        ccnt=lcnt=0
# readline считывает из файла строки
        line=stream.readline()
        while line !='':
            lcnt+=1
            for ch in line:
                print(ch,end='')
                ccnt+=1
            line=stream.readline()
        print('количество символов:',ccnt)
        print('количество строк:',lcnt)

# чтение нескольких строк сразу, где 20 это буфер обмена,
        # кол-во строк, которое будет хранится в переменной
        print(stream.readline(20))
        ср=stream.read()
        while ch!='':
            ch=stream.read()
        print(ch)
        stream.close()
except Exception as exc:
    print('Cannot open the file',exc)



#Запись в файл
stream=open(file,mode='w',encoding=None)
for i in range(10):
    s='line#'+str(i+1) + '\n'
    for ch in s:
        stream.write(ch)
stream.close()
stream=open(file,mode='r',encoding=None)
for i in stream:
    string += i
    print(f'Строки в файле:\n{string}')
stream.close()

# функции

file.fileno() # возвращает целочисленный дескриптор файла
file.flush() # очищает внутренний буфер
file.isatty() # возвращает True, если файл привязан к  терминалу
file.next() # возвращает следующую строку от файла
file.seek() # устанавливает текущую позицию указателя в файле
file.seekable() # проверяет, поддерживает ли файл случайный доступ
file.tell() # возвращает текущую позицию в  файле
file.truncate(n) # уменьшает размер файла, если n указана, то файл обрезается
# до n- байт, если нет, то до текущей позиции
file.writelines(sequence) # добовляет последовательность строк в файл

