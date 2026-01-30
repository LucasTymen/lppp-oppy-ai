import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Proposition P4S — Joël Courtois",
  description:
    "Suite à notre échange — ce que je peux faire pour P4S Architecture.",
};

export default function P4SArchiLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return <>{children}</>;
}
