#!/usr/bin/env python3
"""
QR code generator for wine catalog
Creates QR codes that link to specific pages of the PDF on GitHub Pages
"""

import qrcode
import os
import argparse

def main():
    # Configuration
    GITHUB_USERNAME = "pagaliv"  
    REPO_NAME = "carta_vinos_galeon"
    PDF_NAME = "catalogo-con-marcadores.pdf"
    
    # List of wines and their pages (customize this)
    vinos = {
        "Monastel Javier Calvo": 1,
        "Mazuelo Tío Manolo": 2,
        "Vino Espumoso Rosé": 3,
    }
    
    base_url = f"https://{GITHUB_USERNAME}.github.io/{REPO_NAME}/{PDF_NAME}"
    
    # Create directory for QR codes
    os.makedirs('qr-codes', exist_ok=True)
    
    print("🚀 Generating QR codes for wines...")
    print(f"📁 Base PDF URL: {base_url}")
    print("-" * 50)
    
    for nombre_vino, pagina in vinos.items():
    # URL with page anchor
        url = f"{base_url}/index.html?pagina={pagina}"
        
    # Generate QR
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)
        
        img = qr.make_image(fill_color="black", back_color="white")
        
        # Save
        nombre_archivo = f"qr-codes/qr_{nombre_vino}.png"
        img.save(nombre_archivo)
        print(f"✅ QR created: {nombre_archivo}")
        print(f"   📄 Page: {pagina} | 🔗 URL: {url}")
        print()
    
    print(f"🎉 Generated {len(vinos)} QR codes in the 'qr-codes/' folder")

if __name__ == "__main__":
    main()
