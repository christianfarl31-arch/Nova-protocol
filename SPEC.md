# N.O.V.A. Spec v1.2 "Peanuts"

1. TISCH ruft: `WHO:<JOB_TYPE> B:<MAX_BID> LAT:<MAX_MS>`
2. SLOT antwortet: `ME:<ID> LAT:<PING> B:<MY_BID> HEAT:<TRUE|FALSE>`
3. TISCH wählt: `YOU:<ID> JOB:<JOB_ID>` 
4. SLOT liefert: `DONE:<JOB_ID> HASH:<SHA256> DATA:<BASE64>`
5. TISCH zahlt: `PAID:<JOB_ID> TO:<ID> AMT:<PEANUTS>`
6. Port: `4761` = `4e:6f:76:61` = NOVA in Hex
7. Regel: Niedrigste Latenz gewinnt. Bei Gleichstand: Niedrigste Bid.
8. Wärme-Bonus: Slots mit `HEAT:TRUE` dürfen 0.01€ unterbieten.
9. Alles ist Text. UTF-8. `\n` terminiert. Alles außer JOB_ID ist optional.
10. Lizenz: MIT. Forke mich. Bau drauf. Nenn es N.O.V.A.-kompatibel.

**Beispiel-Ablauf:**
TISCH: `WHO:FRAME_RENDER B:0.05 LAT:200`
SLOT: `ME:PC-BERLIN-442 LAT:12 B:0.04 HEAT:TRUE`
TISCH: `YOU:PC-BERLIN-442 JOB:FRAME_4821`
SLOT: `DONE:FRAME_4821 HASH:a3f2... DATA:iVBORw0...`
TISCH: `PAID:FRAME_4821 TO:PC-BERLIN-442 AMT:0.04`
