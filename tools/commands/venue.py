from __future__ import annotations

import argparse
import re
from pathlib import Path
from textwrap import dedent


VISIT_PAGE = """
---
import BaseLayout from "../layouts/BaseLayout.astro";
import Header from "../components/Header.astro";
import Footer from "../components/Footer.astro";
import { festival } from "../data/festival";
import "../styles/global.css";
---

<BaseLayout
  title="Plan Your Visit | Blewbury Beer Festival 2026"
  description="Plan your visit to Blewbury Beer Festival at Blewbury Village Hall on Saturday 3 October 2026."
>
  <Header />

  <main class="visit-page">
    <section class="page-hero page-hero-visit">
      <div class="container">
        <p class="eyebrow eyebrow-gold">SATURDAY 3 OCTOBER 2026</p>
        <h1>Plan your visit.</h1>
        <p class="page-hero-lead">
          {festival.venue}<br />
          {festival.address.street}<br />
          {festival.address.locality}, {festival.address.postcode}
        </p>
      </div>
    </section>

    <section class="visit-details">
      <div class="container visit-details-grid">
        <div class="visit-primary">
          <p class="eyebrow">VENUE</p>
          <h2>Blewbury Village Hall</h2>

          <address class="venue-address">
            Church End<br />
            Blewbury<br />
            Didcot<br />
            Oxfordshire<br />
            OX11 9QQ
          </address>

          <div class="visit-actions">
            <a
              class="button button-dark"
              href="https://www.google.com/maps/search/?api=1&query=Blewbury+Village+Hall+OX11+9QQ"
              target="_blank"
              rel="noopener noreferrer"
            >
              Open in Google Maps ↗
            </a>
          </div>
        </div>

        <div class="visit-note">
          <p class="eyebrow">GOOD TO KNOW</p>
          <h3>We're still filling in the practical details.</h3>
          <p>
            The venue and date are confirmed. Opening times, parking
            arrangements, accessibility information and other practical
            details will be added as the festival plans are finalised.
          </p>
        </div>
      </div>
    </section>

    <section class="visit-info">
      <div class="container">
        <div class="visit-info-grid">
          <article class="visit-info-card">
            <p class="eyebrow">OPENING TIMES</p>
            <h3>Coming soon</h3>
            <p>Festival opening and closing times will be published here once confirmed.</p>
          </article>

          <article class="visit-info-card">
            <p class="eyebrow">PARKING</p>
            <h3>Details to follow</h3>
            <p>We'll publish the recommended parking arrangements before the festival.</p>
          </article>

          <article class="visit-info-card">
            <p class="eyebrow">ACCESSIBILITY</p>
            <h3>Details to follow</h3>
            <p>Accessibility information for the festival setup will be added once arrangements are confirmed.</p>
          </article>

          <article class="visit-info-card">
            <p class="eyebrow">GETTING HERE</p>
            <h3>Blewbury, Oxfordshire</h3>
            <p>Information for walking, cycling and public transport will be added closer to the event.</p>
          </article>

          <article class="visit-info-card">
            <p class="eyebrow">PAYMENT</p>
            <h3>To be confirmed</h3>
            <p>We'll confirm payment arrangements for the bar and food vendors before festival day.</p>
          </article>

          <article class="visit-info-card">
            <p class="eyebrow">QUESTIONS?</p>
            <h3>More FAQs coming</h3>
            <p>We'll add the common practical questions here as plans are finalised.</p>
          </article>
        </div>
      </div>
    </section>
  </main>

  <Footer />
</BaseLayout>
"""


VISIT_CSS = """
.visit-page { background: var(--cream); }

.page-hero { padding: 10rem 0 5rem; }

.page-hero-visit {
  background:
    radial-gradient(circle at 85% 25%, rgba(217,154,41,0.26), transparent 24rem),
    linear-gradient(135deg, var(--burgundy-dark), var(--burgundy));
  color: white;
}

.page-hero h1 {
  max-width: 950px;
  margin-bottom: 2rem;
  font-size: clamp(4rem, 9vw, 8rem);
  line-height: 0.84;
}

.page-hero-lead {
  margin: 0;
  font-size: clamp(1.15rem, 2vw, 1.5rem);
  color: rgba(255,255,255,0.8);
}

.visit-details { padding: 5rem 0; }

.visit-details-grid {
  display: grid;
  grid-template-columns: 1fr 0.8fr;
  gap: 6rem;
}

.visit-primary h2 {
  margin-bottom: 2rem;
  font-size: clamp(2.8rem, 5vw, 5rem);
}

.venue-address {
  font-style: normal;
  font-size: 1.2rem;
  line-height: 1.65;
}

.visit-actions { margin-top: 2rem; }

.visit-note {
  padding: 2rem;
  align-self: start;
  border-top: 1px solid var(--border-dark);
  border-bottom: 1px solid var(--border-dark);
}

.visit-note h3 {
  font-size: clamp(1.8rem, 3vw, 2.8rem);
  line-height: 1;
}

.visit-note p:not(.eyebrow),
.visit-info-card p:not(.eyebrow) {
  color: var(--muted);
}

.visit-info { padding: 1rem 0 6rem; }

.visit-info-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  border-top: 1px solid var(--border-dark);
  border-left: 1px solid var(--border-dark);
}

.visit-info-card {
  min-height: 250px;
  padding: 2rem;
  border-right: 1px solid var(--border-dark);
  border-bottom: 1px solid var(--border-dark);
}

.visit-info-card h3 {
  margin-bottom: 1rem;
  font-size: 1.7rem;
}

@media (max-width: 950px) {
  .visit-details-grid {
    grid-template-columns: 1fr;
    gap: 3rem;
  }

  .visit-info-grid { grid-template-columns: repeat(2, 1fr); }
}

@media (max-width: 720px) {
  .page-hero { padding: 8rem 0 4rem; }
  .visit-details { padding: 4rem 0; }
  .visit-info { padding-bottom: 4rem; }
  .visit-info-grid { grid-template-columns: 1fr; }
  .visit-info-card { min-height: auto; }
}
"""


def update_festival_data(root: Path) -> None:
    path = root / "src/data/festival.ts"
    text = path.read_text(encoding="utf-8")

    text = re.sub(
        r'location:\\s*"[^"]*",',
        'location: "Blewbury Village Hall, Blewbury, Oxfordshire",',
        text,
        count=1,
    )
    text = re.sub(
        r'venue:\\s*"[^"]*",',
        'venue: "Blewbury Village Hall",',
        text,
        count=1,
    )

    if "address:" not in text:
        marker = '  venue: "Blewbury Village Hall",\n'
        addition = (
            '  address: {\n'
            '    street: "Church End",\n'
            '    locality: "Blewbury",\n'
            '    town: "Didcot",\n'
            '    region: "Oxfordshire",\n'
            '    postcode: "OX11 9QQ",\n'
            '    country: "GB",\n'
            '  },\n'
        )
        text = text.replace(marker, marker + addition, 1)

    path.write_text(text, encoding="utf-8")
    print("WROTE src/data/festival.ts")


def update_base_layout(root: Path) -> None:
    path = root / "src/layouts/BaseLayout.astro"
    text = path.read_text(encoding="utf-8")
    text = text.replace('name: "Blewbury, Oxfordshire",', 'name: "Blewbury Village Hall",')

    old = (
        'address: {\n'
        '            "@type": "PostalAddress",\n'
        '            addressLocality: "Blewbury",\n'
        '            addressRegion: "Oxfordshire",\n'
        '            addressCountry: "GB"\n'
        '          }'
    )
    new = (
        'address: {\n'
        '            "@type": "PostalAddress",\n'
        '            streetAddress: "Church End",\n'
        '            addressLocality: "Blewbury",\n'
        '            postalCode: "OX11 9QQ",\n'
        '            addressRegion: "Oxfordshire",\n'
        '            addressCountry: "GB"\n'
        '          }'
    )
    text = text.replace(old, new)
    path.write_text(text, encoding="utf-8")
    print("WROTE src/layouts/BaseLayout.astro")


def update_header(root: Path) -> None:
    path = root / "src/components/Header.astro"
    text = path.read_text(encoding="utf-8").replace('>Visit</a>', '>Plan Your Visit</a>')
    path.write_text(text, encoding="utf-8")
    print("WROTE src/components/Header.astro")


def write_file(root: Path, relative: str, content: str) -> None:
    path = root / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(dedent(content).lstrip(), encoding="utf-8")
    print(f"WROTE {relative}")


def ensure_css_import(root: Path) -> None:
    path = root / "src/styles/global.css"
    text = path.read_text(encoding="utf-8")
    marker = '@import "./visit.css";'
    if marker not in text:
        homepage = '@import "./homepage.css";'
        text = text.replace(homepage, homepage + "\n" + marker, 1) if homepage in text else marker + "\n\n" + text
        path.write_text(text, encoding="utf-8")
        print("WROTE src/styles/global.css")
    else:
        print("OK    src/styles/global.css")


def run(args: argparse.Namespace, root: Path) -> int:
    update_festival_data(root)
    update_base_layout(root)
    update_header(root)
    write_file(root, "src/pages/plan-your-day.astro", VISIT_PAGE)
    write_file(root, "src/styles/visit.css", VISIT_CSS)
    ensure_css_import(root)
    print("\nVenue and Visit page update complete.")
    return 0


def register(subparsers) -> None:
    parser = subparsers.add_parser(
        "venue",
        help="Apply confirmed Blewbury Village Hall details and build the Visit page.",
    )
    parser.set_defaults(func=run)
