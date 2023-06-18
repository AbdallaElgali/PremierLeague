# Premier League Scraper (Deutsch)
Dieses Programm ist dazu gedacht, Informationen über die aktuelle Tabellenplatzierung der Premier League abzurufen und Benutzern die Möglichkeit zu geben, Spielinformationen für ein bestimmtes Datum abzurufen. Das Programm ruft Daten von zwei Websites ab: https://www.skysports.com/premier-league-table für die aktuelle Tabellenplatzierung und https://sports.ndtv.com/english-premier-league/schedules-fixtures für Spielinformationen.

## Installation
Um das Premier League Scraper-Programm auszuführen, befolgen Sie diese Schritte:

1. Klonen Sie das Repository oder laden Sie die Quellcode-Dateien herunter.
2. Installieren Sie die erforderlichen Abhängigkeiten:
 - Requests-Bibliothek: Verwenden Sie den Befehl pip install requests, um sie zu installieren.
 - Beautiful Soup 4-Bibliothek: Verwenden Sie den Befehl pip install beautifulsoup4, um sie zu installieren.
 - bs4-Modul: Dies ist in der Beautiful Soup 4-Bibliothek enthalten.
3. Öffnen Sie ein Terminal oder die Kommandozeile und navigieren Sie zum Verzeichnis, in dem sich die Programmdateien befinden.
4. Führen Sie das Programm aus, indem Sie den Befehl python dateiname.py ausführen, wobei dateiname.py der Name des Python-Skripts mit dem Programmcode ist.

## Verwendung
Nach dem Ausführen des Programms werden Ihnen folgende Optionen angezeigt:

1. Aktuelle Tabellenplatzierung der Premier League-Teams anzeigen
2. Premier League-Spiele an einem bestimmten Datum überprüfen
3. Spiele von heute anzeigen
4. Beenden
Um eine Option auszuwählen, geben Sie die entsprechende Nummer ein und drücken Sie die Eingabetaste.


## 1. Aktuelle Tabellenplatzierung der Premier League-Teams anzeigen
Diese Option zeigt die aktuelle Tabellenplatzierung der Premier League-Teams an. Das Programm ruft die Daten von https://www.skysports.com/premier-league-table ab und ermittelt die Teamnamen und ihre entsprechenden Punkte. Die Tabellenplatzierung wird dann im Terminal angezeigt.

## 2. Premier League-Spiele an einem bestimmten Datum überprüfen
Mit dieser Option können Sie die Spielinformationen für ein bestimmtes Datum abrufen. Sie werden aufgefordert, ein Datum im Format tt-mm-jjjj einzugeben. Das Programm ruft die Spielinformationen von https://sports.ndtv.com/english-premier-league/schedules-fixtures ab und zeigt die Spiele, Teams und Ergebnisse für das angegebene Datum an.

## 3. Spiele von heute anzeigen
Wenn Sie diese Option auswählen, wird automatisch das aktuelle Datum abgerufen und die Spielinformationen für heute abgerufen. Das Programm zeigt die Spiele, Teams und Ergebnisse für das aktuelle Datum an.

## 4. Beenden
Wenn Sie diese Option auswählen, wird das Programm beendet.

## Anforderungen
Das Premier League Scraper-Programm erfordert die folgenden Abhängigkeiten:

Python 3.x
Requests-Bibliothek
Beautiful Soup 4-Bibliothek
Diese Abhängigkeiten können mit dem Paketmanager pip installiert werden. Weitere Informationen finden Sie im Abschnitt "Installation" oben.
