ESERCITAZIONE S9 L3

Valutazione Quantitativa Disastri

Formule --- ALE = SLE * ARO --- SLE = AV * EF
ALE = Annualized Loss Expectancy, SLE = Single Loss Expectancy, ARO = Annualized Rate Occurance
AV = Asset Value, EF = Exposure Factor

Dati:
	Asset		ES = Edificio Secondario, DC = Data Center, EP = Edificio Primario.
	Valore $		150 000			100 000			350 000

	Evento		Terremoto	Incendio	Inondazione
	ARO 		1 in 30 anni	1 in 20 anni	1 in 50 anni
			1/30		1/20		1/50

	Fattore Esposizione	Terremoto	Incendio	Inondazione
		EP		80%		60%		55%
		ES		80%		50%		40%
		DC		95%		60%		35%	


Risoluzione:

- inondazione asset <ES>:
	SLE = 150 000 * 0,40 = 60 000 €
	ALE = SLE x 1/50 = 1200 €

- terremoto asset <DC>:
	SLE = 100 000 * 0,95 = 95 000 €
	ALE = SLE x 1/30 = 3166,67 €

- incendio asset <EP>:
	SLE = 350 000 * 0,60 = 210 000 €
	ALE = SLE x 1/20 = 10 500 €

- incendio asset <ES>:
	SLE = 150 000 * 0,5 = 75 000 €
	ALE = SLE x 1/20 = 3750 €

- inondazione asset <EP>:
	SLE = 350 000 * 0,55 = 192 500 €
	ALE = SLE x 1/50 = 3850 €

- terremoto asset <EP>:
	SLE = 350 000 * 0,80 = 280 000 €
	ALE = SLE x 1/30 = 9333,34 €