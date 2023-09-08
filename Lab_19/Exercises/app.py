import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt
from Database import *

Ui_MainWindow, QtBaseClass = uic.loadUiType('main_window.ui')


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.part_database = PartDatabase()
        self.battalion_database = BattalionDatabase()
        self.regiment_database = RegimentDatabase()
        self.staff_database = StaffDatabase()

        self.part_number.valueChanged.connect(lambda x: self.change_qspinbox(x, 'part'))
        self.part_action.clicked.connect(lambda: self.action_button('part'))
        self.part_delete.clicked.connect(lambda: self.delete_button('part'))

        self.battalion_number.valueChanged.connect(lambda x: self.change_qspinbox(x, 'battalion'))
        self.battalion_action.clicked.connect(lambda: self.action_button('battalion'))
        self.battalion_delete.clicked.connect(lambda: self.delete_button('battalion'))

        self.regiment_number.valueChanged.connect(lambda x: self.change_qspinbox(x, 'regiment'))
        self.regiment_action.clicked.connect(lambda: self.action_button('regiment'))
        self.regiment_delete.clicked.connect(lambda: self.delete_button('regiment'))

        self.staff_number.valueChanged.connect(lambda x: self.change_qspinbox(x, 'staff'))
        self.staff_action.clicked.connect(lambda: self.action_button('staff'))
        self.staff_delete.clicked.connect(lambda: self.delete_button('staff'))

        types = ['part', 'battalion', 'regiment', 'staff']
        for i in types:
            self.change_qspinbox(1, i)

    def action_button(self, action_type):
        button = None
        if action_type == "part":
            button = self.part_action
        elif action_type == "battalion":
            button = self.battalion_action
        elif action_type == "regiment":
            button = self.regiment_action
        else:
            button = self.staff_action

        if button.text() == 'Создать':
            if action_type == "part":
                self.part_database.add_part(self.part_country.toPlainText(),
                                            self.part_city.toPlainText(),
                                            self.part_address.toPlainText(),
                                        int(self.part_area.toPlainText()),
                                            self.part_type.toPlainText(),
                                        int(self.part_count.toPlainText()))
            elif action_type == "battalion":
                self.battalion_database.add_battalion(self.battalion_country.toPlainText(),
                                                      self.battalion_city.toPlainText(),
                                                      self.battalion_address.toPlainText(),
                                                  int(self.battalion_area.toPlainText()),
                                                      self.battalion_type.toPlainText(),
                                                      self.battalion_headquarters.toPlainText(),
                                                      self.battalion_commander.toPlainText(),
                                                  int(self.battalion_count.toPlainText()))
            elif action_type == "regiment":
                self.regiment_database.add_regiment(self.regiment_country.toPlainText(),
                                                    self.regiment_city.toPlainText(),
                                                    self.regiment_address.toPlainText(),
                                                int(self.regiment_area.toPlainText()),
                                                    self.regiment_type.toPlainText(),
                                                    self.regiment_headquarters.toPlainText(),
                                                    self.regiment_commander.toPlainText(),
                                                int(self.regiment_count.toPlainText()))
            elif action_type == "staff":
                self.staff_database.add_staff(self.staff_last_name.toPlainText(),
                                              self.staff_rota.toPlainText(),
                                          int(self.staff_rota_count.toPlainText()),
                                              self.staff_post.toPlainText(),
                                              self.staff_birth.toPlainText(),
                                              self.staff_admission_date.toPlainText(),
                                          int(self.staff_seniority.toPlainText()),
                                              self.staff_awards.toPlainText().split(', '),
                                              self.staff_events.toPlainText().split(', '))
        elif button.text() == 'Изменить':
            if action_type == "part":
                value = self.part_number.value()
                self.part_database.change_country(value, self.part_country.toPlainText())
                self.part_database.change_city(value, self.part_city.toPlainText())
                self.part_database.change_address(value, self.part_address.toPlainText())
                self.part_database.change_area(value, int(self.part_area.toPlainText()))
                self.part_database.change_type_name(value, self.part_type.toPlainText())
                self.part_database.change_count(value, int(self.part_count.toPlainText()))

                self.part_database.save_database()
            elif action_type == "battalion":
                value = self.battalion_number.value()
                self.battalion_database.change_country(value, self.battalion_country.toPlainText())
                self.battalion_database.change_city(value, self.battalion_city.toPlainText())
                self.battalion_database.change_address(value, self.battalion_address.toPlainText())
                self.battalion_database.change_area(value, int(self.battalion_area.toPlainText()))
                self.battalion_database.change_type_name(value, self.battalion_type.toPlainText())
                self.battalion_database.change_count(value, int(self.battalion_count.toPlainText()))
                self.battalion_database.change_headquarters(value, self.battalion_headquarters.toPlainText())
                self.battalion_database.change_commander(value, self.battalion_commander.toPlainText())

                self.battalion_database.save_database()
            elif action_type == "regiment":
                value = self.regiment_number.value()
                self.regiment_database.change_country(value, self.regiment_country.toPlainText())
                self.regiment_database.change_city(value, self.regiment_city.toPlainText())
                self.regiment_database.change_address(value, self.regiment_address.toPlainText())
                self.regiment_database.change_area(value, int(self.regiment_area.toPlainText()))
                self.regiment_database.change_type_name(value, self.regiment_type.toPlainText())
                self.regiment_database.change_count(value, int(self.regiment_count.toPlainText()))
                self.regiment_database.change_headquarters(value, self.regiment_headquarters.toPlainText())
                self.regiment_database.change_commander(value, self.regiment_commander.toPlainText())

                self.regiment_database.save_database()
            elif action_type == "staff":
                value = self.staff_number.value()
                self.staff_database.change_last_name(value, self.staff_last_name.toPlainText())
                self.staff_database.change_rota_name(value, self.staff_rota.toPlainText())
                self.staff_database.change_rota_count(value, int(self.staff_rota_count.toPlainText()))
                self.staff_database.change_post(value, self.staff_post.toPlainText())
                self.staff_database.change_birth(value, self.staff_birth.toPlainText())
                self.staff_database.change_admission_date(value, self.staff_admission_date.toPlainText())
                self.staff_database.change_seniority(value, int(self.staff_seniority.toPlainText()))
                self.staff_database.change_awards(value, self.staff_awards.toPlainText().split(', '))
                self.staff_database.change_events(value, self.staff_events.toPlainText().split(', '))

                self.staff_database.save_database()

        self.change_qspinbox(eval(f'self.{action_type}_number.value()'), action_type)

    def delete_button(self, action_type):
        if action_type == "part":
            value = self.part_number.value()
            self.part_database.delete_part(value)
        elif action_type == "battalion":
            value = self.battalion_number.value()
            self.battalion_database.delete_battalion(value)
        elif action_type == "regiment":
            value = self.regiment_number.value()
            self.regiment_database.delete_regiment(value)
        else:
            value = self.staff_number.value()
            self.staff_database.delete_staff(value)
        self.change_qspinbox(eval(f'self.{action_type}_number.value()'), action_type)

    def load_inputs_part(self, value, state):
        if state == 'full':
            self.part_country.setText(value.dislocation.country)
            self.part_city.setText(value.dislocation.city)
            self.part_address.setText(value.dislocation.address)
            self.part_area.setText(str(value.dislocation.area))
            self.part_type.setText(value.type.name)
            self.part_count.setText(str(value.count))
        else:
            self.part_country.setText("")
            self.part_city.setText("")
            self.part_address.setText("")
            self.part_area.setText("")
            self.part_type.setText("")
            self.part_count.setText("")

    def load_inputs_battalion(self, value, state):
        if state == 'full':
            self.battalion_country.setText(value.dislocation.country)
            self.battalion_city.setText(value.dislocation.city)
            self.battalion_address.setText(value.dislocation.address)
            self.battalion_area.setText(str(value.dislocation.area))
            self.battalion_type.setText(value.type.name)
            self.battalion_count.setText(str(value.count))
            self.battalion_commander.setText(value.commander)
            self.battalion_headquarters.setText(value.headquarters)
        else:
            self.battalion_country.setText("")
            self.battalion_city.setText("")
            self.battalion_address.setText("")
            self.battalion_area.setText("")
            self.battalion_type.setText("")
            self.battalion_count.setText("")
            self.battalion_commander.setText("")
            self.battalion_headquarters.setText("")

    def load_inputs_regiment(self, value, state):
        if state == 'full':
            self.regiment_country.setText(value.dislocation.country)
            self.regiment_city.setText(value.dislocation.city)
            self.regiment_address.setText(value.dislocation.address)
            self.regiment_area.setText(str(value.dislocation.area))
            self.regiment_type.setText(value.type.name)
            self.regiment_count.setText(str(value.count))
            self.regiment_commander.setText(value.commander)
            self.regiment_headquarters.setText(value.headquarters)
        else:
            self.regiment_country.setText("")
            self.regiment_city.setText("")
            self.regiment_address.setText("")
            self.regiment_area.setText("")
            self.regiment_type.setText("")
            self.regiment_count.setText("")
            self.regiment_commander.setText("")
            self.regiment_headquarters.setText("")

    def load_inputs_staff(self, value, state):
        if state == 'full':
            self.staff_last_name.setText(value.last_name)
            self.staff_rota.setText(value.rota.name)
            self.staff_rota_count.setText(str(value.rota.count))
            self.staff_post.setText(value.post)
            self.staff_birth.setText(value.birth)
            self.staff_admission_date.setText(value.admission_date)
            self.staff_seniority.setText(str(value.seniority))
            self.staff_awards.setText(', '.join(value.awards))
            self.staff_events.setText(', '.join(value.events))
        else:
            self.staff_last_name.setText('')
            self.staff_rota.setText('')
            self.staff_rota_count.setText('')
            self.staff_post.setText('')
            self.staff_birth.setText('')
            self.staff_admission_date.setText('')
            self.staff_seniority.setText('')
            self.staff_awards.setText('')
            self.staff_events.setText('')

    def change_qspinbox(self, value, spin_type):
        if spin_type == "part":
            part = self.part_database.get_part_by_number(value)
            if part is not None:
                self.print_info(part, spin_type)
                self.load_inputs_part(part, 'full')
                self.part_action.setText('Изменить')
                self.label_5.setText('Редактирование воинской части:')
                self.part_delete.setEnabled(True)
            else:
                self.part_action.setText('Создать')
                self.part_info.setText('Данные не были найдены!')
                self.load_inputs_part(part, 'empty')
                self.label_5.setText('Создание воинской части:')
                self.part_delete.setEnabled(False)

        elif spin_type == "battalion":
            battalion = self.battalion_database.get_battalion_by_number(value)
            if battalion is not None:
                self.print_info(battalion, spin_type)
                self.load_inputs_battalion(battalion, 'full')
                self.battalion_action.setText('Изменить')
                self.label_12.setText('Редактирование батальона:')
                self.battalion_delete.setEnabled(True)
            else:
                self.battalion_action.setText('Создать')
                self.load_inputs_battalion(battalion, 'empty')
                self.battalion_info.setText('Данные не были найдены!')
                self.label_12.setText('Создание батальона:')
                self.battalion_delete.setEnabled(False)
        elif spin_type == "regiment":
            regiment = self.regiment_database.get_regiment_by_number(value)
            if regiment is not None:
                self.print_info(regiment, spin_type)
                self.load_inputs_regiment(regiment, 'full')
                self.regiment_action.setText('Изменить')
                self.label_30.setText('Редактирование полка:')
                self.regiment_delete.setEnabled(True)
            else:
                self.regiment_action.setText('Создать')
                self.load_inputs_regiment(regiment, 'empty')
                self.regiment_info.setText('Данные не были найдены!')
                self.label_30.setText('Создание полка:')
                self.regiment_delete.setEnabled(False)
        elif spin_type == "staff":
            staff = self.staff_database.get_staff_by_number(value)
            if staff is not None:
                self.print_info(staff, spin_type)
                self.load_inputs_staff(staff, 'full')
                self.staff_action.setText('Изменить')
                self.label_41.setText('Редактирование служащих:')
                self.staff_delete.setEnabled(True)
            else:
                self.staff_action.setText('Создать')
                self.load_inputs_staff(staff, 'empty')
                self.staff_info.setText('Данные не были найдены!')
                self.label_41.setText('Создание служащих:')
                self.staff_delete.setEnabled(False)

    def print_info(self, value, info_type):
        eval(f'self.{info_type}_info.setText(value.info())')


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
