import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QDateEdit, QFileDialog, QMessageBox
from PyQt5.QtCore import QDateTime
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import pandas as pd

class TemperatureApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Temperature Graph App')
        self.setGeometry(100, 100, 800, 600)

        # Date range selection
        self.start_date_label = QLabel('Start Date:')
        self.start_date_edit = QDateEdit()
        self.start_date_edit.setDateTime(QDateTime.currentDateTime().addDays(-30))

        self.end_date_label = QLabel('End Date:')
        self.end_date_edit = QDateEdit()
        self.end_date_edit.setDateTime(QDateTime.currentDateTime())

        # Graph display area
        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)

        # Load data button
        self.load_data_button = QPushButton('Load Data from CSV')
        self.load_data_button.clicked.connect(self.load_data_from_csv)

        # Generate button
        self.generate_button = QPushButton('Generate Graph')
        self.generate_button.clicked.connect(self.generate_graph)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.start_date_label)
        layout.addWidget(self.start_date_edit)
        layout.addWidget(self.end_date_label)
        layout.addWidget(self.end_date_edit)
        layout.addWidget(self.load_data_button)
        layout.addWidget(self.generate_button)
        layout.addWidget(self.canvas)
        self.setLayout(layout)

        self.show()

    def load_data_from_csv(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Open CSV File", "", "CSV Files (*.csv);;All Files (*)", options=options)

        if file_path:
            self.data = pd.read_csv(file_path, parse_dates=['Date'])
            QMessageBox.information(self, 'Data Loaded', 'CSV data loaded successfully.')

    def generate_graph(self):
        if not hasattr(self, 'data'):
            QMessageBox.warning(self, 'Data Missing', 'Please load data from CSV first.')
            return

        start_date = self.start_date_edit.date().toPyDate()
        end_date = self.end_date_edit.date().toPyDate()

        start_date = pd.to_datetime(start_date)
        end_date = pd.to_datetime(end_date)


        filtered_data = self.data[(pd.to_datetime(self.data['Date']) >= start_date) & (pd.to_datetime(self.data['Date']) <= end_date)]

        self.ax.clear()
        self.ax.plot(filtered_data['Date'], filtered_data['Temperature'], marker='o', linestyle='-')
        self.ax.set_title('Temperature Data')
        self.ax.set_xlabel('Date')
        self.ax.set_ylabel('Temperature (°C)')

        self.canvas.draw()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TemperatureApp()
    sys.exit(app.exec_())
