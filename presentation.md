---
marp: true
theme: gaia
_class: lead
paginate: true
backgroundColor: #0d1117
color: #e6edf3
style: |
  section {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
    padding: 40px 60px;
    font-size: 26px;
  }
  h1 {
    color: #58a6ff;
  }
  h2 {
    color: #79c0ff;
    border-bottom: 2px solid #30363d;
    padding-bottom: 8px;
    margin-bottom: 20px;
  }
  h3 {
    color: #a5d6ff;
  }
  code {
    background: #161b22;
    color: #ff7b72;
    border: 1px solid #30363d;
    border-radius: 6px;
    padding: 2px 6px;
    font-size: 0.88em;
  }
  pre code {
    background: #161b22;
    color: #e6edf3;
    border: 1px solid #30363d;
    border-radius: 8px;
    padding: 16px;
    font-size: 0.72em;
    line-height: 1.4;
  }
  table {
    width: 100%;
    border-collapse: collapse;
    margin: 15px 0;
    font-size: 0.78em;
  }
  th {
    background: #1f242c;
    color: #58a6ff;
    border: 1px solid #30363d;
    padding: 10px 14px;
    text-align: left;
  }
  td {
    border: 1px solid #30363d;
    padding: 8px 14px;
    background: #0d1117;
  }
  tr:nth-child(even) td {
    background: #161b22;
  }
  .grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 24px;
  }
  .card {
    background: #161b22;
    border: 1px solid #30363d;
    border-radius: 8px;
    padding: 8px;
  }
  .highlight {
    color: #7ee787;
    font-weight: bold;
  }
  .accent {
    color: #f0883e;
    font-weight: bold;
  }
  .badge {
    display: inline-block;
    padding: 2px 10px;
    font-size: 0.75em;
    font-weight: 600;
    border-radius: 12px;
    background: #1f6feb;
    color: #ffffff;
  }
  footer {
    font-size: 0.55em;
    color: #8b949e;
  }
  header {
    font-size: 0.6em;
    color: #8b949e;
  }
---

<!-- _class: lead -->
<!-- _paginate: false -->
# 🐍 MicroPython
### Python for the Physical World

**An Introduction to Embedded Python & Microcontroller Computing**

**PhillyPUG 2026-09-17**

---
## Overview

- **Bell Ringer**: MicroPython code ringing the bell to keep track of this presentation
- Overview of MicroPython
- Hands-on setup and programming of the parts used in the **Bell Ringer**
- Conclusion & QA

---
## What is MicroPython?

- **Created by Damien George** in 2013 via a wildly successful Kickstarter.
- A complete, highly optimized software implementation of **Python 3.4+**.
- Designed from the ground up to run on **bare-metal microcontrollers**.
- Includes an interactive **REPL** (Read-Eval-Print Loop) over serial/UART.

<br>

```python
>>> import sys
>>> sys.implementation
(name='micropython', version=(1, 23, 0), _machine='Raspberry Pi Pico with RP2040')
>>> print("Hello from hardware!")
Hello from hardware!
```

---

## Why Microcontrollers (MCUs)?

<div class="grid">
<div class="card">

### 💰 Cost & Accessibility
- Chips cost **$1 to $5** (e.g. RP2040, RP2350, ESP32).
- Complete dev boards available under **$5–$10**.
- Low barrier to entry for prototyping and mass manufacturing.
</div>

<div class="card">

### 🔋 Ultra-Low Power
- Run for **months or years** on standard AA or coin-cell batteries.
- Deep sleep modes consume **microamps ($\mu A$)**.
- Instant-on capability without boot latency.
</div>
</div>

<br>

<div class="card">

### 🔌 Direct Hardware Interfaces
- Direct register / pin access: **GPIO**, **PWM**, **ADC**, **DAC**.
- Industry-standard serial buses: **I2C**, **SPI**, **UART**, **CAN**, **I2S**.
- Microsecond timing determinism without OS overhead.
</div>

---

## Evolution: 1980s PC vs Today's MCU

How does a $4 microcontroller compare to the computers that started the PC revolution?

| System | Year | CPU & Clock | RAM | Storage | Typical Cost |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Commodore 64** | 1982 | 6510 @ 1.02 MHz | **64 KB** | 170 KB Floppy | ~$595 |
| **IBM PC/AT** | 1984 | Intel 80286 @ 6 MHz | **256–512 KB** | 20 MB Hard Disk | ~$4,000+ |
| **Pentium 150 PC** | 1995 | Intel Pentium @ 150 MHz | **16–32 MB** | 1.6 GB Hard Disk | ~$2,500 |
| **ESP32-S3** | 2022 | Dual Xtensa @ 240 MHz | **512 KB** (+PSRAM) | 8–16 MB Flash | **~$4** |
| **Raspberry Pi Pico 2** | 2024 | Dual Cortex-M33 @ 150 MHz | **520 KB** | 4 MB Flash | **~$5** |
| **Modern Smartphone** | Today | 8 Cores @ ~3.5 GHz | **8–16 GB** | 128–512 GB Flash | ~$800+ |
| **Modern Laptop / PC** | Today | 8–16 Cores @ 4.0+ GHz | **16–64 GB** | 1–2 TB NVMe SSD | ~$1,200+ |

<div class="card" style="margin-top: 10px; text-align: center; padding: 10px 16px;">
💡 <span class="highlight">A $5 Pico 2 delivers the 150 MHz CPU clock speed of a mid-90s $2,500 Pentium PC!</span>
</div>

---

## Microcontroller vs Full Operating System

<div class="grid">
<div class="card">

### 💻 Full OS (Linux / macOS / Windows)
- **Multi-tasking & Abstraction**: Hundreds of processes, preemptive scheduler.
- **Boot Time**: 10 to 60 seconds.
- **Resource Footprint**: Gigabytes of RAM, high idle power draw.
- **I/O Access**: Mediated through kernel drivers, non-deterministic latency.
</div>

<div class="card">

### ⚡ Bare-Metal MicroPython
- **Single Process / Direct Execution**: Python bytecode executes directly on the chip.
- **Boot Time**: Instant (< 100 milliseconds).
- **Resource Footprint**: Kilobytes of RAM, milliwatts of power.
- **I/O Access**: Direct bit-banging & hardware registers via `machine` module.
</div>
</div>

---

## MCU Language Landscape: C/C++, Rust & Python


<div class="card">

### ⚙️ C / C++ (The Industry Standard)
- **Strengths**: Maximum speed, minimal memory, direct register access, vendor SDKs.
- **Trade-offs**: Memory management, complex toolchains, slow compile-flash cycle.
</div>

<div class="card">

### 🦀 Rust (Modern & Memory-Safe)
- **Strengths**: Zero-cost abstractions, guaranteed memory safety without GC
- **Trade-offs**: Steep learning curve, requires flashing every change.
</div>


<div class="card">

### 🐍 MicroPython (The Productivity Champion)
- **Strengths**: Instant iteration via **REPL**, no toolchains, readable syntax.
- **Trade-offs**: Higher memory footprint, slower raw compute.
</div>

---

## MicroPython vs CPython: Key Limitations

MicroPython is a lean reimplementation of Python 3 with intentional hardware trade-offs:

<div class="grid">
<div class="card">

### 📦 Standard Library & PyPI
- **Slimmed Standard Library**.
- **No Heavy PyPI Packages**: no `numpy`, `pandas`
- Uses embedded package managers (**`mip`**).
</div>

<div class="card">

### 🧠 Memory & Heap Limits
- **Strict RAM Limits**: Heap is **hundreds of KBs**, not gigabytes.
- **Garbage Collection**: GC pauses and heap fragmentation need careful management.
- **Stack Depth**: Shallow recursion / call stack limits.
</div>
</div>

---

## The MicroPython Workflow

```
[ Developer PC ]  ================ USB Serial / REPL ================>  [ RP2040 / ESP32 ]
  - VS Code                                                                 - MicroPython VM
  - MicroPico Extension                                                     - Hardware Pins
  - Fast Code Sync                                                          - Sensors & Actuators
```

### Standard Boot Sequence
1. **`boot.py`** *(Optional)*: Runs first at power-on. Configures file systems, network, and early setup.
2. **`main.py`**: Your application logic. Runs automatically after `boot.py`.
3. **Interactive REPL**: Live Python prompt over USB serial for testing and debugging without re-flashing!

---

## Getting Started with Raspberry Pi Pico

<div class="grid">
<div class="card">

### 1. Flashing Firmware
1. Download `.uf2` firmware from [micropython.org](https://micropython.org/download/rp2-pico/).
2. Hold the **BOOTSEL** button on the Pico.
3. Plug in the USB cable (Pico mounts as a USB drive named `RPI-RP2`).
4. Drag and drop the `.uf2` file.
5. Pico reboots automatically into MicroPython!
</div>

<div class="card">

### 2. VS Code Setup
- Install the **MicroPico** extension.
- Connect your Pico via USB.
- Click **MicroPico: Connect** in the status bar.
- Instantly get an interactive REPL terminal and 1-click file synchronization!
</div>
</div>

---

## Example 1: The Interactive REPL

Run commands live directly on the microcontroller — no compile or flash cycle:

```python
# In the VS Code MicroPico REPL:
>>> print("Hello from Raspberry Pi Pico!")
Hello from Raspberry Pi Pico!

>>> import machine, time
>>> import os
>>> os.listdir()
['boot.py', 'main.py']

>>> machine.freq()
125000000  # Running at 125 MHz!
```

---

## Example 2A: Digital I/O (Blinking an LED)

The embedded equivalent of *"Hello World"* — toggling a hardware pin:

```python
import machine
import time

# On Raspberry Pi Pico, onboard LED is "LED" (or GPIO 25 on original Pico)
led = machine.Pin("LED", machine.Pin.OUT)

print("Starting LED blink loop (Ctrl+C to stop)...")

while True:
    led.toggle()         # Flip pin state (High <-> Low)
    time.sleep_ms(500)   # Non-blocking or millisecond delay
```

<div class="card" style="margin-top: 10px;">
✨ <b>Pin control is simple:</b> <code>Pin.value(1)</code> turns it on, <code>Pin.value(0)</code> turns it off.
</div>

---

## Example 2B: PWM (Pulse-Width Modulation)

Simulate analog voltages to smoothly fade an LED:

```python
import machine
import time
import math

# Configure Pin as PWM output at 1000 Hz
pwm_led = machine.PWM(machine.Pin(15))
pwm_led.freq(1000)

print("Pulsing LED brightness with a sine wave...")

t = 0.0
while True:
    # Calculate 16-bit duty cycle (0 to 65535) using sine wave
    duty = int((math.sin(t) + 1) / 2 * 65535)
    pwm_led.duty_u16(duty)
    t += 0.05
    time.sleep_ms(20)
```

---

## Example 3: Precision Servo Motor Control

Controlling a servo angle via 50 Hz PWM pulse width (0.5 ms to 2.5 ms):

Uses [servo.py](https://github.com/mchobby/micropython-pico/blob/main/lib/servo.py)

```python
import servo

s = servo.Servo(19)

s.angle(20)
s.angle(120)
```

---

## Example 4: Adding an I2C OLED Display

Connect a 0.96" SSD1306 OLED ($2) via standard I2C bus:
Uses [ssd1306.py](https://github.com/micropython/micropython/blob/master/drivers/display/ssd1306.py)

```python
import machine
import ssd1306  # Standard MicroPython driver

# Initialize Hardware I2C (SCL=Pin 17, SDA=Pin 16)
i2c = machine.I2C(0, scl=machine.Pin(17), sda=machine.Pin(16), freq=400000)
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# Draw shapes and text to the framebuffer
oled.fill(0)                               # Clear screen
oled.rect(0, 0, 128, 64, 1)                # Border
oled.text("MicroPython", 16, 12, 1)
oled.text("Pico 2 Display", 10, 28, 1)

oled.show()  # Push buffer to physical display
```

---

<!-- _class: lead -->
## Summary & Key Takeaways

1. **MicroPython combines Python's productivity with embedded speed.**
2. **Modern MCUs ($4-$5) are astonishingly powerful** compared to early computing giants.
3. **No compile-flash cycle needed** — the interactive REPL transforms hardware debugging.
4. **Massive ecosystem**: Displays, sensors, motors, Wi-Fi/Bluetooth, and robotics.

<br>

<div class="card" style="text-align: center;">
📚 <b>Resources:</b> <a href="https://micropython.org">micropython.org</a> &nbsp;|&nbsp; <a href="https://docs.micropython.org">docs.micropython.org</a> &nbsp;|&nbsp; <a href="https://github.com/micropython/micropython">GitHub</a>
</div>

---

<!-- _class: lead -->
<!-- _paginate: false -->
# Questions ?

<div style="display: flex; justify-content: center; margin: 18px 0;">
  <img src="qr-code.png" width="220" alt="QR Code" style="background: white; padding: 10px; border-radius: 12px; display: block;" />
</div>

**Thank you!** 🚀


