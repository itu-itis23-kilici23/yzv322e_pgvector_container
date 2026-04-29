-- 1. ADIM: pgvector eklentisini veritabanında aktif et
-- Bu komut olmazsa 'vector' veri tipini veritabanı tanımaz.
CREATE EXTENSION IF NOT EXISTS vector;

-- 2. ADIM: Örnek bir 'Kitaplar' tablosu oluştur
-- 'embedding' sütunu, 3 boyutlu bir vektör tutacak şekilde ayarlandı.
-- (Gerçek projelerde bu 768 veya 1536 gibi çok daha yüksek boyutlu olur)
CREATE TABLE books (
    id serial PRIMARY KEY,
    title text NOT NULL,
    category text,
    summary text,
    embedding vector(3) -- [Aksiyon, Bilim, Romantizm] yoğunluğunu temsil etsin
);

-- 3. ADIM: Örnek verileri (Vektörleri) yerleştir
-- Vektör değerlerini manuel veriyoruz (Sanki bir AI modeli çıkarmış gibi)
INSERT INTO books (title, category, summary, embedding) VALUES
('Marslı', 'Bilim Kurgu', 'Mars’ta mahsur kalan bir astronotun hayatta kalma çabası.', '[0.1, 0.9, 0.1]'),
('Gurur ve Önyargı', 'Klasik', '19. yüzyıl İngiltere’sinde geçen romantik bir dram.', '[0.1, 0.1, 0.9]'),
('Mad Max', 'Aksiyon', 'Distopik bir dünyada geçen yüksek tempolu kovalamaca.', '[0.9, 0.2, 0.1]'),
('Interstellar', 'Bilim Kurgu', 'Zaman ve uzayda geçen duygusal bir yolculuk.', '[0.3, 0.8, 0.6]');

-- 4. ADIM: (Opsiyonel ama Profesyonel) İndeks oluştur
-- Veri büyüdüğünde aramaların hızlı olması için HNSW indeksi ekliyoruz.
CREATE INDEX ON books USING hnsw (embedding vector_cosine_ops);
