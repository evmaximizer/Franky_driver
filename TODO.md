# TODO — Franky · Personal Driver & Concierge

Cose da completare prima di considerare il sito "live e definitivo".
I placeholder nel codice sono scritti in MAIUSCOLO così sono facili da trovare.

## 🔴 Placeholder da sostituire

| Dove | Cosa | Valore attuale (placeholder) |
|------|------|------------------------------|
| `index.html` — Company | Contatto diretto del capo (opzionale) | commento nel blocco "Bookings" |

## 🟠 Da verificare (accuratezza)

- **Link PayPal tips**: impostato a `https://paypal.me/Ost378`. ⚠️ CONFERMARE che sia
  l'handle PayPal.me corretto (il pulsante invia denaro reale lì).
- **Pagina "Places & Stories"** (`places/index.html`): nuova pagina-guida collegata dalla
  card "Places & Stories" nella landing. 4 città (Florence, Pisa, Lucca, Siena) con luoghi
  come card; al tap si apre una scheda con foto + storia + curiosità + "Get directions".
  - **Foto**: caricate live dall'API ufficiale di Wikipedia (licenze CC/pubblico dominio,
    credito "Photo: Wikimedia" + link alla fonte). Servono internet sul telefono del cliente.
    Se una foto non è ideale, si può forzare un'immagine specifica (dimmelo e la cambio).
  - **Get directions**: usa il nome ufficiale del luogo (Google risolve all'ingresso).
  - **Testi storici/curiosità**: scritti accurati e sintetici; rilettura consigliata.
  - **Scalabile**: per aggiungere un luogo o una città basta estendere l'array `CITIES`
    in fondo a `places/index.html` (istruzioni nei commenti del file).

### ✅ Compilati
- **TripAdvisor**: collegato a `tripadvisor.it/...Stefano_Favilli_Autista_Personale...` (verificato funzionante).
- **Testimonianze**: 4 recensioni reali TripAdvisor (Melissa L, Mike M, Chris M, Sally B,
  ago–set 2023) inserite come citazioni tradotte in inglese nella sezione "A kind word".
  Per aggiungerne altre: duplicare un blocco `<blockquote class="quote">` in index.html.
- **Google reviews**: RIMOSSO su richiesta (richiederebbe un profilo Google Business).
- **Card "Places & Stories"**: la ex card "Private tours" ora apre la pagina-guida `places/`.
  (Passaggio resta un'idea futura: quando l'app sarà pronta si potrà aggiungere una card a sé.)
- **PayPal tips**: link `paypal.me/Ost378` + logo ufficiale PayPal (SVG) accanto al testo.
- **Places & Stories**: pagina-guida dedicata (`places/`) — vedi sezione "Da verificare".

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
