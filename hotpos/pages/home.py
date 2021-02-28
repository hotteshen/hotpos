from hotpos.widgets.table import OrdersTable
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QPushButton

from ..widgets.group_box import GroupBox
from ..widgets.label import Label
from ..widgets.table import OrdersTable


class Home(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        root_layout = QHBoxLayout()
        self.setLayout(root_layout)

        left_layout = QVBoxLayout()
        root_layout.addLayout(left_layout, 8)
        right_layout = QVBoxLayout()
        root_layout.addLayout(right_layout, 2)

        gb = GroupBox()
        left_layout.addWidget(gb)
        gb_root = gb.getRootLayout()
        gb_root.addWidget(Label('Late orders').setSize(20))
        late_orders_table = OrdersTable()
        late_orders_table.setData([
            ['001212', '15900', '2020-04-16'],
            ['001211', '23700', '2020-04-16'],
            ['001210', '26200', '2020-04-16'],
        ])
        gb_root.addWidget(late_orders_table)

        gb = GroupBox()
        left_layout.addWidget(gb)
        gb_root = gb.getRootLayout()
        gb_root.addWidget(Label('Upcoming orders').setSize(20))
        upcoming_orders_table = OrdersTable()
        upcoming_orders_table.setData([
            ['001212', '15900', '2020-04-16'],
            ['001211', '23700', '2020-04-16'],
            ['001210', '26200', '2020-04-16'],
        ])
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
