import ctypes
import sys


def change_speed(speed):
    #   1 - slow
    #   10 - standard
    #   20 - fast
    set_mouse_speed = 113   # 0x0071 for SPI_SETMOUSESPEED
    ctypes.windll.user32.SystemParametersInfoA(set_mouse_speed, 0, speed, 0)


def get_current_speed():
    get_mouse_speed = 112   # 0x0070 for SPI_GETMOUSESPEED
    speed = ctypes.c_int()
    ctypes.windll.user32.SystemParametersInfoA(get_mouse_speed, 0, ctypes.byref(speed), 0)

    return speed.value


def proper_close():
    change_speed(standard_speed)
    root.destroy()


print('Current mouse speed = ', get_current_speed())
print('\n')
#print('Number of arguments:', len(sys.argv), 'arguments.')

filename = str(sys.argv[0]).split('/')[-1]

if len(sys.argv) == 1:
    print(filename, '[SPEED]')
    print('\n')
    print('Please use SPEED value between 1 and 20')
else:
     
    if sys.argv[1].isdigit() and int(sys.argv[1]) >= 1 and int(sys.argv[1]) <= 20:
        change_speed(int(sys.argv[1]))
        print('New mouse speed = ', get_current_speed())
    else:
        print('Invalid new mouse speed')
        print('Please use SPEED value between 1 and 20')
