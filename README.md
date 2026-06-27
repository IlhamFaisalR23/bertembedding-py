# Layanan Embedding BERT dengan FastAPI

Aplikasi sederhana berbasis **FastAPI** dan **SentenceTransformers** untuk menghasilkan embedding teks menggunakan model `all-MiniLM-L6-v2` (model ringan berbasis BERT).

## Fitur
- Endpoint REST API untuk menghasilkan embedding teks
- Mendukung input berupa string tunggal maupun list string
- Mengembalikan embedding dalam format JSON array

## Kebutuhan
- Python 3.8+
- FastAPI
- Uvicorn
- SentenceTransformers
- Pydantic

Instalasi dependensi:
```(VIRTUAL ENVIRONMENT DIREKOMENDASIKAN)```

```bash
pip install -r requirements.txt

▶️ Cara Menjalankan
Jalankan server:
uvicorn main:app --reload

Kirim Request:
POST /embedding
Content-Type: application/json

{
  "text": "Halo dunia"
}

ATAU

{
  "text": [
    "Halo",
    "Dunia",
    "Lagi"
  ]
}

Respons:
{
  "embedding": [0.123, -0.456, ...]
}
```

## Struktur Proyek
```.
├── main.py              # Aplikasi FastAPI
├── requirements.txt     # Daftar dependensi
├── README.md            # Dokumentasi proyek
└── venv/                # Virtual environment (diabaikan oleh Git)
```

## Contoh Penggunaan
```curl -X POST "[http://127.0.0.1:8000/embedding](http://127.0.0.1:8000/embedding)" \
     -H "Content-Type: application/json" \
     -d '{"text": ["Halo dunia", "FastAPI itu keren"]}'
```