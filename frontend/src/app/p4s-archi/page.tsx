"use client";

const CONTENT = {
  hero_title: "Joël, suite à notre échange — ce que je peux faire pour P4S",
  hero_subtitle: "Pour P4S — Joël",
  cta_text: "Reprendre la conversation",
  positionnement:
    "Je me positionne en Growth Engineer : acquisition B2B, automatisation des pipelines de données et évangélisation. J'ai une idée assez précise de ce que P4S apporte — une techno disruptive, souveraine, avec un vrai gap par rapport aux solutions logicielles — et je vois bien où je pourrais vous être utile.",
  activite_pain_points:
    "Votre force, c'est le produit : SOFTLESS, les SF-106, la latence, le Made in France. Le défi, à mon sens, c'est moins la techno que la diffusion : identifier les bons décideurs (industrie, médical, gouvernement), les sensibiliser aux incidents cyber récents qui les concernent, et automatiser une partie de la veille et du ciblage. C'est exactement le type de travail sur lequel je peux embarquer.",
  produit_commercial:
    "J'ai préparé une petite étude (concurrence, PESTEL, SWOT, Porter) pour cadrer le contexte. Si l'angle vous parle, je serais ravi d'en discuter autour d'un café ou d'un appel — sans engagement, juste pour voir si on peut avancer ensemble sur la partie acquisition et évangélisation.",
};

const CTA_HREF =
  process.env.NEXT_PUBLIC_CONTACT_EMAIL
    ? `mailto:${process.env.NEXT_PUBLIC_CONTACT_EMAIL}?subject=Suite à notre échange P4S — reprise de contact`
    : "mailto:?subject=Suite à notre échange P4S — reprise de contact";

export default function P4SArchiPage() {
  return (
    <div className="min-h-screen bg-[#0d0d0d] text-[#e6e6e6] p-4 md:p-8">
      <main className="max-w-[720px] mx-auto">
        <section className="text-center py-8 md:py-12">
          <h1 className="text-xl md:text-2xl font-semibold mb-2">
            {CONTENT.hero_title}
          </h1>
          <p className="text-base text-[#999] mb-6">{CONTENT.hero_subtitle}</p>
          <a
            href={CTA_HREF}
            className="inline-flex min-h-[44px] min-w-[44px] items-center justify-center px-6 py-3 bg-[#4a9eff] text-[#0d0d0d] font-semibold rounded-lg no-underline hover:bg-[#3a8eef] transition-colors"
          >
            {CONTENT.cta_text}
          </a>
        </section>

        <section className="bg-[#1a1a1a] rounded-lg p-4 mb-6">
          <h2 className="text-lg font-semibold mb-2">Positionnement</h2>
          <p className="text-[#e6e6e6] leading-relaxed">
            {CONTENT.positionnement}
          </p>
        </section>

        <section className="bg-[#1a1a1a] rounded-lg p-4 mb-6">
          <h2 className="text-lg font-semibold mb-2">Votre activité & besoins</h2>
          <p className="text-[#e6e6e6] leading-relaxed">
            {CONTENT.activite_pain_points}
          </p>
        </section>

        <section className="bg-[#1a1a1a] rounded-lg p-4 mb-6">
          <h2 className="text-lg font-semibold mb-2">Me contacter</h2>
          <p className="text-[#e6e6e6] leading-relaxed">
            {CONTENT.produit_commercial}
          </p>
        </section>
      </main>
    </div>
  );
}
