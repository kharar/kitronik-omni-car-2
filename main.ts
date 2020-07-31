bluetooth.onBluetoothConnected(function () {
    basic.showLeds(`
        . . # # .
        # . # . #
        . # # # .
        # . # . #
        . . # # .
        `)
})
bluetooth.onBluetoothDisconnected(function () {
    basic.showIcon(IconNames.No)
})
function SetMotors () {
    FR = DirY + DirX + RotZ
    FL = DirY - DirX - RotZ
    BR = DirY - DirX + RotZ
    BL = DirY + DirX - RotZ
    robotbit.GeekServo(robotbit.Servos.S1, FR + 90)
    robotbit.GeekServo(robotbit.Servos.S2, 90 - FL)
    robotbit.GeekServo(robotbit.Servos.S3, BR + 90)
    robotbit.GeekServo(robotbit.Servos.S4, 90 - BL)
    basic.pause(50)
}
control.onEvent(EventBusSource.MES_DPAD_CONTROLLER_ID, EventBusValue.MICROBIT_EVT_ANY, function () {
    if (control.eventValue() == EventBusValue.MES_DPAD_BUTTON_1_DOWN) {
        DirY = Speed
    } else if (control.eventValue() == EventBusValue.MES_DPAD_BUTTON_1_UP) {
    	
    } else if (control.eventValue() == EventBusValue.MES_DPAD_BUTTON_2_DOWN) {
        DirY = 0 - Speed
    } else if (control.eventValue() == EventBusValue.MES_DPAD_BUTTON_2_UP) {
    	
    } else if (control.eventValue() == EventBusValue.MES_DPAD_BUTTON_3_DOWN) {
        DirX = 0 - Speed
    } else if (control.eventValue() == EventBusValue.MES_DPAD_BUTTON_3_UP) {
    	
    } else if (control.eventValue() == EventBusValue.MES_DPAD_BUTTON_4_DOWN) {
        DirX = Speed
    } else if (control.eventValue() == EventBusValue.MES_DPAD_BUTTON_4_UP) {
    	
    } else if (control.eventValue() == EventBusValue.MES_DPAD_BUTTON_A_DOWN) {
        DirX = 0
        DirY = 0
        RotZ = 0
        basic.showArrow(ArrowNames.North)
    } else if (control.eventValue() == EventBusValue.MES_DPAD_BUTTON_A_UP) {
        basic.clearScreen()
    } else if (control.eventValue() == EventBusValue.MES_DPAD_BUTTON_B_DOWN) {
        DirX = 0
        DirY = 0
        RotZ = 0
        basic.showArrow(ArrowNames.South)
    } else if (control.eventValue() == EventBusValue.MES_DPAD_BUTTON_B_UP) {
        basic.clearScreen()
    } else if (control.eventValue() == EventBusValue.MES_DPAD_BUTTON_C_DOWN) {
        if (DirX != 0 && DirY != 0) {
        	
        } else {
            RotZ = 0 - Speed
        }
    } else if (control.eventValue() == EventBusValue.MES_DPAD_BUTTON_C_UP) {
    	
    } else if (control.eventValue() == EventBusValue.MES_DPAD_BUTTON_D_DOWN) {
        if (DirX != 0 && DirY != 0) {
        	
        } else {
            RotZ = Speed
        }
    } else if (control.eventValue() == EventBusValue.MES_DPAD_BUTTON_D_UP) {
    	
    } else {
    	
    }
})
let BL = 0
let BR = 0
let FL = 0
let FR = 0
let RotZ = 0
let DirX = 0
let DirY = 0
let Speed = 0
Speed = 60
basic.showLeds(`
    . # . . .
    . # # . .
    . # # # .
    . # # . .
    . # . . .
    `)
DirY = Speed
SetMotors()
DirY = 0
SetMotors()
DirY = 0 - Speed
SetMotors()
DirY = 0
SetMotors()
DirX = Speed
SetMotors()
DirX = 0
SetMotors()
DirX = 0 - Speed
SetMotors()
DirX = 0
SetMotors()
RotZ = Speed
SetMotors()
RotZ = 0
SetMotors()
RotZ = 0 - Speed
SetMotors()
RotZ = 0
SetMotors()
basic.clearScreen()
basic.forever(function () {
    SetMotors()
})
