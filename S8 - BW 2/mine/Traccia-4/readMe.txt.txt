PRE BUILD WEEK 2

0 - configurazione di rete dispositivi attaccante e target:	Attaccante 192.168.50.100, Target 192.168.50.150

1 - Scansione nella rete per rilevare il target: sudoo arp-scan -l

2 - Scansione con nmpa identifica la porta per poi rilevare il servizio in uso. Porta: 445/tcp 
	Scansione base con nessus, per capire la vulnerabilità che viene sfruttata: Samba Badlock Vulnerability, dal exploit suggerito: usermap_script.
	(vedere: nessus_scan_short.html && nessus_scan_detailed.html && nmpa_scan.txt)

3 - dopo la ricerca su msfconsole tramite il comando "search" si seleziona con "use" exploit/multi/samba/usermap_script.
	Con comando "options" si visiona le configurazioni, con "set" si impostano le varie variabili del exploit, compreso il payload. Con "run" viene lanciato l'Exploit,
	si apre una sessione reverse_netcat dalla quale si accende una shell sul dispositivo target con credenziali root.

4 - con il comando "ifconfig" ottengo la configurazione di rete del sistema target.