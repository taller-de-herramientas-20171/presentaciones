#!/usr/bin/python3

import math

M_CHICO = 47
M_GRANDE = 67
p = 1.038
c = 3.7
K = 5.4e-3
Tw = 100
Ty = 70
To_1 = 20
To_2 = 4

#################################
# Primer tiempo de cocción para #
# el huevo grande               #
#################################

t = (((M_GRANDE ** (2 / 3.0)) * c * (p ** (1 / 3.0))) /
     (K * (math.pi ** 2)
      * ((4 * math.pi) / 3) ** (2 / 3))) * math.log(0.76 * ((To_1 - Tw) / (Ty - Tw)))

print("El tiempo de cocción para el huevo grande fue de {} minutos y {} segundos, temp inicial {}"
      .format(int(t / 60), int(t % 60), To_1))


##################################
# Segundo tiempo de cocción para #
# el huevo grande                #
##################################

t1 = (((M_GRANDE ** (2 / 3.0)) * c * (p ** (1 / 3.0))) /
      (K * (math.pi ** 2)
       * ((4 * math.pi) / 3) ** (2 / 3))) * math.log(0.76 * ((To_2 - Tw) / (Ty - Tw)))

print("El tiempo de cocción para el huevo grande fue de {} minutos y {} segundos, temp inicial {}"
      .format(int(t1 / 60), int(t1 % 60), To_2))

#################################
# Primer tiempo de cocción para #
# el huevo chico                #
#################################

t2 = (((M_CHICO ** (2 / 3.0)) * c * (p ** (1 / 3.0))) / (K * (math.pi ** 2)
                                                         * ((4 * math.pi) / 3) ** (2 / 3))) * math.log(0.76 * ((To_1 - Tw) / (Ty - Tw)))
print("El tiempo de cocción para el huevo chico fue de {} minutos y {} segundos, temp inicial {}"
      .format(int(t2 / 60), int(t2 % 60), To_1))

##################################
# Segundo tiempo de cocción para #
# el huevo chico                 #
##################################

t3 = (((M_CHICO ** (2 / 3.0)) * c * (p ** (1 / 3.0))) / (K * (math.pi ** 2)
                                                         * ((4 * math.pi) / 3) ** (2 / 3))) * math.log(0.76 * ((To_2 - Tw) / (Ty - Tw)))
print("El tiempo de cocción para el huevo chico fue de {} minutos y {} segundos, temp inicial {}"
      .format(int(t3 / 60), int(t3 % 60), To_2))
