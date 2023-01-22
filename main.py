def on_button_pressed_a():
    global Score
    if Mode == 0:
        Score += -1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global Mode
    if Mode == 0:
        Mode = 1
    else:
        Mode = 0
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global Score
    if Mode == 0:
        Score += 1
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    global RandomNum
    if Mode == 1:
        RandomNum = randint(1, 6)
    else:
        pass
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

RandomNum = 0
Score = 0
Mode = 0
Mode = 0

def on_forever():
    if Mode == 0:
        basic.show_number(Score)
    elif RandomNum == 1:
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . # . .
                        . . . . .
                        . . . . .
        """)
    elif RandomNum == 2:
        basic.show_leds("""
            . . . . #
                        . . . . .
                        . . . . .
                        . . . . .
                        # . . . .
        """)
    elif RandomNum == 3:
        basic.show_leds("""
            . . . . #
                        . . . . .
                        . . # . .
                        . . . . .
                        # . . . .
        """)
    elif RandomNum == 4:
        basic.show_leds("""
            # . . . #
                        . . . . .
                        . . . . .
                        . . . . .
                        # . . . #
        """)
    elif RandomNum == 5:
        basic.show_leds("""
            # . . . #
                        . . . . .
                        . . # . .
                        . . . . .
                        # . . . #
        """)
    else:
        basic.show_leds("""
            # . # . #
                        . . . . .
                        . . . . .
                        . . . . .
                        # . # . #
        """)
basic.forever(on_forever)
