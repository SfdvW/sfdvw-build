---
date: "2023-04-15T00:20:00+02:00"
publishdate: "2023-04-15+20:00"
lastmod: "2023-04-15+20:00"
draft: false
title: "SfdvW - 125 - CB Funk"
tags: ["CB", "Funk", "11-Meter-Band"]
series: ["SfdvW"]
categories: ["Sendebeitrag"]
img: ""
toc: true
summary: "Sendung Nummer 125 CB Funk"
link: "https://cdn.sfdvw.de/audio/Sendung_fuer_die_vernetzte_Welt_(125)_2023_04_15_CB_Funk.mp3"
audio: "https://cdn.sfdvw.de/audio/Sendung_fuer_die_vernetzte_Welt_(125)_2023_04_15_CB_Funk.mp3"
---

<div align="center" id="example"></div>
<script src="https://cdn.podlove.org/web-player/embed.js"></script>

Feedback zur Sendung?
[Schreibe uns ein Kommentar](mailto:SfdvW@radiocorax.de)

## SfdvW - 125 - CB Funk
mit dabei: littlealex, markus, tmk, nilo, jotilux

### Worum geht es heute
Heute befinden wir uns thematisch im 11 Meter Band oder anders gesagt auf der Funkfrequenz bei 27MHz. Es geht um CB Funk (citizens band radio) und all seinen Betriebsarten und Eigenheiten. Mit dabei sind unsere Gäste Alex und Markus, die extra Spielzeug mitgebracht haben. Was das mit dem Wetter zu tun hat müsst Ihr selbst erhöhren!

### Shownotes 

##### Technik, Geschichte und Unterschiede zu anderen Funktechniken
* Einleitung
    * Beweggründe (weitestgehend ungenutzt, hoher Hackfaktor, soziale Komponente)
    * Jedermannfunkanwendung, also ohne Lizenz, wie auch das WIFI-Band, keine abgeschlossene Benutzergruppe wie bei HAM oder Betriebsfunk, gehört zum ISM
    * unterscheidet sich von anderem Sprechfunk
        * Freenet (nur BRD, UKW,149MHz,1W)
        * SRD (Short Range Device, ehem. LPD, 70cm, 433MHz,10mW)
        * PMR/DMR (EU-weit, Personal Mobile Radio, 466MHz,0.5W, max. 180sec, Frequenzzuteilung befristet bis 31.12.2030) 
* Übersicht CB
       * 11m-Band, 27MHz
       * Feststationen, Mobilgeräte, Handfunkgeräte
       * AM, FM, SSB
       * 4w, 12W
* Geschichte CB
       * 1975 in der BRD, DDR ab 1990, dafür für Betriebsfunk etc genutzt, sogenannte K-Geräte
       * erste Geräte hatten AM, 0.1W mobil, 0.5W fest, Kanäle 4-15
       * seit 1996 80 Kanäle, 4W FM, 1W AM, seit 2011 4W FM/AM, 12W SSB
* Technische Eigenschaften
     * Kurzwelle
         * analog
         * 27MHz, 11m
         * Wellenausbreitung
             * Bodenwelle (folget der Erdkrümmung, "Ortsgespräch")
             * Raumwelle (kann an der Ionosphäre reflektiert werden, DX)
             * je leitfähiger der Boden um so bessere Ausbreitung
     * Reichweiten 100m - 100km, DX tausende Kilometer (abhängig vom Funkwetter, Standort usw.)
         * Stationsantennen 20-100km
         * Mobilantennen auf KFZ 10-25km
         * Handfunkgeräte 100m-5km
     * Normen
         * CEPT (EU plus weitere Staaten, 40 Kanäle, AM/FM, 1W/4W)
         * Polen (40FM 4W, 40AM 4W, 40SSB 12W9)
         * UK (40FM 4W, AM & SSB sollen irgendwann komnmen)
         * EU-Grundnorm (40FM 4W, 40AM 4W, 40 SSB 12W)
         * BRD (80Kanäle, 1-40 AM/FM 4W, 12W SSB, 40-80 FM 4W)
         * nur zugelassene Geräte dürfen betrieben werden, d.h. kein Selbstbau
     * Antennen
         * müssen abgestimmt werden, ansonsten drohen Defekte am Funkgerät
         * Basis (bis zu 8m lang, meist an Mast, starr oder flexibel, λ1/2 oder λ5/8, selten λ1/4 )
         * Mobil (KFZ, fest, Magnetfuss, Klemmantenne, 30cm bis 2m, halbstarr oder flexibel, meist λ1/4, selten λ1/2 oder λ5/8) 
         * Handfunkgeräte (10cm - 50cm, meist flexibel, meist λ1/4)
         * meist Groundplane, aber auch Langdrahtantennen
             
##### Sicherheit
* keine Verschlüsselung

##### Funkbetrieb
* anders als bei HAM oder Betriebsfunk keine zugeteilten Rufzeichen, wählt man selbst
* keine Anmeldung
* keine Gebühren
* keine Lizenz
* Verhalten
       * viel vom Amateurfunk abgeschaut
       * Leben und Leben lassen
       * bei Fehlverhalten kommen die anderen und sägen die Antenne ab und irgendwann kommt auch die Bundesnetzagentur
* Verbotenes
       * andere stören
       * Dauersendungen (a.k.a. Radio machen)
       * Verstärker (alias Brenner oder Oma)
       * nicht zugelassene oder manipulierte Geräte
       * Richtfunk (mit Einschränkungen, zum Beispiel Fuchsjagt)

##### Gründe sich mit CB Funk zu beschäftigen
* Krisenfunk (siehe Arltal)
* Funk mitunter praktischer als Handy
* Hobby verbindet Technik mit Sozialem
* sehr niedriche Einstiegshürde
     * keine Lizenz
     * keine Anmeldung
     * Geräte liegen in Kellern und Dachböden

##### digitale Betriebsarten
* Packet Radio
      * Datenübertragung über Funk
      * bei CB ist die Bandbreite begrenzt
      * üblich ist AFSK mit 1.2kBit, 2.4kBit möglich, 4.8kBit geht manchmal, aber ausserhalb der Kanalbreite
           * AMTOR, ROS
           * AX.25, FX.25, IP, KISS
           * Kommunikation
           * Statusmeldungen
           * Telemetrie
           * Fernwirkung
           * Warum nicht LoRA? (andere Technik, anderes Ziel, schwer vergleichbar)
* Geräte
     * TNC (implementieren AX.25 und AFSK)
           * kommerziell
           * Arduino, ESP
           * Raspbery PI
     * analoge Modems (implementieren AFSK, AX.25 in Software auf Hostrechner)
           * kommerziell (Minicom, CB-Com)
           * Eigenbau 
     * Soundmodem (alles in Software, nur Adapterkabel nötig)
           * gibts für alle OS
           * einfach zu upgraden/erweitern
           * flexibel
* Netzwerken
      * im Prinzip alles machbar was man mit LAN oder WIFI machen kann
      * IP geht, aber recht viel Overhead
      * AX.25 ist Quasistandard, anderes theoretisch möglich
      * Routing, Direktverbindung, Store&Forward
      * Tunneling über Internet
      * Mailboxen (BBS), Chat, Email usw.
      * Datenübertragung

##### Links mit Audiobeispiel
* https://de.wikipedia.org/wiki/Packet_Radio#AFSK-Modus
* https://de.wikipedia.org/wiki/AMTOR
* https://de.wikipedia.org/wiki/ROS_(Betriebsart)


<script>
  podlovePlayer('#example', '/blog/sfdvw125.json');
</script>
