import { Link } from "react-router-dom";
import { useState } from "react";
import RevealOnScroll from "../components/RevealOnScroll";

const TRUST_ITEMS = [
  "Kigali",
  "Environmental monitoring",
  "Machine learning",
  "Governance analytics",
  "Compliance assessment",
];

const SCENARIOS = [
  { time: "Today · 14:32", text: "Construction noise near residential zone" },
  { time: "Yesterday · 22:15", text: "Night-time traffic exceedance detected" },
  { time: "Mon · 09:08", text: "Commercial venue within legal limits" },
  { time: "Sun · 18:40", text: "Industrial zone moderate severity alert" },
  { time: "Sat · 11:22", text: "Quiet zone compliance verified" },
];

const TESTIMONIALS = [
  {
    quote:
      "UNGS helped our team move from guesswork to evidence. We can now show exactly when and where noise limits were exceeded.",
    name: "Environmental officer, Kigali",
  },
  {
    quote:
      "Uploading a recording and getting compliance status in seconds changed how we respond to community complaints.",
    name: "Urban planning researcher",
  },
];

const FAQ_ITEMS = [
  {
    q: "What audio format is supported?",
    a: "The system accepts WAV recordings. Upload a clear sample of the noise event you want analyzed.",
  },
  {
    q: "How is compliance determined?",
    a: "Recorded levels are compared against venue-based legal limits for Kigali, adjusted for day or night periods.",
  },
  {
    q: "Can I download a formal report?",
    a: "Yes. After each analysis you can generate and download a PDF report for records or governance review.",
  },
  {
    q: "Is my data stored securely?",
    a: "Analysis results are saved locally on the server for history and dashboard views. No login is required for v1.",
  },
];

function FaqItem({ question, answer }) {
  const [open, setOpen] = useState(false);

  return (
    <div className={`faq-item ${open ? "is-open" : ""}`}>
      <button
        type="button"
        className="faq-trigger"
        onClick={() => setOpen((o) => !o)}
        aria-expanded={open}
      >
        {question}
        <span className="faq-icon" aria-hidden="true">
          +
        </span>
      </button>
      <div className="faq-panel">
        <div className="faq-panel-inner">
          <p>{answer}</p>
        </div>
      </div>
    </div>
  );
}

function LandingPage() {
  const [email, setEmail] = useState("");
  const [waitlistSent, setWaitlistSent] = useState(false);

  const handleWaitlist = (e) => {
    e.preventDefault();
    if (!email.trim()) return;
    setWaitlistSent(true);
    setEmail("");
  };

  return (
    <div className="landing">
      {/* 1 — Hero */}
      <section className="hero">
        <div className="hero-inner reveal">
          <div className="hero-badge">ML powered urban noise governance</div>

          <h1 className="hero-title">
            Smarter
            <span className="script accent-word">Noise</span>
            governance for healthier cities
          </h1>

          <p className="hero-subtitle">
            Analyze environmental noise, detect violations, assess governance
            risks, and support evidence based decision making.
          </p>

          <div className="hero-actions">
            <Link to="/analyze" className="primary-btn">
              Start analysis
            </Link>
            <Link to="/dashboard" className="secondary-btn">
              View dashboard
            </Link>
          </div>
        </div>
      </section>

      {/* 2 — Trust bar */}
      <section className="trust-bar" aria-hidden="true">
        <div className="trust-bar-track">
          {[...TRUST_ITEMS, ...TRUST_ITEMS].map((item, i) => (
            <span key={`${item}-${i}`}>{item}</span>
          ))}
        </div>
      </section>

      {/* 3 — Scenario scroll */}
      <section>
        <div className="landing-container">
          <RevealOnScroll>
            <header className="landing-section-header">
              <h2>Recent scenarios</h2>
              <p>
                Sample noise events classified by source, severity, and
                compliance status.
              </p>
            </header>
          </RevealOnScroll>
        </div>
        <div className="landing-container landing-container--wide">
          <RevealOnScroll>
            <div className="scenario-scroll-wrap">
              <div className="scenario-scroll">
                {SCENARIOS.map((s) => (
                  <article key={s.time + s.text} className="scenario-card">
                    <span className="scenario-card-time">{s.time}</span>
                    <p className="scenario-card-text">{s.text}</p>
                  </article>
                ))}
              </div>
            </div>
          </RevealOnScroll>
        </div>
      </section>

      {/* 4 — App preview */}
      <section className="phone-stack-section">
        <div className="landing-container">
          <RevealOnScroll>
            <header className="landing-section-header landing-section-header--center">
              <h2>See the experience</h2>
              <p>
                Upload, classify, and review compliance from a calm,
                mobile-first interface.
              </p>
            </header>
          </RevealOnScroll>

          <RevealOnScroll>
            <div className="phone-stack">
              <div className="phone-mockup phone-mockup--left">
                <div className="phone-screen">
                  <div className="phone-notch" />
                  <span className="phone-label">History</span>
                  <span className="phone-stat">12</span>
                  <span className="phone-label">Reports saved</span>
                  <div className="phone-mini-bar">
                    <div
                      className="phone-mini-bar-fill"
                      style={{ width: "72%" }}
                    />
                  </div>
                </div>
              </div>

              <div className="phone-mockup phone-mockup--center">
                <div className="phone-screen">
                  <div className="phone-notch" />
                  <span className="phone-label">Estimated level</span>
                  <span className="phone-stat">74 dB</span>
                  <span className="phone-label">Construction · Night</span>
                  <span className="phone-pulse-btn">Analyze</span>
                </div>
              </div>

              <div className="phone-mockup phone-mockup--right">
                <div className="phone-screen">
                  <div className="phone-notch" />
                  <span className="phone-label">Compliance</span>
                  <span className="phone-stat">68%</span>
                  <span className="phone-label">Across all venues</span>
                  <div className="phone-mini-bar">
                    <div
                      className="phone-mini-bar-fill"
                      style={{ width: "68%" }}
                    />
                  </div>
                </div>
              </div>
            </div>
          </RevealOnScroll>
        </div>
      </section>

      {/* 5 — Features */}
      <section>
        <div className="landing-container">
          <RevealOnScroll>
            <header className="landing-section-header">
              <h2>What you can do</h2>
              <p>
                End-to-end noise governance from upload to policy-ready
                recommendations.
              </p>
            </header>
          </RevealOnScroll>

          <RevealOnScroll>
            <div className="feature-grid">
              <div className="feature-large">
                <h2>Noise analysis</h2>
                <p>
                  Upload audio recordings and automatically estimate noise
                  levels using ML powered acoustic processing and source
                  classification.
                </p>
              </div>
              <div className="feature-small">
                <h3>Compliance</h3>
                <p>Compare recordings against legal venue-based limits.</p>
              </div>
              <div className="feature-small">
                <h3>Governance risk</h3>
                <p>Evaluate severity and policy risk scores automatically.</p>
              </div>
              <div className="feature-small">
                <h3>Reports</h3>
                <p>Generate downloadable PDF reports.</p>
              </div>
            </div>
          </RevealOnScroll>
        </div>
      </section>

      {/* 6 — How it works */}
      <section>
        <div className="landing-container">
          <RevealOnScroll>
            <header className="landing-section-header landing-section-header--center">
              <h2>How it works</h2>
              <p>Four steps from recording to actionable insight.</p>
            </header>
          </RevealOnScroll>

          <RevealOnScroll>
            <div className="workflow-grid">
              <div className="step-card">
                <h3>1</h3>
                <p>Upload audio</p>
              </div>
              <div className="step-card">
                <h3>2</h3>
                <p>ML classification</p>
              </div>
              <div className="step-card">
                <h3>3</h3>
                <p>Compliance check</p>
              </div>
              <div className="step-card">
                <h3>4</h3>
                <p>Governance insights</p>
              </div>
            </div>
          </RevealOnScroll>
        </div>
      </section>

      {/* 7 — Testimonials */}
      <section>
        <div className="landing-container">
          <RevealOnScroll>
            <header className="landing-section-header landing-section-header--center">
              <h2>Field notes</h2>
              <p>How teams use UNGS in practice.</p>
            </header>
          </RevealOnScroll>

          <RevealOnScroll>
            <div className="testimonials-grid">
              {TESTIMONIALS.map((t) => (
                <blockquote key={t.name} className="testimonial-card">
                  <p className="testimonial-quote">&ldquo;{t.quote}&rdquo;</p>
                  <footer className="testimonial-signature">
                    <span className="testimonial-line" aria-hidden="true" />
                    <cite className="testimonial-name">{t.name}</cite>
                  </footer>
                </blockquote>
              ))}
            </div>
          </RevealOnScroll>
        </div>
      </section>

      {/* 8 — Built for Kigali */}
      <section>
        <div className="landing-container">
          <RevealOnScroll>
            <div className="research">
              <h2>
                Built for
                <span className="script accent-word">Kigali</span>
              </h2>
              <p>
                This platform combines machine learning, acoustic analysis,
                compliance monitoring, governance risk assessment, and policy
                recommendations into a single system.
              </p>
            </div>
          </RevealOnScroll>
        </div>
      </section>

      {/* 9 — Waitlist */}
      <section className="waitlist-section">
        <div className="landing-container">
          <RevealOnScroll>
            <div className="waitlist-bg" aria-hidden="true">
              <div className="waitlist-bg-blob waitlist-bg-blob--1" />
              <div className="waitlist-bg-blob waitlist-bg-blob--2" />
            </div>
            <div className="waitlist-card">
              <div className="waitlist-icon">
                <div className="waitlist-icon-dot" />
              </div>
              <h2>Stay updated</h2>
              <p>
                Get notified when new governance features and deployment updates
                ship.
              </p>
              <form className="waitlist-form" onSubmit={handleWaitlist}>
                <input
                  type="email"
                  className="waitlist-input"
                  placeholder="you@example.com"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  required
                />
                <button type="submit" className="waitlist-submit">
                  Join waitlist
                </button>
              </form>
              {waitlistSent && (
                <p className="waitlist-success">
                  You&apos;re on the list — thank you!
                </p>
              )}
            </div>
          </RevealOnScroll>
        </div>
      </section>

      {/* 10 — FAQ */}
      <section>
        <div className="landing-container">
          <RevealOnScroll>
            <header className="landing-section-header landing-section-header--center">
              <h2>Common questions</h2>
              <p>Quick answers before you start analyzing.</p>
            </header>
          </RevealOnScroll>

          <RevealOnScroll>
            <div className="faq-list">
              {FAQ_ITEMS.map((item) => (
                <FaqItem key={item.q} question={item.q} answer={item.a} />
              ))}
            </div>
          </RevealOnScroll>
        </div>
      </section>

      {/* 11 — Final CTA */}
      <section>
        <div className="landing-container">
          <RevealOnScroll>
            <div className="cta-section">
              <h2>Ready to analyze urban noise?</h2>
              <Link to="/analyze" className="primary-btn">
                Start now
              </Link>
            </div>
          </RevealOnScroll>
        </div>
      </section>
    </div>
  );
}

export default LandingPage;
