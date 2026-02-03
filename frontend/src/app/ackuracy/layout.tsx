import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "ACKURACY — Alexis, suite à notre échange au Cyber Show",
  description:
    "Suite à notre échange au Cyber Show Paris — ce que je peux faire pour ACKURACY.",
};

export default function AckuracyLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return <>{children}</>;
}
