import  RPi.GPIO as GPIO
import time

PWMA = 18
AIN1   =  22
AIN2   =  27

PWMB = 23
BIN1   = 25
BIN2  =  24

T_SensorRight = 26
T_SensorLeft  = 13

TRIG = 20
ECHO = 21

def setup():
    GPIO.setwarnings(False) 
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(AIN2,GPIO.OUT)
    GPIO.setup(AIN1,GPIO.OUT)
    GPIO.setup(PWMA,GPIO.OUT)
    GPIO.setup(BIN1,GPIO.OUT)
    GPIO.setup(BIN2,GPIO.OUT)
    GPIO.setup(PWMB,GPIO.OUT)
    GPIO.setup(T_SensorRight,GPIO.IN)
    GPIO.setup(T_SensorLeft,GPIO.IN)
    GPIO.setup(ECHO,GPIO.IN)
    GPIO.setup(TRIG,GPIO.OUT)
    
def up(speed,time):
        GPIO.output(AIN2,False)#AIN2
        GPIO.output(AIN1,True) #AIN1
        GPIO.output(BIN2,False)#BIN2
        GPIO.output(BIN1,True) #BIN1
        L_Motor= GPIO.PWM(PWMA,100)
        L_Motor.start(speed)
        R_Motor = GPIO.PWM(PWMB,100)
        R_Motor.start(speed)
        time.sleep(t_time)
        
def stop():
        GPIO.output(AIN2,False)#AIN2
        GPIO.output(AIN1,False) #AIN1
        GPIO.output(BIN2,False)#BIN2
        GPIO.output(BIN1,False) #BIN1
        L_Motor= GPIO.PWM(PWMA,100)
        L_Motor.start(speed)
        R_Motor = GPIO.PWM(PWMB,100)
        R_Motor.start(speed)
        
def down(speed,time):
        GPIO.output(AIN2,True)#AIN2
        GPIO.output(AIN1,False) #AIN1
        GPIO.output(BIN2,True)#BIN2
        GPIO.output(BIN1,False) #BIN1
        L_Motor= GPIO.PWM(PWMA,100)
        L_Motor.start(speed)
        R_Motor = GPIO.PWM(PWMB,100)
        R_Motor.start(speed)
        time.sleep(t_time)

def left(speed,time):
        GPIO.output(AIN2,True)#AIN2
        GPIO.output(AIN1,False) #AIN1
        GPIO.output(BIN2,False)#BIN2
        GPIO.output(BIN1,True) #BIN1
        L_Motor= GPIO.PWM(PWMA,100)
        L_Motor.start(speed)
        R_Motor = GPIO.PWM(PWMB,100)
        R_Motor.start(speed)
        time.sleep(t_time)

def right(speed,time):
        GPIO.output(AIN2,False)#AIN2
        GPIO.output(AIN1,True) #AIN1
        GPIO.output(BIN2,True)#BIN2
        GPIO.output(BIN1,False) #BIN1
        L_Motor= GPIO.PWM(PWMA,100)
        L_Motor.start(speed)
        R_Motor = GPIO.PWM(PWMB,100)
        R_Motor.start(speed)
        time.sleep(t_time)
def distance():#这里返回距离
	GPIO.output(TRIG, 0)
	time.sleep(0.000002)

	GPIO.output(TRIG, 1)
	time.sleep(0.00001)
	GPIO.output(TRIG, 0)

	
	while GPIO.input(ECHO) == 0:
		a = 0
	time1 = time.time()
	while GPIO.input(ECHO) == 1:
		a = 1
	time2 = time.time()

	during = time2 - time1
	return during * 340 / 2 * 100

def speed():
    distance1=distance()
    time1=time.time()
    up(50,2)
    distance2=distance()
    time2=time.time()
    return (distance1-distance2)/(time2-time1)
       
