#Charts in PyQT
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PySide6.QtCharts import QtCharts

app = QApplication([])

# Hauptfenster erstellen
window = QMainWindow()
window.setWindowTitle("Chart Beispiel")

# Zentrales Widget erstellen
central_widget = QWidget()
window.setCentralWidget(central_widget)

# Layout für das zentrale Widget erstellen
layout = QVBoxLayout(central_widget)

# ChartView erstellen
chart_view = QtCharts.QChartView()
layout.addWidget(chart_view)

# Chart erstellen
chart = QtCharts.QChart()
chart.setTitle("Chart Beispiel")

# Datenpunkte hinzufügen
series = QtCharts.QLineSeries()
series.append(0, 0)
series.append(1, 1)
series.append(2, 3)
series.append(3, 2)
series.append(4, 4)
chart.addSeries(series)

# Achsen erstellen und dem Chart hinzufügen
axis_x = QtCharts.QValueAxis()
axis_x.setLabelFormat("%.1f")
chart.addAxis(axis_x, QtCharts.Qt.AlignBottom)
series.attachAxis(axis_x)

axis_y = QtCharts.QValueAxis()
axis_y.setLabelFormat("%.1f")
chart.addAxis(axis_y, QtCharts.Qt.AlignLeft)
series.attachAxis(axis_y)

# ChartView konfigurieren
chart_view.setChart(chart)
chart_view.setRenderHint(QtCharts.QPainter.Antialiasing)

# Hauptfenster anzeigen
window.show()

app.exec()
#Charts in matplotlib.pyplot
import matplotlib.pyplot as plt

# Beispiel-Daten
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Diagramm erstellen
plt.plot(x, y)

# Achsentitel hinzufügen
plt.xlabel('X-Achse')
plt.ylabel('Y-Achse')

# Diagramm anzeigen
plt.show()

