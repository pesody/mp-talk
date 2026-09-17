"""
main.py - Talk timer bell ringer for Raspberry Pi Pico (MicroPython).

Rings a bell at configured intervals after boot and displays:
- minutes/seconds since start
- minutes/seconds till next ring
- minutes/seconds till last ring
Stops automatically after the last ring.
"""
import time
from machine import Pin
from motor import Ringer
from display import init_display, show_status, show_completed
from schedule import BELL_SCHEDULE

def format_time(total_seconds):
    """Format seconds into MM:SS string."""
    if total_seconds < 0:
        total_seconds = 0
    minutes = int(total_seconds) // 60
    seconds = int(total_seconds) % 60
    return "{:02d}:{:02d}".format(minutes, seconds)

def main():
    print("=" * 40)
    print("Pico Talk Timer starting...")
    print("=" * 40)

    # Initialize OLED Display 
    try:
        oled = init_display(sda_pin=0, scl_pin=1)
        print("OLED display initialized.")
    except Exception as e:
        print("Warning: Could not initialize OLED display ({})".format(e))
        oled = None

    # Initialize Bell Ringer Servo (GP19)
    try:
        ringer = Ringer(pin_id=19)
        ringer.detach()  # Ensure motor is unpowered at start
        print("Bell ringer initialized on GP19.")
    except Exception as e:
        print("Error initializing ringer: {}".format(e))
        ringer = None

    # Prepare schedule
    schedule = sorted(BELL_SCHEDULE, key=lambda entry: entry[0])
    if not schedule:
        print("No schedule configured. Exiting.")
        return

    last_target_time = schedule[-1][0]
    total_events = len(schedule)
    current_event_idx = 0

    print("Loaded schedule ({} events, final event at {}s):".format(total_events, last_target_time))
    for idx, (target_sec, count) in enumerate(schedule, 1):
        print("  Event {}: {:>5}s ({}) -> {} ring(s)".format(
            idx, target_sec, format_time(target_sec), count
        ))

    start_ticks = time.ticks_ms()
    last_printed_sec = -1

    while current_event_idx < total_events:
        now_ticks = time.ticks_ms()
        elapsed_ms = time.ticks_diff(now_ticks, start_ticks)
        elapsed_sec = elapsed_ms // 1000

        target_sec, ring_count = schedule[current_event_idx]

        # Check if it is time to ring
        if elapsed_sec >= target_sec:
            print("\n" + "*" * 40)
            print("[{}] TRIGGER: {} ring(s)! (Target: {}s)".format(
                format_time(elapsed_sec), ring_count, target_sec
            ))
            print("*" * 40)

            # Show ringing alert on display
            elapsed_str = format_time(elapsed_sec)
            show_status(oled, elapsed_str, "00:00", format_time(max(0, last_target_time - elapsed_sec)),
                        next_count=ring_count, ringing=True)

            # Ring the bell
            if ringer:
                ringer.ring(count=ring_count)

            current_event_idx += 1

            # Check if this was the last ring
            if current_event_idx >= total_events:
                print("\nLast ring complete! Stopping program.")
                break

            # Continue to next iteration immediately to refresh state
            continue

        # Calculate countdowns
        remaining_next = max(0, target_sec - elapsed_sec)
        remaining_last = max(0, last_target_time - elapsed_sec)

        elapsed_str = format_time(elapsed_sec)
        next_str = format_time(remaining_next)
        last_str = format_time(remaining_last)

        # Update console and display once every second
        if elapsed_sec != last_printed_sec:
            last_printed_sec = elapsed_sec
            print("[{}] Since start: {} | Next: {} ({}x) | Last: {}".format(
                format_time(elapsed_sec),
                elapsed_str,
                next_str,
                ring_count,
                last_str
            ))
            show_status(oled, elapsed_str, next_str, last_str, next_count=ring_count, ringing=False)

        time.sleep_ms(100)

    # Program finished after last ring
    final_elapsed_sec = time.ticks_diff(time.ticks_ms(), start_ticks) // 1000
    final_elapsed_str = format_time(final_elapsed_sec)
    print("\nTalk Timer Finished. Total elapsed time: {}".format(final_elapsed_str))

    if ringer:
        ringer.detach()

    show_completed(oled, final_elapsed_str)

if __name__ == "__main__":
    main()
