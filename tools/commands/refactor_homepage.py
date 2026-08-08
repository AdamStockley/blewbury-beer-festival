from __future__ import annotations

import argparse
from pathlib import Path
from textwrap import dedent


FILES = {
    "src/components/FestivalHero.astro": r"""
---
import { festival } from "../data/festival";
---

<section class="hero hero-compact">
  <div class="hero-decoration hero-decoration-one"></div>
  <div class="hero-decoration hero-decoration-two"></div>

  <div class="container hero-inner hero-inner-compact">
    <div class="hero-topline">
      <span>{festival.location}</span>
      <span>Saturday 3 October 2026</span>
    </div>

    <div class="hero-main hero-main-compact">
      <p class="hero-kicker">SAVE THE DATE</p>

      <h1>
        Blewbury
        <span>Beer Festival</span>
      </h1>

      <div class="hero-date hero-date-compact">
        <span class="hero-day">SAT</span>
        <strong>03</strong>
        <div>
          <span>OCTOBER</span>
          <span>2026</span>
        </div>
      </div>

      <p class="hero-description">
        Good beer. Good music. Good company.<br />
        All in support of good causes.
      </p>

      <div class="button-row">
        <a class="button button-light" href="/plan-your-day">
          Plan your visit
        </a>

        <a class="text-link-light" href="/drinks">
          What's on the bar? <span>→</span>
        </a>
      </div>
    </div>

    <div class="hero-bottom">
      <p>{festival.strapline}</p>
    </div>
  </div>
</section>
""",

    "src/components/CountdownStrip.astro": r"""
---
import { festival } from "../data/festival";
---

<section class="countdown-section countdown-section-compact">
  <div class="container countdown-grid countdown-grid-compact">
    <div>
      <p class="eyebrow eyebrow-dark">COUNTING DOWN</p>
      <h2>See you in October.</h2>
    </div>

    <div
      class="countdown"
      data-countdown={festival.dateISO}
      aria-label="Countdown to Blewbury Beer Festival"
    >
      <div class="countdown-unit">
        <strong data-days>--</strong>
        <span>Days</span>
      </div>

      <div class="countdown-unit">
        <strong data-hours>--</strong>
        <span>Hours</span>
      </div>

      <div class="countdown-unit">
        <strong data-minutes>--</strong>
        <span>Minutes</span>
      </div>
    </div>
  </div>
</section>

<script is:inline>
  (() => {
    const el = document.querySelector("[data-countdown]");
    if (!el) return;

    const target = new Date(el.dataset.countdown).getTime();

    const daysEl = el.querySelector("[data-days]");
    const hoursEl = el.querySelector("[data-hours]");
    const minutesEl = el.querySelector("[data-minutes]");

    function update() {
      const now = Date.now();
      const remaining = Math.max(0, target - now);

      const days = Math.floor(remaining / (1000 * 60 * 60 * 24));
      const hours = Math.floor((remaining / (1000 * 60 * 60)) % 24);
      const minutes = Math.floor((remaining / (1000 * 60)) % 60);

      daysEl.textContent = String(days);
      hoursEl.textContent = String(hours).padStart(2, "0");
      minutesEl.textContent = String(minutes).padStart(2, "0");
    }

    update();
    setInterval(update, 60000);
  })();
</script>
""",

    "src/components/FeatureGrid.astro": r"""
---
const features = [
  {
    kicker: "BEER & CIDER",
    title: "What's on the bar?",
    text: "We're choosing the 2026 line-up now. Breweries and drinks will appear as they're confirmed.",
    href: "/drinks",
    link: "See the drinks",
  },
  {
    kicker: "LIVE MUSIC",
    title: "Who's playing?",
    text: "The entertainment programme is taking shape. We'll add performers and timings as bookings are confirmed.",
    href: "/entertainment",
    link: "See the line-up",
  },
  {
    kicker: "FOOD",
    title: "What's cooking?",
    text: "Food details are being finalised and will be published here as soon as they're confirmed.",
    href: "/food",
    link: "See the food",
  },
];
---

<section class="home-features">
  <div class="container">
    <div class="home-feature-grid">
      {features.map((feature) => (
        <a class="home-feature-card" href={feature.href}>
          <p class="eyebrow">{feature.kicker}</p>
          <h2>{feature.title}</h2>
          <p>{feature.text}</p>
          <span>{feature.link} →</span>
        </a>
      ))}
    </div>
  </div>
</section>
""",

    "src/components/GoodCausesBand.astro": r"""
---
import { festival } from "../data/festival";
---

<section class="home-causes">
  <div class="container home-causes-grid">
    <div>
      <p class="eyebrow eyebrow-gold">THE IMPORTANT BIT</p>
      <h2>Drinking beer.<br />Doing good.</h2>
    </div>

    <div class="home-causes-copy">
      <p class="home-causes-strapline">{festival.strapline}</p>
      <p>
        The festival brings people together and raises money for worthwhile
        causes. We'll announce the 2026 beneficiaries as they're confirmed.
      </p>
      <a class="text-link-light" href="/causes">
        Our good causes <span>→</span>
      </a>
    </div>
  </div>
</section>
""",

    "src/components/LatestUpdate.astro": r"""
---
import { news } from "../data/festival";

const latest = news[0];
---

<section class="home-latest">
  <div class="container home-latest-grid">
    <div>
      <p class="eyebrow">LATEST</p>
      <h2>Festival news</h2>
    </div>

    {latest && (
      <article class="home-latest-card">
        <div class="news-meta">{latest.date}</div>
        <h3>{latest.title}</h3>
        <p>{latest.text}</p>
      </article>
    )}
  </div>
</section>
""",

    "src/components/VolunteerCTA.astro": r"""
<section class="home-volunteer">
  <div class="container home-volunteer-grid">
    <div>
      <p class="eyebrow eyebrow-dark">GET INVOLVED</p>
      <h2>Festivals don't run themselves.</h2>
      <p>
        If you'd like to lend a hand before or during the festival, we'd love
        to hear from you.
      </p>
    </div>

    <a class="button button-dark" href="/volunteer">
      Volunteer for 2026 →
    </a>
  </div>
</section>
""",

    "src/pages/index.astro": r"""
---
import BaseLayout from "../layouts/BaseLayout.astro";
import Header from "../components/Header.astro";
import Footer from "../components/Footer.astro";
import FestivalHero from "../components/FestivalHero.astro";
import CountdownStrip from "../components/CountdownStrip.astro";
import FeatureGrid from "../components/FeatureGrid.astro";
import GoodCausesBand from "../components/GoodCausesBand.astro";
import LatestUpdate from "../components/LatestUpdate.astro";
import VolunteerCTA from "../components/VolunteerCTA.astro";
import "../styles/global.css";
---

<BaseLayout>
  <Header />

  <main>
    <FestivalHero />
    <CountdownStrip />
    <FeatureGrid />
    <GoodCausesBand />
    <LatestUpdate />
    <VolunteerCTA />
  </main>

  <Footer />
</BaseLayout>
""",

    "src/styles/homepage.css": r"""
/*
 * Homepage-specific layout for the concise 2026 landing page.
 * Imported by global.css.
 */

.hero-compact {
  min-height: 76vh;
}

.hero-inner-compact {
  min-height: 76vh;
}

.hero-main-compact {
  padding: 2.5rem 0 2rem;
}

.hero-date-compact {
  margin-top: -0.25rem;
}

.countdown-section-compact {
  padding: 2.4rem 0;
}

.countdown-grid-compact {
  align-items: center;
}

.countdown-grid-compact h2 {
  font-size: clamp(2rem, 3.5vw, 3.6rem);
}

.home-features {
  padding: 4.5rem 0;
  background: var(--cream-light);
}

.home-feature-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  border-top: 1px solid var(--border-dark);
  border-bottom: 1px solid var(--border-dark);
}

.home-feature-card {
  min-height: 300px;
  padding: 2rem;
  text-decoration: none;
  border-right: 1px solid var(--border-dark);
  display: flex;
  flex-direction: column;
}

.home-feature-card:first-child {
  padding-left: 0;
}

.home-feature-card:last-child {
  border-right: 0;
}

.home-feature-card h2 {
  font-size: clamp(2rem, 3.5vw, 3.6rem);
  margin-bottom: 1rem;
}

.home-feature-card p:not(.eyebrow) {
  color: var(--muted);
  max-width: 32rem;
}

.home-feature-card span {
  margin-top: auto;
  font-weight: 850;
}

.home-causes {
  padding: 5.5rem 0;
  background: var(--green);
  color: white;
}

.home-causes-grid {
  display: grid;
  grid-template-columns: 1.15fr 0.8fr;
  gap: 6rem;
  align-items: end;
}

.home-causes h2 {
  margin-bottom: 0;
  font-size: clamp(3rem, 6vw, 6rem);
}

.home-causes-copy {
  color: rgba(255,255,255,0.78);
}

.home-causes-strapline {
  color: white;
  font-size: 1.2rem;
  font-style: italic;
}

.home-latest {
  padding: 4.5rem 0;
  background: #e8dbc5;
}

.home-latest-grid {
  display: grid;
  grid-template-columns: 0.65fr 1.35fr;
  gap: 5rem;
  align-items: start;
}

.home-latest h2 {
  font-size: clamp(2.6rem, 4.5vw, 4.4rem);
  margin-bottom: 0;
}

.home-latest-card {
  border-top: 1px solid var(--border-dark);
  padding-top: 1.5rem;
}

.home-latest-card .news-meta {
  margin-bottom: 1.2rem;
}

.home-latest-card h3 {
  margin-bottom: 0.75rem;
  font-size: clamp(1.7rem, 3vw, 2.6rem);
}

.home-latest-card p {
  color: var(--muted);
  max-width: 42rem;
}

.home-volunteer {
  padding: 3.5rem 0;
  background: var(--gold);
}

.home-volunteer-grid {
  display: grid;
  grid-template-columns: 1fr auto;
  gap: 3rem;
  align-items: center;
}

.home-volunteer h2 {
  margin-bottom: 0.75rem;
  font-size: clamp(2.4rem, 4vw, 4rem);
}

.home-volunteer p:not(.eyebrow) {
  margin-bottom: 0;
  max-width: 42rem;
}

@media (max-width: 950px) {
  .hero-compact,
  .hero-inner-compact {
    min-height: 68vh;
  }

  .home-feature-grid {
    grid-template-columns: 1fr;
  }

  .home-feature-card,
  .home-feature-card:first-child {
    min-height: auto;
    padding: 2rem 0;
    border-right: 0;
    border-bottom: 1px solid var(--border-dark);
  }

  .home-feature-card:last-child {
    border-bottom: 0;
  }

  .home-feature-card span {
    margin-top: 1rem;
  }

  .home-causes-grid,
  .home-latest-grid,
  .home-volunteer-grid {
    grid-template-columns: 1fr;
    gap: 2rem;
  }
}

@media (max-width: 720px) {
  .hero-compact,
  .hero-inner-compact {
    min-height: 620px;
  }

  .hero-main-compact {
    padding: 2rem 0 1.5rem;
  }

  .countdown-section-compact {
    padding: 2rem 0;
  }

  .countdown-grid-compact {
    gap: 1.25rem;
  }

  .home-features,
  .home-latest {
    padding: 3.5rem 0;
  }

  .home-causes {
    padding: 4rem 0;
  }

  .home-volunteer {
    padding: 3rem 0;
  }
}
""",
}


def _write(root: Path, relative: str, content: str, check_only: bool) -> bool:
    path = root / relative
    wanted = dedent(content).lstrip()
    current = path.read_text(encoding="utf-8") if path.exists() else None
    changed = current != wanted

    if check_only:
        print(f"{'DIFF' if changed else 'OK':4} {relative}")
        return changed

    path.parent.mkdir(parents=True, exist_ok=True)
    if changed:
        path.write_text(wanted, encoding="utf-8")
        print(f"WROTE {relative}")
    else:
        print(f"OK    {relative}")
    return changed


def _ensure_global_import(root: Path, check_only: bool) -> bool:
    path = root / "src/styles/global.css"
    if not path.exists():
        raise FileNotFoundError("src/styles/global.css was not found")

    current = path.read_text(encoding="utf-8")
    marker = '@import "./homepage.css";'

    if marker in current:
        print("OK    src/styles/global.css (homepage import present)")
        return False

    if check_only:
        print("DIFF  src/styles/global.css (homepage import missing)")
        return True

    path.write_text(marker + "\n\n" + current, encoding="utf-8")
    print("WROTE src/styles/global.css (added homepage import)")
    return True


def run(args: argparse.Namespace, root: Path) -> int:
    changed = 0

    for relative, content in FILES.items():
        changed += int(_write(root, relative, content, args.check))

    changed += int(_ensure_global_import(root, args.check))

    if args.check:
        print(f"\n{changed} homepage file(s) differ.")
        return 1 if changed else 0

    print(f"\nHomepage refactor complete. {changed} file(s) changed.")
    print("Next: run `npm run build` and review the site locally.")
    return 0


def register(subparsers) -> None:
    parser = subparsers.add_parser(
        "refactor-homepage",
        help="Refactor the homepage into reusable components and shorten it.",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Check whether the homepage refactor is current without changing files.",
    )
    parser.set_defaults(func=run)
