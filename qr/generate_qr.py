#!/usr/bin/env python3
"""
Genera i due QR code per il progetto "Franky — Personal Driver & Concierge".

- QR "Profilo / hub"  -> apre la landing personale (/)            uso: durante i tour
- QR "Maisons"        -> apre la pagina con gli atelier (/maisons/) uso: cliente a bordo
                         (mostra Galleria Michelangelo + Aquaflor, scalabile)

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
    "qr_profile": BASE_URL,              # landing / hub
    "qr_maisons": BASE_URL + "maisons/", # pagina atelier (Michelangelo + Aquaflor)
}

# ---- Palette ----
GOLD  = "#9c7c41"   # versione "stampa" elegante (oro su avorio)
PAPER = "#faf5ea"
INK   = "#1b150f"   # versione "schermo" ad alto contrasto (nero su bianco)
WHITE = "#ffffff"


def make_qr(url: str, filename: str, fill: str, back: str, box: int = 14, border: int = 4) -> None:
    qr = qrcode.QRCode(
        version=None,
        error_correction=ERROR_CORRECT_H,  # alta tolleranza, robusto da fotocamera
        box_size=box,
        border=border,
    )
    qr.add_data(url)
    qr.make(fit=True)
    qr.make_image(fill_color=fill, back_color=back).save(f"{filename}.png")
    print(f"  [ok] {filename}.png -> {url}")


def main() -> None:
    print("Generazione QR code…")
    for name, url in TARGETS.items():
        make_qr(url, name, GOLD, PAPER)                          # versione oro (stampa)
        make_qr(url, name + "_bw", INK, WHITE, box=16, border=2) # versione bw (schermo)
    print("Fatto. Controlla i PNG nella cartella /qr/.")


if __name__ == "__main__":
    main()
