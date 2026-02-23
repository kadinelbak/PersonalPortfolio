# GRAPHICS TODO — Medical Portfolio

## Required Graphics (6 total)

All images go in: `/medical-template/assets/img/`

Format: **PNG or SVG** (PNG preferred for diagrams, SVG for technical illustrations)
Resolution: 1200px wide minimum
Style: Clean, labeled, minimal (no complex rendering)

---

## FLEXIFOOT (Post-Operative Foot Surgery)

### 1. FlexiFoot Outsole Diagram (PRIORITY)
**File:** `flexifoot-outsole-diagram.png`
**Location on page:** After "FlexiFoot Concept" heading, above "Existing vs. FlexiFoot"
**Content:**
- Top-down AND side view of outsole
- Label regions: "Stable Hindfoot" + "Compressible Forefoot"
- Show material difference or color coding
- Dimensions optional but helpful
- **Style:** Simple schematic, not CAD

**Suggested tools:** Inkscape, PowerPoint, Figma, or hand-drawn + scanned

---

### 2. FlexiFoot Side Profile Comparison (PRIORITY)
**File:** `flexifoot-comparison.png`
**Location on page:** Below Fig 1
**Content:**
- Left side: Reverse camber shoe (existing solution)
- Right side: FlexiFoot (new concept)
- Show patient standing/walking posture comparison
- Highlight: stability of hindfoo, off-loading of forefoot
- Arrow or annotation showing gait improvement
- **Style:** Side-view stick figure or simplified silhouette

---

### 3. FlexiFoot Force-Path Illustration (NEW — CREATE THIS)
**File:** `flexifoot-force-path.png`
**Location on page:** Below Fig 2, under "Force-Path & Load Distribution" heading
**Content:**
- Simplified foot cross-section (sagittal plane)
- Arrow showing body weight → heel → mid-foot
- Arrow showing NO load transfer to forefoot/surgical site
- Color code: Green (safe) / Red (avoid)
- Label: "Weight-bearing regions" vs. "Off-loaded regions"
- **Style:** Anatomical schematic with color overlays, no equations

---

## NEUROVAC (Sunken Skin Flap Syndrome)

### 4. NeuroVac System Schematic (PRIORITY)
**File:** `neurovac-system-schematic.png`
**Location on page:** After "NeuroVac System" heading, under "System-Level Schematic"
**Content:**
- Head outline with cranial defect
- Interface cushion over defect
- Vacuum chamber (represented as box)
- Tubing connecting head to chamber
- Sensor symbol (pressure gauge or arrow)
- Pump symbol
- Control unit icon
- **Style:** Block diagram, top-down view of head + components around

---

### 5. NeuroVac Pressure Modulation Diagram (PRIORITY)
**File:** `neurovac-pressure-modulation.png`
**Location on page:** Below Fig 4, under "Pressure Modulation Principle"
**Content:**
- Left side: Head with flap (sunken) + atmospheric pressure arrows
- Middle: Vacuum chamber reducing pressure
- Right side: Equalized pressure + flap restored to position
- Annotation: "Atmospheric P → Reduced P → Equalization"
- **Style:** Three-stage process diagram, use color or arrows to show progression

---

### 6. NeuroVac Feedback Loop Illustration (NEW — CREATE THIS)
**File:** `neurovac-feedback-loop.png`
**Location on page:** Below Fig 5, under "Closed-Loop Feedback Control"
**Content:**
- Flow diagram showing loop:
  - Depth Sensor → reads flap depth
  - Controller → compares to target
  - Pump → adjusts vacuum
  - Pressure Chamber → delivers modulated pressure
  - Back to Sensor (loop)
- Add safety annotations: "Safety limits prevent over-correction" or "Gradual adjustment"
- **Style:** Circular flow chart, annotated with safety notes

---

# GRAPHICS PRIORITY MATRIX

| Priority | File | Purpose | Tool |
|----------|------|---------|------|
| 1 (ASAP) | flexifoot-outsole-diagram.png | Explain concept | Inkscape, PowerPoint |
| 1 (ASAP) | flexifoot-comparison.png | Show improvement | PowerPoint, Figma |
| 1 (ASAP) | neurovac-system-schematic.png | System overview | Lucidchart, PowerPoint |
| 1 (ASAP) | neurovac-pressure-modulation.png | Physics explanation | PowerPoint, Figma |
| 2 (Nice) | flexifoot-force-path.png | Force distribution | Inkscape, Adobe Draw |
| 2 (Nice) | neurovac-feedback-loop.png | Control strategy | Lucidchart, OmniGraffle |

---

# GRAPHIC SPECIFICATIONS

**All images should:**
- Use consistent color scheme (e.g., blue/gray palette)
- Include clear labels and scale bars where applicable
- Be PDF or PNG (PNG preferred for web)
- Have 150-300 DPI for printing quality
- Include 1-2 line caption below each image

**Caption style:**
```
*Fig [#]: [Brief description—what the figure shows]*
```

Example:
```
*Fig 3: Body weight transmitted to heel and mid-foot; forefoot compression without load transfer to surgical site*
```

---

# PLACEHOLDER STATUS IN WEBSITE

✅ **Already added to clinical-solutions.md:**
- Fig 1: flexifoot-outsole-diagram.png
- Fig 2: flexifoot-comparison.png
- Fig 3: flexifoot-force-path.png
- Fig 4: neurovac-system-schematic.png
- Fig 5: neurovac-pressure-modulation.png
- Fig 6: neurovac-feedback-loop.png

When you create each graphic, save it to `/medical-template/assets/img/` and the page will automatically display it.

---

# RECOMMENDED TOOLS

| Tool | Best For | Cost |
|------|----------|------|
| **PowerPoint** | Flowcharts, side-by-side comparisons, simple diagrams | Included in Office |
| **Figma** | Professional multi-panel layouts, color consistency | Free tier available |
| **Inkscape** | Precise technical drawings, SVG output | Free, open-source |
| **Lucidchart** | Complex feedback loops, flowcharts | Free tier available |
| **Adobe Illustrator** | Polish and vector quality | Subscription |

---

# NEXT STEPS

1. ✅ Page created with placeholders
2. ⏳ Create 6 graphics (Figures 1–6)
3. ⏳ Add them to `/assets/img/` folder
4. ⏳ Server will automatically display them

**Questions?** Let me know if you need specific graphic recommendations or alternative layouts.

