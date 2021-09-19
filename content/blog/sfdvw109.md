---
date: "2021-09-18T00:20:00+02:00"
publishdate: "2021-09-18+20:00"
lastmod: "2021-09-18+20:00"
draft: false
title: "SfdvW - 109 - LoRaWAN"
tags: ["LoRaWAN", "TTN", "WAN", "Zirpenfrequenzspreizung"]
series: ["SfdvW"]
categories: ["Sendebeitrag"]
img: ""
toc: true
summary: "Sendung Nummer 109 LoRaWAN"
link: "https://cdn.sfdvw.de/audio/Sendung_fuer_die_vernetzte_Welt_(109)_2021_09_18_LoRaWAN.mp3"
audio: "https://cdn.sfdvw.de/audio/Sendung_fuer_die_vernetzte_Welt_(109)_2021_09_18_LoRaWAN.mp3"
---

<div align="center" id="example"></div>
<script src="https://cdn.podlove.org/web-player/embed.js"></script>

Feedback zur Sendung?
[Schreibe uns ein Kommentar](mailto:SfdvW@radiocorax.de)

## SfdvW - 109 - LoRaWAN
mit dabei: tmk, nilo, markus, Andreas, Spiegie

### Worum geht es Heute?
In Folge 109 geht es um LoRaWAN - dem "Long Range Wide Area Netzwork". Wir haben mit Andreas gesprochen,
ein "Early Adopter" von LoRaWAN und Initiator der lokalen TTN Community. Im zweiten Teil der Sendung berichtet
spiegie über zwei seiner eigenen LoRa-Projekte. 

### zum Anfang
* Jugend hackt Ost 2016
    * https://youtu.be/CldlrDOTxVI?t=1999

### Grundlegendes
* Long Range Wide Area Network
* proprietäres, patentiertes Übertragungsverfahren basierend auf einer "Zirpenfrequenzspreizung" genannten Modulationstechnik
    * "Als ein Chirp oder eine Zirpe wird in der Signalverarbeitung ein Signal bezeichnet, dessen Frequenz sich zeitlich ändert."
    * Vorteile CSS gegenüber anderer Modulationstechniken (z.B. AM, FM)
        * Energieeffizient
        * hohe Störunanfälligkeit
            * Reflektionen sind kein Problem, daher gut für Stadt geeignet
            * Doppler-Effekt sind kein Problem, daher gut für mobile Anwendungen geeignet
    * Tipp zum vertiefen: https://media.ccc.de/v/33c3-7945-decoding_the_lora_phy
* 863 bis 870 MHz
* durch niedrige Frequenz hohe Reichweiten > 10km möglich, auch gute Abdeckung in Innenstädten
* Übertragungsraten bis zu 50kbit/s (1MB in 46h)
* geeignet für Messdaten, Steuersignale
* energiesparend (z.B. für Sender mit Batterieversorgung)

### Funktionsweise
* Gateways haben Internet
* Empfangene Daten werden über Internet an Application Server weitergeschickt
* Dort werden die Daten dann an die Anwendungen weitergeleitet
* Rückkanal entsprechend andersrum

### "Stacks"
* Es gibt verschiedene, proprietäre "Stacks", aber auch offene.
* Der jeweilige Stack muss auf den Gateways vorhanden sein, die die "Reichweite" der Anwendung abdecken.
* Am verbreitetsten ist TTN (The Things Network)
    * Kann frei genutzt werden
    * fair-use Policy
    * The Things Industries ist kommerzielle Firma, die das The Things Network "sponsort"
* Es gibt auch alternative "Stacks"

### LoRa Community
* TTN Halle-Saalkreis https://www.thethingsnetwork.org/community/halle-saalekreis/
* TTN Mitteldeutschland https://www.thethingsnetwork.org/community/mitteldeutschland/
* Freifunk Halle https://freifunk-halle.org

### Konkrete Anwendungen
* Openbike https://github.com/stadtulm/OpenBike
* Katzentracker
* LoRa-Chat-Pager
* TTN Mapper https://ttnmapper.org




<script>
  podlovePlayer('#example', '/blog/sfdvw109.json');
</script>
