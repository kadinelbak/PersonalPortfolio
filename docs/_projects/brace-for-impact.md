---
title: Brace for Impact — Adaptive Ankle Brace
layout: project
---

<p class="section-lead"><a href="../../designathons/">Designathons</a> / DTE Designathon 2026 / Team project</p>

## Brace for Impact (Designathon Project)

An adaptive ankle brace that stays loose during normal movement and stiffens only as the ankle approaches a dangerous roll. Four semi-active magnetorheological (MR) fluid dampers provide the resistance, an ESP32 reads ankle rotation and muscle fatigue, and the athlete gets two-way stiffness alerts on their phone and Apple Watch. Built as a team at the DTE Designathon 2026 (October 2026).

<figure>
  <img src="../../assets/img/brace-for-impact/01-brace-cad-render.jpg" alt="SolidWorks render of the full adaptive ankle brace assembly" />
  <figcaption>The final brace in SolidWorks: a rigid shell with MR dampers along the ankle.</figcaption>
</figure>

## The Problem

Ankle sprains are one of the most common sports injuries, especially on sudden cuts, jumps, and changes in direction. Several people on our team had sprained an ankle. Traditional braces give constant support, but that same stiffness restricts natural movement and costs performance, so athletes often skip them.

The design constraints were:

- **Protection without restriction:** free motion in the normal range, resistance only near an unsafe inversion angle.
- **Proportional, fast control:** resistance that scales with risk and responds in milliseconds, not an on/off lock.
- **Wearable size:** sensors, electronics, and actuators small and light enough to fit around an ankle.
- **Athlete in the loop:** clear alerts and a simple way to raise or lower stiffness without a custom app.

## Designed Solution

### Semi-active MR dampers

MR fluid is oil with tiny iron particles suspended in it. With no magnetic field it flows like oil. With a field across it, the particles chain up and the fluid behaves almost like a solid until it is pushed hard enough. More coil current means a stronger hold, so the resistance is proportional rather than binary.

<figure class="figure--narrow">
  <img src="../../assets/img/brace-for-impact/06-mr-fluid-off-on.png" alt="MR fluid with the coil off and on" />
  <figcaption>Coil off, the particles float and the fluid flows. Coil on, they chain up and resist.</figcaption>
</figure>

Each damper is a sealed Ø10 × 60 mm steel tube of MR fluid with the coil wound inside a steel piston and a 0.3 mm gap between the piston and the wall. The rod runs out both ends, so the fluid volume never changes and no accumulator or pump is needed. The ankle moves the rod; the coil only decides how hard it pushes back.

<figure class="figure--narrow">
  <img src="../../assets/img/brace-for-impact/07-mr-damper-section.png" alt="Cross-section of the semi-active MR damper" />
  <figcaption>Damper cross-section: the coil sits in the piston and the hollow rod carries its wires out.</figcaption>
</figure>

### Damper placement

<figure>
  <img src="../../assets/img/brace-for-impact/04-concept-side-view.png" alt="Concept side view of the brace showing dampers, potentiometer, EMG sleeve and ESP32" />
  <figcaption>Concept layout: rigid cuff, foot shell, dampers, a potentiometer at the ankle axis, and an EMG sleeve.</figcaption>
</figure>

<figure>
  <img src="../../assets/img/brace-for-impact/05-damper-layout.png" alt="Top-down layout of four dampers around the ankle" />
  <figcaption>Four dampers at the corners: the outer pair resists rolling, the inner pair the opposite way, and all four resist twist.</figcaption>
</figure>

### Sensing and electronics

- **Rotation:** a potentiometer at the ankle axis and stretch sensors in a Wheatstone bridge.
- **Fatigue:** surface EMG on the lower leg through an instrumentation front end with an 8 Hz high-pass, an ~800 Hz low-pass, and a total gain of about 1200, built on TLC272 and MCP6002 op-amps.
- **Mains rejection in firmware:** the ESP32 samples EMG at 1200 Hz and cancels 60 Hz hum with a one-cycle comb filter before computing a smoothed activity envelope.
- **Power and feedback:** ESP32 DevKit on a 9 V battery and 7805 regulator, with green, yellow, and red LEDs for the current stiffness level.

<figure class="figure--narrow">
  <img src="../../assets/img/brace-for-impact/08-emg-board-pcb.png" alt="EMG and stretch-sensor PCB layout in KiCad" />
  <figcaption>The EMG and stretch-sensor board in KiCad, built around a 38-pin ESP32 DevKit.</figcaption>
</figure>

### Alerts on the wrist

When the brace detects danger, the ESP32 sends a "Danger mode approached" push notification over WiFi through ntfy. It appears on the phone and mirrors to the Apple Watch with Increase and Decrease buttons, and the athlete's tap comes back to the ESP32 the same way to set stiffness from 0 to 5. No custom app was needed.

## Prototype

We built a wearable proof of concept alongside the full CAD design. The MR dampers could not be manufactured in the time available, so the prototype proves out the sensing, electronics, and alerts, while the dampers live in the final CAD.

<figure>
  <img src="../../assets/img/brace-for-impact/02-prototype-on-ankle.jpg" alt="The wearable prototype on an ankle with the ESP32 and sensor wiring" />
  <figcaption>The wearable prototype: a printed brace with the ESP32 and sensor electronics strapped on.</figcaption>
</figure>

<figure>
  <img src="../../assets/img/brace-for-impact/03-emg-test-setup.jpg" alt="Testing surface EMG on the calf with a breadboard circuit" />
  <figcaption>Bench-testing the EMG front end with electrodes on the calf.</figcaption>
</figure>

<figure class="project-video">
  <video src="../../assets/img/brace-for-impact/prototype-demo.mp4" poster="../../assets/img/brace-for-impact/prototype-demo-poster.jpg" controls muted playsinline preload="none"></video>
  <figcaption>Demo: the blue warning and red danger LEDs light up as the ankle rolls toward its limits.</figcaption>
</figure>

## Technical Contribution

- Designed the semi-active MR damper: a sealed Ø10 × 60 mm cylinder with the coil wound inside the piston, sized to fit four around the ankle.
- Designed the EMG and stretch-sensor board in KiCad and wrote the ESP32 firmware for sensing, filtering, and alerts.
- Built the two-way phone and Apple Watch alerts over WiFi with ntfy.

**Skills:** SolidWorks · CadQuery · KiCad · analog signal conditioning · ESP32 / C++ · WiFi push notifications · biomechanics research · prototyping

## Challenges

- **Protection without restriction:** a stiff brace would be no different from what is on the market. Motors, pulleys, and elastics each needed bulky electronics or gave resistance that was hard to control. MR hydraulics gave electrically controlled resistance in a tiny package with very few moving parts.
- **Low-amplitude EMG:** muscle signals are tiny and noisy, so the front end needed careful amplification, filtering, and a 60 Hz notch for wall-outlet noise.
- **Fitting electronics on a wearable:** the stretch sensors were much longer than ideal, which made them tricky to mount on a light, comfortable brace.
- **Getting the ESP32 online:** phone hotspots often default to 5 GHz or WPA3, which the ESP32 cannot use, so the connection had to be debugged before alerts worked.
- **Organic modeling:** the upper brace took most of one member's time, so the lower brace used simpler geometry with a few tricks to look more life-like.

## What I Learned

- Using an ESP32's WiFi for the first time, including two-way notifications to an Apple Watch.
- Building a full EMG chain with op-amp ICs; earlier EKG work transferred over well.
- Applying Wheatstone bridges to stretch sensors.
- How MR fluid, magnetic circuits, and damper geometry trade off against size and force.
- Turning biomechanics research on sprain mechanics into hardware requirements.

## Next Iteration

More advanced control algorithms, a compact manufactured damper, and testing with athletes to tune the brace for different sports, movement patterns, and injury risks. The long-term goal is a wearable that protects athletes without sacrificing mobility, giving support only when it is truly needed.

## Exhibit Links

- [Source code, KiCad board, and SolidWorks CAD on GitHub](https://github.com/kadinelbak/DTE2026)
- [All designathon projects](../../designathons/)
