#Timer mit Button zum Starten
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton
from PySide6.QtCore import QTimer

app = QApplication([])

# Hauptfenster erstellen
window = QMainWindow()
window.setWindowTitle("Timer Beispiel")

# Zentrales Widget erstellen
central_widget = QWidget()
window.setCentralWidget(central_widget)

# Layout für das zentrale Widget erstellen
layout = QVBoxLayout(central_widget)

# Timer-Button erstellen
button_start = QPushButton("Start Timer")

# QTimer-Objekt erstellen
timer = QTimer()

def start_timer():
    print("Timer started")

# Timer-Button mit der Funktion zum Starten des Timers verknüpfen
button_start.clicked.connect(start_timer)

# Timer zum Layout hinzufügen
layout.addWidget(button_start)

# Hauptfenster anzeigen
window.show()

app.exec()

#Blanker Timer
from PySide6.QtCore import QTimer

# QTimer-Objekt erstellen
timer = QTimer()

# Timer-Intervall in Millisekunden festlegen
timer.setInterval(1000)  # 1 Sekunde

# Timeout-Signal mit einer Funktion verknüpfen
timer.timeout.connect(your_function)

# Timer starten
timer.start()

