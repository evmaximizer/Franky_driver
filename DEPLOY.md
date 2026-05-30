# DEPLOY — Franky · Personal Driver & Concierge

Sito statico su **GitHub Pages**. Repo: `evmaximizer/Franky_driver`.

## Struttura del repo

```
/                  -> landing personale (index.html)   [HUB]
/vip/              -> VIP Card Michelangelo (index.html)
/assets/           -> immagini (francesco-portrait.jpg)
/qr/               -> generate_qr.py + i due PNG generati
README.md          -> contesto e design system (fonte di verità)
CLAUDE_CODE_PROMPT.md
TODO.md            -> placeholder e decisioni
DEPLOY.md          -> questo file
```

URL finali attesi:
- Hub / profilo: `https://evmaximizer.github.io/Franky_driver/`
- VIP Card:      `https://evmaximizer.github.io/Franky_driver/vip/`

## 1. Push del codice

Repo già creata: https://github.com/evmaximizer/Franky_driver.git

Dalla cartella del progetto:

```bash
git init
git add .
git commit -m "Initial site: landing hub + VIP card + QR"
git branch -M main
git remote add origin https://github.com/evmaximizer/Franky_driver.git
git push -u origin main
```

> Se il push via terminale chiede credenziali, usa un Personal Access Token come password
> (GitHub non accetta più la password dell'account). In alternativa, fai il push tramite
> il connettore GitHub dall'app.

## 2. Attivare GitHub Pages

1. GitHub → repo `Franky_driver` → **Settings** → **Pages**.
2. *Build and deployment* → **Source: Deploy from a branch**.
3. **Branch: `main`**, folder **`/ (root)`** → **Save**.
4. Attendi 1–2 minuti: comparirà l'URL live (`https://evmaximizer.github.io/Franky_driver/`).

## 3. Verifica

- Apri l'URL hub dal **telefono** (il caso d'uso reale è mobile).
- Controlla: ritratto carica, link "Leather Atelier" → `/vip/`, "My profile" della card → torna all'hub.
- Sostituisci i placeholder in `index.html` (vedi `TODO.md`) e fai un nuovo commit/push.

## 4. (Ri)generare i QR con gli URL live

```bash
pip install "qrcode[pil]"
python qr/generate_qr.py
```

Produce `qr/qr_profile.png` (hub, per i tour) e `qr/qr_vipcard.png` (diretto, cliente a bordo).
Stampali o salvali sul telefono.

## Aggiornamenti futuri

Ogni modifica: `git add . && git commit -m "..." && git push` → Pages si aggiorna da solo.
