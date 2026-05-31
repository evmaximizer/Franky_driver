# TODO — Franky · Personal Driver & Concierge

Cose da completare prima di considerare il sito "live e definitivo".
I placeholder nel codice sono scritti in MAIUSCOLO così sono facili da trovare.

## 🔴 Placeholder da sostituire

| Dove | Cosa | Valore attuale (placeholder) |
|------|------|------------------------------|
| `index.html` — Tips | Link PayPal personale | `https://paypal.me/PLACEHOLDER` |
| `index.html` — Reputation | Link recensioni **Google** | `https://GOOGLE-REVIEWS-PLACEHOLDER` (serve profilo Google Business) |
| `index.html` — Company | Contatto diretto del capo (opzionale) | commento nel blocco "Bookings" |

### ✅ Compilati
- **TripAdvisor**: collegato a `tripadvisor.it/...Stefano_Favilli_Autista_Personale...`.
  ⚠️ DA VERIFICARE: la scheda è intestata a "Stefano Favilli", non a Francesco Urbani/Franky.
  Confermare che sia il profilo corretto o crearne uno per Franky.
- **Private tours (Passaggio)**: messo come *Coming soon* (bloccato), da agganciare quando Passaggio sarà pronto.

### ℹ️ Google reviews — come ottenere il link
Per raccogliere recensioni su Google serve un **profilo Google Business** (gratuito).
Opzioni: (a) creare un account Gmail dedicato e poi un Profilo dell'attività su
business.google.com; (b) il profilo genera un link "scrivi recensione" da incollare
al posto di `GOOGLE-REVIEWS-PLACEHOLDER`. Senza profilo Business non esiste un link
recensioni Google. NB: come per TripAdvisor, valutare il vincolo da dipendente NCC.

### Nota sul link PayPal (tips)
Il connettore PayPal collegato serve a creare fatture, non a ricevere mance da una pagina.
Per il link "tips" serve un **PayPal.me**: vai su https://paypal.me, scegli un handle
(es. `paypal.me/FrancescoUrbani`, gratuito), poi sostituisci `PLACEHOLDER` con quell'handle.

## 🟢 Decisioni prese (registro)

- **Brand landing**: "Franky — Personal Driver & Concierge" (scelta del committente).
- **VIP Card**: lasciata invariata (header "FRANCESCO URBANI"), spostata in `/vip/`.
  Differenza voluta: la landing è il brand personale "Franky", la card resta com'era.
- **Nessuno strumento di vendita/prenotazione**: in linea col vincolo (Francesco è
  dipendente NCC, non procaccia clienti). Le richieste di prenotazione sono rimandate
  **all'azienda** tramite il blocco "Bookings" → https://www.fastlivorno.com/.
- **Tips PayPal**: confermato dal committente che non viola le regole aziendali; reso
  molto discreto (riga testuale in fondo, niente bottone vistoso).
- **Logo Galleria Michelangelo**: NON riprodotto (marchio registrato), solo tipografia.
- **Struttura scalabile**: per aggiungere un'esperienza basta duplicare un blocco
  `<a class="branch">` in `index.html` (vedi commento nel file). Slot "Wine tasting
  San Gimignano" già predisposto come *coming soon*.
- **URL GitHub Pages previsto**: https://evmaximizer.github.io/Franky_driver/

## ⚙️ Dopo il deploy

1. Verificare che `BASE_URL` in `qr/generate_qr.py` corrisponda all'URL live.
2. Rilanciare `python qr/generate_qr.py` per rigenerare i due QR.
3. Stampare i QR: `qr_profile.png` (hub, per i tour) e `qr_vipcard.png` (diretto, a bordo).
4. Aggiornare il link "My profile" nella VIP Card è già automatico (`../`), nessuna azione.
