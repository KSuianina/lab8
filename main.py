import sys

from PyQt5 import QtWidgets

import win.main_window as main_win

import classes.sold_class
import classes.client_org_class
import classes.client_person_class
import classes.supplied_class
import classes.supplier_org_class
import classes.supplier_person_class
import classes.orders_class
import classes.storage_class
import classes.contract_class


class MainWindow(QtWidgets.QMainWindow, main_win.Ui_MainWindow):
    def sold(self):
        self.window = classes.sold_class.Sold()
        self.window.show()

    def client_org(self):
        self.window = classes.client_org_class.ClientOrg()
        self.window.show()

    def client_person(self):
        self.window = classes.client_person_class.ClientPerson()
        self.window.show()

    def contract(self):
        self.window = classes.contract_class.Contract()
        self.window.show()

    def order(self):
        self.window = classes.orders_class.Orders()
        self.window.show()

    def supplier_org(self):
        self.window = classes.supplier_org_class.SupplierOrg()
        self.window.show()

    def suppllier_person(self):
        self.window = classes.supplier_person_class.SupplierPerson()
        self.window.show()

    def storage(self):
        self.window = classes.storage_class.Storage()
        self.window.show()

    def supplied(self):
        self.window = classes.supplied_class.Supplied()
        self.window.show()

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton_sold.clicked.connect(self.sold)
        self.pushButton_client_org.clicked.connect(self.client_org)
        self.pushButton_client_person.clicked.connect(self.client_person)
        self.pushButton_contract.clicked.connect(self.contract)
        self.pushButton_order.clicked.connect(self.order)
        self.pushButton_supplier_org.clicked.connect(self.supplier_org)
        self.pushButton_supplier_person.clicked.connect(self.suppllier_person)
        self.pushButton_storage.clicked.connect(self.storage)
        self.pushButton_supplied.clicked.connect(self.supplied)


def run_main_win():
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec_()


if __name__ == '__main__':
    run_main_win()
