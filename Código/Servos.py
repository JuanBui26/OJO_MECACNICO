from machine import Pin, ADC, PWM
import utime
from time import sleep

# Initialize potentiometers
pot1 = ADC(Pin(14))
pot2 = ADC(Pin(12))

"""while True:
    #print(pot1.read())
    print(pot1.read_u16()) #[0-65535]
    sleep(1)
# pot2 = ADC(Pin(12))
"""

servo1 = PWM(Pin(18), freq=50)
servo2 = PWM(Pin(32), freq=50)
servo3 = PWM(Pin(33), freq=50)
servo4 = PWM(Pin(25), freq=50)

m_adc = 12/4369

def angleFromAdc(adc):
    #print(adc.read_u16(), m_adc)
    return m_adc*adc.read_u16() 

m = 100/3
b = 1800

def posicion(servo, angle):
    print(angle)
    servo.duty_u16(int(m*angle + b))

while True:
    posicion(servo1, angleFromAdc(pot1))
    posicion(servo2, angleFromAdc(pot1))
    posicion(servo3, angleFromAdc(pot2))
    posicion(servo4, angleFromAdc(pot2))
    sleep(0.1)
