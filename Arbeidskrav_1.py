# -*- coding: utf-8 -*-
"""
Arbeidskrav 1

Mostafa Benmoussa

13.02.2022
"""

Antallkm = 10000 
#forsikring per år
ForsikringE = 5000 #For El-bil
ForsikringB = 7500 # For bensinbil
AAR = 365  # {antall dager i året}
Trafikk = 8.38*AAR # Trafikkforsikringsavgift for begge bilene
DrivstoffE = 0.2*2*Antallkm  # {elbil}
DrivstoffB = 1*Antallkm  # {bensinbil}
BomE = 0.1*Antallkm # For El-bil
BomB = 0.3*Antallkm # For bensinbil
Elbil = ForsikringE + Trafikk + DrivstoffE + BomE #Årlige kostnader El-bil
Bensinbil = ForsikringB + Trafikk + DrivstoffB + BomB #Årlige kostnader Bensinbil

print('Elbil kostnader per år')
print('Forsikring', ForsikringE)
print('Trafikkforsikringsavgift', Trafikk)
print('Strømkostnader', DrivstoffE)
print('Bomavgift per år', BomE)
print('###################################')
print('###################################')
print('Bensinbil kostnader per år')
print('Forsikring per år bensinbil', ForsikringB)
print('Trafikkforsikringsavgift bensinbil per år', Trafikk)
print('Drivstoffkostnader ved 10000 km per år', DrivstoffB)
print('Bomavgift per år ved 10000 km for bensinbil', BomB)
print('###################################')
print('Årlige kostnader for elbil er')
print(Elbil )
print('###################################')
print('Ålige kostnader for bensinbil er')
print(Bensinbil )
print('###################################')
print('Den årlige kostnadsdifferansen er')
print(Bensinbil - Elbil)

