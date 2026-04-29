import psycopg
from pgvector.psycopg import register_vector

def main():
    # 1. Adım: Veritabanına bağlantı ayarları (docker-compose'daki ile aynı olmalı)
    conn_dict = {
        "dbname": "vector_search_db",
        "user": "itu_student",
        "password": "dateng2026",
        "host": "localhost",
        "port": "5433"
    }
    
    print("Veritabanına bağlanılıyor...\n")
    
    try:
        with psycopg.connect(**conn_dict) as conn:
            # 2. Adım: Postgres bağlantısına 'vector' veri tipini öğret
            register_vector(conn)
            
            # 3. Adım: Arama Vektörünü Tanımla
            # init.sql'deki sıramız: [Aksiyon, Bilim, Romantizm]
            # Örnek Kullanıcı İsteği: "Biraz bilim kurgu, biraz da duygu barındıran bir kitap"
            search_vector = [0.2, 0.8, 0.5] 
            print(f"Aranan Vektör (Kullanıcı İsteği): {search_vector}\n")
            
            # 4. Adım: Vektör Benzerlik Sorgusu (Similarity Search)
            # <=> operatörü Cosine Distance (Kosinüs Uzaklığı) hesaplar.
            # Uzaklık sıfıra ne kadar yakınsa, benzerlik o kadar yüksektir (1 - uzaklık = benzerlik).
            with conn.cursor() as cur:
                cur.execute("""
                    SELECT title, category, summary, 
                           1 - (embedding <=> %s::vector) AS similarity_score
                    FROM books
                    ORDER BY embedding <=> %s::vector
                    LIMIT 2;
                """, (search_vector, search_vector))
                
                print("--- En İyi 2 Eşleşme ---")
                for row in cur.fetchall():
                    title, category, summary, score = row
                    print(f"Kitap: {title} ({category})")
                    print(f"Özet: {summary}")
                    print(f"Benzerlik Skoru: {score:.4f}\n")
                    
    except Exception as e:
        print(f"Bir hata oluştu: {e}")

if __name__ == "__main__":
    main()
