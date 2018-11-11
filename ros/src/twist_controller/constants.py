# The DBW system on Carla expects messages at this frequency, 
# and will disengage (reverting control back to the driver) 
# if control messages are published at less than 10hz. 
DBW_UPDATE_FREQ = 50 

GAS_DENSITY = 2.858
ONE_MPH = 0.44704
CLOSE_TO_ZERO_SPEED = 0.15 # Consider this 0 speed
THROTTLE_MIN = 0
THROTTLE_MAX = 1

THROTTLE_KP = 0.74181 #0.25
THROTTLE_KI = 0.08889 #0.0025
THROTTLE_KD = 0.00000 #0.05

BRAKE_STATIONARY_FORCE = 700 # Nm to keep car stationary

MIN_NUM = float('-inf')
MAX_NUM = float('inf')