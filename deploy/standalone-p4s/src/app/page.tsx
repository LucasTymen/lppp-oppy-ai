"use client";

import CONTENT from "@/content/landing.json";

/* Clone 1:1 de la page Django /p/p4s-archi/ (template proposition.html).
 * Contenu = landing.json (même source que Django : docs/contacts/p4s-archi/landing-proposition-joel.json).
 * Liens rapport / prospects / proposition → # (page statique Vercel, pas de sous-pages Django).
 */

const CTA_HREF =
  process.env.NEXT_PUBLIC_CONTACT_EMAIL
    ? `mailto:${process.env.NEXT_PUBLIC_CONTACT_EMAIL}?subject=Suite à notre échange P4S — reprise de contact`
    : (CONTENT as { contact_gmail?: string }).contact_gmail ||
      "mailto:lucas.tymen@gmail.com?subject=Suite à notre échange P4S — reprise de contact";

type Content = {
  page_title?: string;
  hero_background_url?: string;
  hero_headline?: string;
  hero_sub_headline?: string;
  hero_subtitle?: string;
  intro?: string;
  icebreaker?: string;
  cta_text?: string;
  pain_points?: string[];
  solution_workflow?: string;
  positionnement?: string;
  activite_pain_points?: string;
  workflow_image_url?: string;
  services?: { title: string; description: string }[];
  expertise_stack?: Record<string, string[]>;
  mission_flash?: string;
  produit_commercial?: string;
  why_growth_engineer?: string;
  contact_gmail?: string;
  contact_linkedin?: string;
  contact_github?: string;
  contact_linktree?: string;
};

const c = CONTENT as Content;
const hasContacts =
  c.contact_gmail || c.contact_linkedin || c.contact_github || c.contact_linktree;
const heroSub =
  c.hero_sub_headline ?? c.hero_subtitle ?? "Pour P4S Architecture — Joël";

export default function Page() {
  return (
    <>
      <nav className="nav">
        <span style={{ fontWeight: 700, color: "var(--lp-text)" }}>
          P4S Architecture
        </span>
        <div className="nav-links">
          {(c.pain_points?.length ?? 0) > 0 || c.activite_pain_points ? (
            <a href="#enjeux">Enjeux</a>
          ) : null}
          {(c.solution_workflow ?? c.positionnement) && (
            <a href="#solution">Solution</a>
          )}
          {c.services?.length ? <a href="#services">Services</a> : null}
          {c.expertise_stack && Object.keys(c.expertise_stack).length > 0 ? (
            <a href="#stack">Stack</a>
          ) : null}
          {(c.mission_flash ?? c.produit_commercial) && (
            <a href="#offre">Offre</a>
          )}
          <a href="#rapport">Consulter le rapport</a>
          <a href="#prospects">Prospects</a>
          <a href="#proposition">Proposition de valeur</a>
          {hasContacts ? (
            <a href="#coordonnees">Me contacter</a>
          ) : (
            <a href={CTA_HREF} className="nav-cta">
              {c.cta_text ?? "Contact"}
            </a>
          )}
        </div>
      </nav>

      <main id="top">
        {/* Hero : même structure que Django (has-bg-image + image en style si hero_background_url) */}
        <section
          className={`hero ${c.hero_background_url ? "has-bg-image" : ""}`}
          style={
            c.hero_background_url
              ? { backgroundImage: `url('${c.hero_background_url}')` }
              : undefined
          }
        >
          <h1>{c.hero_headline ?? c.page_title ?? "P4S Architecture"}</h1>
          <p className="hero-sub">{heroSub}</p>
          {c.cta_text && hasContacts && (
            <a href="#coordonnees" className="cta">
              {c.cta_text}
            </a>
          )}
        </section>

        {c.icebreaker ? <p className="icebreaker">{c.icebreaker}</p> : null}
        {c.intro ? <p className="icebreaker">{c.intro}</p> : null}

        {/* 01 Vos enjeux */}
        {(c.pain_points?.length ?? 0) > 0 || c.activite_pain_points ? (
          <section className="section" id="enjeux">
            <div className="section-head">
              <span className="section-num">01</span>
              <h2>Vos enjeux</h2>
            </div>
            {c.pain_points?.length ? (
              <ul className="pain-list">
                {c.pain_points.map((item, i) => (
                  <li key={i}>{item}</li>
                ))}
              </ul>
            ) : (
              <p>{c.activite_pain_points}</p>
            )}
          </section>
        ) : null}

        {/* 02 Comment je transforme le chaos en système */}
        {(c.solution_workflow ?? c.positionnement) && (
          <section className="section" id="solution">
            <div className="section-head">
              <span className="section-num">02</span>
              <h2>Comment je transforme le chaos en système</h2>
            </div>
            <div className="card">
              <p>{c.solution_workflow ?? c.positionnement}</p>
              {c.workflow_image_url && (
                <figure className="workflow-figure">
                  <img
                    src={c.workflow_image_url}
                    alt="Workflow"
                    loading="lazy"
                  />
                </figure>
              )}
            </div>
          </section>
        )}

        {/* 03 Ce que j'offre (services + onglets) */}
        {c.services?.length ? (
          <section className="section" id="services">
            <div className="section-head">
              <span className="section-num">03</span>
              <h2>Ce que j'offre</h2>
            </div>
            <div className="rapport-cta-block">
              <a href="#rapport" className="rapport-cta-link">
                Consulter le rapport complet (société, stratégie, SEO) →
              </a>
            </div>
            <p className="services-annexes">
              <a href="#rapport">Rapport complet</a>
              <span className="sep">·</span>
              <a href="#prospects">Prospects</a>
              <span className="sep">·</span>
              <a href="#proposition">Proposition de valeur</a>
            </p>
            <div className="services-tabs">
              {c.services.map((service, i) => (
                <input
                  key={i}
                  type="radio"
                  name="services-tab"
                  id={`service-${i}`}
                  defaultChecked={i === 0}
                />
              ))}
              {c.services.map((service, i) => (
                <label key={i} htmlFor={`service-${i}`}>
                  {service.title}
                </label>
              ))}
              <div className="services-panels">
                {c.services.map((service, i) => (
                  <div key={i} className="services-panel">
                    <h3>{service.title}</h3>
                    <p>{service.description}</p>
                  </div>
                ))}
              </div>
            </div>
          </section>
        ) : null}

        {/* 04 Stack technique */}
        {c.expertise_stack && Object.keys(c.expertise_stack).length > 0 ? (
          <section className="section" id="stack">
            <div className="section-head">
              <span className="section-num">04</span>
              <h2>Stack technique</h2>
            </div>
            {Object.entries(c.expertise_stack).map(
              ([key, labels]) =>
                labels?.length > 0 && (
                  <div key={key} className="stack-group">
                    <p className="stack-label">
                      {key.charAt(0).toUpperCase() + key.slice(1)}
                    </p>
                    <div className="stack-tags">
                      {labels.map((item, i) => (
                        <span key={i} className="stack-tag">
                          {item}
                        </span>
                      ))}
                    </div>
                  </div>
                )
            )}
          </section>
        ) : null}

        {/* 05 Mission Flash */}
        {(c.mission_flash ?? c.produit_commercial) && (
          <section className="section" id="offre">
            <div className="section-head">
              <span className="section-num">05</span>
              <h2>Mission Flash</h2>
            </div>
            <div className="mission-flash">
              <p className="tag-line">Offre pour vous</p>
              <p>{c.mission_flash ?? c.produit_commercial}</p>
            </div>
          </section>
        )}

        {/* Pourquoi un Growth Engineer */}
        {c.why_growth_engineer && (
          <section className="section" id="why-ge">
            <h2>Pourquoi un Growth Engineer et pas une agence ?</h2>
            <blockquote className="why-quote">
              {c.why_growth_engineer}
            </blockquote>
          </section>
        )}

        {/* 07 Coordonnées */}
        {hasContacts && (
          <section className="section" id="coordonnees">
            <div className="section-head">
              <span className="section-num">07</span>
              <h2>Coordonnées</h2>
            </div>
            <div className="card">
              <p className="coordonnees-intro">
                Pour échanger ou planifier un Diagnostic Flash, retrouvez mes
                coordonnées ci-dessous.
              </p>
              <ul className="coordonnees-list">
                {c.contact_gmail && (
                  <li>
                    <a
                      href={c.contact_gmail}
                      target="_blank"
                      rel="noopener noreferrer"
                    >
                      Gmail
                    </a>
                  </li>
                )}
                {c.contact_linkedin && (
                  <li>
                    <a
                      href={c.contact_linkedin}
                      target="_blank"
                      rel="noopener noreferrer"
                    >
                      LinkedIn
                    </a>
                  </li>
                )}
                {c.contact_github && (
                  <li>
                    <a
                      href={c.contact_github}
                      target="_blank"
                      rel="noopener noreferrer"
                    >
                      GitHub
                    </a>
                  </li>
                )}
                {c.contact_linktree && (
                  <li>
                    <a
                      href={c.contact_linktree}
                      target="_blank"
                      rel="noopener noreferrer"
                    >
                      Linktree
                    </a>
                  </li>
                )}
              </ul>
            </div>
          </section>
        )}

        {/* CTA final */}
        {c.cta_text && hasContacts && (
          <div className="cta-wrap">
            <a href="#coordonnees" className="cta">
              {c.cta_text}
            </a>
          </div>
        )}
      </main>
    </>
  );
}
