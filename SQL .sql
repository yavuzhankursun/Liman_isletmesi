CREATE TABLE IF NOT EXISTS Gemi (
    seri_no VARCHAR(50) PRIMARY KEY,
    ad VARCHAR(100),
    agirlik VARCHAR(50),
    yapim_yili VARCHAR(50),
    tur VARCHAR(30)
);

CREATE TABLE IF NOT EXISTS Kaptan (
    ID VARCHAR(50) PRIMARY KEY,
    ad VARCHAR(100),
    soyad VARCHAR(100),
    adres VARCHAR(200),
    vatandaslik VARCHAR(50),
    dogum_tarihi DATE,
    ise_giris_tarihi DATE,
    lisans VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS Murettabat (
    ID VARCHAR(50) PRIMARY KEY,
    ad VARCHAR(100),
    soyad VARCHAR(100),
    adres VARCHAR(200),
    vatandaslik VARCHAR(50),
    dogum_tarihi DATE,
    ise_giris_tarihi DATE,
    lisans VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS Liman (
    liman_adi VARCHAR(100) PRIMARY KEY,
    ulke VARCHAR(100),
    nufus INTEGER,
    pasaport_gerekli BOOLEAN,
    demirleme_ucreti DECIMAL(10, 2)
);

CREATE TABLE IF NOT EXISTS Limansefer (
	liman_adi VARCHAR(100),
	sefer_id VARCHAR(50),
	PRIMARY KEY(liman_adi, sefer_id)
);

CREATE TABLE IF NOT EXISTS Sefer (
    ID VARCHAR(50) PRIMARY KEY,
    yolcu_gemi VARCHAR(50),
    petrol_tankeri VARCHAR(50),
    konteyner_gemisi VARCHAR(50),
    kaptanlar VARCHAR(1000),
    murettabatlar VARCHAR(1000),
    limanlar VARCHAR(1000),
    yolcu_kalkis_tarihi DATE,
    yolcu_donus_tarihi DATE
);