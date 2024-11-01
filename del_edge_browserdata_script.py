"""
Das Skript beendet alle aktiven Edge-Prozesse
und ERZWINGT danach die Löschung aller Edge-Browserdaten rekursiv!
Created by Fabian
Last updated on 2024-11-01
"""
import subprocess

def clear_edge_data():
    # PowerShell-Befehl zum Löschen der Edge-Browserdaten
    command = r'''
    # Beende alle Edge-Prozesse, um Sperren zu vermeiden
    Get-Process -Name msedge -ErrorAction SilentlyContinue | Stop-Process -Force
    
    # Pfad zu den Edge-Browserdaten
    $path = "$env:LOCALAPPDATA\Microsoft\Edge\User Data\Default"
    
    # Lösche die Daten, falls das Verzeichnis existiert
    if (Test-Path $path) {
        Remove-Item -Path $path\* -Recurse -Force -ErrorAction SilentlyContinue
        Write-Output "Die Edge-Browserdaten wurden geloescht."
    } else {
        Write-Output "Das Edge-Datenverzeichnis wurde nicht gefunden."
    }
    '''
    
    # PowerShell-Skript ausführen und Ausgabe anzeigen
    result = subprocess.run(["powershell", "-Command", command], capture_output=True, text=True)
    print(result.stdout)


# Funktion ausführen
clear_edge_data()
