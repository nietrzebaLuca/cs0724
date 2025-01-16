ESERCITAZIONE S9 L4

Creazione e Gestione delle Regole per i File di Log della Sicurezza in Windows

1 - Premi "Win+R" poi digita regedit una volta aperto l'Edito di Registro di Sistema si cerca la directory: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System. Qui si crea una nuova regola "D_WORD" (32 o 64 bit), nominata "AuditLogonEvents", si imposta il valore esadecimale su 1, salva e RIAVVIA IL SISTEMA.

2 - Al riavvio premere "Win+R" digitare "eventvwr", andare in "Registri di Windows\Sicurezza", si verifica che al login dopo il riavvio si hanno nuovi eventi: 4624 Accesso, 4627 Appartenenza a gruppi, 4672 Accesso Speciale