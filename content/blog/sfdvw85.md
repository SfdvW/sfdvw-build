---
date: "2019-10-19T00:20:00+02:00"
publishdate: "2019-10-19+20:00"
lastmod: "2019-10-19+20:00"
draft: false
title: "SfdvW - 85 - mobile Messenger"
tags: ["Messenger", "moblie", "Riot", "signal", "whatsapp", "threema", "telegram", "XMPP/jabber", "chiffry", "briar", "slack", "discord", "twitter"]
series: ["SfdvW"]
categories: ["Sendebeitrag"]
img: ""
toc: true
summary: "Sendung Nummer 85 mobile Messenger"
link: "https://sfdvw.de/audio/Sendung_fuer_die_vernetzte_Welt_(85)_2019_10_19_Mobile_Messenger.mp3"
chapters: "<chapter start=\"00:00:00\" title=\"Intro\" />"
---

<div align="center" id="example"></div>
<script src="https://cdn.podlove.org/web-player/embed.js"></script>



Feedback zur Sendung?
[Schreibe uns ein Kommentar](mailto:SfdvW@radiocorax.de)

### SfdvW - 85 - mobile Messenger
Sendungstermin 19.10.2019 20-21Uhr
mit dabei: tmk, nilo, Wolfgang, markus

#### Worum geht es Heute
* Thema mobile messenger: "Die Liste von Kommunikationsprogrammen resp. Diensten ist lang. Eine Auswahl schwierig. Meist wird daher der Dienst zur **eigenen Gewohnheit** übernommen, welcher auch das **persönliche Umfeld** am häufigsten benutzt. Die Unterschiede sind jedoch gross, so dass sich eine genauere Betrachtung lohnt." - digitale-gesellschaft.ch 2016-11-07 
* [Überblick Wikipedia](https://de.wikipedia.org/wiki/Liste_von_mobilen_Instant-Messengern)
* [Überblick digitale Gesellschaft](https://www.digitale-gesellschaft.ch/2016/11/07/whatsapp-e-mail-sms-co-auf-sicherheit-und-nachhaltigkeit-bewertet-produktvergleich/)
* Funktionen die ein mobile messenger haben kann
    * Textnachrichten, Sprachnachrichten, Bildnachrichten, Gruppenchat, Asynchrone Kommunikation (Nachricht wird bei Status Offline zwischengespeichert)

#### "früher"
* pager ([quix](https://de.wikipedia.org/wiki/Quix), telmi, [scall](https://de.wikipedia.org/wiki/Scall), [skyper](https://de.wikipedia.org/wiki/Skyper_(Pager)))
    * [Funkmeldeempfänger und Pager Computer:Club2](https://www.youtube.com/watch?v=7N-CxZXpV_8)
* sms / [stille sms](https://de.wikipedia.org/wiki/Stille_SMS)

#### wie verbreitet ist es
* Persönliche Erfahrung:  Was nutzen/haben wir genutzt?
    * Riot (Matrix)
        * [Matrix_(communication_protocol)](https://en.wikipedia.org/wiki/Matrix_(communication_protocol))
    * Whatsapp
        * am weiten verbreitetestr Ende zu Ende verschlüsselter Messanger 
            * Verschlüsselung von Signal "eingekauft"
    * Signal
        * [signal-foundation](https://signal.org/blog/signal-foundation/)
        * benötigt eine Telefonnummer
    * Threema
        * Bosch und Schweizer Bundesbehörden nutzen es
        * closed Source
    * Telegram
        * open Source Client, Server closed Source
        * Selbstentwickelte Verschlüsselung [MTProto-Protokoll](https://de.wikipedia.org/wiki/Telegram#cite_note-88)
    * XMPP/Jabber
        * Selbst hosten, kompliziert aber Grundlage vieler anderer messagnger (facebook)
        * [Androidclient](https://conversations.im/)
    * [Chiffry](https://www.chiffry.de/)
        * Regional (Teutschenthal)
    * [briar](https://briarproject.org/)
        * serverless
    
    **gibt auch noch andere Tools, die für messaging benutzt werden können**
    
    * Slack, discord
        * closed Source
        * freie alternativen: rocketchat, mattermost, zulip, ...

    **auch DM-Funktionen in sozialen netzwerken werden benutzt**
    
    * twitter

* [Telefonzelle_(Deutschland)](https://de.wikipedia.org/wiki/Telefonzelle_(Deutschland))
* [Dia_(Fotografie)](https://de.wikipedia.org/wiki/Dia_(Fotografie))
* [Heise.de - Studie zu Darknet Preisen Daten von Europaeern sind teuer](https://www.heise.de/newsticker/meldung/Studie-zu-Darknet-Preisen-Daten-von-Europaeern-sind-teuer-4560072.html)
 

#### Thema Sicherheit
* Wer bezahlt die infrastruktur / Entwickt die Software 
    * Wie verdienen Sie ihren unterhalt?
* Metadaten (Wer, mit wem, wann, wie oft)
* welche Verschlüsselungstechnologie bzw. welches Verschlüsselungsprotokoll kommt zum Einsatz
    * Sollte offen kommuniziert sein und kein Geheimnis
    * E2E-Verschlüsselung (Client-Client)
        * keine, Eigententwicklung, Standardverfahren(OTR, TLS)
    * Client-Server-Verschlüsselung (unverschlüsselt auf dem Server, bzw. unvers. Server-Server)
        * keine, Eigententwicklung, Standardverfahren([OTR](https://de.wikipedia.org/wiki/Off-the-Record_Messaging), [Signal Protokoll](https://de.wikipedia.org/wiki/Signal-Protokoll, [TLS](https://de.wikipedia.org/wiki/Transport_Layer_Security),)
* Authentifizierung (kryptographische Methoden, mit denen die Echtheit einer Nachricht überprüft werden kann)
* Abstreitbarkeit (siehe Wikipedia)
* Perfect Forward Secrecy (PFS, jede Nachricht wird mit einem neuen Kurzzeitschlüssel verschlüsselt, der von einem Langzeitschlüssel abgeleitet wird und innerhalb kurzer Zeit gelöscht wird -> Schlüsselleak für nicht zur entschlüsselung älterer Nachrichten!)
#### Thema Datenschutz und Risiken
* Metadaten (Übertragung der Verbindungsdaten)
* Übertragung der Kontakte
* personalisierte Werbung
* Cybermobbing (Messenger sind unmoderiert, Es gibt meist keine Möglichkeit, Störer oder Belästiger zu melden. Deshalb liegen hier auch die Hemmschwellen für Belästigungen niedriger. Mobile Messenger werden häufig für Cybermobbing genutzt – den Ausschluss aus Gruppen, das Gründen von Hetz-Gruppen, das Verbreiten peinlicher Fotos und das Versenden beleidigender Nachrichten. Durch die Mobilität der Anwendungen werden so Konflikte aus dem Klassenzimmer und vom Schulhof bis nach Hause mitgenommen. Für die Opfer bedeutet das eine noch größere Belastung und Hilflosigkeit.)
* Ungeeignete Inhalte (Propaganda sowie Pornografie- oder Gewaltvideos)
* Wem gehören die Übertragenen Inhalte
#### self hosted vs. cloud vs. serverless



#### eigene Erfahrungen und Empfehlungen
* Nachhaltigkeit
    * Offener Standard: Es wird ein offener Standard verwendet, der frei implementiert werden kann.
    * Open Source Software: Die Software steht im Quellcode zur Verfügung und kann von Dritten eingesehen, geändert und weiterverwendet werden.
        * Heißt nicht mehr Sicherheit
        * Wenn die Entwickler das Projekt ablegen können andere übernehmen
    * Dezentrale Architektur: Die Software ist nicht von einem einzigen, zentralen Anbieter abhängig.

#### extra
* Mobile Messenger: Nichts für Kinder? (Laut der europäischen Datenschutzgrundverordnung (DSGVO) dürfen Onlineanbieter personenbezogene Daten von Kindern unter 16 Jahren nicht ohne Einwilligung ihrer Eltern verarbeitet werden. Das gilt auch für Messenger. Installation und Anmeldung der Angebote sind also eigentlich Elternsache. In der Umsetzung wird das durch die meisten Anbieter jedoch nicht kontrolliert. Oft genügt die Eingabe des Geburtsdatums oder eine einfache Bestätigung zur Datenverarbeitung - bei Angaben können also leicht von Kindern allein gemacht werden.)

* WhatsApp-Sprachnachricht

* [Netzpolitikartikel über Messenger](https://netzpolitik.org/tag/messenger/)

* non-verbale-Kommunikation aka warum gibt es die bunten bildchen eigentlich
    * [emojis in der Forschung - wie emojis unsere Kommunikation ergaenzen](https://www.stuttgarter-nachrichten.de/inhalt.emojis-in-der-forschung-wie-emojis-unsere-kommunikation-ergaenzen.61649867-1f7d-4c30-8c5f-4a6e38e00f79.html)
    * [Die-Emoji-Falle](https://www.n-joy.de/multimedia/Die-Emoji-Falle,emoji672.html)

*  [Sieben Regeln für mehr Social-Media-Gelassenheit](https://gegen-die-panik.de)  / [Artikel Süddeutsche](https://www.sueddeutsche.de/digital/nach-dem-anschlag-von-muenster-gegen-die-panik-1.3935620)


#### Veranstaltungshinweise
* Chaos Communication Congress auch diese Jahr wieder in Leipzig
    * [36C3: Resource Exhaustion.](https://www.ccc.de/en/updates/2019/36c3-in-leipzig)
* [jungend hackt Halle 8.-10. November 2019](https://jugendhackt.org/events/halle/)

<script>
  podlovePlayer('#example', '/blog/sfdvw85.json');
</script>
