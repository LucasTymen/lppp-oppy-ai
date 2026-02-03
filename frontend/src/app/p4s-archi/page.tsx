"use client";

import CONTENT from "./landing.json";

const CTA_HREF =
  process.env.NEXT_PUBLIC_CONTACT_EMAIL
    ? `mailto:${process.env.NEXT_PUBLIC_CONTACT_EMAIL}?subject=Suite à notre échange P4S — reprise de contact`
    : (CONTENT as { contact_gmail?: string }).contact_gmail ||
      "mailto:?subject=Suite à notre échange P4S — reprise de contact";

type Content = {
  hero_headline: string;
  hero_subtitle: string;
  cta_text: string;
  positionnement: string;
  activite_pain_points: string;
  produit_commercial: string;
};

const c = CONTENT as Content;

export default function P4SArchiPage() {
  return (
    <div className="min-h-screen bg-[#0d0d0d] text-[#e6e6e6] p-4 md:p-8">
      <main className="max-w-[720px] mx-auto">
        <section className="text-center py-8 md:py-12">
          <h1 className="text-xl md:text-2xl font-semibold mb-2">{c.hero_headline}</h1>
          <p className="text-base text-[#999] mb-6">{c.hero_subtitle}</p>
          <a
            href={CTA_HREF}
            className="inline-flex min-h-[44px] min-w-[44px] items-center justify-center px-6 py-3 bg-[#4a9eff] text-[#0d0d0d] font-semibold rounded-lg no-underline hover:bg-[#3a8eef] transition-colors"
          >
            {c.cta_text}
          </a>
        </section>
        <section className="bg-[#1a1a1a] rounded-lg p-4 mb-6">
          <h2 className="text-lg font-semibold mb-2">Positionnement</h2>
          <p className="text-[#e6e6e6] leading-relaxed">{c.positionnement}</p>
        </section>
        <section className="bg-[#1a1a1a] rounded-lg p-4 mb-6">
          <h2 className="text-lg font-semibold mb-2">Votre activité & besoins</h2>
          <p className="text-[#e6e6e6] leading-relaxed">{c.activite_pain_points}</p>
        </section>
        <section className="bg-[#1a1a1a] rounded-lg p-4 mb-6">
          <h2 className="text-lg font-semibold mb-2">Me contacter</h2>
          <p className="text-[#e6e6e6] leading-relaxed">{c.produit_commercial}</p>
        </section>
      </main>
    </div>
  );
}
