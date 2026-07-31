---
title: Retractor Arm
layout: project
---

## Retractor Arm

Mechanical design concept for an open thoracoabdominal aortic aneurysm (TAAA) repair retractor system. The project focused on reducing surgical clutter, improving access, and making retraction more stable and adjustable.

<img src="../../assets/img/retractor-arm/locking-mechanism.png" alt="CAD render of a mechanical locking mechanism for the retractor arm" />

## Clinical Context

Open TAAA repair requires exposure across a large thoracoabdominal field, where the operative team must maintain access to deep anatomy while working around the current omni-retractor frame, rods, blades, and support hardware.

The clinical pain points from the project were:

- **Rigid blades:** difficult to form to patient anatomy and hard to adjust mid-procedure.
- **High resting frame:** rods and supports sit above the working field and can create difficult angles of access.
- **Slow setup and adjustment:** large joints and friction-based locks can be awkward to position, tighten, and reconfigure.

The design response was split into three engineering tracks: flexible blades, lower rod heights, and faster joint setup.

<img src="../../assets/img/retractor-arm/aortic-extent-context.png" alt="Thoracoabdominal aortic aneurysm extent diagram used as clinical context" />

## Track 1: Flexible Blades and Layer Jamming

The first track explored a blade that could be flexible during placement, conform around patient anatomy, and then stiffen after positioning. The deck framed this around **layer jamming**, where stacked layers can move relative to each other in a soft state and become much stiffer when vacuum pressure increases interlayer friction.

<img src="../../assets/img/retractor-arm/layer-jamming-strength.png" alt="Layer jamming strength plot comparing solid steel sheet, layer jamming sheet, and granular jamming block" />

The engineering idea was to preserve adjustability while avoiding a bulky gripping mechanism. The deck compared bending capacity across cross-sectional area and showed why a thin layer-jamming structure could be more promising than a thick granular jamming block for a low-profile surgical blade.

Key design logic:

- Keep the blade thin enough to avoid crowding the operative field.
- Allow shape change during placement rather than forcing anatomy to match a rigid blade.
- Use vacuum-stiffened layer coupling so the blade can resist bending after it is positioned.
- Treat stiffness, thickness, and edge-load capacity as coupled design constraints.

## Track 2: Lower Rod Heights and FEA

The second track addressed the height of the support structure. A high omni-retractor frame can make the angle of access more difficult for surgeons, so the project explored lower rod placement and arm geometry that keeps hardware closer to the bed while still positioning the blade over the surgical site.

<img src="../../assets/img/retractor-arm/low-rod-side-view.png" alt="Side-view concept showing lower rods, arms, blade, surgical site, and bed" />

<img src="../../assets/img/retractor-arm/low-rod-lateral-view.png" alt="Lateral-view concept showing blade and arm geometry around the patient" />

Finite element analysis was used to test whether the lower-profile arm geometry could handle expected loads without creating unacceptable stress concentration. The FEA visual highlights von Mises stress along the arm and shows the main concern area around the bend and load path.

<img src="../../assets/img/retractor-arm/fea-stress.png" alt="FEA von Mises stress plot for the retractor arm geometry" />

Key design logic:

- Lower the support rods to improve access angles and reduce visual/physical obstruction.
- Route the arm from the lower frame to the retractor blade while preserving clearance over the patient.
- Use FEA to identify stress concentration around bends and transitions.
- Iterate geometry around the tradeoff between low profile, stiffness, and manufacturability.

## Track 3: Mechanical Locks and Setup Time

The third track focused on the joints. The current setup problem was not only strength; it was also usability. Large joints can be hard to use quickly, and friction-based locks depend heavily on clamping force and surface conditions.

<img src="../../assets/img/retractor-arm/lock-comparison.png" alt="Comparison between friction-based locking and mechanical locking for torque load transfer" />

The design direction moved toward **mechanical locking**, where load is transferred through geometry rather than only surface friction. A spline-like or faceted interface can resist rotation through positive engagement, reducing slip risk when torque is applied.

<img src="../../assets/img/retractor-arm/patient-clearance.png" alt="Concept sketch showing the retractor arm positioned above the patient with clearance" />

Key design logic:

- Reduce reliance on friction-only tightening.
- Use mechanical engagement to carry torque through face-to-face load transfer.
- Make the joint faster to lock, unlock, and reposition.
- Preserve enough adjustability for intraoperative changes without sacrificing stability.

## Technical Contribution

This project combined clinical problem framing, mechanism exploration, CAD, FEA, and comparative mechanical reasoning. My contribution centered on turning a broad clinical access problem into testable engineering tracks: how the blade changes stiffness, how the arm geometry affects access and stress, and how the joint transmits torque without slipping.

## What This Project Shows

The retractor system is strongest as an engineering design story because it does not rely on one idea. It breaks a surgical workflow problem into separable mechanisms:

- **Layer jamming** for conformable but stiffenable blades
- **FEA-guided arm geometry** for lower-profile access
- **Mechanical locks** for faster, more reliable positioning

## Next Iteration

Future work would focus on bench testing torque resistance, validating layer-jamming stiffness under realistic loading, comparing FEA predictions against physical prototypes, refining sterilizable geometry, and evaluating setup time with clinicians.
