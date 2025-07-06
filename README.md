
# 📚 Sejarah Chatbot with Scraper + FastAPI

Proyek ini adalah chatbot berbasis **FastAPI** yang memanfaatkan scraping data sejarah menggunakan **BeautifulSoup** dan **Requests**, lalu disajikan melalui REST API. Proyek ini juga dapat digunakan untuk integrasi RAG (Retrieval-Augmented Generation).

---

## 🛠️ Instalasi & Menjalankan Proyek

Ikuti langkah-langkah di bawah ini untuk menjalankan proyek di lingkungan lokal:

### 1. Clone Repository
    ```bash
    https://github.com/DwiPratamaKadek/beckend-chatbot-sejarahb
    cd backend-chatbot-sejarah
    ```
### 2. Buat dan Aktifkan Virtual Environment
untuk windows
    ```bash 
    python -m venv env
    .\env\Scripts\Activate
    ```

### 4. Install Dependencies
    ``` bash 
    pip install 
    
    fastapi 
    uvicorn 
    pillow 
    python-dotenv 
    google-generativeai
    langchain-google-genai 
    langchain-community
    langchain 
    tiktoken
    chromadb
    beautifulsoup4
    python-multipart

    atau 

    pip install -r requirements.txt
    ```

### 5. Install Liblary Tambahan 
    ```bash 

    ```

### 6. Jalankan Web Scrape
    ```bash
    python app/scraped_sejarah.py
    ```

### 7. Jalankan Ingset data 
    ```bash
    python app/ingset.py
    ```

### 8. Jalankan Server API
    ```bash
    uvicorn app.main:app --reload
    ```


# 🔗 Endpoint Utama
| Endpoint     | Method | Deskripsi                  |
| ------------ | ------ | -------------------------- |
| `/docs`      | GET    | Dokumentasi Swagger UI     |
| `/api/chat`  | POST   | Endpoint untuk chat        |
| `/api/image` | POST   | (Jika ada) Endpoint gambar |

# ✅ Catatan
    - Pastikan koneksi internet aktif saat scraping data.
    - Jalankan scrape_sejarah.py terlebih dahulu agar data tersedia sebelum ingest.
    - Gunakan Python 3.9 atau lebih baru untuk kompatibilitas maksimal.

# 👨‍💻 Author
Dibuat oleh Dwi Pratama (ENJI)