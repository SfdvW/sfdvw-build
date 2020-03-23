---
date: "2019-12-21T00:20:00+02:00"
publishdate: "2019-12-21+20:00"
lastmod: "2019-12-21+20:00"
draft: false
title: "SfdvW - 87 - Backups"
tags: ["Backup"]
series: ["SfdvW"]
categories: ["Sendebeitrag"]
img: ""
toc: true
summary: "Sendung Nummer 87 Backups"
link: "https://cdn.sfdvw.de/audio/Sendung_fuer_die_vernetzte_Welt_(87)_2019_12_21_Backups.mp3"
audio: "https://cdn.sfdvw.de/audio/Sendung_fuer_die_vernetzte_Welt_(87)_2019_12_21_Backups.mp3"
---

<div align="center" id="example"></div>
<script src="https://cdn.podlove.org/web-player/embed.js"></script>



Feedback zur Sendung?
[Schreibe uns ein Kommentar](mailto:SfdvW@radiocorax.de)

## SfdvW - 87 - Backups
mit dabei: tmk, markus, reem, jotilux

### Worum geht es Heute
Weihnachtszeit ist Backup-Zeit -> Chaos Communicaton Congress + IT Support bei der Familie

Hardware- oder Softwaredefekt, Viren/Trojaner, Diebstahl oder höhere Gewalt(Überspannung/Hochwasser): schon sind die Daten weg

### Hinweise
Ihr wollte nicht Daten-Sichern, Ihr wollt sie Wiederherstellen.

Backup(Datensicherung) heißt Daten mindestens zweimal zu haben
möglichst ortsgetrennt(Disaster Recovery)

### Backupstrategien
* Großvater-Vater-Sohn-Prinzip  / [Generationsprinzip](https://de.wikipedia.org/wiki/Generationenprinzip)
    * 21 Bänder
        * 12 Stück Januar - Dezember (Großvater)
        * 5 Stück Freitag 1 - Freitag 5 (Vater)
        * 4 Stück Mo - Do (Sohn)

* Vollbackup
    * pro: alle Dateien, Restore mit nur einem Medium
    * con: viel Platz pro Backup

* Inkrementelles Backup ([Archiv-Bit](https://de.wikipedia.org/wiki/Archivbit))
    * Mo - Vollbackup
    * Di - Do Intrementell (Änderungen täglich)
    * Ausfall Do d.h. benötigt Do, Mi, Di, Mo

* Differenzielles Backup
    * Mo - Vollbackup
    * Di - Do Differenziell (Änderungen Wöchentlich)
    * Do beinhaltet alle Änderungen bis Mo
    * Ausfall Do d.h. benötigt Do, Mo

### Fragen über Fragen
* Datensicherungen
    * machen oder nicht?
        * habe ich wichtige Daten?
            * Bewerbung, Zeugniskopie/Urkunden, Zertifikate, digitale Fotos, Videoaufnahmen der ersten Schritte des Kindes, Audioaufnahmen der Band, Spielstände, Verträge, 
    * wenn ja wohin?
        * zu Fremden?
    * Immer alles oder nur die unterschiede
        * incrementell/ differenziell / vollbackup
    * Verschlüsseln?
    * Wie oft
        * Automatisch machen lassen? push/pull?
    * Einhörnchen strategie
        * Überall mal ein Backup "vergraben"
    * Backups zurückspielen zwingend prüfen!
    * Raid ist kein Backup!

* Closed oder Opensource Software?

* Linux
    * restic
    * rsync /grsync
    * Onboard Software
* Windows
    * "Aktenkoffer"
    * onboard backup
    * einfach kopieren
    * restic
* *OS
    * Time-machine

* Dateisysteme
    * [zfs](https://de.wikipedia.org/wiki/ZFS_(Dateisystem))

### Firma:
* Gesetzliche Archivierungspflicht über Jahre (z.B. Multimediaarchiv für TV in 4k mit Datenmengen in Größenordnungen)
* [Disaster_Recovery](https://de.wikipedia.org/wiki/Disaster_Recovery)
* [Bandlaufwerksroboter für Wartung begehbar](https://www.youtube.com/watch?v=X5UCfU9Q-iA) [Teil2](https://www.youtube.com/watch?v=74l96vMPI5c)
* NAS
* Cloud

### privat
* 08/15 usb sticks vs. vernünftige externe festplatte/ssd vs. NAS vs. Cloud

### Verein
* Wie macht das Radio Corax mit dem Backup?

### unsere Empfehlungen
* [clonezilla](https://clonezilla.org/) bzw. bei mehreren Geräten [FOG Project](https://fogproject.org/)
* [Der Backup-Reminder vom Browser Ballett](https://www.youtube.com/watch?v=jN5mICXIG9M)


### Flash/SSD vs. Tape libary vs. Helium HDDs vs. NAS
* Tapes lohnen sich preislich erst ab vielen
* Festplatten sind billig

### Veranstaltungshinweise
* 28.12.2019 Congress Junghacker-Tag
* 16.05.2020Llinux Präsentation Day
* 31.03.2020 [World Backup Day](http://www.worldbackupday.com/de/)

<script>
  podlovePlayer('#example', '/blog/sfdvw87.json');
</script>
