ESERCITAZIONE S7 L3

0 - ricerca della macchina vittima e scansione per vulnerabilita

1 - avvio msfconsole, ricerca e configurazione del exploit postgres_payload

2 - sessione precedente va in background, si usa l'exploit local-exploit-suggestor per trovare possibili
	exploit utili per la escalation dei privilegi, si configura e poi avvia.

3 - si fa un test con exploit su_login, FALLISCE (ERRORE: payload meterpèreter reverse_tcp 64bit)

4 - si fa un test con exploit setuid_nmap, FALLISCE (ERRORE: payload meterpèreter reverse_tcp 64bit)

5 - si fa un test con exploit netfilter_priv_esc_ipv4, FALLISCE (ERRORE: payload meterpèreter 
	reverse_tcp x64)

6 - si fa un test con exploit glibc_ld_audit_dso_load_priv_esc, FUNZIONA (mi sono deciso a
	mettere meterpreter reverse_tcp x86) come si può notare dall'image n.6 ho ottenuto
	accesso privilegiato  root

7 - la sessione va in background, procedo con la creazione in locale di una backdoor con msfvenom:
	'snake.elf'
	
8 - upload sulla macchina vittima della backdoor in: '/usr/games/'

9 - creo la persistenza della backdoor sul sistema della vittima

10 - avvio della backdoor e collegamento ad essa

-----------------

note: ottimizzazione della backdoor con autorun