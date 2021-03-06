from datetime import date as Date

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidget, QAbstractItemView, QHeaderView, QTableWidgetItem


class OrdersTableWidget(QTableWidget):

    def __init__(self, *args):
        QTableWidget.__init__(self, *args)

        self.setStyleSheet("QTableWidget::item{ selection-background-color: #26A9E0}")
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setAlternatingRowColors(True)
        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.setObjectName("tw_items")
        self.setColumnCount(3)
        self.setRowCount(0)
        horHeaders = ["Order#", "Price(LBP)", "Date"]
        self.setHorizontalHeaderLabels(horHeaders)
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.setData([])

    def setData(self, data: list, sortColumn: int = 0):
        def toString(x):
            if type(x) == int:
                return str(x)
            elif type(x) == Date:
                return str(x)
            else:
                return str(x)
        self.setRowCount(0)
        self.setSortingEnabled(False)
        for item in data:
            r = self.rowCount()
            self.insertRow(r)
            for i in range(3):
                cell = QTableWidgetItem(toString(item[i]))
                cell.setTextAlignment(Qt.AlignHCenter)
                self.setItem(r, i, cell)
        self.setSortingEnabled(True)
        # self.sortByColumn(sortColumn, Qt.AscendingOrder)
