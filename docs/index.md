---
title: Explore
layout: default
---

<section class="world-hero" id="explore">
  <canvas class="world-hero__canvas" data-world-canvas aria-hidden="true"></canvas>
  <div class="world-hero__copy">
    <div class="world-kicker">Enter the system</div>
    <h1>Kadin El Bakkouri</h1>
    <p>Future physicianeer building clinically aware workflows, adaptive medical devices, computational research tools, and health systems that connect engineering skill to patient impact.</p>
    <div class="world-hero__actions">
      <a href="#constellation">Explore the constellation</a>
      <a href="#workbench">Open the workbench</a>
    </div>
  </div>
</section>

<section class="world-section world-section--constellation" id="constellation">
  <div class="world-section__header">
    <div>
      <div class="world-kicker">Explore</div>
      <h2>Constellation World</h2>
      <p>Projects, research, skills, organizations, hobbies, and goals arranged as a galaxy of connected ideas.</p>
    </div>
  </div>

  <div class="world-constellation" data-world-constellation>
    <svg class="world-constellation__links" viewBox="0 0 100 100" preserveAspectRatio="none" aria-hidden="true">
      <path data-link-category="access" d="M70 18 L82 23 L78 35 L63 32 L70 18 M63 32 L82 23" />
      <path data-link-category="research" d="M18 25 L29 35 L13 43 L18 25 M29 35 L13 43" />
      <path data-link-category="health" d="M51 26 L60 36 L69 44 L64 58 L53 66 L42 53 L51 26 M42 53 L60 36 M53 66 L69 44" />
      <path data-link-category="making" d="M16 69 L27 58 L38 68 L30 80 L16 69 M27 58 L30 80" />
      <path data-link-category="journey" d="M73 72 L84 79 L78 88 L68 83 L73 72 M84 79 L68 83" />
    </svg>

    <div class="world-cluster-label" style="--x:73; --y:11;" data-cluster-label="access">
      <span>GRiP</span>
      <em>leadership, prosthetics, operations</em>
    </div>
    <div class="world-cluster-label" style="--x:20; --y:17;" data-cluster-label="research">
      <span>BEAT Cancer</span>
      <em>models, image analysis, research overview</em>
    </div>
    <div class="world-cluster-label" style="--x:56; --y:20;" data-cluster-label="health">
      <span>Clinical Design</span>
      <em>devices, clinical ML, patient education</em>
    </div>
    <div class="world-cluster-label" style="--x:28; --y:89;" data-cluster-label="making">
      <span>Personal Projects</span>
      <em>apps, servers, prints, fabrication</em>
    </div>
    <div class="world-cluster-label" style="--x:77; --y:94;" data-cluster-label="journey">
      <span>Journey</span>
      <em>friends, food, fabrication, family</em>
    </div>

    <a class="world-node" style="--x:70; --y:18; --s:0.96;" href="{{ '/projects/grip-admin-platform/' | relative_url }}" data-category="access">
      <span></span>
      <strong>GRiP Admin</strong>
      <em>operations</em>
    </a>
    <a class="world-node" style="--x:82; --y:23; --s:0.86;" href="{{ '/projects/grip-bike-prosthetics/' | relative_url }}" data-category="access">
      <span></span>
      <strong>GRiP Bike</strong>
      <em>prosthetic cycling</em>
    </a>
    <a class="world-node" style="--x:63; --y:32; --s:0.8;" href="{{ '/leadership/' | relative_url }}" data-category="access">
      <span></span>
      <strong>Leadership + Events</strong>
      <em>community</em>
    </a>

    <a class="world-node" style="--x:18; --y:25; --s:0.92;" href="{{ '/projects/disease-treatment-modeling/' | relative_url }}" data-category="research">
      <span></span>
      <strong>Disease Modeling</strong>
      <em>population dynamics</em>
    </a>
    <a class="world-node" style="--x:29; --y:35; --s:0.78;" href="{{ '/projects/qupath-cell-count-pipeline/' | relative_url }}" data-category="research">
      <span></span>
      <strong>QuPath Pipeline</strong>
      <em>image analysis</em>
    </a>
    <a class="world-node" style="--x:13; --y:43; --s:0.72;" href="{{ '/research/' | relative_url }}" data-category="research">
      <span></span>
      <strong>Research Overview</strong>
      <em>lab thread</em>
    </a>
    <a class="world-node" style="--x:51; --y:26; --s:0.78;" href="{{ '/projects/heart-smart/' | relative_url }}" data-category="health">
      <span></span>
      <strong>Heart Smart</strong>
      <em>education device</em>
    </a>
    <a class="world-node" style="--x:60; --y:36; --s:0.76;" href="{{ '/projects/neurovac/' | relative_url }}" data-category="health">
      <span></span>
      <strong>NeuroVac</strong>
      <em>device concept</em>
    </a>
    <a class="world-node" style="--x:69; --y:44; --s:0.7;" href="{{ '/projects/retractor-arm/' | relative_url }}" data-category="health">
      <span></span>
      <strong>Retractor Arm</strong>
      <em>mechanics</em>
    </a>
    <a class="world-node" style="--x:42; --y:53; --s:0.72;" href="{{ '/projects/vitalintel/' | relative_url }}" data-category="health">
      <span></span>
      <strong>VitalIntel</strong>
      <em>clinical ML</em>
    </a>
    <a class="world-node" style="--x:53; --y:66; --s:0.7;" href="{{ '/projects/assistive-prosthetics/' | relative_url }}" data-category="health">
      <span></span>
      <strong>Flexi-Foot</strong>
      <em>post-op footwear</em>
    </a>
    <a class="world-node" style="--x:64; --y:58; --s:0.68;" href="https://kadinelbak.github.io/HIV-Proteases-Detector/" target="_blank" rel="noreferrer" data-category="health">
      <span></span>
      <strong>HIV-1 Protease</strong>
      <em>drug discovery ML</em>
    </a>

    <a class="world-node" style="--x:16; --y:69; --s:0.78;" href="{{ '/projects/homelab-infrastructure/' | relative_url }}" data-category="making">
      <span></span>
      <strong>Homelab</strong>
      <em>server systems</em>
    </a>
    <a class="world-node" style="--x:27; --y:58; --s:0.74;" href="{{ '/projects/forge-labs-fitness/' | relative_url }}" data-category="making">
      <span></span>
      <strong>ForgeLabs</strong>
      <em>nutrition app</em>
    </a>
    <a class="world-node" style="--x:30; --y:80; --s:0.76;" href="{{ '/fabrication/' | relative_url }}" data-category="making">
      <span></span>
      <strong>Fabrication</strong>
      <em>CAD to print</em>
    </a>
    <a class="world-node" style="--x:38; --y:68; --s:0.68;" href="https://makerworld.com/en/@KadinKreates/upload" target="_blank" rel="noreferrer" data-category="making">
      <span></span>
      <strong>MakerWorld</strong>
      <em>published prints</em>
    </a>

    <a class="world-node" style="--x:73; --y:72; --s:0.9;" href="{{ '/journey/' | relative_url }}" data-category="journey">
      <span></span>
      <strong>Journey Map</strong>
      <em>life map</em>
    </a>
    <a class="world-node" style="--x:84; --y:79; --s:0.72;" href="{{ '/journey/' | relative_url }}" data-category="journey">
      <span></span>
      <strong>Cooking + Making</strong>
      <em>craft, circuits, 3D prints</em>
    </a>
    <a class="world-node" style="--x:78; --y:88; --s:0.7;" href="{{ '/journey/' | relative_url }}" data-category="journey">
      <span></span>
      <strong>Photo Story</strong>
      <em>2023-2025</em>
    </a>
  </div>
</section>

<section class="world-section world-section--workbench" id="workbench">
  <div class="world-section__header">
    <div>
      <div class="world-kicker">Workbench</div>
      <h2>How the Things Were Built</h2>
      <p>A table of artifacts: prototypes, notebooks, simulations, code, prints, and device concepts.</p>
    </div>
  </div>

  <div class="artifact-bench" aria-label="Interactive project workbench">
    <a class="artifact artifact--notebook" href="{{ '/projects/disease-treatment-modeling/' | relative_url }}">
      <span></span>
      <strong>Research Notebook</strong>
      <em>ODEs, fits, model selection</em>
    </a>
    <a class="artifact artifact--phone" href="{{ '/projects/forge-labs-fitness/' | relative_url }}">
      <span></span>
      <strong>App Prototype</strong>
      <em>biometrics to execution</em>
    </a>
    <a class="artifact artifact--server" href="{{ '/projects/homelab-infrastructure/' | relative_url }}">
      <span></span>
      <strong>Server Stack</strong>
      <em>identity, monitoring, services</em>
    </a>
    <a class="artifact artifact--cad" href="{{ '/projects/retractor-arm/' | relative_url }}">
      <span></span>
      <strong>CAD Assembly</strong>
      <em>FEA, locks, layer jamming</em>
    </a>
    <a class="artifact artifact--print" href="{{ '/fabrication/' | relative_url }}">
      <span></span>
      <strong>Print Tray</strong>
      <em>MakerWorld objects</em>
    </a>
    <a class="artifact artifact--badge" href="{{ '/leadership/' | relative_url }}">
      <span></span>
      <strong>Event Board</strong>
      <em>teams, designathons, impact</em>
    </a>
  </div>
</section>

<section class="world-section world-section--gallery" id="gallery">
  <div class="world-section__header">
    <div>
      <div class="world-kicker">Gallery</div>
      <h2>Museum of Impact</h2>
      <p>A curated hall for the work that should matter most to recruiters, collaborators, admissions committees, and investors.</p>
    </div>
  </div>

  <div class="museum-hall">
    <a class="exhibit-case exhibit-case--large" href="{{ '/projects/disease-treatment-modeling/' | relative_url }}">
      <span>Research</span>
      <strong>Disease & Treatment Modeling</strong>
      <p>Transforms experimental growth curves into interpretable parameters for treatment strategy reasoning.</p>
    </a>
    <a class="exhibit-case" href="{{ '/projects/forge-labs-fitness/' | relative_url }}">
      <span>Shipped Product</span>
      <strong>ForgeLabs Fitness</strong>
      <p>Mobile health app connecting biometric context, nutrition planning, workouts, and grocery execution.</p>
    </a>
    <a class="exhibit-case" href="{{ '/projects/homelab-infrastructure/' | relative_url }}">
      <span>Infrastructure</span>
      <strong>Homelab</strong>
      <p>A live server ecosystem for services, monitoring, backups, media, AI, and access control.</p>
    </a>
    <a class="exhibit-case" href="{{ '/leadership/' | relative_url }}">
      <span>Leadership</span>
      <strong>HealthHacks + GRiP Designathon</strong>
      <p>Design events that turned student teams into useful assistive-technology project pipelines.</p>
    </a>
  </div>
</section>

<section class="world-section world-section--journey" id="journey">
  <div class="world-section__header">
    <div>
      <div class="world-kicker">Journey</div>
      <h2>Explorer's Journal</h2>
      <p>A photo story about friends, cooking, circuits, 3D printing, family, travel, and the person behind the engineering.</p>
    </div>
    <a class="world-section__link" href="{{ '/journey/' | relative_url }}">Open the journey map</a>
  </div>

  <div class="journey-strip" aria-label="Journey themes">
    <a data-kind="travel" href="{{ '/journey/travel/' | relative_url }}">Travel</a>
    <a data-kind="outdoors" href="{{ '/journey/photography/' | relative_url }}">Photography</a>
    <a data-kind="conference" href="{{ '/journey/circuits-prints/' | relative_url }}">Circuits + Prints</a>
    <a data-kind="volunteer" href="{{ '/journey/friends-family/' | relative_url }}">Friends + Family</a>
    <a data-kind="hobby" href="{{ '/journey/cooking/' | relative_url }}">Cooking</a>
  </div>
</section>

<section class="world-contact" id="contact">
  <div>
    <span>Contact</span>
    <strong>Kadin El Bakkouri</strong>
    <p><a href="mailto:kelbakkouri@ufl.edu">kelbakkouri@ufl.edu</a> | <a href="https://github.com/kadinelbak">GitHub</a> | <a href="https://www.linkedin.com/in/kadin-el-bakkouri-09531b289/">LinkedIn</a></p>
  </div>
  <div>
    <a href="{{ '/assets/pdf/Kadin El Bakkouri CV.pdf' | relative_url }}" download>Download CV</a>
    <a href="{{ '/assets/pdf/Resume.pdf' | relative_url }}" download>Download Resume</a>
  </div>
</section>
