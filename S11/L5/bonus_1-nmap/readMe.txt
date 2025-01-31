ESERCITAZIONE S11 L5

NMAP

Eseguo l'esercizio su VM CyberOps Workstation

Nmap è uno strumento per l'analisi della rete e la scansione di porte e vulnerabilità.
Permette di identificare host attivi, servizi in esecuzione e sistemi operativi di una rete. È utilizzato per la scansione delle porte, audit di sicurezza, gestione dell’inventario di rete e rilevamento di vulnerabilità.
0 - con "man nmap" si ottiene la guida, esempi e riferimenti del tool.
Si può navigare nel documento per cercare info e metodi di utilizzo con: / + la parola ricercata.
la prima istanza trovata è "Example 1" che presenta il comando "nmap -A -T4 scanme.nmap.org"

1 - eseguendo "nmap -A -T4 localhost" si fa una scansione del localhost, ottengo le seguenti informazioni:
	-A: rilevamento avanzato: scansione di porte, rilevamento del OS, rilevamento dei servizi e loro versioni, e vengono utilizzati script.
	-T4: imposta la velocità della scansione su "aggressive", aumentando la rapidità ma anche la possibilità di essere rilevati.
	-localhost: l'host da analizzare (127.0.0.1).
	Output:
	- Host attivo: 127.0.0.1 .
	- Porte aperte:
		- 21/tcp (FTP - vsftpd 2.0.8 o successivo) supporta l'accesso anonimo. Mostra informazioni di stato, inclusa la versione del server (vsFTPd 3.0.3).
		- 22/tcp (SSH - OpenSSH 7.7): elenca le chiavi host supportate (RSA, ECDSA, ED25519).
	Informazioni generali: nome host rilevato è "Welcome", sono stati esaminati 1 host e 1000 porte, con 998 porte chiuse.

  - eseguendo "ip address" le informazioni sul mio dispositivo, di preciso l'indirizzo ip, la rete alla quale appartiene, la subnet mask.

2 - eseguendo "nmap -A -T4 10.0.2.0/24" si fa una scansione dell'intera rete per rilevare gli host della rete:
	-A: rilevamento avanzato: scansione di porte, rilevamento del OS, rilevamento dei servizi e loro versioni, e vengono utilizzati script.
	-T4: imposta la velocità della scansione su "aggressive", aumentando la rapidità ma anche la possibilità di essere rilevati.
	-10.0.2.0/24: rete da scansionare.
	Output:
	- Host attivo: 10.0.2.15 .
	- Porte aperte:
		- 21/tcp (FTP - vsftpd 2.0.8 o successivo) supporta l'accesso anonimo. Mostra informazioni di stato, inclusa la versione del server (vsFTPd 3.0.3).
		- 22/tcp (SSH - OpenSSH 7.7): elenca le chiavi host supportate (RSA, ECDSA, ED25519).
	Informazioni generali: nome host rilevato è "Welcome", sono stati esaminati 1 host e 1000 porte, con 998 porte chiuse.
	
  - eseguendo "nmap -A -T4 scanme.nmap.org" si fa una scansione da remoto del sito:
	[...]
	-scanme.nmap.org
	

