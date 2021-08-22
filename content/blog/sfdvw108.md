---
date: "2021-08-21T00:20:00+02:00"
publishdate: "2021-08-21+20:00"
lastmod: "2021-08-21+20:00"
draft: false
title: "SfdvW - 108 - Datenträger"
tags: ["Dateisystem", "Datenträger", "Speichermedien", "Disk", "Raid"]
series: ["SfdvW"]
categories: ["Sendebeitrag"]
img: ""
toc: true
summary: "Sendung Nummer 108 Datenträger"
link: "https://cdn.sfdvw.de/audio/Sendung_fuer_die_vernetzte_Welt_(108)_2021_08_21_Datenträger.mp3"
audio: "https://cdn.sfdvw.de/audio/Sendung_fuer_die_vernetzte_Welt_(108)_2021_08_21_Datenträger.mp3"
---

<div align="center" id="example"></div>
<script src="https://cdn.podlove.org/web-player/embed.js"></script>

Feedback zur Sendung?
[Schreibe uns ein Kommentar](mailto:SfdvW@radiocorax.de)

## SfdvW - 108 - Datenträger
mit dabei: markus, honky


### Informationsbegriff

- Information https://de.wikipedia.org/wiki/Information
    - Information ist in der Informationstheorie das Wissen, das ein Absender einem Empfänger über einen Informationskanal vermittelt. 


- Daten https://www.duden.de/rechtschreibung/Daten
    - elektronisch gespeicherte Zeichen, Angaben, Informationen
        - Zeichen, die eine Information darstellen -> 0,1 Bits, Alphabet, etc.
- Datei
    -  Bestand meist inhaltlich zusammengehöriger Daten, der auf einem Datenträger oder Speichermedium gespeichert
    -  eindimensionale Aneinanderreihung von https://de.wikipedia.org/wiki/Bit
        -   Bit ist eine Wortkreuzung aus binary digit – englisch für „binäre Ziffer“ oder auch Binärziffer


- Dateiformat https://de.wikipedia.org/wiki/Dateiformat
    - offene Dateiformate
    - proprietäre Dateiformaten


### Speichermedien:

- Lochkarte https://de.wikipedia.org/wiki/Lochkarte
    - lochkartengesteuerte Webstühle 
    - Drehorgeln 

- Schallplatte https://de.wikipedia.org/wiki/Schallplatte
    - https://de.wikipedia.org/wiki/Voyager_Golden_Record

- Magnetbänder https://de.wikipedia.org/wiki/Magnetband
    - einer langen, schmalen Folie aus Kunststoff, die mit einem magnetisierbaren Material beschichtet
    - Drahtaufzeichnungsgeräte noch bis in die 1970er in Satelliten und anderen unbemannten Raumschiffen Verwendung
    - ausschließlich sequentiellen Zugriff 

- eine Sammlung von adressierbaren Datenblöcken
    - 512 Bytes = 2^9 oder 4.096 Bytes = 212 
- https://de.wikipedia.org/wiki/Festplattengeometrie
- https://de.wikipedia.org/wiki/Zylinder-Kopf-Sektor-Adressierung
    - die Kopfnummer der Höhe,  die Zylindernummer dem Radius,    die Sektornummer dem Winkel
    - früher per Hand eingestellt
    - mehr Sektoren auf den Außenbahnen https://de.wikipedia.org/wiki/Zone_Bit_Recording 
- Fesplatten Kopf-Fahrwege: https://youtu.be/SZ0xXI9kvPo
    - https://youtu.be/SZ0xXI9kvPo?t=1907
- https://de.wikipedia.org/wiki/Logical_Block_Addressing
    - Blöcke einfach gezählt, beginnend mit Null
    - Festplatten haben eigene Kontroller
    - Typische Grenzen sind 504 MiB, 8 GiB, 32 GiB, 128 GiB. Die 128-GiB-Grenze resultiert aus der Verwendung von 28-Bit-LBA, 
- Kontinuierliche Speicherung (aufsteigend hintereinander)
    - Vorteile:
        - minimale Positionierungszeit
        - schneller Zugriff auf bestimmte Dateiposition
        - z.B. bei CD-Roms
    - Nachteile:
        - Problem des freien Platzes,
        - Fragmentierung, 
        - Größe bei neuen Dateien nicht immer bekannt, Erweitern schwierig
        
- Verkettete Speicherung (am Ende des Blocks verweis auf Folgeblock)
    - z.B. C64 und auch FAT
    - Datei kann wachsen uns schrumpfen
    - Adressen brauchen Platz! Verzeigerung
    - Fehleranfälligkeit
    - Schlechter direkter Zugriff (viele Sprünge)
    - aufwendige Suche

- Indiziertes Speichern z.B. Inodes usw.

- https://de.wikipedia.org/wiki/Programmed_Input/Output
    - Regelwerk zur Steuerung des Datenaustauschs zwischen dem Prozessor und den Peripheriegeräten
    - Nachteil Zwischenschritt bis zum Arbeitsspeicher
- https://de.wikipedia.org/wiki/Speicherdirektzugriff
    - Direct Memory Access (DMA) bezeichnet in der Computertechnik eine Zugriffsart, die über ein Bussystem direkt auf den Speicher zugreift
    - separaten Baustein wie zum Beispiel den 8237 oder den 8257 von Intel. 
    - Remote Direct Memory Access auch über Netzwerkverbindungen möglich z.B. bei NFS

- https://de.wikipedia.org/wiki/Small_Computer_System_Interface
    - 1986 wurde die SCSI-Spezifikation als X3.131-1986 von der ANSI standardisiert
    - Festplatten und Bandlaufwerken genutzt, auch Scannern und optische Laufwerken 
    - Heute definiert SCSI zusätzlich zu Parallel SCSI (SPI) weitere Übertragungswege, wie Serial Attached SCSI (SAS), Fibre Channel und iSCSI. 
    - SAS heute so gut wie ausschließlich in Servern SAS Platten mittels bsp. HBA oder RAID


- ATA Festplatten (WD 1984 IDE danach als ATA-1 ATA-2 etc danach PATA )
        - https://de.wikipedia.org/wiki/ATA/ATAPI
        - (IBM) A(dvanced) T(echnologie) Attachment
    - ATA-1 (1989–1999, ANSI X3.221-1994)
        - Gleichzeitige Ansteuerung von maximal zwei Festplatten mit einer Übertragungsrate von bis zu 8,3 MB/s 
        - inkl. DMA
    - ATA-2 (1994–2001, ANSI X3.279-1996)
        - PIO-Modus 3: 11,1 MB/s; PIO 4: 16,6 MB/s
        - DMA-Modus 1: 13,3 MB/s, Modus 2 (DMA 2): 16,6 MB/s (ab hier immer Multi Word)
    - ATA/ATAPI-6 (seit 2000, ANSI NCITS 361-2002)
        - 2^28 · 512 Byte = 128 GiB auf 2^48 · 512 Byte = 134.217.728 GiB (≈ 144.115.188 GB) = 128 PiB erhöht


- Serial ATA (Serial AT Attachment) 
    - Daten werden seriell übertragen (Bit für Bit) und nicht, wie bei den alten ATA-Standards, in 16-Bit-Wörtern
    - höhere Datentransferrate, vereinfachte Kabelführung und die Fähigkeit zum Austausch von Datenträgern im laufenden Betrieb (Hot-Plug)
    - SATA zudem in Konkurrenz zu USB, FireWire und Thunderbolt
    -  Mit 10 Leitungsbits werden 8 Bit Daten übertragen
    - Sata-1 1,2 Gbit/s 
    - Sata-2 2,4 Gbit/s
    - Sata-3.0 4,8 (600 MB/s). 
- https://de.wikipedia.org/wiki/PCI_Express
    - alles schneller und besser
    - Gegensatz zum parallelen PCI-Bus kein geteiltes (shared) Bus-System
    - für jedes Gerät dedizierten Punkt-zu-Punkt-
    - :) 

- https://de.wikipedia.org/wiki/Solid-State-Drive
    - https://de.wikipedia.org/wiki/Nichtfl%C3%BCchtiger_Datenspeicher
    - keine beweglichen Teile
    - unempfindlich gegen Stöße, Erschütterungen und Vibrationen. 
    - kürzere Zugriffszeiten und arbeiten geräuschlos
    - benötigt weniger Strom
    - produziert weniger Abwärme

- https://de.wikipedia.org/wiki/Master_Boot_Record
    - Beschränkt Festplatten auf 2 TiB
- https://de.wikipedia.org/wiki/GUID_Partition_Table
    - Spezifikation ist Teil des UEFI-Standards ersetzt zunehmend https://de.wikipedia.org/wiki/BIOS


### DAS Dateisysteme

https://de.wikipedia.org/wiki/Direct_Attached_Storage

- Dateisystem https://de.wikipedia.org/wiki/Dateisystem
    - CRUD Create, Read, Update, Delete https://de.wikipedia.org/wiki/CRUD 
    - auch Metadaten 
        - Zeitpunkt der Dateierstellung
        - Besitzer der Datei
    - effiziente Organisation
    - Dateisystemspezifikation von einem Treiber https://de.wikipedia.org/wiki/Ger%C3%A4tetreiber
        - (Kernel)
        - Programm im Userspace

#### Single Disk 

- FAT https://de.wikipedia.org/wiki/File_Allocation_Table
    -  ist eine Art Tabelle fester Größe, in der über die belegten und freien Cluster eines FAT-Dateisystems Buch geführt wird. 
    -  Ein Cluster ist die aus einem oder mehreren Sektoren bestehende Zuordnungseinheit, die von einer Datei belegt werden kann.
    -   Cluster existiert ein Eintrag in der FAT
    -   existieren in der Regel zwei Kopien der FAT
    -   Acht Zeichen für den Dateinamen und drei Zeichen für die Dateinamenserweiterung https://de.wikipedia.org/wiki/8.3 
- NTFS https://de.wikipedia.org/wiki/NTFS
    - TFS ist ein proprietäres Dateisystem von Microsoft für alle Betriebssysteme der Windows-NT-Reihe (ab 1993). Die Abkürzung steht für New Technology File System
    - gezielten Zugriffsschutz auf Dateiebene sowie größere Datensicherheit durch Journaling
        - das alle Änderungen vor dem eigentlichen Schreiben in einem dafür reservierten Speicherbereich, dem Journal, aufzeichnet https://de.wikipedia.org/wiki/Journaling-Dateisystem 
    - Dateigröße nicht wie bei FAT auf 4 GiB beschränkt
    - werden bei NTFS alle Informationen zu Dateien in einer Datei (Konzept: alles ist in einer Datei), der Master File Table, kurz MFT gespeichert. 
    - Sehr kleine Dateien und Verzeichnisse werden in der MFT direkt abgespeichert. 
    -  MFT ein fester Platz reserviert, falls voll wird woanders freier Speicher verwendet (Fragmentierung)
    -  Standardmäßig wird ein Bereich von 12,5 % der Partitionsgröße für die MFT reserviert

- DOS  / Multics / Unix - Verzeichnisse
    - Unix-Konzept Everything is a file  http://www.netzmafia.de/skripten/unix/unix1.html#1.5
        - Normale Dateien
        - Verzeichnisse
        - Spezialdatenen
            - E/A Geräte
    -  MS-DOS ab Version 2.0) gibt es ebenfalls Gerätedateien: COM:, CON:, LPT:, PRN:
    
- ext ext2 ext3
    - extended filesystem 
    - https://de.wikipedia.org/wiki/Ext2 
    - https://de.wikipedia.org/wiki/Ext3
    - https://de.wikipedia.org/wiki/Ext4
    - https://de.wikipedia.org/wiki/Jahr-2038-Problem
    - https://de.wikipedia.org/wiki/Inode 
        - ls -i Dateiname && stat Dateiname
        - Diese enthält die Metadaten der Datei und verweist auf die Daten der Datei beziehungsweise die Dateiliste des Verzeichnisses.
        -  Schrägstrich / (slash) begrenzten Namen ist genau ein Inode zugeordnet
        -   Dieser speichert folgende Metainformationen zur Datei, aber nicht den eigentlichen Namen:
            - Die Art der Datei (reguläre Datei, Verzeichnis, Symbolischer Link, …), siehe unten;
            - die numerische Kennung des Eigentümers (UID, user id) und der Gruppe (GID, group id);
            - die Zugriffsrechte für den Eigentümer (user), die Gruppe (group) und alle anderen (others);
            - Die klassische Benutzer- und Rechteverwaltung geschieht mit den Programmen chown (change owner), chgrp (change group) und chmod (change mode). Durch Access Control Lists (ACL) wird eine feinere Rechtevergabe ermöglicht.
            - verschiedene Zeitpunkte der Datei: Erstellung, Zugriff (access time, atime) und letzte Änderung (modification time, mtime);
            - die Zeit der letzten Status-Änderung des Inodes (status, ctime);
            - die Größe der Datei;
            - den Linkzähler (viele Dateiennamen auf diesen verweisen);
            -  einen oder mehrere Verweise auf die Blöcke, in denen die eigentlichen Daten gespeichert sind.
    
    - https://de.wikipedia.org/wiki/Unixoides_System
- Apple? not my department
    - MFS https://de.wikipedia.org/wiki/Macintosh_File_System 
        - nur ein Jahr, flat file system (keine Verzeichnisse :)
    - HFS  https://de.wikipedia.org/wiki/HFS_(Dateisystem)
        - proprietäres Format
        - gut dokumentiert, deswegen oft zugreifbar
        - maximale Anzahl Dateien (65.536)
        - Dateinamen bis zu einer Länge von 31 Zeichen
        - 
    - HFS+ https://de.wikipedia.org/wiki/HFS_Plus 
        - 1998 -2016
    - APFS https://de.wikipedia.org/wiki/Apple_File_System
        - Verwendung von Flash-Speicher wie SSDs 
        - https://de.wikipedia.org/wiki/Copy-On-Write
        - https://de.wikipedia.org/wiki/Schnappschuss_(Informationstechnik)#Massenspeicher
        - „Fast Directory Sizing“
        - „Atomic Safe-Save“ 
        - Verschlüsselung
        - https://www.macwelt.de/a/high-sierra-was-apfs-hevc-und-heif-bringen,3437774

#### DAS Multiple Disk

- RAID https://de.wikipedia.org/wiki/RAID
    - Redundant Array of Independent Disks
    - Hardware Raid vs. Software Raid
    - RAID 0: Striping – Beschleunigung ohne Redundanz
    - RAID 1: Mirroring – Spiegelung
    - RAID 5: Leistung + Parität, Block-Level Striping mit verteilter Paritätsinformation
- JBOD https://de.wikipedia.org/wiki/RAID#JBOD

##### DAS Software Raid

- Vorteil zum Hardware Raid, belegte und unbelegte Blöcke können unterschieden werden, was Wiederherstellungen deutlich effizienter macht
- brauchen Host Bus Adapter https://de.wikipedia.org/wiki/Host-Bus-Adapter

- LVM https://de.wikipedia.org/wiki/Logical_Volume_Manager
- Windows: Basic and Dynamic Disks https://docs.microsoft.com/en-us/windows/win32/fileio/basic-and-dynamic-disks?redirectedfrom=MSDN
- Windows 10+: Storage Spaces in Windows 10 https://support.microsoft.com/en-us/windows/storage-spaces-in-windows-10-b6c8b540-b8d8-fb8a-e7ab-4a75ba11f9f2

- ZFS  (Zetta File System) https://de.wikipedia.org/wiki/ZFS_(Dateisystem)
    - https://de.wikipedia.org/wiki/Transaktionaler_Speicher
    - https://cre.fm/cre049-das-zfs-dateisystem
    - https://media.ccc.de/search/?q=ZFS
    - große Dateigrößen
    - Raid und LVM inkludiert
    - Encryption
    - Deduplication
    - prüfsummenbasierte Schutz vor Datenübertragungsfehlern
    - zfs send / receive
    - 128-Bit Copy-On-Write-Dateisystem 
        - Snapshots ohne Zeitverlust
    - eher nicht so auf Windows https://superuser.com/questions/289189/access-a-zfs-volume-in-windows
    
- BTRFS https://de.wikipedia.org/wiki/Btrfs
    - https://media.ccc.de/search/?q=BTRFS
    - Btrfs mit der B-Baum-Struktur / https://de.wikipedia.org/wiki/B-Baum
        - ist ein immer vollständig balancierter Baum, der Daten nach Schlüsseln sortiert speichert
        - kann binär sein, ist es aber hier nicht
    - freie Software unter GPL
    - sehr ähnlich zu ZFS, geschaffen um dessen Lizenzprobleme zu umgehen
    - Gibts auch für Windows
    - btrfs-convert, kann ext3- und ext4-Dateisysteme reversibel Konvertieren
    - erweiterter Speicherbereich (264 Byte)
    - effizientes Speichern kleiner Dateien und Verzeichnisse
    - dynamische Inodes
    - Schnappschüsse
    - mehrere Subvolumen
    - Datenkompression
    - Dateisystemcheck und Defragmentierung während des Betriebs
    - effiziente interne inkrementelle Datensicherung
    - Copy-On-Write
    - Prüfsummen



<script>
  podlovePlayer('#example', '/blog/sfdvw108.json');
</script>
