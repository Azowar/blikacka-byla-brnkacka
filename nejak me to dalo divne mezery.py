def on_button_pressed_a():
    global mode    mode = mode - 1input.on_button_pressed(Button.A, on_button_pressed_a)
def on_button_pressed_b():
    global mode    mode = mode + 1input.on_button_pressed(Button.B, on_button_pressed_b)
mode = 0mode = 0def on_forever():
    if mode == 0:
        basic.show_leds("""            . . . . .                        . . . . .                        . . . . .                        . . . . .                        . . . . .        """)
    if mode == 1:
        basic.show_leds("""            # # # # #                        # # # # #                        # # # # #                        # # # # #                        # # # # #        """)
    if mode == 2:
        basic.show_leds("""            # # # # #                        # # # # #                        # # # # #                        # # # # #                        # # # # #        """)
        basic.show_leds("""            . . . . .                        . . . . .                        . . . . .                        . . . . .                        . . . . .        """)
    if mode == 3:
        basic.show_leds("""            . . . # #                        . . . # #                        . . . # #                        . . . # #                        . . . # #        """)
        basic.show_leds("""            # # . . .                        # # . . .                        # # . . .                        # # . . .                        # # . . .        """)
basic.forever(on_forever)
