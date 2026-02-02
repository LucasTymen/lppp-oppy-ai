import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "P4S Architecture — Joël, suite à notre échange",
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
