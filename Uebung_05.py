import sys  # Importiere das sys-Modul, das Funktionen und Variablen zur Interaktion mit dem Python-Interpreter bereitstellt
from PyQt5.QtCore import *  # Importiere die Kernfunktionalität von PyQt5
from PyQt5.QtWidgets import *  # Importiere Widgets und Tools aus PyQt5
from PyQt5.QtGui import *  # Importiere grafische Elemente aus PyQt5

# Definition der Hauptklasse, die ein QMainWindow erbt
class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()  # Rufe den Konstruktor der Elternklasse auf

        # Fenstertitel festlegen
        self.setWindowTitle("GUI - Programmierung")

        # Layout erstellen (FormLayout für Anordnung in Formular)
        layout = QFormLayout()

        # GUI-Elemente erstellen
        self.Vorname = QLineEdit()  # Textfeld für den Vornamen
        self.Name = QLineEdit()  # Textfeld für den Nachnamen
        self.Geburtstag = QDateEdit()  # Datumsfeld für das Geburtsdatum
        self.Adresse = QLineEdit()  # Textfeld für die Adresse
        self.Postleitzahl = QLineEdit()  # Textfeld für die Postleitzahl
        self.Ort = QLineEdit()  # Textfeld für den Ort
        self.Land = QComboBox()  # Dropdown-Liste für das Land
        self.Button = QPushButton("Save")  # Schaltfläche zum Speichern
        self.button1 = QPushButton("Auf Karte zeigen")  # Schaltfläche zum Anzeigen der Adresse auf der Karte
        self.button2 = QPushButton("Laden")  # Schaltfläche zum Laden von Daten
        self.Land.addItems(["Schweiz", "Deutschland", "Österreich"])  # Elemente zur Dropdown-Liste hinzufügen

        # GUI-Elemente zum Layout hinzufügen
        layout.addRow("Vorname:", self.Vorname)
        layout.addRow("Name:", self.Name)
        layout.addRow("Geburtstag:", self.Geburtstag)
        layout.addRow("Adresse:", self.Adresse)
        layout.addRow("Postleizahl:", self.Postleitzahl)
        layout.addRow("Ort:", self.Ort)
        layout.addRow("Land:", self.Land)
        layout.addRow(self.button1)
        layout.addRow(self.button2)
        layout.addRow(self.Button)

        # Menüleiste erstellen
        menubar = self.menuBar()  # Menüleiste des Hauptfensters abrufen
        file = menubar.addMenu("File")  # Menü "File" hinzufügen
        view = menubar.addMenu("View")  # Menü "View" hinzufügen

        # Aktionen (Menüoptionen) erstellen
        self.save = QAction("Save", self)  # Aktion "Save" erstellen
        self.quit = QAction("Quit", self)  # Aktion "Quit" erstellen
        self.kartee = QAction("Karte", self)  # Aktion "Karte" erstellen
        self.ladenn = QAction("Laden", self)  # Aktion "Laden" erstellen

        # Aktionen den Menüs hinzufügen
        file.addAction(self.save)
        file.addAction(self.quit)
        view.addAction(self.kartee)
        file.addAction(self.ladenn)

        # Button-Verbindungen einrichten (Signale mit Slots verbinden)
        self.Button.clicked.connect(self.textFile)  # Klick auf "Save"-Schaltfläche ruft textFile-Methode auf
        self.save.triggered.connect(self.textFile)  # Auslösen des "Save"-Menüpunkts ruft textFile-Methode auf
        self.quit.triggered.connect(self.close)  # Auslösen des "Quit"-Menüpunkts ruft close-Methode auf
        self.kartee.triggered.connect(self.karte)  # Auslösen des "Karte"-Menüpunkts ruft karte-Methode auf
        self.ladenn.triggered.connect(self.laden)  # Auslösen des "Laden"-Menüpunkts ruft laden-Methode auf
        self.button1.clicked.connect(self.karte)  # Klick auf "Auf Karte zeigen"-Schaltfläche ruft karte-Methode auf
        self.button2.clicked.connect(self.laden)  # Klick auf "Laden"-Schaltfläche ruft laden-Methode auf

        # Zentrales Widget (Layout) festlegen
        center = QWidget()
        center.setLayout(layout)
        self.setCentralWidget(center)  # Layout des Hauptfensters festlegen

        # Fenster anzeigen
        self.show()

    # Methode zum Speichern der Eingaben in eine Textdatei
    def textFile(self):
        filename, filter = QFileDialog.getSaveFileName(self, "Datei speichern", "", "Text Datei (*.txt)")  # Dateidialog zum Speichern öffnen
        g = self.Geburtstag.date().toString("dd.MM.yyyy")  # Geburtsdatum in das gewünschte Format konvertieren
        text = f"{self.Vorname.text()},{self.Name.text()},{g},{self.Adresse.text()},{self.Postleitzahl.text()},{self.Ort.text()},{self.Land.currentText()}"  # Daten zu einem Textstring formatieren
        file = open(filename, "w", encoding="utf-8")  # Textstring in eine Datei schreiben
        file.write(text)
    
    # Methode zum Schließen der Anwendung
    def close(self):
        self.close()  # Anwendung schließen

    # Methode zum Anzeigen der Adresse auf einer Karte
    def karte(self):
        import urllib.parse
        query = "Hello World"
        a = urllib.parse.quote(query)
        # Google Maps-Link mit den eingegebenen Adressinformationen erstellen
        link = f"https://www.google.ch/maps/place/{self.Adresse.text()}+{self.Postleitzahl.text()}+{self.Ort.text()}+{self.Land.currentText()}"
        # Link in einem Browser öffnen
        QDesktopServices.openUrl(QUrl(link))

    # Methode zum Laden von Daten aus einer Textdatei
    def laden(self):
        # Dateiauswahldialog zum Öffnen anzeigen
        filename, filter = QFileDialog.getOpenFileName(self, "Datei öffnen", "", "Text Datei(*.txt)")
        # Wenn eine Datei ausgewählt wurde
        if filename:
            with open(filename, "r", encoding="utf-8") as f:
                data = f.read()  # Daten aus der Datei lesen
        # Daten aus der Datei extrahieren und in die entsprechenden GUI-Elemente einfügen
        fields = data.split(",")
        self.Vorname.setText(fields[0])
        self.Name.setText(fields[1])
        date = QDate.fromString(fields[2], "dd.MM.yyyy")
        self.Geburtstag.setDate(date)
        self.Adresse.setText(fields[3])
        self.Postleitzahl.setText(fields[4])
        self.Ort.setText(fields[5])  
        self.Land.setCurrentText(fields[6])  

# Hauptfunktion zum Starten der Anwendung
def main():
    app = QApplication(sys.argv)  # Qt Applikation erstellen
    mainwindow = MyWindow()  # Instanz Fenster erstellen
    mainwindow.raise_()  # Fenster nach vorne bringen
    app.exec_()  # Applikations-Loop starten

# Prüfen, ob das Skript direkt ausgeführt wird
if __name__ == '__main__':
    main()