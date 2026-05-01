# YZV 322E - pgvector Tool Presentation

### 1. What is this tool?
**pgvector** is an open-source extension for PostgreSQL that enables the storage, querying, and indexing of vector embeddings directly within the database. It solves the problem of integrating AI-driven semantic search into existing data engineering pipelines without the need to maintain a separate, standalone vector database.

### 2. Prerequisites
Before running this project, ensure you have the following installed on your machine:
* **Docker & Docker Compose:** For running the isolated PostgreSQL database environment.
* **Python 3.10+:** For executing the interaction script.
* **pip:** Python package installer.

### 3. Installation
Follow these step-by-step commands to set up the environment. The commands are copy-pasteable for convenience.

1. Clone this repository and navigate into the directory:
```bash
git clone <https://github.com/itu-itis23-kilici23/yzv322e_pgvector_container>
cd <yzv322e_pgvector_container>
```

2. Start the PostgreSQL database and pgAdmin containers in the background:
```bash
docker compose up -d
```
*(Wait a few seconds for the database to fully initialize and run the `init.sql` script).*

3. Install the required Python dependencies:
```bash
pip install -r requirements.txt
```

### 4. Running the example
To execute the vector similarity search demo, simply run the Python script:
```bash
python main.py
```
*Note: You can also explore the vectors visually by navigating to `http://localhost:8080` and logging into pgAdmin (Email: admin@itu.edu.tr | Password: admin).*
### 4.1 Visualizing the Vectors via pgAdmin
You can also explore the database visually by navigating to `http://localhost:8080`.

**Step 1: Log in to the pgAdmin web interface:**
*   **Email:** `admin@itu.edu.tr`
*   **Password:** `admin`

**Step 2: Connect to the PostgreSQL Server:**
Once logged in, right-click on "Servers" > "Register" > "Server..." and enter the following details:
*   **General Tab -> Name:** `pgvector-demo-db` (or any name you prefer)
*   **Connection Tab -> Host name/address:** `vector-db` 
*   **Connection Tab -> Port:** `5432`
*   **Connection Tab -> Username:** `itu_student`
*   **Connection Tab -> Password:** `dateng2026`

After saving, navigate to `Databases` > `your_db_name` > `Schemas` > `public` > `Tables` to view the vectors inside the `books` table.

### 5. Expected output
When you run the script, you should see the system connecting to the database and calculating the cosine distance between the target vector and the books in the database. The output will look exactly like this:
```text
Veritabanına bağlanılıyor...

Aranan Vektör (Kullanıcı İsteği): [0.2, 0.8, 0.5]

--- En İyi 2 Eşleşme ---
Kitap: Interstellar (Bilim Kurgu)
Özet: Zaman ve uzayda geçen duygusal bir yolculuk.
Benzerlik Skoru: 0.9932

Kitap: Marslı (Bilim Kurgu)
Özet: Mars’ta mahsur kalan bir astronotun hayatta kalma çabası.
Benzerlik Skoru: 0.8992
```

### 6. AI usage disclosure
*   **Google Gemini:** Used to structure the `docker-compose.yml` configuration, generate the Python interaction script, formulate the database schema (`init.sql`), and draft this README document according to the assignment rubric.
````</yzv322e_pgvector_container></https://github.com/itu-itis23-kilici23/yzv322e_pgvector_container>
