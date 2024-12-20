ESERCITAZIONE S7 L5 - PROGETTO

0 - configurazione di rete dell'attaccante e del target

1 - avvio msfconsole, scansione della macchina vittima (192.168.11.112) 

2 - ricerca e configurazione exploit=java_rmi_server con  payload=java/meterpreter/reverse_tcp (ho fatto variu tentativi 	falliti, con exploit differenti ma sempre riconducibili a al java_rmi, e con payload differenti [payload generico, 	payload meterpreter/reverse_tcp, payload linux x86])

3 - run exploit, si ottiene accesso alla macchina target, creo un file sul dispositivo target "network_config", ci scrivo dentro 	le configurazioni di rete e la tabella di routing, poi lo scarico sulla macchina attaccante.
