#!/usr/bin/env python3
"""
Genera i due QR code per il progetto "Franky — Personal Driver & Concierge".

- QR "Profilo / hub"  -> apre la landing personale (/)        uso: durante i tour
- QR "VIP Card"       -> apre direttamente la VIP Card (/vip/) uso: cliente a bordo

Estetica coerente col sito: moduli color oro su sfondo avorio.

USO
----
  pip install "qrcode[pil]"
  python generate_qr.py

I due PNG vengono salvati nella stessa cartella /qr/.
Dopo il deploy su GitHub Pages, assicurarsi che BASE_URL qui sotto sia corretto
e rilanciare lo script per rigenerare i QR con gli URL live.
"""

import qrcode
from qrcode.constants import ERROR_CORRECT_H

# ====================================================================
# URL — PARAMETRIZZA QUI (aggiornare dopo il deploy se cambia il path)
# ====================================================================
BASE_URL = "https://evmaximizer.github.io/Franky_driver/"

TARGETS = {
    "qr_profile": BASE_URL,          # landing / hub
    "qr_vipcard": BASE_URL + "vip/", # VIP Card Michelangelo
}

# ---- Palette (coerente col design system del sito) ----
GOLD  = "#9c7c41"   # moduli
PAPER = "#faf5ea"   # sfondo


def make_qr(url: str, filename: str) -> None:
    qr = qrcode.QRCode(
        version=None,                 # auto-size in base al contenuto
        error_correction=ERROR_CORRECT_H,  # alta tolleranza (robusto da fotocamera)
        box_size=14,                  # px per modulo -> immagine ad alta risoluzione
        border=4,                     # quiet zone (minimo consigliato = 4)
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color=GOLD, back_color=PAPER)
    out = f"{filename}.png"
    img.save(out)
    print(f"  [ok] {out:<16} -> {url}")


def main() -> None:
    print("Generazione QR code…")
    for name, url in TARGETS.items():
        make_qr(url, name)
    print("Fatto. Controlla i PNG nella cartella /qr/.")


if __name__ == "__main__":
    main()
