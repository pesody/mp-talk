"""
schedule.py - Bell ringing schedule configuration for Pico Talk.

Each schedule entry is a tuple:
    (target_seconds_after_boot, ring_count)
"""

# Test times after boot and corresponding ring counts:
# BELL_SCHEDULE = [
#     (2, 1),          # 5 seconds
#     (6,2)   
# ]

BELL_SCHEDULE = [
    (3, 1),          # 3 seconds
    (10 * 60, 1),    # 10 minutes (600s)
    (17 * 60, 1),    # 17 minutes (1020s)
    (19 * 60, 2),    # 19 minutes (1140s)
    (20 * 60, 3),    # 20 minutes (1200s)
]
