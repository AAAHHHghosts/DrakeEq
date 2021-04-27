# milky way constants
RAD = 500
DIAM = 2 * RAD
CENTER_RAD = 13

# display constants
BUFFER = 500

# time & clock constants
SIM_SPEED = 100.0

# toggle high and low estimates.
# 1 for optimistic case, and 0
# for pessimistic case
SIM_CASE = 0


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
fp_low = 0.05
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
fi_low = 0.01
fi_high = 0.05

# the fraction of the above life that
# develops the capacity for interstellar
# communication
fc_low = 0.1
fc_high = 0.25

# the number of centuries that such
# communicative civilizations are active
L_low = 4
L_high = 10

# low and high estimate for N, the number of
# currently active, communicative civilizations
# in our galaxy
N_low = drake_eq(R_low, fp_low, ne_low, fl_low, fi_low, fc_low, L_low)
N_high = drake_eq(R_high, fp_high, ne_high, fl_high, fi_high, fc_high, L_high)

# Calculate death rate for civs.
# Because we are assuming a steady
# population, the death rate is equal
# to the birth rate
civ_br_low = N_low / L_low
civ_br_high = N_high / L_high

# set global values based on high or low estimate
if SIM_CASE == 1:
    avg_civ_count = N_high
    avg_num_births = civ_br_high
    avg_lifespan = L_high
else:
    avg_civ_count = N_low
    avg_num_births = civ_br_low
    avg_lifespan = L_low
