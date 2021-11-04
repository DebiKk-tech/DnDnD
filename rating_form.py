from PyQt5.QtWidgets import QWidget, QTableWidgetItem
from PyQt5 import uic

from sqlite_functions import *


class RatingForm(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        uic.loadUi('rating_form.ui', self)
        self.tbl_top_rating.setColumnCount(2)
        self.tbl_top_rating.setVerticalHeaderLabels(['Игрок', 'Очки'])
        all_profiles = get_all_players()
        all_profiles = list(map(lambda x: (x[0], x[2]), all_profiles))
        all_profiles.sort(key=lambda x: x[1])
        for i, row in enumerate(all_profiles):
            self.tbl_top_rating.setRowCount(
                self.tbl_top_rating.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tbl_top_rating.setItem(
                    i, j, QTableWidgetItem(str(elem)))