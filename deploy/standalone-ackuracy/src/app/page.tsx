"use client";

import { useState } from "react";
import CONTENT from "@/content/landing.json";

type Content = {
  page_title?: string;
  hero_background_url?: string;
  hero_headline: string;
  hero_sub_headline: string;
  hero_subtitle: string;
  intro: string;
  icebreaker: string;
  positionnement?: string;
  enjeux_lead?: string;
  coordonnees_intro?: string;
  cta_text: string;
  cta_url?: string;
  contact_email?: string;
  contact_gmail?: string;
  rapport_url?: string;
  contact_linkedin?: string;
  contact_github?: string;
  contact_linktree?: string;
  pain_points: string[];
  solution_workflow: string;
  about_me_title: string;
  about_me: string;
  services: { title: string; description: string }[];
  prestations_headline?: string;
  expertise_stack?: Record<string, string[]>;
  mission_flash: string;
  why_growth_engineer: string;
};

const c = CONTENT as Content;

function getDisplayEmail(): string {
  if (c.contact_email) return c.contact_email;
  const g = c.contact_gmail || "";
  if (g.toLowerCase().startsWith("mailto:")) {
    const part = g.slice(7).split("?")[0].trim();
    return part || "lucas.tymen@gmail.com";
  }
  return g || "lucas.tymen@gmail.com";
}

const displayEmail = getDisplayEmail();
const hasContact =
  c.contact_email ||
  c.contact_gmail ||
  c.contact_linkedin ||
  c.contact_github ||
  c.contact_linktree;

export default function Page() {
  const [showContactModal, setShowContactModal] = useState(false);

  return (
    <div className="min-h-screen bg-[#0a0b12] text-[#e6e6e6]">
      {/* Nav sticky (qualité P4S) */}
      <nav className="nav-ackuracy">
        <a href="#top" className="font-bold text-[#FFFFFF] no-underline hover:text-[#5a5eff]">
          {c.page_title || "ACKURACY"}
        </a>
        <div className="nav-ackuracy__links">
          <a href="#enjeux">Enjeux</a>
          <a href="#solution">Solution</a>
          <a href="#prestations">Prestations</a>
          {c.expertise_stack && Object.keys(c.expertise_stack).length > 0 && (
            <a href="#stack">Stack</a>
          )}
          <a href="#offre">Offre</a>
          <a href="#coordonnees">Coordonnées</a>
          {hasContact && (
            <button
              type="button"
              onClick={() => setShowContactModal(true)}
              className="nav-ackuracy__cta"
            >
              Me contacter
            </button>
          )}
        </div>
      </nav>

      {/* Hero: fond image + parallax + scanlines (actifs par défaut), pleine largeur */}
      <section id="top" className="hero-ackuracy w-full">
        <div
          className="hero-ackuracy__bg"
          aria-hidden
          style={
            c.hero_background_url
              ? {
                  backgroundImage: `url(${c.hero_background_url})`,
                }
              : undefined
          }
        />
        <div className="hero-ackuracy__overlay" aria-hidden />
        <div className="hero-ackuracy__scanlines" aria-hidden />
        <div className="hero-ackuracy__content w-full max-w-[720px] mx-auto text-center px-4 py-10 md:py-16">
          <h1 className="text-2xl md:text-3xl font-bold mb-3 text-[#FFFFFF] leading-tight">
            {c.hero_headline}
          </h1>
          <p className="text-base text-[#5a5eff] font-medium mb-2">
            {c.hero_sub_headline}
          </p>
          <p className="text-base text-[#CCCCCC] mb-4">{c.hero_subtitle}</p>
          {c.intro && <p className="text-sm text-[#CCCCCC] mb-2 max-w-[600px] mx-auto">{c.intro}</p>}
          {c.icebreaker && <p className="text-sm text-[#CCCCCC] mb-6 max-w-[600px] mx-auto">{c.icebreaker}</p>}
          {hasContact && (
            <button
              type="button"
              onClick={() => setShowContactModal(true)}
              className="inline-flex min-h-[44px] min-w-[44px] items-center justify-center px-6 py-3 bg-[#ff0055] text-white font-semibold rounded-2xl no-underline hover:bg-[#ff3366] hover:shadow-[0_0_20px_rgba(255,0,85,0.5)] transition-all cursor-pointer border-0"
            >
              {c.cta_text}
            </button>
          )}
        </div>
      </section>

      <main className="max-w-[720px] mx-auto p-4 md:p-8">
        {/* Positionnement (narratif, après hero) */}
        {c.positionnement && (
          <section className="mb-6 rounded-2xl p-5 bg-[rgba(90,94,255,0.08)] border border-[#5a5eff]/30">
            <p className="text-[#CCCCCC] leading-relaxed">{c.positionnement}</p>
          </section>
        )}

        {/* Pain points */}
        <section id="enjeux" className="bg-[rgba(20,20,40,0.7)] rounded-2xl p-5 mb-6 border border-[#e50041]/40 shadow-[0_0_15px_rgba(229,0,65,0.15)]">
          <h2 className="text-lg font-semibold mb-2 text-[#FFFFFF]">
            <span className="section-num">01</span>Vos enjeux
          </h2>
          {c.enjeux_lead && <p className="text-[#CCCCCC] text-sm mb-3">{c.enjeux_lead}</p>}
          <ul className="list-disc list-inside text-[#CCCCCC] leading-relaxed space-y-2">
            {c.pain_points.map((point, i) => (
              <li key={i}>{point}</li>
            ))}
          </ul>
        </section>

        {/* Solution */}
        <section id="solution" className="bg-[rgba(20,20,40,0.7)] rounded-2xl p-5 mb-6 border border-[#5a5eff]/40 shadow-[0_0_15px_rgba(90,94,255,0.15)]">
          <h2 className="text-lg font-semibold mb-2 text-[#FFFFFF]">
            <span className="section-num">02</span>Ce que je propose
          </h2>
          <p className="text-[#CCCCCC] leading-relaxed">
            {c.solution_workflow}
          </p>
        </section>

        {/* Rapport (si rapport_url renseigné) */}
        {c.rapport_url && (
          <section className="mb-6">
            <a
              href={c.rapport_url}
              target="_blank"
              rel="noopener noreferrer"
              className="inline-block px-4 py-2 rounded-xl bg-[#5a5eff]/20 text-[#5a5eff] font-medium border border-[#5a5eff]/40 no-underline hover:bg-[#5a5eff]/30"
            >
              Consulter le rapport complet (société, stratégie, SEO) →
            </a>
          </section>
        )}

        {/* About me */}
        <section className="bg-[rgba(20,20,40,0.7)] rounded-2xl p-5 mb-6 border border-[#3a7bd5]/40 shadow-[0_0_15px_rgba(58,123,213,0.15)]">
          <h2 className="text-lg font-semibold mb-2 text-[#FFFFFF]">
            <span className="section-num">03</span> {c.about_me_title}
          </h2>
          <p className="text-[#CCCCCC] leading-relaxed">{c.about_me}</p>
        </section>

        {/* Propositions de valeur (grille type wireframe : titre bénéfice + blocs avec CTA) */}
        <section id="prestations" className="mb-8">
          <h2 className="text-xl font-bold mb-2 text-[#FFFFFF]">
            <span className="section-num">04</span>
            {c.prestations_headline || "Ce que je peux livrer pour vous"}
          </h2>
          <p className="text-[#CCCCCC] text-sm mb-6 max-w-[600px]">
            Des livrables concrets, pas du vent. Chaque bloc peut déboucher sur un échange.
          </p>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            {c.services.map((s, i) => (
              <div
                key={i}
                className="rounded-2xl p-5 bg-[rgba(20,20,40,0.7)] border border-[#5a5eff]/30 shadow-[0_0_15px_rgba(90,94,255,0.08)] flex flex-col"
              >
                <h3 className="font-semibold text-[#FFFFFF] mb-2">{s.title}</h3>
                <p className="text-[#CCCCCC] text-sm leading-relaxed flex-grow mb-4">
                  {s.description}
                </p>
                {hasContact && (
                  <button
                    type="button"
                    onClick={() => setShowContactModal(true)}
                    className="self-start px-4 py-2 rounded-xl border border-[#5a5eff] text-[#5a5eff] text-sm font-medium hover:bg-[#5a5eff]/15 transition-colors"
                  >
                    En savoir plus
                  </button>
                )}
              </div>
            ))}
          </div>
        </section>

        {/* Stack technique */}
        {c.expertise_stack && Object.keys(c.expertise_stack).length > 0 && (
          <section id="stack" className="bg-[rgba(20,20,40,0.7)] rounded-2xl p-5 mb-6 border border-[#3a7bd5]/40 shadow-[0_0_15px_rgba(58,123,213,0.15)]">
            <h2 className="text-lg font-semibold mb-3 text-[#FFFFFF]">
              <span className="section-num">05</span>Stack technique
            </h2>
            <div className="space-y-3">
              {Object.entries(c.expertise_stack).map(
                ([key, labels]) =>
                  labels?.length > 0 && (
                    <div key={key}>
                      <p className="text-xs font-semibold uppercase tracking-wider text-[#5a5eff] mb-1">
                        {key}
                      </p>
                      <div className="flex flex-wrap gap-2">
                        {labels.map((item, i) => (
                          <span
                            key={i}
                            className="px-2 py-1 rounded-lg bg-[#3a7bd5]/20 text-[#CCCCCC] text-sm"
                          >
                            {item}
                          </span>
                        ))}
                      </div>
                    </div>
                  )
              )}
            </div>
          </section>
        )}

        {/* Mission flash */}
        <section id="offre" className="bg-[rgba(20,20,40,0.7)] rounded-2xl p-5 mb-6 border border-[#5a5eff]/40 shadow-[0_0_15px_rgba(90,94,255,0.15)]">
          <p className="text-sm font-semibold text-[#5a5eff] mb-2">Offre pour vous</p>
          <p className="text-[#CCCCCC] leading-relaxed italic">
            {c.mission_flash}
          </p>
        </section>

        {/* Why Growth Engineer (callout) */}
        <section className="mb-6 rounded-2xl p-5 border-l-4 border-[#e50041] bg-[rgba(229,0,65,0.06)] shadow-[0_0_15px_rgba(229,0,65,0.1)]">
          <h2 className="text-lg font-semibold mb-2 text-[#FFFFFF]">
            <span className="section-num">06</span>Pourquoi un Growth Engineer
          </h2>
          <p className="text-[#CCCCCC] leading-relaxed italic">
            {c.why_growth_engineer}
          </p>
        </section>

        {/* Coordonnées */}
        {hasContact && (
          <section
            id="coordonnees"
            className="bg-[rgba(20,20,40,0.7)] rounded-2xl p-5 mb-6 border border-[#e50041]/40 shadow-[0_0_15px_rgba(229,0,65,0.15)]"
          >
            <h2 className="text-lg font-semibold mb-2 text-[#FFFFFF]">
              <span className="section-num">07</span>Coordonnées
            </h2>
            <p className="text-[#CCCCCC] text-sm mb-3">
              Pour échanger ou planifier un échange, retrouvez mes coordonnées
              ci-dessous.
            </p>
            <ul className="flex flex-wrap gap-x-4 gap-y-2 list-none p-0 m-0">
              {(c.contact_email || c.contact_gmail) && (
                <li>
                  <button
                    type="button"
                    onClick={() => setShowContactModal(true)}
                    className="text-[#5a5eff] font-medium bg-none border-0 cursor-pointer p-0 text-left hover:underline"
                  >
                    Gmail : <span className="select-all">{displayEmail}</span>
                  </button>
                </li>
              )}
              {c.contact_linkedin && (
                <li>
                  <a
                    href={c.contact_linkedin}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="text-[#5a5eff] no-underline hover:underline"
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
                    className="text-[#5a5eff] no-underline hover:underline"
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
                    className="text-[#5a5eff] no-underline hover:underline"
                  >
                    Linktree
                  </a>
                </li>
              )}
            </ul>
          </section>
        )}

        {/* CTA final */}
        {hasContact && (
          <section className="text-center py-6">
            <button
              type="button"
              onClick={() => setShowContactModal(true)}
              className="inline-flex min-h-[44px] min-w-[44px] items-center justify-center px-6 py-3 bg-[#ff0055] text-white font-semibold rounded-2xl no-underline hover:bg-[#ff3366] hover:shadow-[0_0_20px_rgba(255,0,85,0.5)] transition-all cursor-pointer border-0"
            >
              {c.cta_text}
            </button>
          </section>
        )}
      </main>

      {/* Popup contact (qualité P4S — mailto souvent inopérant) */}
      {showContactModal && (
        <div
          className="contact-modal-overlay"
          role="dialog"
          aria-modal="true"
          aria-labelledby="contact-modal-title"
          onClick={() => setShowContactModal(false)}
        >
          <div
            className="contact-modal-content"
            onClick={(e) => e.stopPropagation()}
          >
            <p id="contact-modal-title">
              Vous pouvez me contacter par Mail à cette adresse :{" "}
              <span className="contact-modal-email">{displayEmail}</span>
            </p>
            <button
              type="button"
              className="contact-modal-close"
              onClick={() => setShowContactModal(false)}
            >
              Fermer
            </button>
          </div>
        </div>
      )}
    </div>
  );
}
