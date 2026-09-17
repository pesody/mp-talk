"""
display.py - SSD1306 OLED display helper for Pico Talk.
"""
from machine import Pin, I2C, SoftI2C
import ssd1306

def init_display(sda_pin=0, scl_pin=1, width=128, height=64):
    """Initialize SSD1306 OLED display using hardware I2C or SoftI2C fallback."""
    try:
        # Hardware I2C 0 on RP2040 (GP4/GP5)
        i2c = I2C(0, sda=Pin(sda_pin), scl=Pin(scl_pin), freq=400000)
    except Exception:
        pass    
    return ssd1306.SSD1306_I2C(width, height, i2c)

def show_status(display, elapsed_str, next_str, last_str, next_count=None, ringing=False):
    """
    Render talk timer status on 128x64 OLED display:
    - minutes/seconds since start
    - minutes/seconds till next ring
    - minutes/seconds till last ring
    """
    if display is None:
        return

    display.fill(0)
    if ringing:
        display.text("****************", 0, 0)
        display.text("**  RINGING!  **", 0, 12)
        if next_count:
            count_label = "({} ring{})".format(next_count, "s" if next_count > 1 else "")
            display.text("    " + count_label, 0, 26)
        display.text("Elapsed: " + elapsed_str, 0, 42)
        display.text("****************", 0, 54)
    else:
        display.text("SINCE START:", 0, 0)
        display.text("     " + elapsed_str, 0, 10)

        if next_str is not None:
            if next_count is not None:
                display.text("TILL NEXT ({}x):".format(next_count), 0, 22)
            else:
                display.text("TILL NEXT RING:", 0, 22)
            display.text("     " + next_str, 0, 32)
        else:
            display.text("TILL NEXT RING:", 0, 22)
            display.text("     --:--", 0, 32)

        display.text("TILL LAST RING:", 0, 44)
        display.text("     " + last_str, 0, 54)

    display.show()

def show_completed(display, elapsed_str):
    """Render final completion screen."""
    if display is None:
        return
    display.fill(0)
    display.text("****************", 0, 0)
    display.text("**  FINISHED  **", 0, 14)
    display.text("Total:   " + elapsed_str, 0, 32)
    display.text("All rings done!", 0, 48)
    display.show()

