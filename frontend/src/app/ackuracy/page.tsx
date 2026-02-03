"use client";

import CONTENT from "./landing.json";

const CTA_HREF =
  process.env.NEXT_PUBLIC_CONTACT_EMAIL
    ? `mailto:${process.env.NEXT_PUBLIC_CONTACT_EMAIL}?subject=Suite à notre échange ACKURACY — Cyber Show Paris`
    : (CONTENT as { contact_gmail?: string }).contact_gmail ||
      "mailto:lucas.tymen@gmail.com?subject=Suite ACKURACY — Cyber Show Paris";

type Content = {
  hero_headline: string;
  hero_sub_headline: string;
  hero_subtitle: string;
  intro: string;
  icebreaker: string;
  cta_text: string;
  pain_points: string[];
  solution_workflow: string;
  about_me_title: string;
  about_me: string;
  services: { title: string; description: string }[];
  mission_flash: string;
  why_growth_engineer: string;
};

const c = CONTENT as Content;

export default function AckuracyPage() {
  return (
    <div className="min-h-screen bg-[#0a0b12] text-[#e6e6e6]">
      {/* Hero: fond image + parallax + scanlines (actifs par défaut), pleine largeur */}
      <section className="hero-ackuracy w-full">
        <div className="hero-ackuracy__bg" aria-hidden />
        <div className="hero-ackuracy__overlay" aria-hidden />
        <div className="hero-ackuracy__scanlines" aria-hidden />
        <div className="hero-ackuracy__content w-full max-w-[720px] mx-auto text-center px-4 py-8 md:py-12">
          <h1 className="text-xl md:text-2xl font-semibold mb-2 text-[#FFFFFF]">
            {c.hero_headline}
          </h1>
          <p className="text-base text-[#5a5eff] font-medium mb-2">
            {c.hero_sub_headline}
          </p>
          <p className="text-base text-[#CCCCCC] mb-4">{c.hero_subtitle}</p>
          <p className="text-sm text-[#CCCCCC] mb-6 max-w-[600px] mx-auto">
            {c.intro} {c.icebreaker}
          </p>
          <a
            href={CTA_HREF}
            className="inline-flex min-h-[44px] min-w-[44px] items-center justify-center px-6 py-3 bg-[#ff0055] text-white font-semibold rounded-2xl no-underline hover:bg-[#ff3366] hover:shadow-[0_0_20px_rgba(255,0,85,0.5)] transition-all"
          >
            {c.cta_text}
          </a>
        </div>
      </section>

      <main className="max-w-[720px] mx-auto p-4 md:p-8">
        {/* Pain points */}
        <section className="bg-[rgba(20,20,40,0.7)] rounded-2xl p-5 mb-6 border border-[#e50041]/40 shadow-[0_0_15px_rgba(229,0,65,0.15)]">
          <h2 className="text-lg font-semibold mb-2 text-[#FFFFFF]">
            Vos enjeux
          </h2>
          <ul className="list-disc list-inside text-[#CCCCCC] leading-relaxed space-y-2">
            {c.pain_points.map((point, i) => (
              <li key={i}>{point}</li>
            ))}
          </ul>
        </section>

        {/* Solution */}
        <section className="bg-[rgba(20,20,40,0.7)] rounded-2xl p-5 mb-6 border border-[#5a5eff]/40 shadow-[0_0_15px_rgba(90,94,255,0.15)]">
          <h2 className="text-lg font-semibold mb-2 text-[#FFFFFF]">
            Ce que je propose
          </h2>
          <p className="text-[#CCCCCC] leading-relaxed">
            {c.solution_workflow}
          </p>
        </section>

        {/* About me */}
        <section className="bg-[rgba(20,20,40,0.7)] rounded-2xl p-5 mb-6 border border-[#3a7bd5]/40 shadow-[0_0_15px_rgba(58,123,213,0.15)]">
          <h2 className="text-lg font-semibold mb-2 text-[#FFFFFF]">
            {c.about_me_title}
          </h2>
          <p className="text-[#CCCCCC] leading-relaxed">{c.about_me}</p>
        </section>

        {/* Services */}
        <section className="bg-[rgba(20,20,40,0.7)] rounded-2xl p-5 mb-6 border border-[#e50041]/40 shadow-[0_0_15px_rgba(229,0,65,0.15)]">
          <h2 className="text-lg font-semibold mb-3 text-[#FFFFFF]">
            Prestations
          </h2>
          <ul className="space-y-4">
            {c.services.map((s, i) => (
              <li key={i}>
                <h3 className="font-medium text-[#FFFFFF] mb-1">{s.title}</h3>
                <p className="text-[#CCCCCC] text-sm leading-relaxed">
                  {s.description}
                </p>
              </li>
            ))}
          </ul>
        </section>

        {/* Mission flash */}
        <section className="bg-[rgba(20,20,40,0.7)] rounded-2xl p-5 mb-6 border border-[#5a5eff]/40 shadow-[0_0_15px_rgba(90,94,255,0.15)]">
          <p className="text-[#CCCCCC] leading-relaxed italic">
            {c.mission_flash}
          </p>
        </section>

        {/* Why Growth Engineer */}
        <section className="bg-[rgba(20,20,40,0.7)] rounded-2xl p-5 mb-6 border border-[#3a7bd5]/40 shadow-[0_0_15px_rgba(58,123,213,0.15)]">
          <h2 className="text-lg font-semibold mb-2 text-[#FFFFFF]">
            Pourquoi un Growth Engineer
          </h2>
          <p className="text-[#CCCCCC] leading-relaxed">
            {c.why_growth_engineer}
          </p>
        </section>

        {/* CTA final */}
        <section className="text-center py-6">
          <a
            href={CTA_HREF}
            className="inline-flex min-h-[44px] min-w-[44px] items-center justify-center px-6 py-3 bg-[#ff0055] text-white font-semibold rounded-2xl no-underline hover:bg-[#ff3366] hover:shadow-[0_0_20px_rgba(255,0,85,0.5)] transition-all"
          >
            {c.cta_text}
          </a>
        </section>
      </main>
    </div>
  );
}
