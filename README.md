# Francesco Urbani — Personal Driver & Concierge (Firenze)

Pacchetto di progetto per sviluppo autonomo con Claude Code.
Contiene: contesto completo, decisioni concordate, asset, specifica della landing page,
la VIP Card già funzionante come riferimento, e istruzioni di deploy + QR.

---

## 1. CHI È IL COMMITTENTE

Francesco Urbani — autista privato (NCC) a Firenze.
**Vincolo importante:** è dipendente di un'azienda di noleggio con conducente.
Non può procacciarsi clienti in proprio. Può però costruire la propria
**reputazione e memorabilità**, così che i clienti:
1. lascino recensioni (Google / TripAdvisor) menzionandolo;
2. richiamino l'azienda chiedendo esplicitamente di lui ("voglio un tour con Francesco").

→ Tutti gli strumenti digitali NON devono essere strumenti di vendita diretta o
prenotazione. Sono strumenti di **esperienza, memorabilità e raccolta recensioni**.
Niente "prenota con me". Sì a "vivi l'esperienza, chiedi di Francesco, lascia una recensione".

---

## 2. ARCHITETTURA GENERALE (l'hub e i rami)

La **landing page personale** è il centro/hub. Da lì partono dei rami (esperienze):

```
        [ Landing personale = HUB ]
         /          |           \
   VIP Card     Passaggio     (futuro)
  Michelangelo   (tour app)   Cantina San Gimignano
   shopping                    wine tasting
```

- **VIP Card Michelangelo** — già costruita (vedi /vip-card/). Pagina referral per
  pelletteria di lusso Galleria Michelangelo, Piazza Santa Croce.
- **Passaggio** — app PWA esistente per i tour (progetto separato, React+Vite).
  La landing ci linka; più avanti Passaggio verrà modificata per ricevere questo traffico.
- **Cantina San Gimignano** — esperienza futura (wine tasting). Predisporre lo
  slot/struttura ma non svilupparla ora.

---

## 3. I DUE QR CODE (decisione chiave)

Servono DUE QR distinti, per due situazioni d'uso diverse:

- **QR "VIP Card" (diretto)** → apre direttamente la VIP Card Michelangelo.
  Uso: cliente a bordo durante un transfer/navetta. "Volete andare lì? Mostrate questo."
  Zero passaggi intermedi.

- **QR "Profilo" (hub)** → apre la landing personale (hub).
  Uso: durante i tour, quando c'è tempo di farsi conoscere e raccogliere recensioni.

Stessi contenuti raggiungibili, due ingressi diversi. Sono semplicemente due URL/QR.

---

## 4. VIP CARD (GIÀ FATTA — riferimento di stile)

File: `vip-card/index.html` — pagina singola, autonoma, mobile-first.
Contenuti attuali:
- Header: FRANCESCO URBANI · Florence · Private Driver · NCC (la card è SUA, non del negozio)
- Ritratto circolare (foto in /assets/francesco-portrait.jpg, attualmente embedded in base64)
- Badge: "Introduced by Francesco Urbani — «A personal guest of mine»"
- Messaggio VIP onesto (host dedicato + tour privato showroom, NESSUNO sconto promesso)
- Blocco "My recommended atelier — Galleria Michelangelo, Piazza Santa Croce, dal 1960"
- Pulsante "Get directions" → Google Maps con coordinate esatte (43.76914, 11.2617218)
  e place_id ufficiale (ChIJ-TVGsgdUKhMRV20_FfQ-YD0) → porta all'ingresso preciso
- Telefono cliccabile: +39 391 798 4633
- WhatsApp: https://wa.me/393917984633
- Link "My profile" → DA COLLEGARE all'URL della landing (placeholder: YOUR-LANDING-URL)
- "Please show this screen at the desk"

Dati negozio (da fonti Google ufficiali, per riferimento):
- The Gallery Michelangelo, Piazza di Santa Croce 8, 50122 Firenze
- Aperto tutti i giorni 9:30–18:30 · Tel +39 055 241621

NOTA IP: il logo/stemma araldico del negozio è loro marchio registrato e NON va
riprodotto. Si usa solo il trattamento tipografico del nome. Il file ufficiale del
logo, se fornito dal negozio, potrà essere inserito accanto al loro nome.

---

## 5. SISTEMA DI DESIGN (da rispettare in tutte le pagine)

Estetica: atelier fiorentino premium, avorio + oro, elegante, mobile-first.
- Colori:
  - ink (testo scuro): #2b2117
  - gold: #9c7c41 / gold-soft: #b89a5e
  - cream: #f3ecdd / paper: #faf5ea
  - line: rgba(156,124,65,.30)
  - sfondo pagina (dietro la card): radiale scuro #312618 → #16110b
- Font: Cormorant Garamond (display/serif), Jost (testo/etichette uppercase con letter-spacing).
- Dettagli: angoli decorativi dorati, divisori con rombo centrale, animazioni di
  comparsa leggere (fade/rise), pulsanti pill con bordo sottile.
- Tono testi: inglese per i clienti (americani), elegante, sobrio.

---

## 6. LANDING PAGE PERSONALE — DA COSTRUIRE

Pagina singola, mobile-first, stessa estetica della VIP Card.
Nome/brand ufficiale (CONFERMATO): **Francesco Urbani — Private Driver & Concierge**.
Usarlo ovunque come identità del brand.

Sezioni:
1. **Hero**: ritratto, nome, "Private Driver & Concierge · Florence", una riga di
   posizionamento (es. "Private transfers and tailor-made experiences across Florence & Tuscany").
2. **Experiences / rami**: card cliccabili verso i rami:
   - Shopping experience → VIP Card Michelangelo (link interno alla pagina card)
   - Private tours → Passaggio (link esterno, placeholder per ora)
   - (slot predisposto) Wine tasting San Gimignano — "coming soon"
3. **Recensioni / Reputation**: CTA eleganti verso Google Reviews e TripAdvisor
   (placeholder link). Messaggio: se hai vissuto una bella esperienza, raccontalo /
   chiedi di Francesco. NON è una vendita.
4. **Contatti**: telefono (+39 391 798 4633, tel:), WhatsApp (wa.me/393917984633),
   eventuale email. Niente form di prenotazione.

Struttura pensata per essere **scalabile**: aggiungere un nuovo "ramo/esperienza"
deve essere banale (un nuovo blocco card).

---

## 7. TECH & DEPLOY

- Sito statico, mobile-first. HTML/CSS puro va benissimo (no framework necessario per
  landing + card). Se si preferisce, struttura a cartelle pronta per GitHub Pages.
- Hosting: **GitHub Pages**. Repo pubblica, file principale `index.html`.
- Struttura repo suggerita:
  ```
  /                → landing personale (index.html)
  /vip/            → VIP Card Michelangelo (index.html)
  /assets/         → immagini
  /qr/             → QR code generati dopo il deploy
  ```
- Dopo il deploy si generano i due QR (vedi /qr/generate_qr.py) puntando agli URL live:
  - QR VIP diretto → https://<user>.github.io/<repo>/vip/
  - QR Profilo/hub → https://<user>.github.io/<repo>/
