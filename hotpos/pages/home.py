from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton

from ..widgets.group_box import GroupBoxWidget
from ..widgets.label import LabelWidget
from ..widgets.table import OrdersTableWidget


class HomePage(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app = QApplication.instance()

        root_layout = QHBoxLayout()
        self.setLayout(root_layout)

        left_layout = QVBoxLayout()
        root_layout.addLayout(left_layout, 8)
        right_layout = QVBoxLayout()
        root_layout.addLayout(right_layout, 2)

        gb = GroupBoxWidget()
        left_layout.addWidget(gb)
        gb_root = gb.getRootLayout()
        gb_root.addWidget(LabelWidget('Late orders').setSize(20))
        late_orders_table = OrdersTableWidget()
        late_orders_table.setData(self.app.backend().getLateOrderList())
        gb_root.addWidget(late_orders_table)

        gb = GroupBoxWidget()
        left_layout.addWidget(gb)
        gb_root = gb.getRootLayout()
        gb_root.addWidget(LabelWidget('Upcoming orders').setSize(20))
        upcoming_orders_table = OrdersTableWidget()
        upcoming_orders_table.setData(self.app.backend().getUpcomingOrderList())
        gb_root.addWidget(upcoming_orders_table)

        def increaseHeight(btn: QPushButton) -> QPushButton:
            btn.setStyleSheet('height: 64px; margin-bottom: 16px;')
            return btn

        button = QPushButton('Take Away')
        increaseHeight(button)
        right_layout.addWidget(button)
        button = QPushButton('Delivery')
        increaseHeight(button)
        right_layout.addWidget(button)
        button = QPushButton('Table')
        increaseHeight(button)
        right_layout.addWidget(button)
        button = QPushButton('Reservation')
        increaseHeight(button)
        right_layout.addWidget(button)
