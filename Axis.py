#Axis PyQt
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PySide6.QtCharts import QtCharts

app = QApplication([])

# Hauptfenster erstellen
window = QMainWindow()
window.setWindowTitle("Axis Beispiel")

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
chart.setTitle("Axis Beispiel")

# Datenpunkte hinzufügen
series = QtCharts.QLineSeries()
series.append(1, 2)
series.append(2, 4)
series.append(3, 6)
series.append(4, 8)
series.append(5, 10)
chart.addSeries(series)

# X-Achse erstellen
axis_x = QtCharts.QValueAxis()
axis_x.setLabelFormat("%d")
axis_x.setTitleText("X-Achse")
chart.addAxis(axis_x, QtCharts.QtAlignBottom)
series.attachAxis(axis_x)

# Y-Achse erstellen
axis_y = QtCharts.QValueAxis()
axis_y.setLabelFormat("%d")
axis_y.setTitleText("Y-Achse")
chart.addAxis(axis_y, QtCharts.QtAlignLeft)
series.attachAxis(axis_y)

# ChartView konfigurieren
chart_view.setChart(chart)
chart_view.setRenderHint(QtCharts.QPainter.Antialiasing)

# Hauptfenster anzeigen
window.show()

app.exec()



#matplotlib
import matplotlib.pyplot as plt

# Beispiel-Daten
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Diagramm erstellen
fig, ax = plt.subplots()

# Daten plotten
ax.plot(x, y)

# Achsenbeschriftungen festlegen
ax.set_xlabel('X-Achse')
ax.set_ylabel('Y-Achse')

# Achsenticks anpassen
ax.set_xticks([1, 3, 5])
ax.set_yticks([0, 5, 10])

# Achsentickbeschriftungen festlegen
ax.set_xticklabels(['Eins', 'Drei', 'Fünf'])
ax.set_yticklabels(['Null', 'Fünf', 'Zehn'])

# Achsenlimits festlegen
ax.set_xlim(0, 6)
ax.set_ylim(0, 12)

# Gitterlinien anzeigen
ax.grid(True)

# Diagramm anzeigen
plt.show()
