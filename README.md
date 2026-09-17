# 🐍 MicroPython Presentation Deck

A modern, [Marp](https://marp.app/)-based slide presentation introducing **MicroPython**, microcontroller computing, hardware architecture differences, and hands-on examples built for the **Raspberry Pi Pico**.

---

## 📋 Outline Covered in `presentation.md`

1. **Introduction & Overview**:
   - What is MicroPython (Damien George, Kickstarter, Python 3 bare-metal engine).
   - **Bell Ringer** concept: MicroPython tracking and pacing the talk.
2. **Why Microcontrollers (MCUs)?**:
   - Cost advantage (\$1–\$5 chips).
   - Ultra-low power consumption (microamp sleep modes, months on batteries).
   - Direct hardware interfaces (GPIO, PWM, ADC, I2C, SPI, UART).
3. **Evolution & Historical Perspective**:
   - Comparison table: 1980s/90s PCs (Commodore 64, IBM PC/AT, Pentium 150) vs Modern MCUs (ESP32-S3, Raspberry Pi Pico 2) vs Modern Smartphones & Laptops.
4. **Architecture Differences**:
   - Bare-metal execution loop vs Full Operating System (Linux/Windows).
   - Boot speed (< 100 ms), determinism, and memory footprints.
5. **MCU Language Landscape**:
   - **C / C++**: Maximum speed & minimal footprint vs complex CMake toolchains.
   - **Rust (Embassy)**: Memory safety & modern async vs steep learning curve.
   - **MicroPython**: Rapid iteration via REPL & readable syntax vs memory overhead.
6. **MicroPython vs CPython Limitations**:
   - Standard library subsets (`u`-modules), no heavy C-extensions/PyPI, strict heap memory/GC, and execution performance.
7. **The MicroPython Workflow**:
   - Boot sequence (`boot.py` ➔ `main.py` ➔ interactive REPL).
8. **Getting Started with Raspberry Pi Pico**:
   - Flashing firmware (`.uf2` drag-and-drop via `BOOTSEL` mode).
   - VS Code setup with the **MicroPico** extension.
9. **Hands-on Code Examples**:
   - **REPL**: Live interactive terminal & clock frequency inspection.
   - **Digital Output**: Toggling onboard LED with `machine.Pin`.
   - **PWM (Pulse-Width Modulation)**: Sine-wave LED fading with `machine.PWM`.
   - **Actuators & Motion**: 50Hz PWM servo positioning (0–180°).
   - **I2C Display**: Driving a 0.96" SSD1306 OLED display (text, borders, framebuf).
10. **Summary, Resources & Q&A**.

---

## 🛠️ Hardware & Software Requirements for Examples

- **Hardware**:
  - Raspberry Pi Pico or Pico 2
  - Micro-USB cable
  - 0.96" I2C SSD1306 OLED display (128x64)
  - Micro servo motor (e.g. SG90)
  - Breadboard and jumper wires
- **Software**:
  - [VS Code](https://code.visualstudio.com/)
  - [MicroPico Extension](https://marketplace.visualstudio.com/items?itemName=paulober.pico-w-go)
  - [Marp for VS Code Extension](https://marketplace.visualstudio.com/items?itemName=marp-team.marp-vscode)

---

## 🚀 How to View & Present

### Option 1: VS Code (Recommended for Presenting)
1. Install the **[Marp for VS Code](https://marketplace.visualstudio.com/items?itemName=marp-team.marp-vscode)** extension.
2. Open [`presentation.md`](presentation.md).
3. Click the **Marp Preview** icon in the editor toolbar to view slides.
4. Press `F11` (or use presentation mode) for full-screen slides during the talk.

### Option 2: NPM Scripts (via `package.json`)
```bash
# Build standalone HTML presentation in dist/index.html
npm run build

# Start live preview server with hot reloading
npm run preview

# Export to PDF (requires Chrome/Chromium installed)
npm run build:pdf

# Export to PowerPoint (.pptx)
npm run build:pptx
```

### Option 3: Direct Marp CLI
```bash
npx @marp-team/marp-cli presentation.md -o dist/index.html
```

---

## 📚 References & Links

- [MicroPython Official Website](https://micropython.org)
- [MicroPython Documentation](https://docs.micropython.org)
- [Raspberry Pi Pico MicroPython Documentation](https://www.raspberrypi.com/documentation/microcontrollers/micropython.html)
- [Marp Markdown Presentation Ecosystem](https://marp.app/)
