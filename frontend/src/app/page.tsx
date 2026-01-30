import Link from "next/link";

export default function Home() {
  return (
    <div className="flex min-h-screen flex-col items-center justify-center bg-[#0d0d0d] p-8 text-[#e6e6e6]">
      <main className="flex max-w-2xl flex-col items-center gap-8 text-center">
        <h1 className="text-2xl font-semibold">LPPP — Landings Pages Pour Prospections</h1>
        <p className="text-[#999]">
          Landing pages personnalisées pour la prospection.
        </p>
        <div className="flex flex-col gap-4 sm:flex-row">
          <Link
            href="/p4s-archi"
            className="flex h-12 items-center justify-center rounded-lg bg-[#4a9eff] px-6 font-semibold text-[#0d0d0d] no-underline transition-colors hover:bg-[#3a8eef]"
          >
            Page P4S-archi
          </Link>
        </div>
      </main>
    </div>
  );
}
