---
title: Foot Ulcer Early-Warning Monitor
layout: project
---

## Foot Ulcer Early-Warning Monitor (Designathon Project)

A low-cost sock-based screening aid that compares left and right foot temperature to flag a developing diabetic foot ulcer before the skin breaks down. Built in 12 hours at the UF BMES x IEEE EMBS design event (October 2026), in two versions: an Arduino build with a live web dashboard, and a chip-level analog alarm with no microcontroller logic.

<img src="../../assets/img/foot-monitor/system-diagram.webp" alt="System diagram: thermistors and a tilt switch in the sock feed either Arduino firmware and a web dashboard, or an analog bridge, LM393 window comparator, NE555 activity timer and 74LS32 alert gate" />

## Clinical Need

Diabetic foot ulcers often begin as local inflammation that a patient with peripheral neuropathy cannot feel. A sustained temperature difference of about 2.2 °C between the same spot on the left and right foot is an established early warning sign, and home temperature monitoring can catch it days before an ulcer opens. Commercial monitoring systems are expensive, which matters most in the resource-limited settings the event prompt targeted.

The design constraints were:

- **Cheap, available parts:** 10k NTC thermistors, tilt/ball switches, a kit of common ICs, and an Arduino Uno.
- **Relative, not absolute, sensing:** the signal is a left/right difference, so room temperature and common drift should cancel.
- **Activity awareness:** walking warms a foot, so movement must not trigger a false alarm.
- **Screening, not diagnosis:** the device should prompt a foot check or clinic visit, not replace one.

## Designed Solution

Each sock carries thermistors at the ball and heel plus a tilt switch. The comparison is spot to spot, ball to ball and heel to heel, rather than whole foot averages.

**Digital build.** An Arduino Uno converts each divider reading to °C with the beta equation and drives three LEDs: two for tilt and one for the temperature difference (off below 1.75 °C, blinking at watch, solid above 2.2 °C, with 0.2 °C hysteresis). It streams one line a second over serial.

**Web dashboard.** A single offline HTML page reads the board over Web Serial and shows temperature over time for ball and heel, the average left/right difference with watch and alert lines, a shaded foot heat map with a replay slider, and the activation periods from the tilt switches. Demo data and CSV import/export let it run without hardware.

<img src="../../assets/img/foot-monitor/dashboard-two-feet.webp" alt="Dashboard in two-feet mode showing ball and heel temperature over time, alarm state, and average left minus right difference" />

**One-sock demo mode.** For a live single-sock demo, a second sketch calibrates to the wearer for 5 seconds, stores it in EEPROM, and alerts when the ball or heel rises 3 °C above calibration with no movement in the last 30 seconds. Warming during movement is labelled as expected instead of alarming.

<img src="../../assets/img/foot-monitor/dashboard-one-sock.webp" alt="Dashboard in one-sock mode showing rise above calibration, shaded movement periods, heat-alert markers and a sock map" />

## Analog Version

The same decision was rebuilt without software, using only kit parts and the Arduino as a 5 V supply:

- **Thermistor bridge:** both thermistors in matched dividers, nulled with a shared 10k pot; 470 Ω offset resistors set a dead band of roughly 2 to 3 °C.
- **LM393 window comparator:** trips if either foot is warmer, wired-AND onto one node with a yellow "feet differ" LED.
- **NE555 one-shot:** each tilt gives a ~1.1 s activity pulse with a green LED.
- **74LS32 alert gate:** the red LED lights only when the feet differ and nothing moved.

The estimated parts cost was about $13.63 for the analog sock against about $42.79 for the digital sock, most of the difference being the Arduino board.

<img src="../../assets/img/foot-monitor/analog-schematic.webp" alt="Analog schematic in five blocks: sensor bridge, LM393 window comparator, NE555 activity timer, 74LS32 alert logic, and power" />

## Debugging and Iteration

- **Sensitivity:** the first divider resistors were 330 Ω, giving about 2 ADC counts per °C. Moving to 10 kΩ raised that to about 10 counts per °C, enough to resolve the 1.75 °C threshold cleanly.
- **Bridge bring-up:** reading the four bridge nodes with the Arduino ADC exposed mislabeled nodes, floating inputs and an unseated thermistor before the bridge balanced at about 335 counts per side with a 0 to +1 count difference.
- **False alert in the demo:** the one-sock alert stayed on after calibration because the sketch calibrated before the sensors reached skin temperature. Waiting 2 to 3 minutes before calibrating fixed it.
- **Data path:** the dashboard parser was rewritten to read the firmware's own serial format, so the page's alarm state always matches the LED on the board.

<img src="../../assets/img/foot-monitor/live-one-sock-session.webp" alt="Live one-sock session from the real sock: ball and heel rise above calibration with warming spikes during movement" />

## Technical Contribution

I chose the problem from a brainstorm of kit-compatible device ideas, built and wired the sensor sock and Arduino prototype, brought up and balanced the analog bridge on a breadboard, and debugged the hardware through the demo. I set the clinical thresholds and movement logic, and directed the firmware, the dashboard and the analog design through several iterations as the build changed.

## Status

Working prototype from a 12-hour event; not clinically validated. The digital one-sock build ran live with the dashboard. The analog bridge was balanced on hardware, but the full analog chain was not yet confirmed end to end. The KiCad boards were generated but not yet checked with ERC/DRC or fabricated.

## Next Iteration

Finish the analog chain block by block and verify a 2 °C trip in both directions, validate readings against a reference thermometer across several wearers, run ERC/DRC and fabricate the board, and move the electronics to a flexible circuit with a coin-cell supply.
