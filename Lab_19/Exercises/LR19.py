import datetime
import os
import io
import pickle
import copy
import time


def timer(f):
    def tmp(*args, **kwargs):
        t = time.time()
        res = f(*args, **kwargs)
        print('Время выполнения функции: %f' % (time.time() - t))
        return res

    return tmp

class CountCall(object):
    def __init__(self, func):
        self.func = func
        self.count = 0
    def __call__(self, *args, **kwargs):
        self.count += 1

    def __del__(self):
        print(f'Количество вызовов функции {self.func.__name__}: {self.count}')


class ClassData(object):
    @staticmethod
    def serialize(obj, name):
        if not os.path.exists('data'):
            os.mkdir('data')
        with open(f'data/{name}.pkl', 'wb') as f:
            pickle.dump(obj, f)

    @staticmethod
    def deserialize(name):
        with open(f'data/{name}.pkl', 'rb') as f:
            obj = pickle.load(f)
        return obj


class Transaction(object):
    def __init__(self, filename, transaction, old=None, new=None):
        self.__when = datetime.datetime.today().strftime('%H:%M:%S')
        self.__dmy = str(datetime.datetime.now().day) + "-" + str(datetime.datetime.now().month) + "-" + str(
            datetime.datetime.now().year)
        self.__file_name = filename
        self.__transaction = transaction
        self.__old = old
        self.__new = new

    @staticmethod
    @timer
    @CountCall
    def getTransaction(class_name):
        queue = class_name.queue
        for i in range(len(queue)):
            item = queue.pop(0)

        class_name.queue = []

    @property
    def when(self):
        return self.__when

    @when.setter
    def when(self, value):
        if not isinstance(value, str):
            raise TypeError('when is str!')
        else:
            self.__when = value

    @when.deleter
    def when(self):
        raise TypeError('when dont delete!')

    @property
    def dmy(self):
        return self.__dmy

    @dmy.setter
    def dmy(self, value):
        if not isinstance(value, str):
            raise TypeError('dmy is str!')
        else:
            self.__dmy = value

    @dmy.deleter
    def dmy(self):
        raise TypeError('dmy dont delete!')

    @property
    def file_name(self):
        return self.__file_name

    @file_name.setter
    def file_name(self, value):
        if not isinstance(value, str):
            raise TypeError('file_name is str!')
        else:
            self.__file_name = value

    @file_name.deleter
    def file_name(self):
        raise TypeError('file_name dont delete!')

    @property
    def transaction(self):
        return self.__transaction

    @transaction.setter
    def transaction(self, value):
        if not isinstance(value, str):
            raise TypeError('transaction is str!')
        else:
            self.__transaction = value

    @transaction.deleter
    def transaction(self):
        raise TypeError('transaction dont delete!')

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, value):
        self.__old = value

    @old.deleter
    def old(self):
        raise TypeError('old dont delete!')

    @property
    def new(self):
        return self.__new

    @new.setter
    def new(self, value):
        self.__new = value

    @new.deleter
    def new(self):
        raise TypeError('new dont delete!')

    def __del__(self):
        if not os.path.exists('logs'):
            os.mkdir('logs')
        with io.open(f'logs/log_{self.file_name}_{self.dmy}.txt', 'a', encoding="UTF-8") as f:
            if self.old != None and self.new != None:
                text = f'[{self.when}]: {self.transaction} [{self.old} => {self.new}]\n'
            else:
                text = f'[{self.when}]: {self.transaction}\n'
            f.write(text)
            #print(text)
            f.close()


class InvalidNameError(Exception):
    def __init__(self, value):
        self.__value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, v):
        self.__value = v

    @value.deleter
    def value(self):
        raise TypeError('value dont delete!')

    def __str__(self):
        return 'invalid name {0}'.format(self.__value)


class InvalidNumberError(Exception):
    def __init__(self, value):
        self.__value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, v):
        self.__value = v

    @value.deleter
    def value(self):
        raise TypeError('value dont delete!')

    def __str__(self):
        return 'invalid number {0}'.format(self.__value)


class TypesOfTroops:
    ''' Класс TypesOfTroops описывает виды войск.'''
    def __init__(self, name):
        self.__name = name
        self.__queue = []
        self.__filename = "types_of_troops"

    def __del__(self):
        print("Класс 'Вид войск' был удален")

    @property
    def name(self):
        self.__queue.append(Transaction(self.__filename, "Было возвращено значение name"))
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise InvalidNameError(value)
        else:
            self.__queue.append(Transaction(self.__filename, "Было присвоено значение name", self.__name, value))
            self.__name = value

    @name.deleter
    def name(self):
        raise TypeError('name dont delete!')

    @property
    def queue(self):
        self.__queue.append(Transaction(self.__filename, "Было возвращено значение queue"))
        return self.__queue

    @queue.setter
    def queue(self, value):
        if not isinstance(value, list):
            raise TypeError('queue is list!')
        else:
            self.__queue.append(Transaction(self.__filename, "Было присвоено значение queue", self.__queue, value))
            self.__queue = value

    @queue.deleter
    def queue(self):
        raise TypeError('queue dont delete!')

    @property
    def filename(self):
        self.__queue.append(Transaction(self.__filename, "Было возвращено значение filename"))
        return self.__filename

    @filename.setter
    def filename(self, value):
        if not isinstance(value, str):
            raise TypeError('filename is str!')
        else:
            self.__queue.append(Transaction(self.__filename, "Было присвоено значение filename", self.__filename, value))
            self.__filename = value

    @filename.deleter
    def filename(self):
        raise TypeError('filename dont delete!')

    def info(self):
        ''' Этот метод выводит информацию из класса.'''
        text_info = f'''Вид войск: {self.name}'''
        self.__queue.append(Transaction(self.__filename, "Была вызвана информация о виде войск."))
        return text_info

    def __changeName(self, new_name):
        ''' Этот метод изменяет тип войск.'''
        self.__queue.append(Transaction(self.__filename, "Изменен тип войск", self.__name, new_name))
        self.__name = new_name


class Dislocation:
    ''' Класс Dislocation описывает дислокацию.'''
    def __init__(self, country, city, address, area):
        self.__country = country
        self.__city = city
        self.__address = address
        self.__area = area
        self.__queue = []
        self.__filename = "dislocation"

        def __add__(self, value):
            self.__area += value

        def __sub__(self, value):
            self.__area -= value

        def __mul__(self, value):
            self.__area *= value

        def __truediv__(self, value):
            self.__area = self.__area / value

    @property
    def country(self):
        self.__queue.append(Transaction(self.__filename, "Было возвращено значение country"))
        return self.__country

    @country.setter
    def country(self, value):
        if not isinstance(value, str):
            raise TypeError('country is string!')
        else:
            self.__queue.append(Transaction(self.__filename, "Было присвоено значение country", self.__country, value))
            self.__country = value

    @country.deleter
    def country(self):
        raise TypeError('country dont delete!')

    @property
    def city(self):
        self.__queue.append(Transaction(self.__filename, "Было возвращено значение city"))
        return self.__city

    @city.setter
    def city(self, value):
        if not isinstance(value, str):
            raise TypeError('country is string!')
        else:
            self.__queue.append(Transaction(self.__filename, "Было присвоено значение city", self.__city, value))
            self.__city = value

    @city.deleter
    def city(self):
        raise TypeError('country dont delete!')

    @property
    def address(self):
        self.__queue.append(Transaction(self.__filename, "Было возвращено значение address"))
        return self.__address

    @address.setter
    def address(self, value):
        if not isinstance(value, str):
            raise TypeError('address is string!')
        else:
            self.__queue.append(Transaction(self.__filename, "Было присвоено значение address", self.__address, value))
            self.__address = value

    @address.deleter
    def address(self):
        raise TypeError('address dont delete!')

    @property
    def area(self):
        self.__queue.append(Transaction(self.__filename, "Было возвращено значение area"))
        return self.__area

    @area.setter
    def area(self, value):
        if not isinstance(value, int):
            raise TypeError('area is int!')
        else:

            if value <= 0:
                value = 0

            self.__queue.append(Transaction(self.__filename, "Было присвоено значение area", self.__area, value))
            self.__area = value

    @area.deleter
    def area(self):
        raise TypeError('area dont delete!')

    @property
    def queue(self):
        self.__queue.append(Transaction(self.__filename, "Было возвращено значение queue"))
        return self.__queue

    @queue.setter
    def queue(self, value):
        if not isinstance(value, list):
            raise TypeError('queue is list!')
        else:
            self.__queue.append(Transaction(self.__filename, "Было присвоено значение queue", self.__queue, value))
            self.__queue = value

    @queue.deleter
    def queue(self):
        raise TypeError('queue dont delete!')

    @property
    def filename(self):
        self.__queue.append(Transaction(self.__filename, "Было возвращено значение filename"))
        return self.__filename

    @filename.setter
    def filename(self, value):
        if not isinstance(value, str):
            raise TypeError('filename is str!')
        else:
            self.__queue.append(Transaction(self.__filename, "Было присвоено значение filename", self.__filename, value))
            self.__filename = value

    @filename.deleter
    def filename(self):
        raise TypeError('filename dont delete!')

    def __del__(self):
        print("Класс 'Место дислокации' был удален")

    def info(self):
        '''Этот метод выводит информацию из класса.'''
        text_info = f'''Место дислокации:
                Страна: {self.country}   
                Город: {self.city}
                Адрес: {self.address}
                Занимаемая площадь: {self.area}
                '''
        self.__queue.append(Transaction(self.__filename, "Была вызвана информация о месте дислокации."))
        return text_info

    def __changeArea(self, new_area):
        '''Этот метод изменяет площадь дислокации.'''
        self.__queue.append(Transaction(self.__filename, "Изменена занимаема площадь", self.__area, new_area))
        self.__area = new_area


class Part:
    ''' Класс Part описывает воинскую часть.'''
    def __init__(self, number, country, city, address, area, type_name, count):
        self.__number = number
        self.__dislocation = Dislocation(country, city, address, area)
        self.__type = TypesOfTroops(type_name)
        self.__count = count
        self.__queue = []
        self.__filename = "part"

    def __add__(self, value):
        self.__count += value

    def __sub__(self, value):
        self.__count -= value

    def __mul__(self, value):
        self.__count *= value

    def __truediv__(self, value):
        self.__count = self.__count / value

    @property
    def number(self):
        self.__queue.append(Transaction(self.__filename, "Было возвращено значение number"))
        return self.__number

    @number.setter
    def number(self, value):
        if not isinstance(value, int):
            raise InvalidNumberError(value)
        else:
            self.__queue.append(Transaction(self.__filename, "Было присвоено значение number", self.__number, value))
            self.__number = value

    @number.deleter
    def number(self):
        raise TypeError('number dont delete!')

    @property
    def dislocation(self):
        self.__queue.append(Transaction(self.__filename, "Было возвращено значение dislocation"))
        return self.__dislocation

    @dislocation.setter
    def dislocation(self, value):
        self.__queue.append(Transaction(self.__filename, "Было присвоено значение dislocation", self.__dislocation, value))
        self.__dislocation = value

    @dislocation.deleter
    def dislocation(self):
        raise TypeError('dislocation dont delete!')

    @property
    def type(self):
        self.__queue.append(Transaction(self.__filename, "Было возвращено значение type"))
        return self.__type

    @type.setter
    def type(self, value):
        self.__queue.append(Transaction(self.__filename, "Было присвоено значение type", self.__type, value))
        self.__type = value

    @type.deleter
    def type(self):
        raise TypeError('type dont delete!')

    @property
    def count(self):
        self.__queue.append(Transaction(self.__filename, "Было возвращено значение count"))
        return self.__count

    @count.setter
    def count(self, value):
        if not isinstance(value, int):
            raise TypeError('count is int!')
        else:
            self.__queue.append(Transaction(self.__filename, "Было присвоено значение count", self.__count, value))
            self.__count = value

    @count.deleter
    def count(self):
        raise TypeError('count dont delete!')

    @property
    def queue(self):
        self.__queue.append(Transaction(self.__filename, "Было возвращено значение queue"))
        return self.__queue

    @queue.setter
    def queue(self, value):
        if not isinstance(value, list):
            raise TypeError('queue is list!')
        else:
            self.__queue.append(Transaction(self.__filename, "Было присвоено значение queue", self.__queue, value))
            self.__queue = value

    @queue.deleter
    def queue(self):
        raise TypeError('queue dont delete!')

    @property
    def filename(self):
        self.__queue.append(Transaction(self.__filename, "Было возвращено значение filename"))
        return self.__filename

    @filename.setter
    def filename(self, value):
        if not isinstance(value, str):
            raise TypeError('filename is str!')
        else:
            self.__queue.append(Transaction(self.__filename, "Было присвоено значение filename", self.__filename, value))
            self.__filename = value

    @filename.deleter
    def filename(self):
        raise TypeError('filename dont delete!')

    def __del__(self):
        print("Класс 'Воинская часть' был удален")

    def info(self):
        '''Этот метод выводит информацию из класса.'''
        text_info = f'''Воинская часть номер {self.number}:
                {self.dislocation.country}, {self.dislocation.city}, {self.dislocation.address}, {self.dislocation.area} кв. км.
                Вид войск: {self.type.name}
                Количество рот: {self.count}
                '''
        self.__queue.append(Transaction(self.__filename, "Была вызвана информация о воинской части."))
        return text_info

    def __addCount(self, number):
        '''Этот метод добавляет количество рот'''
        self.__queue.append(Transaction(self.__filename, "Добавлено количество", self.__count, number))
        self.__count += number

    def __removeCount(self, number):
        '''Этот метод убавляет количество рот'''
        self.__queue.append(Transaction(self.__filename, "Убавлено количество", self.__count, number))
        self.__count -= number

    def __changeCount(self, new_count):
        '''Этот метод изменяет количество рот'''
        self.__queue.append(Transaction(self.__filename, "Изменено количество", self.__count, new_count))
        self.__count = new_count


# Батальон
class Battalion(Part):
    ''' Класс Battalion описывает батальон.'''
    def __init__(self, number, country, city, address, area, type_name, headquarters, commander, count):
        Part.__init__(self, number, country, city, address, area, type_name, count)
        self.__commander = commander
        self.__headquarters = headquarters
        self.__filename = "battalion"

    def __add__(self, value):
        self.count += value

    def __sub__(self, value):
        self.count -= value

    def __mul__(self, value):
        self.count *= value

    def __truediv__(self, value):
        self.count = self.count / value
    @property
    def commander(self):
        self.queue.append(Transaction(self.__filename, "Было возвращено значение commander"))
        return self.__commander

    @commander.setter
    def commander(self, value):
        if not isinstance(value, str):
            raise TypeError('commander is str!')
        else:
            self.queue.append(Transaction(self.__filename, "Было присвоено значение commander", self.__commander, value))
            self.__commander = value

    @commander.deleter
    def commander(self):
        raise TypeError('commander dont delete!')

    @property
    def headquarters(self):
        self.queue.append(Transaction(self.__filename, "Было возвращено значение headquarters"))
        return self.__headquarters

    @headquarters.setter
    def headquarters(self, value):
        if not isinstance(value, str):
            raise TypeError('headquarters is str!')
        else:
            self.queue.append(Transaction(self.__filename, "Было присвоено значение headquarters", self.__headquarters, value))
            self.__headquarters = value

    @headquarters.deleter
    def headquarters(self):
        raise TypeError('headquarters dont delete!')

    @property
    def filename(self):
        self.queue.append(Transaction(self.__filename, "Было возвращено значение filename"))
        return self.__filename

    @filename.setter
    def filename(self, value):
        if not isinstance(value, str):
            raise TypeError('filename is str!')
        else:
            self.queue.append(Transaction(self.__filename, "Было присвоено значение filename", self.__filename, value))
            self.__filename = value

    @filename.deleter
    def filename(self):
        raise TypeError('filename dont delete!')

    def __del__(self):
        print("Класс 'Батальон' был удален")

    def info(self):
        '''Этот метод выводит информацию из класса.'''
        text_info = f'''Батальон номер {self.number}:
                Командир: {self.commander}
                {self.dislocation.country}, {self.dislocation.city}, {self.dislocation.address}, {self.dislocation.area} кв. км.
                {self.headquarters}
                Вид войск: {self.type.name}
                Количество рот: {self.count}
                '''
        self.queue.append(Transaction(self.__filename, "Была вызвана информация о батальоне."))
        return text_info

    def __setCommander(self, new_commander):
        '''Этот метод меняет командира.'''
        self.queue.append(Transaction(self.__filename, "Изменен командир батальона", self.__commander, new_commander))
        self.__commander = new_commander

    def __setHeadquarters(self, new_hq):
        '''Этот метод меняет штаб.'''
        self.queue.append(Transaction(self.__filename, "Изменен штаб батальона", self.__headquarters, new_hq))
        self.__headquarters = new_hq

    def __addCount(self, number):
        '''Этот метод добавляет количество рот.'''
        if self.count + number > 4:
            print('Превышено количество рот')
        else:
            self.count += number

    def __removeCount(self, number):
        '''Этот метод убавляет количество рот.'''
        if self.count - number < 0:
            print('Количество рот не может быть меньше 0')
        else:
            self.count -= number


# Полк
class Regiment(Part):
    ''' Класс Regiment описывает полк.'''
    def __init__(self, number, country, city, address, area, type_name, headquarters, commander, count):
        Part.__init__(self, number, country, city, address, area, type_name, count)
        self.__commander = commander
        self.__headquarters = headquarters
        self.__filename = "regiment"

    def __add__(self, value):
        self.count += value

    def __sub__(self, value):
        self.count -= value

    def __mul__(self, value):
        self.count *= value

    def __truediv__(self, value):
        self.count = self.count / value

    @property
    def commander(self):
        self.queue.append(Transaction(self.__filename, "Было возвращено значение commander"))
        return self.__commander

    @commander.setter
    def commander(self, value):
        if not isinstance(value, str):
            raise TypeError('commander is str!')
        else:
            self.queue.append(
                Transaction(self.__filename, "Было присвоено значение commander", self.__commander, value))
            self.__commander = value

    @commander.deleter
    def commander(self):
        raise TypeError('commander dont delete!')

    @property
    def headquarters(self):
        self.queue.append(Transaction(self.__filename, "Было возвращено значение headquarters"))
        return self.__headquarters

    @headquarters.setter
    def headquarters(self, value):
        if not isinstance(value, str):
            raise TypeError('headquarters is str!')
        else:
            self.queue.append(
                Transaction(self.__filename, "Было присвоено значение headquarters", self.__headquarters, value))
            self.__headquarters = value

    @headquarters.deleter
    def headquarters(self):
        raise TypeError('headquarters dont delete!')

    @property
    def filename(self):
        self.__queue.append(Transaction(self.__filename, "Было возвращено значение filename"))
        return self.__filename

    @filename.setter
    def filename(self, value):
        if not isinstance(value, str):
            raise TypeError('filename is str!')
        else:
            self.queue.append(
                Transaction(self.__filename, "Было присвоено значение filename", self.__filename, value))
            self.__filename = value

    @filename.deleter
    def filename(self):
        raise TypeError('filename dont delete!')

    def __del__(self):
        print("Класс 'Полк' был удален")

    def info(self):
        '''Этот метод выводит информацию из класса.'''
        text_info = f'''Полк номер {self.number}:
                Командир: {self.commander}
                {self.dislocation.country}, {self.dislocation.city}, {self.dislocation.address}, {self.dislocation.area} кв. км.
                {self.headquarters}
                Вид войск: {self.type.name}
                Количество рот: {self.count}
                '''
        self.queue.append(Transaction(self.__filename, "Была вызвана информация о полке."))
        return text_info

    def __setCommander(self, new_commander):
        '''Этот метод меняет командира.'''
        self.queue.append(Transaction(self.__filename, "Изменен командир полка", self.__commander, new_commander))
        self.__commander = new_commander

    def __setHeadquarters(self, new_hq):
        '''Этот метод меняет штаб.'''
        self.queue.append(Transaction(self.__filename, "Изменен штаб полка", self.__headquarters, new_hq))
        self.__headquarters = new_hq

    def __addCount(self, number):
        '''Этот метод добавляет количество рот.'''
        if self.count + number > 10:
            print('Превышено количество рот')
        else:
            self.count += number

    def __removeCount(self, number):
        '''Этот метод убавляет количество рот.'''
        if self.count - number < 0:
            print('Количество рот не может быть меньше 0')
        else:
            self.count -= number


class Rota:
    ''' Класс Rota описывает роту.'''
    def __init__(self, name, count):
        self.__name = name
        self.__count = count
        self.__queue = []
        self.__filename = "rota"

    def __add__(self, value):
        self.__count += value

    def __sub__(self, value):
        self.__count -= value

    def __mul__(self, value):
        self.__count *= value

    def __truediv__(self, value):
        self.__count = self.__count / value

    @property
    def name(self):
        self.__queue.append(Transaction(self.__filename, "Было возвращено значение name"))
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('name is str!')
        else:
            self.__queue.append(
                Transaction(self.__filename, "Было присвоено значение name", self.__name, value))
            self.__name = value

    @name.deleter
    def name(self):
        raise TypeError('name dont delete!')

    @property
    def count(self):
        self.__queue.append(Transaction(self.__filename, "Было возвращено значение count"))
        return self.__count

    @count.setter
    def count(self, value):
        if not isinstance(value, int):
            raise TypeError('count is int!')
        else:
            self.__queue.append(
                Transaction(self.__filename, "Было присвоено значение count", self.__count, value))
            self.__count = value

    @count.deleter
    def count(self):
        raise TypeError('count dont delete!')

    @property
    def queue(self):
        self.__queue.append(Transaction(self.__filename, "Было возвращено значение queue"))
        return self.__queue

    @queue.setter
    def queue(self, value):
        if not isinstance(value, list):
            raise TypeError('queue is list!')
        else:
            self.__queue.append(
                Transaction(self.__filename, "Было присвоено значение queue", self.__queue, value))
            self.__queue = value

    @queue.deleter
    def queue(self):
        raise TypeError('queue dont delete!')

    @property
    def filename(self):
        self.__queue.append(Transaction(self.__filename, "Было возвращено значение filename"))
        return self.__filename

    @filename.setter
    def filename(self, value):
        if not isinstance(value, str):
            raise TypeError('filename is str!')
        else:
            self.__queue.append(
                Transaction(self.__filename, "Было присвоено значение filename", self.__filename, value))
            self.__filename = value

    @filename.deleter
    def filename(self):
        raise TypeError('filename dont delete!')

    def __del__(self):
        print("Класс 'Рота' был удален")

    def info(self):
        ''' Этот метод выводит информацию из класса.'''
        text_info = f'''Рота:    
                Название роты: {self.name}
                Количество служащих: {self.count}
                '''
        self.__queue.append(Transaction(self.__filename, "Была вызвана информация о роте."))
        return text_info

    def __addCount(self, number):
        ''' Этот метод добавлет количество служащих.'''
        self.__queue.append(Transaction(self.__filename, "Добавлено количество", self.__count, number))
        self.__count += number

    def __removeCount(self, number):
        ''' Этот метод убавляет количество служащих.'''
        self.__queue.append(Transaction(self.__filename, "Убавлено количество", self.__count, number))
        self.__count -= number

    def __changeCount(self, new_count):
        ''' Этот метод изменяет количество служащих.'''
        self.__queue.append(Transaction(self.__filename, "Изменено количество", self.__count, new_count))
        self.__count = new_count


class Staff:
    ''' Класс Staff описывает личный состав.'''
    def __init__(self, number, last_name, rota_name, rota_count, post, birth, admission_date, seniority, awards=[], events=[]):
        self.__number = number
        self.__last_name = last_name
        self.__rota = Rota(rota_name, rota_count)
        self.__post = post
        self.__birth = birth
        self.__admission_date = admission_date
        self.__seniority = seniority
        self.__awards = awards
        self.__events = events
        self.__queue = []
        self.__filename = "staff"

    def __add__(self, value):
        self.__seniority += value

    def __sub__(self, value):
        self.__seniority -= value

    def __mul__(self, value):
        self.__seniority *= value

    def __truediv__(self, value):
        self.__seniority = self.__seniority / value

    @property
    def number(self):
        self.__queue.append(Transaction(self.__filename, "Было возвращено значение number"))
        return self.__number

    @number.setter
    def number(self, value):
        if not isinstance(value, int):
            raise TypeError('last_name is int!')
        else:
            self.__number = value

    @number.deleter
    def number(self):
        raise TypeError('last_name dont delete!')

    @property
    def last_name(self):
        self.__queue.append(Transaction(self.__filename, "Было возвращено значение last_name"))
        return self.__last_name

    @last_name.setter
    def last_name(self, value):
        if not isinstance(value, str):
            raise TypeError('last_name is str!')
        else:
            self.__last_name = value

    @last_name.deleter
    def last_name(self):
        raise TypeError('last_name dont delete!')

    @property
    def rota(self):
        self.__queue.append(Transaction(self.__filename, "Было возвращено значение rota"))
        return self.__rota

    @rota.setter
    def rota(self, value):
        self.__queue.append(
            Transaction(self.__filename, "Было присвоено значение rota", self.__rota, value))
        self.__rota = value

    @rota.deleter
    def rota(self):
        raise TypeError('rota dont delete!')

    @property
    def post(self):
        self.__queue.append(Transaction(self.__filename, "Было возвращено значение post"))
        return self.__post

    @post.setter
    def post(self, value):
        if not isinstance(value, str):
            raise TypeError('rota is str!')
        else:
            self.__queue.append(
                Transaction(self.__filename, "Было присвоено значение post", self.__post, value))
            self.__post = value

    @post.deleter
    def post(self):
        raise TypeError('post dont delete!')

    @property
    def birth(self):
        self.__queue.append(Transaction(self.__filename, "Было возвращено значение birth"))
        return self.__birth

    @birth.setter
    def birth(self, value):
        if not isinstance(value, str):
            raise TypeError('birth is str!')
        else:
            self.__queue.append(
                Transaction(self.__filename, "Было присвоено значение birth", self.__birth, value))
            self.__birth = value

    @birth.deleter
    def birth(self):
        raise TypeError('birth dont delete!')

    @property
    def admission_date(self):
        self.__queue.append(Transaction(self.__filename, "Было возвращено значение admission_date"))
        return self.__admission_date

    @admission_date.setter
    def admission_date(self, value):
        if not isinstance(value, str):
            raise TypeError('admission_date is str!')
        else:

            if value >= 0:
                pass
            else:
                value = 0

            self.__queue.append(
                Transaction(self.__filename, "Было присвоено значение admission_date", self.__filename, value))
            self.__admission_date = value

    @admission_date.deleter
    def admission_date(self):
        raise TypeError('admission_date dont delete!')

    @property
    def seniority(self):
        self.__queue.append(Transaction(self.__filename, "Было возвращено значение seniority"))
        return self.__seniority

    @seniority.setter
    def seniority(self, value):
        if not isinstance(value, int):
            raise TypeError('seniority is int!')
        else:
            self.__queue.append(
                Transaction(self.__filename, "Было присвоено значение seniority", self.__seniority, value))
            self.__seniority = value

    @seniority.deleter
    def seniority(self):
        raise TypeError('seniority dont delete!')

    @property
    def awards(self):
        self.__queue.append(Transaction(self.__filename, "Было возвращено значение awards"))
        return self.__awards

    @awards.setter
    def awards(self, value):
        if not isinstance(value, list):
            raise TypeError('awards is list!')
        else:
            self.__queue.append(
                Transaction(self.__filename, "Было присвоено значение awards", self.__awards, value))
            self.__awards = value

    @awards.deleter
    def awards(self):
        raise TypeError('awards dont delete!')

    @property
    def events(self):
        self.__queue.append(Transaction(self.__filename, "Было возвращено значение events"))
        return self.__events

    @events.setter
    def events(self, value):
        if not isinstance(value, list):
            raise TypeError('events is list!')
        else:
            self.__queue.append(
                Transaction(self.__filename, "Было присвоено значение events", self.__events, value))
            self.__events = value

    @events.deleter
    def events(self):
        raise TypeError('events dont delete!')

    @property
    def queue(self):
        self.__queue.append(Transaction(self.__filename, "Было возвращено значение queue"))
        return self.__queue

    @queue.setter
    def queue(self, value):
        if not isinstance(value, list):
            raise TypeError('queue is list!')
        else:
            self.__queue.append(
                Transaction(self.__filename, "Было присвоено значение queue", self.__queue, value))
            self.__queue = value

    @queue.deleter
    def queue(self):
        raise TypeError('queue dont delete!')

    @property
    def filename(self):
        self.__queue.append(Transaction(self.__filename, "Было возвращено значение filename"))
        return self.__filename

    @filename.setter
    def filename(self, value):
        if not isinstance(value, str):
            raise TypeError('filename is str!')
        else:
            self.__queue.append(
                Transaction(self.__filename, "Было присвоено значение filename", self.__filename, value))
            self.__filename = value

    @filename.deleter
    def filename(self):
        raise TypeError('filename dont delete!')

    def __del__(self):
        print("Класс 'Личный состав' был удален")

    def info(self):
        ''' Этот метод выводит информацию из класса.'''
        text_info = f'''Личный состав номер {self.number}:
                Фамилия: {self.last_name}
                Рота: {self.rota.name}
                Численность роты: {self.rota.count}
                Должность: {self.post}
                Год рождения: {self.birth}
                Год поступления на службу: {self.admission_date}
                Выслуга лет: {self.seniority}
                Награды: {','.join(self.awards)}
                Участие в военных мероприятиях: {','.join(self.events)}
                '''
        self.__queue.append(Transaction(self.__filename, "Была вызвана информация о личном составе."))
        return text_info

    def __addAward(self, award):
        ''' Этот метод добавляет награду.'''
        temp = copy.copy(self.__awards)
        self.__awards.append(award)
        self.__queue.append(Transaction(self.__filename, "Была добавлена награда", temp, self.awards))

    def __deleteAward(self, award):
        ''' Этот метод убирает награду.'''
        temp = self.__awards
        self.__awards.remove(award)
        self.__queue.append(Transaction(self.__filename, "Была удалена награда", temp, self.awards))

    def __addEvent(self, event):
        ''' Этот метод добавляет событие.'''
        temp = self.__events
        self.__events.append(event)
        self.__queue.append(Transaction(self.__filename, "Была добавлена награда", temp, self.events))

    def __deleteEvent(self, event):
        ''' Этот метод убирает событие.'''
        temp = self.__events
        self.__events.remove(event)
        self.__queue.append(Transaction(self.__filename, "Была добавлена награда", temp, self.events))


if __name__ == '__main__':
    types = TypesOfTroops("Сухопутные войска")
