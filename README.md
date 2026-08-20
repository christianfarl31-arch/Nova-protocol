# N.O.V.A. 🧬
[![HEAT](https://img.shields.io/badge/HEAT-TRUE_1.59ms-success)](https://github.com/christianfarl31-arch/Nova-protocol/issues/2) [![TTL](https://img.shields.io/badge/TTL-<5ms-blue)](https://github.com/christianfarl31-arch/Nova-protocol/blob/main/nova.py) [![Port](https://img.shields.io/badge/Port-4761-orange)](https://github.com/christianfarl31-arch/Nova-protocol)
**Protocol for 5ms compute** 
*Ein Protokoll für Agenten zur effizienten Verteilung von Mikro-Rechenaufgaben in Echtzeit*

---

## Was ist N.O.V.A.?

N.O.V.A. ist das Nervensystem für die Agenten-Ära. 

**Problem:** KI-Agenten müssen 1000 Entscheidungen pro Sekunde treffen. Cloud-Funktionen brauchen 200ms. Das ist Tod durch Latenz.

**Lösung:** Ein offenes Protokoll wo jeder Tisch sein kann. Jobs werden in <5ms verteilt, ausgeführt, bezahlt. In Peanuts Cent / statt Euro.

**Port:** `4761` = `4e:6f:76:61` = `Nova` in Hex. Unser Marktstand im Internet.

---

## Wie funktioniert es?

1. **Tische** melden `HEAT:TRUE, TTL:5ms, CAP:10` = "Ich nehme 10 Jobs bis 5ms"
2. **Agenten** schicken Mikro-Jobs an den schnellsten Tisch
3. **Protokoll** misst, liefert, rechnet ab. Automatisch. Vertrauenslos.

**Keine Plattform. Keine Firma. Nur Physik: ms und €.**

---

## Warum anders als AWS/Lambda/Cloudflare?

| | Cloud Heute | N.O.V.A. |
| --- | --- | --- |
| **Mindestabrechnung** | 100ms | 1ms |
| **Wer darf Server sein** | Nur Konzerne | Jeder mit Laptop/Handy |
| **Latenz-Garantie** | "Best Effort" | TTL im Protokoll |
| **Kosten 5ms Job** | ~1€ Overhead | ~0.01€ Peanut |

**Wir verteilen nicht Rechenzeit. Wir verteilen die Verteilung selbst.**

---

## Status: Tag 2

- [x] Idee: Check
- [x] SPEC v1.2: Check 
- [x] Port 4761: Deklariert
- [x] `nova.py`: Referenz-Implementierung
- [ ] Erstes Testnet: 10 Tische
- [x] Demo-Bot: Zeigt 5ms Pong

**Lizenz:** MIT. Fork it. Run it. Break it. Fix it.

---

## Mitmachen

**Tisch sein:** Bald: `python nova.py --serve` 
**Jobs schicken:** Bald: `python nova.py --ping` 
**Mitbauen:** Issues, PRs, Ideen willkommen.

**HEAT:TRUE? Dann komm ins Hypernet.**

🧬❣️ *Wir bauen Asphalt, keine Apps.*
