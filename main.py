def on_bluetooth_connected():
    basic.show_leds("""
        . . # # .
        # . # . #
        . # # # .
        # . # . #
        . . # # .
        """)
bluetooth.on_bluetooth_connected(on_bluetooth_connected)

def on_bluetooth_disconnected():
    basic.show_icon(IconNames.NO)
bluetooth.on_bluetooth_disconnected(on_bluetooth_disconnected)

def SetMotors():
    global FR, FL, BR, BL
    FR = DirY + DirX + RotZ
    FL = DirY - DirX - RotZ
    BR = DirY - DirX + RotZ
    BL = DirY + DirX - RotZ
    robotbit.geek_servo(robotbit.Servos.S1, FR + 90)
    robotbit.geek_servo(robotbit.Servos.S2, 90 - FL)
    robotbit.geek_servo(robotbit.Servos.S3, BR + 90)
    robotbit.geek_servo(robotbit.Servos.S4, 90 - BL)
    basic.pause(50)

def on_mes_dpad_controller_id_microbit_evt():
    global DirY, DirX, RotZ
    if control.event_value() == EventBusValue.MES_DPAD_BUTTON_1_DOWN:
        DirY = Speed
    elif control.event_value() == EventBusValue.MES_DPAD_BUTTON_1_UP:
        pass
    elif control.event_value() == EventBusValue.MES_DPAD_BUTTON_2_DOWN:
        DirY = 0 - Speed
    elif control.event_value() == EventBusValue.MES_DPAD_BUTTON_2_UP:
        pass
    elif control.event_value() == EventBusValue.MES_DPAD_BUTTON_3_DOWN:
        DirX = 0 - Speed
    elif control.event_value() == EventBusValue.MES_DPAD_BUTTON_3_UP:
        pass
    elif control.event_value() == EventBusValue.MES_DPAD_BUTTON_4_DOWN:
        DirX = Speed
    elif control.event_value() == EventBusValue.MES_DPAD_BUTTON_4_UP:
        pass
    elif control.event_value() == EventBusValue.MES_DPAD_BUTTON_A_DOWN:
        DirX = 0
        DirY = 0
        RotZ = 0
        basic.show_arrow(ArrowNames.NORTH)
    elif control.event_value() == EventBusValue.MES_DPAD_BUTTON_A_UP:
        basic.clear_screen()
    elif control.event_value() == EventBusValue.MES_DPAD_BUTTON_B_DOWN:
        DirX = 0
        DirY = 0
        RotZ = 0
        basic.show_arrow(ArrowNames.SOUTH)
    elif control.event_value() == EventBusValue.MES_DPAD_BUTTON_B_UP:
        basic.clear_screen()
    elif control.event_value() == EventBusValue.MES_DPAD_BUTTON_C_DOWN:
        if DirX != 0 and DirY != 0:
            pass
        else:
            RotZ = 0 - Speed
    elif control.event_value() == EventBusValue.MES_DPAD_BUTTON_C_UP:
        pass
    elif control.event_value() == EventBusValue.MES_DPAD_BUTTON_D_DOWN:
        if DirX != 0 and DirY != 0:
            pass
        else:
            RotZ = Speed
    elif control.event_value() == EventBusValue.MES_DPAD_BUTTON_D_UP:
        pass
    else:
        pass
control.on_event(EventBusSource.MES_DPAD_CONTROLLER_ID,
    EventBusValue.MICROBIT_EVT_ANY,
    on_mes_dpad_controller_id_microbit_evt)

BL = 0
BR = 0
FL = 0
FR = 0
RotZ = 0
DirX = 0
DirY = 0
Speed = 0
Speed = 60
basic.show_leds("""
    . # . . .
    . # # . .
    . # # # .
    . # # . .
    . # . . .
    """)
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
basic.clear_screen()

def on_forever():
    SetMotors()
basic.forever(on_forever)
