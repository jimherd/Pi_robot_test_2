## Updated "Pi the Robot" animatronic test software
----

Add RP2040 Pico board to manage head hardware

* Head servo motors
* Neck stepper motor

### New hardware

* Servo motor control
    - 16 channel Adafruit PCA9685 board
* Stepper motor control
    - TMC2208 stepper motor board
    
### Notes

* Moved from Visual Studio to Qt Creator to allow cross platform development

### Tools

* Software
    - QtCreator 11.0
    - Qt 6.4.3
    - Git for Windows
    - Visual Studio Code
    - GCC Arm compiler
    - Pico SDK
    - FreeRTOS 
 
* Hardware 
    * RP2040 microprocessor to control low level servos/stepper motors
    * PicoProbe debug probe : CMSIS version
    * Windows 10 laptop for software development


Jim Herd September 2023
