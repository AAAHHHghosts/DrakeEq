# milky way constants
RAD = 500
DIAM = 2 * RAD
CENTER_RAD = 13


# time & clock constants
SIM_SPEED = 100.0


# The Drake Equation
def drake_eq(R, fp, ne, fl, fi, fc, L):
    return R * fp * ne * fl * fi * fc * L


# star formation rate, the rate at
# which stars form in our galaxy
# expressed as stars born per century
R_low = 500
R_high = 1000

# planetary fraction,
# the percent of stars with planets
fp_low = 0.10
fp_high = 0.20

# the number of planets that can
# potentially host life, per star
# that has planets
ne_low = 1
ne_high = 2

# the fraction of the above planets that
# actually do develop life of any kind
fl_low = 0.5
fl_high = 1

# the fraction of the above planets that
# develop intelligent life
fi_low = 0.05
fi_high = 0.1

# the fraction of the above life that
# develops the capacity for interstellar
# communication
fc_low = 0.05
fc_high = 0.1

# the number of centuries that such
# communicative civilizations are active
L_low = 16
L_high = 100

# low and high estimate for N, the number of
# currently active, communicative civilizations
# in our galaxy
N_low = drake_eq(R_low, fp_low, ne_low, fl_low, fi_low, fc_low, L_low)
N_high = drake_eq(R_high, fp_high, ne_high, fl_high, fi_high, fc_high, L_high)


# calculate birth rate for civs
civ_br_low = N_low/L_low
civ_br_high = N_high/L_high

print(N_low, civ_br_low)
print(N_high, civ_br_high)