/**
 * Page d'accueil neutralisée : aucun lien vers les landings.
 * Chaque prospect n'arrive que par lien direct (ex. /p4s-archi).
 * Voir strategie-landings-standalone-vs-hub.md.
 */
export default function Home() {
  return (
    <div className="flex min-h-screen flex-col items-center justify-center bg-[#0d0d0d] p-8 text-[#e6e6e6]">
      <main className="flex max-w-2xl flex-col items-center gap-4 text-center">
        <h1 className="text-xl font-semibold text-[#999]">LPPP</h1>
        <p className="text-sm text-[#666]">
          Landings Pages Pour Prospections — accès par lien direct uniquement.
        </p>
      </main>
    </div>
  );
}
