from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QGroupBox

from ..widgets.table import OrdersTableWidget


class HomePage(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app = QApplication.instance()

        root_layout = QVBoxLayout(self)

        gb = QGroupBox("Late orders")
        root_layout.addWidget(gb)
        gb_root = QVBoxLayout(gb)
        late_orders_table = OrdersTableWidget()
        late_orders_table.setData(self.app.backend().getLateOrderList())
        gb_root.addWidget(late_orders_table)

        gb = QGroupBox("Upcoming orders")
        root_layout.addWidget(gb)
        gb_root = QVBoxLayout(gb)
        upcoming_orders_table = OrdersTableWidget()
        upcoming_orders_table.setData(self.app.backend().getUpcomingOrderList())
        gb_root.addWidget(upcoming_orders_table)
