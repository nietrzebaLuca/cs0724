ESERCITAZIONE S9 L5

Analisi file Cattura_U3_W1_L3.pcapng

Legenda:
	Server = 192.168.200.150
	Terminale = 192.168.200.100

T1:	Riga 1 - Annuncio Host da parte del Server:  METASPLOITABLE, Workstation, Server, Print Queue Server, Xenix Server, NT Workstation, NT Server, Potential Browser.
	Righe 2-7 - Serie di Connessioni TCP: Terminale cerca di stabilire connessione con il Server, risponde con pacchetti SYN_ACK da porta 80, invece con RST-ACK da porta 443.
	Righe 8-11 - Pacchetti ARP Richiesta/Risposta pere risoluzione indirizzi ip in mac.
	Righe 12-20 - Terminale cerca di connettersi alle porte 22/ssh, 21/ftp, IMAPS/993; Server nega connessione con RST.
	Righe 24-34 - Terminale invia ACK per completare handshake ma viene interrotto dal Server con RST-ACK. Server sta rifiutando le connessioni.

T2:	Righe 35-64 - Pattern simile al precedente, Terminale ricerca connessioni con varie porte del Server, ottiene per lo più risposte RST-ACK (negativa) ed alcune SYN-ACK (positive) suggerendo una
	connessione temporanea.
	Righe 65-68 - Server risponde con pacchetti ACK per confermare la ricezione dei pacchetti ricevuti dal Terminale che non danno una connessione stabilita.

T3:	Il pattern si ripete, si vedono vari tentativi di connessione del Terminale al Server tutti con esito negativo. Ora si ha ragione di pensare che il Server è soggetto di un attacco o di una scansione di porte.
T4/T5/T6:	Ancora che si ripete il noto pattern.
	Quindi credo si possa concludere con:

	Server è vittima di:
	- o una scansione sulle porte da parte del Terminale; 
	- oppure un attacco DoS, alta frequenza di invio di pacchetti SYN fa pensare ad un attacco SYN Flood [Terminale (mittente) invia pacchetti in massa per esaurire le risorse della Server (destinatario)].

	E grazie alle risposte del Server si può supporre che questo abbia:
	- o un firewall attivo;
	- o un sistema di protezione attivo che blocca le connessioni;
	- o una configurazione per rifiutare le connessioni;
	- oppure delle politiche di sicurezza.

	
	