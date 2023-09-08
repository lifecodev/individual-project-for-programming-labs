import pickle
from LR19 import *


# Батальон
# Полк
# Личный состав
# Воинская часть

class PartDatabase(object):
    def __init__(self):
        self.filename = 'part.pkl'
        self.database = {}
        self.index = 0
        try:
            self.open_database()
        except:
            self.save_database()

    number = property(lambda self: self.database[self.index].number)
    country = property(lambda self: self.database[self.index].dislocation.country)
    city = property(lambda self: self.database[self.index].dislocation.city)
    address = property(lambda self: self.database[self.index].dislocation.address)
    area = property(lambda self: self.database[self.index].dislocation.area)
    type_name = property(lambda self: self.database[self.index].type_name)
    count = property(lambda self: self.database[self.index].count)

    def __iter__(self):
        for item in self.database:
            yield self.database[item]

    def next(self):
        if self.index == len(self.database):
            raise StopIteration
        self.index = self.index + 1
        return self.database[self.index]

    def prev(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.database[self.index]

    def open_database(self):
        with open(self.filename, 'rb') as f:
            self.database = pickle.load(f)
        f.closed

    def save_database(self):
        with open(self.filename, 'wb') as f:
            pickle.dump(self.database, f)
        f.closed

    def add_part(self, country, city, address, area, type_name, count, number=1):
        part = Part(number, country, city, address, area, type_name, count)
        if part.number in self.database:
            part.number = len(self.database) + 1
        self.database[part.number] = part
        self.save_database()

    def get_part_by_number(self, number):
        if number not in self.database:
            return None
        return self.database[number]

    def delete_part(self, number):
        del self.database[number]
        self.save_database()

    def change_country(self, number, country):
        part = self.get_part_by_number(number)
        if not part:
            raise ValueError('value does not exist')
        part.dislocation.country = country
        self.save_database()

    def change_city(self, number, city):
        part = self.get_part_by_number(number)
        if not part:
            raise ValueError('value does not exist')
        part.dislocation.city = city
        self.save_database()

    def change_address(self, number, address):
        part = self.get_part_by_number(number)
        if not part:
            raise ValueError('value does not exist')
        part.dislocation.address = address
        self.save_database()

    def change_area(self, number, area):
        part = self.get_part_by_number(number)
        if not part:
            raise ValueError('value does not exist')
        part.dislocation.area = area
        self.save_database()

    def change_type_name(self, number, type_name):
        part = self.get_part_by_number(number)
        if not part:
            raise ValueError('value does not exist')
        part.type.name = type_name
        self.save_database()

    def change_count(self, number, count):
        part = self.get_part_by_number(number)
        if not part:
            raise ValueError('value does not exist')
        part.count = count
        self.save_database()


class BattalionDatabase(object):
    def __init__(self):
        self.filename = 'battalion.pkl'
        self.database = {}
        self.index = 0
        try:
            self.open_database()
        except:
            self.save_database()

    number = property(lambda self: self.database[self.index].number)
    country = property(lambda self: self.database[self.index].dislocation.country)
    city = property(lambda self: self.database[self.index].dislocation.city)
    address = property(lambda self: self.database[self.index].dislocation.address)
    area = property(lambda self: self.database[self.index].dislocation.area)
    type_name = property(lambda self: self.database[self.index].type_name)
    commander = property(lambda self: self.database[self.index].commander)
    headquarters = property(lambda self: self.database[self.index].headquarters)
    count = property(lambda self: self.database[self.index].count)

    def __iter__(self):
        for item in self.database:
            yield self.database[item]

    def next(self):
        if self.index == len(self.database):
            raise StopIteration
        self.index = self.index + 1
        return self.database[self.index]

    def prev(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.database[self.index]

    def open_database(self):
        with open(self.filename, 'rb') as f:
            self.database = pickle.load(f)
        f.closed

    def save_database(self):
        with open(self.filename, 'wb') as f:
            pickle.dump(self.database, f)
        f.closed

    def add_battalion(self, country, city, address, area, type_name, headquarters, commander, count, number=1):
        part = Battalion(number, country, city, address, area, type_name, headquarters, commander, count)
        if part.number in self.database:
            part.number = len(self.database) + 1
        self.database[part.number] = part
        self.save_database()

    def get_battalion_by_number(self, number):
        if number not in self.database:
            return None
        return self.database[number]

    def delete_battalion(self, number):
        del self.database[number]
        self.save_database()

    def change_country(self, number, country):
        part = self.get_battalion_by_number(number)
        if not part:
            raise ValueError('value does not exist')
        part.dislocation.country = country
        self.save_database()

    def change_city(self, number, city):
        part = self.get_battalion_by_number(number)
        if not part:
            raise ValueError('value does not exist')
        part.dislocation.city = city
        self.save_database()

    def change_address(self, number, address):
        part = self.get_battalion_by_number(number)
        if not part:
            raise ValueError('value does not exist')
        part.dislocation.address = address
        self.save_database()

    def change_area(self, number, area):
        part = self.get_battalion_by_number(number)
        if not part:
            raise ValueError('value does not exist')
        part.dislocation.area = area
        self.save_database()

    def change_type_name(self, number, type_name):
        part = self.get_battalion_by_number(number)
        if not part:
            raise ValueError('value does not exist')
        part.type.name = type_name
        self.save_database()

    def change_headquarters(self, number, headquarters):
        part = self.get_battalion_by_number(number)
        if not part:
            raise ValueError('value does not exist')
        part.headquarters = headquarters
        self.save_database()

    def change_commander(self, number, commander):
        part = self.get_battalion_by_number(number)
        if not part:
            raise ValueError('value does not exist')
        part.commander = commander
        self.save_database()

    def change_count(self, number, count):
        part = self.get_battalion_by_number(number)
        if not part:
            raise ValueError('value does not exist')
        part.count = count
        self.save_database()


class RegimentDatabase(object):
    def __init__(self):
        self.filename = 'regiment.pkl'
        self.database = {}
        self.index = 0
        try:
            self.open_database()
        except:
            self.save_database()

    number = property(lambda self: self.database[self.index].number)
    country = property(lambda self: self.database[self.index].dislocation.country)
    city = property(lambda self: self.database[self.index].dislocation.city)
    address = property(lambda self: self.database[self.index].dislocation.address)
    area = property(lambda self: self.database[self.index].dislocation.area)
    type_name = property(lambda self: self.database[self.index].type_name)
    commander = property(lambda self: self.database[self.index].commander)
    headquarters = property(lambda self: self.database[self.index].headquarters)
    count = property(lambda self: self.database[self.index].count)

    def __iter__(self):
        for item in self.database:
            yield self.database[item]

    def next(self):
        if self.index == len(self.database):
            raise StopIteration
        self.index = self.index + 1
        return self.database[self.index]

    def prev(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.database[self.index]

    def open_database(self):
        with open(self.filename, 'rb') as f:
            self.database = pickle.load(f)
        f.closed

    def save_database(self):
        with open(self.filename, 'wb') as f:
            pickle.dump(self.database, f)
        f.closed

    def add_regiment(self, country, city, address, area, type_name, headquarters, commander, count, number=1):
        part = Regiment(number, country, city, address, area, type_name, headquarters, commander, count)
        if part.number in self.database:
            part.number = len(self.database) + 1
        self.database[part.number] = part
        self.save_database()

    def get_regiment_by_number(self, number):
        if number not in self.database:
            return None
        return self.database[number]

    def delete_regiment(self, number):
        del self.database[number]
        self.save_database()

    def change_country(self, number, country):
        part = self.get_regiment_by_number(number)
        if not part:
            raise ValueError('value does not exist')
        part.dislocation.country = country
        self.save_database()

    def change_city(self, number, city):
        part = self.get_regiment_by_number(number)
        if not part:
            raise ValueError('value does not exist')
        part.dislocation.city = city
        self.save_database()

    def change_address(self, number, address):
        part = self.get_regiment_by_number(number)
        if not part:
            raise ValueError('value does not exist')
        part.dislocation.address = address
        self.save_database()

    def change_area(self, number, area):
        part = self.get_regiment_by_number(number)
        if not part:
            raise ValueError('value does not exist')
        part.dislocation.area = area
        self.save_database()

    def change_type_name(self, number, type_name):
        part = self.get_regiment_by_number(number)
        if not part:
            raise ValueError('value does not exist')
        part.type.name = type_name
        self.save_database()

    def change_headquarters(self, number, headquarters):
        part = self.get_regiment_by_number(number)
        if not part:
            raise ValueError('value does not exist')
        part.headquarters = headquarters
        self.save_database()

    def change_commander(self, number, commander):
        part = self.get_regiment_by_number(number)
        if not part:
            raise ValueError('value does not exist')
        part.commander = commander
        self.save_database()

    def change_count(self, number, count):
        part = self.get_regiment_by_number(number)
        if not part:
            raise ValueError('value does not exist')
        part.count = count
        self.save_database()


class StaffDatabase(object):
    def __init__(self):
        self.filename = 'staff.pkl'
        self.database = {}
        self.index = 0
        try:
            self.open_database()
        except:
            self.save_database()

    number = property(lambda self: self.database[self.index].number)
    last_name = property(lambda self: self.database[self.index].last_name)
    rota_name = property(lambda self: self.database[self.index].rota.name)
    rota_count = property(lambda self: self.database[self.index].rota.count)
    post = property(lambda self: self.database[self.index].post)
    birth = property(lambda self: self.database[self.index].birth)
    count = property(lambda self: self.database[self.index].count)
    admission_date = property(lambda self: self.database[self.index].admission_date)
    seniority = property(lambda self: self.database[self.index].seniority)
    awards = property(lambda self: self.database[self.index].awards)
    events = property(lambda self: self.database[self.index].events)
    def __iter__(self):
        for item in self.database:
            yield self.database[item]

    def next(self):
        if self.index == len(self.database):
            raise StopIteration
        self.index = self.index + 1
        return self.database[self.index]

    def prev(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.database[self.index]

    def open_database(self):
        with open(self.filename, 'rb') as f:
            self.database = pickle.load(f)
        f.closed

    def save_database(self):
        with open(self.filename, 'wb') as f:
            pickle.dump(self.database, f)
        f.closed

    def add_staff(self, last_name, rota_name, rota_count, post, birth, admission_date, seniority, awards, events,
                  number=1):
        part = Staff(number, last_name, rota_name, rota_count, post, birth, admission_date, seniority, awards, events)
        if part.number in self.database:
            part.number = len(self.database) + 1
        self.database[part.number] = part
        self.save_database()

    def get_staff_by_number(self, number):
        if number not in self.database:
            return None
        return self.database[number]

    def delete_staff(self, number):
        del self.database[number]
        self.save_database()

    def change_last_name(self, number, last_name):
        staff = self.get_staff_by_number(number)
        if not staff:
            raise ValueError('value does not exist')
        staff.last_name = last_name
        self.save_database()

    def change_rota_name(self, number, rota_name):
        staff = self.get_staff_by_number(number)
        if not staff:
            raise ValueError('value does not exist')
        staff.rota.name = rota_name
        self.save_database()

    def change_rota_count(self, number, rota_count):
        staff = self.get_staff_by_number(number)
        if not staff:
            raise ValueError('value does not exist')
        staff.rota.count = rota_count
        self.save_database()

    def change_post(self, number, post):
        staff = self.get_staff_by_number(number)
        if not staff:
            raise ValueError('value does not exist')
        staff.post = post
        self.save_database()

    def change_birth(self, number, birth):
        staff = self.get_staff_by_number(number)
        if not staff:
            raise ValueError('value does not exist')
        staff.birth = birth
        self.save_database()

    def change_admission_date(self, number, admission_date):
        staff = self.get_staff_by_number(number)
        if not staff:
            raise ValueError('value does not exist')
        staff.admission_date = admission_date
        self.save_database()

    def change_seniority(self, number, seniority):
        staff = self.get_staff_by_number(number)
        if not staff:
            raise ValueError('value does not exist')
        staff.seniority = seniority
        self.save_database()

    def change_awards(self, number, awards):
        staff = self.get_staff_by_number(number)
        if not staff:
            raise ValueError('value does not exist')
        staff.awards = awards
        self.save_database()

    def change_events(self, number, events):
        staff = self.get_staff_by_number(number)
        if not staff:
            raise ValueError('value does not exist')
        staff.events = events
        self.save_database()


class PartTerm(object):
    def __init__(self):
        self.part_database = PartDatabase()

    def printDB(self):
        for part in self.part_database:
            print('=' * 15)
            print(part.info())
            print('=' * 15)

    def run(self):
        choice = 0
        choices = {
            1: lambda: self.printDB(),
            2: lambda: self.part_database.add_part(
                country=input('Enter country: '),
                city=input('Enter city: '),
                address=input('Enter address: '),
                area=int(input('Enter area: ')),
                type_name=input('Enter types of troops name: '),
                count=int(input('Enter count: '))
            ),
            3: lambda: self.part_database.delete_part(
                int(input('Enter number: '))
            ),
            4: lambda: self.part_database.change_country(
                int(input('Enter number: ')), input('Enter country: ')
            ),
            5: lambda: self.part_database.change_city(
                int(input('Enter number: ')), input('Enter city: ')
            ),
            6: lambda: self.part_database.change_address(
                int(input('Enter number: ')), input('Enter address: ')
            ),
            7: lambda: self.part_database.change_area(
                int(input('Enter number: ')), int(input('Enter area: '))
            ),
            8: lambda: self.part_database.change_type_name(
                int(input('Enter number: ')), input('Enter types of troops name: ')
            ),
            9: lambda: self.part_database.change_count(
                int(input('Enter number: ')), int(input('Enter count: '))
            )
        }
        while (choice != 10):
            print()
            print('1. print database')
            print('2. add part')
            print('3. delete part')
            print('4. change country')
            print('5. change city')
            print('6. change address')
            print('7. change area')
            print('8. change types of troops name')
            print('9. change count')

            print('10. EXIT')
            print('choose:')
            choice = int(input())
            if choice in choices:
                choices[choice]()


class BattalionTerm(object):
    def __init__(self):
        self.battalion_database = BattalionDatabase()

    def printDB(self):
        for battalion in self.battalion_database:
            print('=' * 15)
            print(battalion.info())
            print('=' * 15)

    def run(self):
        choice = 0
        choices = {
            1: lambda: self.printDB(),
            2: lambda: self.battalion_database.add_battalion(
                country=input('Enter country: '),
                city=input('Enter city: '),
                address=input('Enter address: '),
                area=int(input('Enter area: ')),
                type_name=input('Enter types of troops name: '),
                headquarters=input('Enter headquarters: '),
                commander=input('Enter commander: '),
                count=int(input('Enter count: '))
            ),
            3: lambda: self.battalion_database.delete_battalion(
                int(input('Enter number: '))
            ),
            4: lambda: self.battalion_database.change_country(
                int(input('Enter number: ')), input('Enter country: ')
            ),
            5: lambda: self.battalion_database.change_city(
                int(input('Enter number: ')), input('Enter city: ')
            ),
            6: lambda: self.battalion_database.change_address(
                int(input('Enter number: ')), input('Enter address: ')
            ),
            7: lambda: self.battalion_database.change_area(
                int(input('Enter number: ')), int(input('Enter area: '))
            ),
            8: lambda: self.battalion_database.change_type_name(
                int(input('Enter number: ')), input('Enter types of troops name: ')
            ),
            9: lambda: self.battalion_database.change_headquarters(
                int(input('Enter number: ')), input('Enter headquarters: ')
            ),
            10: lambda: self.battalion_database.change_commander(
                int(input('Enter number: ')), input('Enter commander: ')
            ),
            11: lambda: self.battalion_database.change_count(
                int(input('Enter number: ')), int(input('Enter count: '))
            )
        }
        while (choice != 12):
            print()
            print('1. print database')
            print('2. add battalion')
            print('3. delete battalion')
            print('4. change country')
            print('5. change city')
            print('6. change address')
            print('7. change area')
            print('8. change types of troops name')
            print('9. change headquarters')
            print('10. change commander')
            print('11. change count')

            print('12. EXIT')
            print('choose:')
            choice = int(input())
            if choice in choices:
                choices[choice]()


class RegimentTerm(object):
    def __init__(self):
        self.regiment_database = RegimentDatabase()

    def printDB(self):
        for regiment in self.regiment_database:
            print('=' * 15)
            print(regiment.info())
            print('=' * 15)

    def run(self):
        choice = 0
        choices = {
            1: lambda: self.printDB(),
            2: lambda: self.regiment_database.add_regiment(
                country=input('Enter country: '),
                city=input('Enter city: '),
                address=input('Enter address: '),
                area=int(input('Enter area: ')),
                type_name=input('Enter types of troops name: '),
                headquarters=input('Enter headquarters: '),
                commander=input('Enter commander: '),
                count=int(input('Enter count: '))
            ),
            3: lambda: self.regiment_database.delete_regiment(
                int(input('Enter number: '))
            ),
            4: lambda: self.regiment_database.change_country(
                int(input('Enter number: ')), input('Enter country: ')
            ),
            5: lambda: self.regiment_database.change_city(
                int(input('Enter number: ')), input('Enter city: ')
            ),
            6: lambda: self.regiment_database.change_address(
                int(input('Enter number: ')), input('Enter address: ')
            ),
            7: lambda: self.regiment_database.change_area(
                int(input('Enter number: ')), int(input('Enter area: '))
            ),
            8: lambda: self.regiment_database.change_type_name(
                int(input('Enter number: ')), input('Enter types of troops name: ')
            ),
            9: lambda: self.regiment_database.change_headquarters(
                int(input('Enter number: ')), input('Enter headquarters: ')
            ),
            10: lambda: self.regiment_database.change_commander(
                int(input('Enter number: ')), input('Enter commander: ')
            ),
            11: lambda: self.regiment_database.change_count(
                int(input('Enter number: ')), int(input('Enter count: '))
            )
        }
        while (choice != 12):
            print()
            print('1. print database')
            print('2. add regiment')
            print('3. delete regiment')
            print('4. change country')
            print('5. change city')
            print('6. change address')
            print('7. change area')
            print('8. change types of troops name')
            print('9. change headquarters')
            print('10. change commander')
            print('11. change count')

            print('12. EXIT')
            print('choose:')
            choice = int(input())
            if choice in choices:
                choices[choice]()


class StaffTerm(object):
    def __init__(self):
        self.staff_database = StaffDatabase()

    def printDB(self):
        for staff in self.staff_database:
            print('=' * 15)
            print(staff.info())
            print('=' * 15)

    def run(self):
        choice = 0
        choices = {
            1: lambda: self.printDB(),
            2: lambda: self.staff_database.add_staff(
                last_name=input('Enter last name: '),
                rota_name=input('Enter rota name: '),
                rota_count=int(input('Enter rota count: ')),
                post=input('Enter post: '),
                birth=input('Enter birth: '),
                admission_date=input('Enter admission date: '),
                seniority=int(input('Enter seniority: ')),
                awards=input('Enter awards: ').split(', '),
                events=input('Enter events: ').split(', ')
            ),
            3: lambda: self.staff_database.delete_staff(
                int(input('Enter number: '))
            ),
            4: lambda: self.staff_database.change_last_name(
                int(input('Enter number: ')), input('Enter last name: ')
            ),
            5: lambda: self.staff_database.change_rota_name(
                int(input('Enter number: ')), input('Enter rota name: ')
            ),
            6: lambda: self.staff_database.change_rota_count(
                int(input('Enter number: ')), int(input('Enter rota count: '))
            ),
            7: lambda: self.staff_database.change_post(
                int(input('Enter number: ')), input('Enter post: ')
            ),
            8: lambda: self.staff_database.change_birth(
                int(input('Enter number: ')), input('Enter birth: ')
            ),
            9: lambda: self.staff_database.change_admission_date(
                int(input('Enter number: ')), input('Enter admission date: ')
            ),
            10: lambda: self.staff_database.change_seniority(
                int(input('Enter number: ')), int(input('Enter seniority: '))
            ),
            11: lambda: self.staff_database.change_awards(
                int(input('Enter number: ')), input('Enter awards: ').split(', ')
            ),
            12: lambda: self.staff_database.change_events(
                int(input('Enter number: ')), input('Enter events: ').split(', ')
            ),
        }
        while (choice != 13):
            print()
            print('1. print database')
            print('2. add staff')
            print('3. delete staff')
            print('4. change last name')
            print('5. change rota name')
            print('6. change rota count')
            print('7. change post')
            print('8. change birth')
            print('9. change admission date')
            print('10. change seniority')
            print('11. change awards')
            print('12. change events')

            print('13. EXIT')
            print('choose:')
            choice = int(input())
            if choice in choices:
                choices[choice]()
