# PROMPT PER CLAUDE CODE

Scompatta la cartella `concierge-firenze/`, apri Claude Code dentro quella cartella
(`cd concierge-firenze` poi `claude`), e incolla il prompt qui sotto come primo messaggio.
Claude Code ha già accesso ai file del progetto, quindi può leggere il README da solo.

---

Sei Claude Code e lavori a un piccolo progetto web statico per **Francesco Urbani**,
autista privato (NCC) a Firenze. Leggi prima `README.md` nella root del progetto:
contiene TUTTO il contesto, i vincoli e il sistema di design. Rispettalo alla lettera.

## Obiettivo
Costruire un sito statico mobile-first, in stile atelier fiorentino premium (avorio + oro,
font Cormorant Garamond + Jost), composto da:

1. **Landing page personale (hub)** in `/index.html` — da creare da zero seguendo la
   sezione 6 del README. È il centro da cui partono i "rami" (esperienze).
   Nome/brand ufficiale CONFERMATO: **Francesco Urbani — Private Driver & Concierge**.
2. **VIP Card Michelangelo** in `/vip/index.html` — usa il file già pronto
   `vip-card/index.html` come base (spostalo in `/vip/index.html`). Verifica che tutto
   funzioni e che il link "My profile" punti alla landing (`/`).
3. **QR code**: script in `/qr/generate_qr.py` (Python, libreria `qrcode`) che genera
   due PNG eleganti: uno per la landing (`/`) e uno per la VIP card (`/vip/`).
   Gli URL finali vanno parametrizzati in cima allo script.

## Requisiti vincolanti
- Mobile-first assoluto: questi QR si aprono dal telefono di clienti a bordo auto.
- NESSUNO strumento di vendita o prenotazione. Solo esperienza, memorabilità, recensioni
  (Google/TripAdvisor). Vedi sezione 1 del README (Francesco è dipendente, non può
  procacciare clienti — il sito serve a farlo ricordare e a raccogliere recensioni).
- NON riprodurre il logo/stemma di Michelangelo (marchio registrato). Solo tipografia.
- Coerenza totale col design system (sezione 5 del README): stessi colori, font, dettagli
  dorati, animazioni leggere, pulsanti pill.
- Testi rivolti ai clienti in inglese, eleganti e sobri.
- Tutti i link non ancora definitivi vanno lasciati come placeholder ben evidenziati
  (es. `https://YOUR-LANDING-URL`, link Passaggio, Google Reviews, TripAdvisor) e
  raccolti in un breve `TODO.md` perché Francesco li compili.
- Struttura scalabile: aggiungere una futura esperienza (es. "Wine tasting San Gimignano",
  già da predisporre come slot "coming soon") deve richiedere solo un nuovo blocco card.

## Deploy
- Target: **GitHub Pages**. Prepara la struttura pronta (file in root, `/vip/`, `/assets/`,
  `/qr/`) e scrivi in `DEPLOY.md` i passi esatti per: creare la repo, caricare i file,
  attivare Pages, ottenere gli URL, poi rigenerare i QR con gli URL live.

## Output atteso
- `/index.html` (landing hub), `/vip/index.html` (card), `/assets/` (immagini),
  `/qr/generate_qr.py`, `TODO.md`, `DEPLOY.md`.
- Codice pulito, commentato dove utile, nessuna dipendenza inutile.

Leggi prima i file con i tuoi strumenti, poi procedi in autonomia. Dove il README lascia
scelte aperte, opta per la soluzione più semplice e di qualità premium, e annota le
decisioni in cima al `TODO.md`. Mostrami un piano sintetico prima di scrivere il codice.
