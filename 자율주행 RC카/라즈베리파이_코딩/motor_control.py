import RPi.GPIO as GPIO

dcMotors = [22,13,20,12]
wheels=[]
MOT_FREQ=1000.0

SPEED_MIN = 10
SPEED_MAX = 100


forward = [True,False]
backward = [False,True]
STOP = [False,False]

SPEED_MAX_FB = SPEED_MAX - SPEED_MIN

def initMotor():
    for i in range(0,len(dcMotors),2):
        GPIO.setup(dcMotors[i], GPIO.OUT)
        GPIO.output(dcMotors[i], False)
        
        GPIO.setup(dcMotors[i+1], GPIO.OUT)
        wheel = GPIO.PWM(dcMotors[i+1], MOT_FREQ)
        wheel.start(0.0)
        wheels.append(wheel)
        
def goForward(spd):
    if spd<0 : spd=0
    spd += SPEED_MIN
    if spd>SPEED_MAX : spd=SPEED_MAX
    
    for i in range(0,len(dcMotors),2):
        GPIO.output(dcMotors[i], forward[i%2])
        wheels[i//2].ChangeDutyCycle(SPEED_MAX-spd)
        
def stopMotor():
    for i in range(0, len(dcMotors), 2):
        GPIO.output(dcMotors[i], STOP[i%2])
        wheels[i//2].ChangeDutyCycle(0.0)
        
def goBackward(spd):
    if spd<0 : spd=0
    spd += SPEED_MIN
    if spd>SPEED_MAX : spd=SPEED_MAX
    
    for i in range(0,len(dcMotors),2):
        GPIO.output(dcMotors[i], backward[i%2])
        wheels[i//2].ChangeDutyCycle(spd)
        
def turnLeft(spd):
    GPIO.setmode(GPIO.BCM)
    if spd<0 : spd=0
    spd += SPEED_MIN
    if spd>SPEED_MAX : spd=SPEED_MAX
    
    for i in range(0,len(dcMotors)//2,2):
        GPIO.output(dcMotors[i], backward[i%2])
        wheels[i//2].ChangeDutyCycle(spd)
    
    for i in range(len(dcMotors)//2,len(dcMotors),2):
        GPIO.output(dcMotors[i], forward[i%2])
        wheels[i//2].ChangeDutyCycle(SPEED_MAX-spd)
        
def turnRight(spd):
    GPIO.setmode(GPIO.BCM)
    if spd<0 : spd=0
    spd += SPEED_MIN
    if spd>SPEED_MAX : spd=SPEED_MAX
    
    for i in range(0,len(dcMotors)//2,2):
        GPIO.output(dcMotors[i], forward[i%2])
        wheels[i//2].ChangeDutyCycle(SPEED_MAX-spd)
    
    for i in range(len(dcMotors)//2,len(dcMotors),2):
        GPIO.output(dcMotors[i], backward[i%2])
        wheels[i//2].ChangeDutyCycle(spd)
        
def exitMotor():
    for i in range(0,len(dcMotors)//2,2):
        wheels[i//2].stop()
 