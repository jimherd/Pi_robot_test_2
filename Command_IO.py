# This Python file uses the following encoding: utf-8

import serial
import array as arr

from enum import Enum, IntEnum
from itertools import repeat

from PySide6.QtCore import QObject, Slot, Signal

#from globals import This_platform

import Globals

class Joints(IntEnum):

    LEFT_EYE_RIGHT_LEFT  = 1
    LEFT_EYE_UP_DOWN     = 2
    LEFT_EYE_LID         = 3
    LEFT_EYE_BROW        = 4
    RIGHT_EYE_LEFT_RIGHT = 5
    RIGHT_EYE_UP_DOWN    = 6
    RIGHT_EYE_LID        = 7
    RIGHT_EYE_BROW       = 8


class ErrorCode(IntEnum):
    OK                              = 0
    LETTER_ERROR                    = -100
    DOT_ERROR                       = -101
    PLUSMINUS_ERROR                 = -102
    BAD_COMMAND                     = -103
    BAD_PORT_NUMBER                 = -104
    BAD_NOS_PARAMETERS              = -105
    BAD_BASE_PARAMETER              = -106
    PARAMETER_OUTWITH_LIMITS        = -107
    BAD_SERVO_COMMAND               = -108
    STEPPER_CALIBRATE_FAIL          = -109
    BAD_STEPPER_COMMAND             = -110
    BAD_STEP_VALUE                  = -111
    MOVE_ON_UNCALIBRATED_MOTOR      = -112
    EXISTING_FAULT_WITH_MOTOR       = -113
    SM_MOVE_TOO_SMALL               = -114
    LIMIT_SWITCH_ERROR              = -115
    UNKNOWN_STEPPER_MOTOR_STATE     = -116
    STEPPER_BUSY                    = -117
    SERVO_BUSY                      = -118

    BAD_COMPORT_OPEN                = -200     # PC errors
    UNKNOWN_COM_PORT                = -201
    BAD_COMPORT_READ                = -202
    BAD_COMPORT_WRITE               = -203
    NULL_EMPTY_STRING               = -204
    BAD_COMPORT_CLOSE               = -205

class Modes(IntEnum):
    MODE_U = 0
    MODE_I = 1
    MODE_R = 2
    MODE_S = 3

class ServoCommands(IntEnum):
    ABS_MOVE           = 0
    ABS_MOVE_SYNC      = 1
    SPEED_MOVE         = 2
    SPEED_MOVE_SYNC    = 3
    RUN_SYNC_MOVES     = 4
    STOP               = 5
    STOP_ALL           = 6

class StepperCommands(IntEnum):
    REL_MOVE           = 0
    ABS_MOVE           = 1
    REL_MOVE_SYNC      = 2
    ABS_MOVE_SYNC      = 3
    CALIBRATE          = 4

class Command_IO(QObject):
    def __init__(self, parent):
        super(Command_IO, self).__init__
        self.parent = parent
        self.reply_string = ""

        self.MAX_COMMAND_PARAMETERS = 10
        self.READ_TIMEOUT = 4  # seconds
        self.MAX_COMMAND_STRING_LENGTH = 100
        self.MAX_REPLY_STRING_LENGTH = 100

        self.ser = serial.Serial()

        self.argc = 0
        self.int_parameter   = arr.array('i', repeat(0, self.MAX_COMMAND_PARAMETERS))
        self.float_parameter = arr.array('f', repeat(0, self.MAX_COMMAND_PARAMETERS))
        self.param_type      = arr.array('i', repeat(0, self.MAX_COMMAND_PARAMETERS))

    def open_port(self, MainWindow, port, baud_rate):
        self.ser.baudrate = baud_rate
        self.ser.timeout = self.READ_TIMEOUT
        self.ser.port = port
        try:
            self.ser.open()
        except:
            return ErrorCode.BAD_COMPORT_OPEN
        return ErrorCode.OK

    def close_port(self):
        self.ser.close()
        return ErrorCode.OK

    def send_command(self, send_string):
        if(self.ser.isOpen() == False):
            return ErrorCode.BAD_COMPORT_WRITE
        self.ser.write(str.encode(send_string)) # convert to bytes
        return ErrorCode.OK

    def get_reply(self):
        try:
            self.reply_string = self.ser.read_until(b'\n')
            print("Reply received")
            return ErrorCode.OK
        except:
            return ErrorCode.BAD_COMPORT_READ

    def do_command(self, cmd_string, first_int):
        status = self.send_command(cmd_string)
        if(status != ErrorCode.OK):
            return status
        status = self.get_reply()
        if(status != ErrorCode.OK):
            return status
        status = self.Parse_string(cmd_string)
        if(status != ErrorCode.OK):
            return status

    def Parse_string(self, string_data):
        for index in range(self.MAX_COMMAND_PARAMETERS):
            self.int_parameter[index] = 0
            self.float_parameter[index] = 0.0
            self.param_type[index] = int(Modes.MODE_U)
            self.argc = 0
        self.string_parameters = string_data.split()
        self.argc = len(self.string_parameters)

        for index in range(self.argc):
            if not isinstance(self.string_parameters[index], str):
                return None
            if self.string_parameters[index].isdigit():
                self.int_parameter[index] = int(self.string_parameters[index])
                self.param_type[index] = Modes.MODE_I
            try:
                self.float_parameter[index] = float(self.string_parameters[index])
                self.param_type[index] = Modes.MODE_R
            except ValueError:
                self.param_type[index] = Modes.MODE_S

        return ErrorCode.OK

