from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCharts import QtCharts

app = QApplication([])

# Hauptfenster erstellen
window = QMainWindow()
window.setWindowTitle("ChartView Beispiel")

# ChartView erstellen
chart_view = QtCharts.QChartView()
window.setCentralWidget(chart_view)

# Chart erstellen
chart = QtCharts.QChart()
chart.setTitle("ChartView Beispiel")

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
chart.addAxis(axis_x, QtCharts.QtAlignBottom)
series.attachAxis(axis_x)

axis_y = QtCharts.QValueAxis()
axis_y.setLabelFormat("%.1f")
chart.addAxis(axis_y, QtCharts.QtAlignLeft)
series.attachAxis(axis_y)

# ChartView konfigurieren
chart_view.setChart(chart)
chart_view.setRenderHint(QtCharts.QPainter.Antialiasing)

# Hauptfenster anzeigen
window.show()

app.exec()

"""
In diesem Beispiel wird ein einfaches Liniendiagramm erstellt 
und in einem QChartView-Widget angezeigt. Das QChartView-Widget
wird als zentrales Widget in einem QMainWindow verwendet.
Die Datenpunkte werden mit einem QLineSeries hinzugefügt und die 
Achsen werden erstellt und dem Chart hinzugefügt. Schließlich wird das QChartView konfiguriert und das Hauptfenster angezeigt.

Um dieses Beispiel ausführen zu können, solltest du sicherstellen, 
dass du PySide6 und QtCharts installiert hast. Du kannst dies mit dem Befehl pip install pyside6 erledigen.
"""
#matplotlib
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from matplotlib.backends.backend_qt6agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

app = QApplication(sys.argv)

# Hauptfenster erstellen
window = QMainWindow()
window.setWindowTitle("Matplotlib ChartView Beispiel")

# Zentrales Widget erstellen
central_widget = QWidget()
window.setCentralWidget(central_widget)

# Layout für das zentrale Widget erstellen
layout = QVBoxLayout(central_widget)

# Figure erstellen
figure = Figure()

# Plot erstellen
axis = figure.add_subplot(111)
axis.set_title("Matplotlib ChartView Beispiel")
axis.plot([1, 2, 3, 4, 5], [2, 4, 6, 8, 10])

# FigureCanvas erstellen und dem Layout hinzufügen
canvas = FigureCanvas(figure)
layout.addWidget(canvas)

# Hauptfenster anzeigen
window.show()

sys.exit(app.exec())
