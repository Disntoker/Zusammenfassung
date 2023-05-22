#QThread
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton
from PySide6.QtCore import QThread, QTimer, Signal

app = QApplication([])

# Hauptfenster erstellen
window = QMainWindow()
window.setWindowTitle("QThread Beispiel")

# Zentrales Widget erstellen
central_widget = QWidget()
window.setCentralWidget(central_widget)

# Layout für das zentrale Widget erstellen
layout = QVBoxLayout(central_widget)

# Worker-Thread erstellen
class WorkerThread(QThread):
    # Signal definieren
    update_signal = Signal(int)

    def run(self):
        for i in range(1, 11):
            # Signal aussenden
            self.update_signal.emit(i)
            self.msleep(1000)  # 1 Sekunde warten

# Thread-Objekt erstellen
thread = WorkerThread()

# Funktion zum Aktualisieren der UI
def update_ui(value):
    print(f"Counter: {value}")

# Signal mit der Funktion zum Aktualisieren der UI verknüpfen
thread.update_signal.connect(update_ui)

# Start-Button
button_start = QPushButton("Start Thread")
button_start.clicked.connect(thread.start)

# Thread und Button zum Layout hinzufügen
layout.addWidget(button_start)

# Hauptfenster anzeigen
window.show()

app.exec()
"""
Ein QThread ist wie ein Helfer, der dir hilft, Dinge zu erledigen,
während du andere Sachen machst. Er kann längere Aufgaben in kleinere
Teile aufteilen und dir Bescheid geben, wenn er einen Teil erledigt
hat, damit du währenddessen andere Dinge tun kannst. Dadurch kannst
du deine Zeit effizienter nutzen und musst nicht alles auf einmal erledigen.
"""