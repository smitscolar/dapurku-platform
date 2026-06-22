# 🚀 Panduan Deploy DapurKu ke Vercel

## Cara 1: Deploy Otomatis via Vercel Dashboard (PALING MUDAH)

1. Buka https://vercel.com/new
2. Login dengan GitHub
3. Pilih repo: **smitscolar/dapurku-platform**
4. Klik **Import**
5. Di bagian **Configure Project**:
   - Framework Preset: **Other**
   - Build Command: *(kosongkan)*
   - Output Directory: *(kosongkan / `.`)*
   - Install Command: *(kosongkan)*
6. Klik **Deploy**
7. ✅ Selesai! URL akan muncul otomatis

## Cara 2: Via Vercel CLI

```bash
npm i -g vercel
vercel login
vercel --prod
```

## File Penting

- `index.html` — Aplikasi utama DapurKu (29 halaman, 295 KB)
- `vercel.json` — Konfigurasi deployment Vercel
- `README.md` — Dokumentasi lengkap
- `INVESTOR.md` — Informasi untuk investor

## Live Demo (Netlify)
https://ghostkitchenumkm.netlify.app

## Repo GitHub
https://github.com/smitscolar/dapurku-platform
