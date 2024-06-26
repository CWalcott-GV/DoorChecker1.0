# DoorChecker1.0
circuitPython utilization of Adafruit CircuitPlayground and Arduino Uno microcontrollers to create a door checking ultrasonic sensor device.

This release is a 1.0 initial upload for class credit. However, logic can be added to mitigate issues related to:

    a. device only responds when password is entered when entering through "Bluefruit Connect" app.
    b. device bluetooth signal weak. (directional? not sure)
    c. device not weatherproofed or no standard mounting hardware in garage setting.
    d. two power sources instead of one.

SETUP: I used alligator clips and heatshrunk-twisted onto long 22ga wire snippets to solid copper breadboard-compatible pins to attach my two micro
controllers to the mainboard. I mounted the ultrasonic sensor straight to the breadboard for ease of use.

Picture context. I mounted both boards to the wall of my garage with brass cabinet screws (Arduino Uno has through-holes for mounting purposes) 
Adafruit CircuitPlayground Express is mounted via a GND port.

Adafruit CircuitPlayground can be found here (https://learn.adafruit.com/adafruit-circuit-playground-express)
Arduino UNo can be found here (https://store.arduino.cc/products/arduino-uno-rev3)
Ultrasonic Sensor can be found here (https://www.sparkfun.com/products/15569)

(fritzing picture)

Known issues: 
    1. device is at a 40 degree angle to the garage door, so the trigger-echo signal bounces and does not return expected values. 

