import psycopg2
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime


class Veritabani:
    def __init__(self, dbname, user, password, host, port):
        self.conn = psycopg2.connect(
            dbname=dbname, user=user, password=password, host=host, port=port
        )
        self.cursor = self.conn.cursor()
        print("Veritabanına başarıyla bağlandı.")

    def gemileri_getir(self):
        self.cursor.execute("SELECT * FROM Gemi")
        return self.cursor.fetchall()

    def limanlari_getir(self):
        self.cursor.execute("SELECT *FROM Liman")
        return self.cursor.fetchall()

    def gemi_ekle(self, gemi):
        self.cursor.execute(
            "INSERT INTO Gemi (seri_no, ad, agirlik, yapim_yili, tur) VALUES (%s, %s, %s, %s, %s)",
            (gemi.seri_no, gemi.ad, gemi.agirlik, gemi.yapim_yili, gemi.tur),
        )
        self.conn.commit()

    def liman_ekle(self, liman):
        self.cursor.execute(
            "INSERT INTO Liman (liman_adi, ulke, nufus, pasaport_gerekli, demirleme_ucreti) VALUES (%s, %s, %s, %s, %s)",
            (
                liman.liman_adi,
                liman.ulke,
                liman.nufus,
                liman.pasaport_gerekli,
                liman.demirleme_ucreti,
            ),
        )
        self.conn.commit()

    def kaptan_ekle(self, kaptan):
        self.cursor.execute(
            "INSERT INTO Kaptan (id, ad, soyad, adres, vatandaslik, dogum_tarihi, ise_giris_tarihi, lisans) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",
            (
                kaptan.id_no,
                kaptan.ad,
                kaptan.soyad,
                kaptan.adres,
                kaptan.vatandaslik,
                kaptan.dogum_tarihi,
                kaptan.ise_giris_tarihi,
                kaptan.lisans,
            ),
        )
        self.conn.commit()

    def murettebat_ekle(self, murettabat):
        self.cursor.execute(
            "INSERT INTO Murettabat (id, ad, soyad, adres, vatandaslik, dogum_tarihi, ise_giris_tarihi, lisans) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",
            (
                murettabat.id_no,
                murettabat.ad,
                murettabat.soyad,
                murettabat.adres,
                murettabat.vatandaslik,
                murettabat.dogum_tarihi,
                murettabat.ise_giris_tarihi,
                murettabat.lisans,
            ),
        )
        self.conn.commit()

    def liman_sil(self, liman_adi):
        self.cursor.execute("DELETE FROM Liman WHERE liman_adi = %s", (liman_adi,))
        self.conn.commit()

    def liman_guncelle(self, liman):
        self.cursor.execute(
            "UPDATE Liman SET ulke = %s, nufus = %s, pasaport_gerekli = %s, demirleme_ucreti = %s WHERE liman_adi = %s",
            (
                liman.ulke,
                liman.nufus,
                liman.pasaport_gerekli,
                liman.demirleme_ucreti,
                liman.liman_adi,
            ),
        )
        self.conn.commit()


class Gemi:
    def __init__(self, seri_no, ad, agirlik, yapim_yili, tur):
        self.seri_no = seri_no
        self.ad = ad
        self.agirlik = agirlik
        self.yapim_yili = yapim_yili
        self.tur = tur


class YolcuGemisi(Gemi):
    def __init__(self, seri_no, ad, agirlik, yapim_yili, yolcu_kapasitesi, tur):
        super().__init__(seri_no, ad, agirlik, yapim_yili, tur)
        self.yolcu_kapasitesi = yolcu_kapasitesi


class PetrolTankeri(Gemi):
    def __init__(self, seri_no, ad, agirlik, yapim_yili, petrol_kapasitesi, tur):
        super().__init__(seri_no, ad, agirlik, yapim_yili, tur)
        self.petrol_kapasitesi = petrol_kapasitesi


class KonteynerGemisi(Gemi):
    def __init__(
        self, seri_no, ad, agirlik, yapim_yili, konteyner_sayisi, maks_agirlik, tur
    ):
        super().__init__(seri_no, ad, agirlik, yapim_yili, tur)
        self.konteyner_sayisi = konteyner_sayisi
        self.maks_agirlik = maks_agirlik


class YolcuGemisiForm(tk.Tk):
    def __init__(self, veritabani):
        super().__init__()

        self.veritabani = veritabani
        self.title("Yolcu Gemisi Bilgileri")

        # Listbox bileşeni oluştur
        self.gemi_listbox = tk.Listbox(self)
        self.gemi_listbox.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

        # Diğer bileşenler
        self.label_seri_no = tk.Label(self, text="Seri No:")
        self.entry_seri_no = tk.Entry(self)
        self.label_seri_no.grid(row=0, column=0, padx=5, pady=5)
        self.entry_seri_no.grid(row=0, column=1, padx=5, pady=5)

        self.label_ad = tk.Label(self, text="Ad:")
        self.entry_ad = tk.Entry(self)
        self.label_ad.grid(row=1, column=0, padx=5, pady=5)
        self.entry_ad.grid(row=1, column=1, padx=5, pady=5)

        self.label_agirlik = tk.Label(self, text="Ağırlık:")
        self.entry_agirlik = tk.Entry(self)
        self.label_agirlik.grid(row=2, column=0, padx=5, pady=5)
        self.entry_agirlik.grid(row=2, column=1, padx=5, pady=5)

        self.label_yapim_yili = tk.Label(self, text="Yapım Yılı:")
        self.entry_yapim_yili = tk.Entry(self)
        self.label_yapim_yili.grid(row=3, column=0, padx=5, pady=5)
        self.entry_yapim_yili.grid(row=3, column=1, padx=5, pady=5)

        self.label_yolcu_kapasitesi = tk.Label(self, text="Yolcu Kapasitesi:")
        self.entry_yolcu_kapasitesi = tk.Entry(self)
        self.label_yolcu_kapasitesi.grid(row=4, column=0, padx=5, pady=5)
        self.entry_yolcu_kapasitesi.grid(row=4, column=1, padx=5, pady=5)

        self.button_kaydet = tk.Button(self, text="Kaydet", command=self.kaydet)
        self.button_kaydet.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

    def veritabanini_yenile(self):
        # Eski verileri temizle
        self.gemi_listbox.delete(0, tk.END)
        # Yeni verileri getir ve listbox'a ekle
        gemiler = self.veritabani.gemileri_getir()
        for gemi in gemiler:
            self.gemi_listbox.insert(tk.END, gemi)

    def kaydet(self):
        seri_no = self.entry_seri_no.get()
        ad = self.entry_ad.get()
        agirlik = self.entry_agirlik.get()
        yapim_yili = self.entry_yapim_yili.get()
        yolcu_kapasitesi = self.entry_yolcu_kapasitesi.get()

        try:
            gemi = YolcuGemisi(
                seri_no, ad, agirlik, yapim_yili, yolcu_kapasitesi, "Yolcu Gemisi"
            )
            self.veritabani.gemi_ekle(gemi)
            self.veritabanini_yenile()
            messagebox.showinfo("Başarılı", "Yolcu gemisi başarıyla eklendi.")
        except Exception as e:
            messagebox.showerror("Hata", f"Bir hata oluştu: {e}")
            self.destroy()


class PetrolTankeriForm(tk.Tk):
    def __init__(self, veritabani):
        super().__init__()

        self.veritabani = veritabani
        self.title("Petrol Tankeri Bilgileri")
        # Listbox bileşeni oluşturduk

        self.gemi_listbox = tk.Listbox(self)
        self.gemi_listbox.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

        self.label_seri_no = tk.Label(self, text="Seri No:")
        self.entry_seri_no = tk.Entry(self)
        self.label_seri_no.grid(row=0, column=0, padx=5, pady=5)
        self.entry_seri_no.grid(row=0, column=1, padx=5, pady=5)

        self.label_ad = tk.Label(self, text="Ad:")
        self.entry_ad = tk.Entry(self)
        self.label_ad.grid(row=1, column=0, padx=5, pady=5)
        self.entry_ad.grid(row=1, column=1, padx=5, pady=5)

        self.label_agirlik = tk.Label(self, text="Ağırlık:")
        self.entry_agirlik = tk.Entry(self)
        self.label_agirlik.grid(row=2, column=0, padx=5, pady=5)
        self.entry_agirlik.grid(row=2, column=1, padx=5, pady=5)

        self.label_yapim_yili = tk.Label(self, text="Yapım Yılı:")
        self.entry_yapim_yili = tk.Entry(self)
        self.label_yapim_yili.grid(row=3, column=0, padx=5, pady=5)
        self.entry_yapim_yili.grid(row=3, column=1, padx=5, pady=5)

        self.label_petrol_kapasitesi = tk.Label(self, text="Petrol Kapasitesi:")
        self.entry_petrol_kapasitesi = tk.Entry(self)
        self.label_petrol_kapasitesi.grid(row=4, column=0, padx=5, pady=5)
        self.entry_petrol_kapasitesi.grid(row=4, column=1, padx=5, pady=5)

        self.button_kaydet = tk.Button(self, text="Kaydet", command=self.kaydet)
        self.button_kaydet.grid(row=8, column=0, columnspan=2, padx=5, pady=5)

    def veritabanini_yenile(self):
        self.gemi_listbox.delete(0, tk.END)
        gemiler = self.veritabani.gemileri_getir()
        for gemi in gemiler:
            self.gemi_listbox.insert(tk.END, gemi)

    def kaydet(self):
        seri_no = self.entry_seri_no.get()
        ad = self.entry_ad.get()
        agirlik = self.entry_agirlik.get()
        yapim_yili = self.entry_yapim_yili.get()
        petrol_kapasitesi = self.entry_petrol_kapasitesi.get()

        try:
            gemi = PetrolTankeri(
                seri_no, ad, agirlik, yapim_yili, petrol_kapasitesi, "Petrol Tankeri"
            )
            self.veritabani.gemi_ekle(gemi)
            self.veritabanini_yenile()
            messagebox.showinfo("Başarılı", "Petrol tankeri başarıyla eklendi.")
        except Exception as e:
            messagebox.showerror("Hata", f"Bir hata oluştu: {e}")
            self.destroy()


class KonteynerGemisiForm(tk.Tk):
    def __init__(self, veritabani):
        super().__init__()

        self.veritabani = veritabani
        self.title("Konteyner Gemisi Bilgileri")
        # Listbox bileşeni oluştur

        self.gemi_listbox = tk.Listbox(self)
        self.gemi_listbox.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

        self.label_seri_no = tk.Label(self, text="Seri No:")
        self.entry_seri_no = tk.Entry(self)
        self.label_seri_no.grid(row=0, column=0, padx=5, pady=5)
        self.entry_seri_no.grid(row=0, column=1, padx=5, pady=5)

        self.label_ad = tk.Label(self, text="Ad:")
        self.entry_ad = tk.Entry(self)
        self.label_ad.grid(row=1, column=0, padx=5, pady=5)
        self.entry_ad.grid(row=1, column=1, padx=5, pady=5)

        self.label_agirlik = tk.Label(self, text="Ağırlık:")
        self.entry_agirlik = tk.Entry(self)
        self.label_agirlik.grid(row=2, column=0, padx=5, pady=5)
        self.entry_agirlik.grid(row=2, column=1, padx=5, pady=5)

        self.label_yapim_yili = tk.Label(self, text="Yapım Yılı:")
        self.entry_yapim_yili = tk.Entry(self)
        self.label_yapim_yili.grid(row=3, column=0, padx=5, pady=5)
        self.entry_yapim_yili.grid(row=3, column=1, padx=5, pady=5)

        self.label_konteyner_sayisi = tk.Label(self, text="Konteyner Sayısı:")
        self.entry_konteyner_sayisi = tk.Entry(self)
        self.label_konteyner_sayisi.grid(row=4, column=0, padx=5, pady=5)
        self.entry_konteyner_sayisi.grid(row=4, column=1, padx=5, pady=5)

        self.label_maks_agirlik = tk.Label(self, text="Maksimum Ağırlık:")
        self.entry_maks_agirlik = tk.Entry(self)
        self.label_maks_agirlik.grid(row=5, column=0, padx=5, pady=5)
        self.entry_maks_agirlik.grid(row=5, column=1, padx=5, pady=5)

        self.button_kaydet = tk.Button(self, text="Kaydet", command=self.kaydet)
        self.button_kaydet.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

    def veritabanini_yenile(self):
        self.gemi_listbox.delete(0, tk.END)
        gemiler = self.veritabani.gemileri_getir()
        for gemi in gemiler:
            self.gemi_listbox.insert(tk.END, gemi)

    def kaydet(self):
        seri_no = self.entry_seri_no.get()
        ad = self.entry_ad.get()
        agirlik = self.entry_agirlik.get()
        yapim_yili = self.entry_yapim_yili.get()
        konteyner_sayisi = self.entry_konteyner_sayisi.get()
        maks_agirlik = self.entry_maks_agirlik.get()

        try:
            gemi = KonteynerGemisi(
                seri_no,
                ad,
                agirlik,
                yapim_yili,
                konteyner_sayisi,
                maks_agirlik,
                "Konteyner Gemisi",
            )
            self.veritabani.gemi_ekle(gemi)
            self.veritabanini_yenile()
            messagebox.showinfo("Başarılı", "Konteyner gemisi başarıyla eklendi.")
        except Exception as e:
            messagebox.showerror("Hata", f"Bir hata oluştu: {e}")
            self.destroy()


class Kaptan:
    def __init__(
        self,
        id_no,
        ad,
        soyad,
        adres,
        vatandaslik,
        dogum_tarihi,
        ise_giris_tarihi,
        lisans,
    ):
        self.id_no = id_no
        self.ad = ad
        self.soyad = soyad
        self.adres = adres
        self.vatandaslik = vatandaslik
        self.dogum_tarihi = dogum_tarihi
        self.ise_giris_tarihi = ise_giris_tarihi
        self.lisans = lisans


class Murettabat:
    def __init__(
        self,
        id_no,
        ad,
        soyad,
        adres,
        vatandaslik,
        dogum_tarihi,
        ise_giris_tarihi,
        lisans,
    ):
        self.id_no = id_no
        self.ad = ad
        self.soyad = soyad
        self.adres = adres
        self.vatandaslik = vatandaslik
        self.dogum_tarihi = dogum_tarihi
        self.ise_giris_tarihi = ise_giris_tarihi
        self.lisans = lisans


class Liman:
    def __init__(self, liman_adi, ulke, nufus, pasaport_gerekli, demirleme_ucreti):
        self.liman_adi = liman_adi
        self.ulke = ulke
        self.nufus = nufus
        self.pasaport_gerekli = pasaport_gerekli
        self.demirleme_ucreti = demirleme_ucreti


class Sefer:
    def __init__(
        self,
        id_no,
        yolcu_gemi,
        petrol_tankeri,
        konteyner_gemisi,
        kaptanlar,
        murettabatlar,
        limanlar,
        yolcu_kalkis_tarihi,
        yolcu_donus_tarihi,
    ):
        self.id_no = id_no
        self.yolcu_gemi = yolcu_gemi
        self.petrol_tankeri = petrol_tankeri
        self.konteyner_gemisi = konteyner_gemisi
        self.kaptanlar = kaptanlar
        self.murettabatlar = murettabatlar
        self.limanlar = limanlar
        self.yolcu_kalkis_tarihi = yolcu_kalkis_tarihi
        self.yolcu_donus_tarihi = yolcu_donus_tarihi


class GemiVeritabani(Veritabani):
    def __init__(self):
        super().__init__("GemiSirketi", "postgres", "787614", "localhost", "5432")

    def gemi_ekle(self, gemi):
        self.cursor.execute(
            "INSERT INTO Gemi (seri_no, ad, agirlik, yapim_yili) VALUES (%s, %s, %s, %s, %s)",
            (gemi.seri_no, gemi.ad, gemi.agirlik, gemi.yapim_yili, gemi.tur),
        )
        self.conn.commit()

    def gemi_sil(self, seri_no):
        self.cursor.execute("DELETE FROM Gemi WHERE seri_no = %s", (seri_no,))
        self.conn.commit()

    def gemi_guncelle(self, gemi):
        self.cursor.execute(
            "UPDATE Gemi SET ad = %s, agirlik = %s, yapim_yili = %s WHERE seri_no = %s",
            (gemi.ad, gemi.agirlik, gemi.yapim_yili, gemi.seri_no),
        )
        self.conn.commit()


class KaptanVeritabani(Veritabani):
    def __init__(self):
        super().__init__("GemiSirketi", "postgres", "787614", "localhost", "5432")

    def kaptan_ekle(self, kaptan):
        self.cursor.execute(
            "INSERT INTO Kaptan (id_no, ad, soyad, adres, vatandaslik, dogum_tarihi, ise_giris_tarihi, lisans) VALUES "
            "(%s, %s, %s, %s, %s, %s, %s, %s)",
            (
                kaptan.id_no,
                kaptan.ad,
                kaptan.soyad,
                kaptan.adres,
                kaptan.vatandaslik,
                kaptan.dogum_tarihi,
                kaptan.ise_giris_tarihi,
                kaptan.lisans,
            ),
        )
        self.conn.commit()

    def kaptan_sil(self, id_no):
        self.cursor.execute("DELETE FROM Kaptan WHERE id_no = %s", (id_no,))
        self.conn.commit()

    def kaptan_guncelle(self, kaptan):
        self.cursor.execute(
            "UPDATE Kaptan SET ad = %s, soyad = %s, adres = %s, vatandaslik = %s, dogum_tarihi = %s, ise_giris_tarihi "
            "= %s, lisans = %s WHERE id_no = %s",
            (
                kaptan.ad,
                kaptan.soyad,
                kaptan.adres,
                kaptan.vatandaslik,
                kaptan.dogum_tarihi,
                kaptan.ise_giris_tarihi,
                kaptan.lisans,
                kaptan.id_no,
            ),
        )
        self.conn.commit()


class MurettabatVeritabani(Veritabani):
    def __init__(self):
        super().__init__("GemiSirketi", "postgres", "787614", "localhost", "5432")

    def murettebat_ekle(self, murettabat):
        self.cursor.execute(
            "INSERT INTO Murettabat (id_no, ad, soyad, adres, vatandaslik, dogum_tarihi, ise_giris_tarihi) VALUES (%s, %s, %s, %s, %s, %s, %s)",
            (
                murettabat.id_no,
                murettabat.ad,
                murettabat.soyad,
                murettabat.adres,
                murettabat.vatandaslik,
                murettabat.dogum_tarihi,
                murettabat.ise_giris_tarihi,
            ),
        )
        self.conn.commit()

    def murettabat_sil(self, id_no):
        self.cursor.execute("DELETE FROM Murettabat WHERE id_no = %s", (id_no,))
        self.conn.commit()

    def murettabat_guncelle(self, murettabat):
        self.cursor.execute(
            "UPDATE Murettabat SET ad = %s, soyad = %s, adres = %s, vatandaslik = %s, dogum_tarihi = %s, ise_giris_tarihi = %s WHERE id_no = %s",
            (
                murettabat.ad,
                murettabat.soyad,
                murettabat.adres,
                murettabat.vatandaslik,
                murettabat.dogum_tarihi,
                murettabat.ise_giris_tarihi,
                murettabat.id_no,
            ),
        )
        self.conn.commit()


class LimanVeritabani(Veritabani):
    def __init__(self):
        super().__init__("GemiSirketi", "postgres", "787614", "localhost", "5432")

    def liman_ekle(self, liman):
        self.cursor.execute(
            "INSERT INTO Liman (liman_adi, ulke, nufus, pasaport_gerekli, demirleme_ucreti) VALUES (%s, %s, %s, %s, %s)",
            (
                liman.liman_adi,
                liman.ulke,
                liman.nufus,
                liman.pasaport_gerekli,
                liman.demirleme_ucreti,
            ),
        )
        self.conn.commit()

    def liman_sil(self, liman_adi):
        self.cursor.execute("DELETE FROM Liman WHERE liman_adi = %s", (liman_adi,))
        self.conn.commit()

    def liman_guncelle(self, liman):
        self.cursor.execute(
            "UPDATE Liman SET ulke = %s, nufus = %s, pasaport_gerekli = %s, demirleme_ucreti = %s WHERE liman_adi = %s",
            (
                liman.ulke,
                liman.nufus,
                liman.pasaport_gerekli,
                liman.demirleme_ucreti,
                liman.liman_adi,
            ),
        )
        self.conn.commit()


class SeferVeritabani(Veritabani):
    def __init__(self):
        super().__init__("GemiSirketi", "postgres", "787614", "localhost", "5432")

    def sefer_ekle(self, sefer):
        self.cursor.execute(
            "INSERT INTO Sefer (id_no, yolcu_gemi, petrol_tankeri, konteyner_gemisi, kaptanlar, murettabatlar, limanlar, yolcu_kalkis_tarihi, yolcu_donus_tarihi) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (
                sefer.id_no,
                sefer.yolcu_gemi,
                sefer.petrol_tankeri,
                sefer.konteyner_gemisi,
                sefer.kaptanlar,
                sefer.murettabatlar,
                sefer.limanlar,
                sefer.yolcu_kalkis_tarihi,
                sefer.yolcu_donus_tarihi,
            ),
        )
        self.conn.commit()

    def sefer_sil(self, id_no):
        self.cursor.execute("DELETE FROM Sefer WHERE id_no = %s", (id_no,))
        self.conn.commit()

    def sefer_guncelle(self, sefer):
        self.cursor.execute(
            "UPDATE Sefer SET yolcu_gemi = %s, petrol_tankeri = %s, konteyner_gemisi = %s, kaptanlar = %s, murettabatlar = %s, limanlar = %s, yolcu_kalkis_tarihi = %s, yolcu_donus_tarihi = %s WHERE id_no = %s",
            (
                sefer.yolcu_gemi,
                sefer.petrol_tankeri,
                sefer.konteyner_gemisi,
                sefer.kaptanlar,
                sefer.murettabatlar,
                sefer.limanlar,
                sefer.yolcu_kalkis_tarihi,
                sefer.yolcu_donus_tarihi,
                sefer.id_no,
            ),
        )
        self.conn.commit()


class GemiForm(tk.Frame):
    def __init__(self, parent, veritabani):
        super().__init__(parent)

        self.veritabani = veritabani
        self.pack()
        self.veritabani = Veritabani(
            "GemiSirketi", "postgres", "787614", "localhost", "5432"
        )
        if isinstance(parent, tk.Tk):
            window = parent
        else:
            window = parent.winfo_toplevel()

        window.title("Gemi Bilgileri Formu")
        self.label_tur = tk.Label(self, text="Gemi Türü:")
        self.combobox_tur = ttk.Combobox(
            self, values=["Yolcu Gemisi", "Petrol Tankeri", "Konteyner Gemisi"]
        )
        self.label_tur.grid(row=0, column=0, padx=5, pady=5)
        self.combobox_tur.grid(row=0, column=1, padx=5, pady=5)

        self.button_sec = tk.Button(self, text="Seç", command=self.sec)
        self.button_sec.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

    def sec(self):
        secilen_tur = self.combobox_tur.get()
        if secilen_tur == "Yolcu Gemisi":
            self.yolcu_gemisi_formunu_ac()
        elif secilen_tur == "Petrol Tankeri":
            self.petrol_tankeri_formunu_ac()
        elif secilen_tur == "Konteyner Gemisi":
            self.konteyner_gemisi_formunu_ac()

    def yolcu_gemisi_formunu_ac(self):
        self.destroy()
        form = YolcuGemisiForm(self.veritabani)
        form.mainloop()

    def petrol_tankeri_formunu_ac(self):
        self.destroy()
        form = PetrolTankeriForm(self.veritabani)
        form.mainloop()

    def konteyner_gemisi_formunu_ac(self):
        self.destroy()
        form = KonteynerGemisiForm(self.veritabani)
        form.mainloop()


class LimanForm(tk.Toplevel):
    def __init__(self, parent, veritabani):
        super().__init__(parent)
        self.veritabani = veritabani
        self.geometry("600x400+100+100")
        self.title("Liman Bilgileri Formu")

        # Metin kutuları ve etiketleri ekle
        self.label_liman_adi = tk.Label(self, text="Liman Adı:")
        self.entry_liman_adi = tk.Entry(self)
        self.label_ulke = tk.Label(self, text="Ülke:")
        self.entry_ulke = tk.Entry(self)
        self.label_nufus = tk.Label(self, text="Nüfus:")
        self.entry_nufus = tk.Entry(self)
        self.label_pasaport_gerekli = tk.Label(self, text="Pasaport Gerekli:")
        self.combobox_pasaport_gerekli = ttk.Combobox(self, values=["Evet", "Hayır"])
        self.label_demirleme_ucreti = tk.Label(self, text="Demirleme Ücreti:")
        self.entry_demirleme_ucreti = tk.Entry(self)

        # Metin kutuları ve etiketleri pencereye yerleştir
        self.label_liman_adi.grid(row=0, column=0, padx=5, pady=5)
        self.entry_liman_adi.grid(row=0, column=1, padx=5, pady=5)
        self.label_ulke.grid(row=1, column=0, padx=5, pady=5)
        self.entry_ulke.grid(row=1, column=1, padx=5, pady=5)
        self.label_nufus.grid(row=2, column=0, padx=5, pady=5)
        self.entry_nufus.grid(row=2, column=1, padx=5, pady=5)
        self.label_pasaport_gerekli.grid(row=3, column=0, padx=5, pady=5)
        self.combobox_pasaport_gerekli.grid(row=3, column=1, padx=5, pady=5)
        self.label_demirleme_ucreti.grid(row=4, column=0, padx=5, pady=5)
        self.entry_demirleme_ucreti.grid(row=4, column=1, padx=5, pady=5)

        # Butonları ekle ve pencereye yerleştir
        self.button_kaydet = tk.Button(self, text="Kaydet", command=self.kaydet)
        self.button_guncelle = tk.Button(self, text="Güncelle", command=self.guncelle)
        self.button_sil = tk.Button(self, text="Sil", command=self.sil)
        self.update_button = tk.Button(
            self, text="Veritabanı Bilgilerini Güncelle", command=self.update_veritabani
        )

        self.button_kaydet.grid(row=5, column=0, padx=5, pady=5, sticky="nsew")
        self.button_guncelle.grid(row=5, column=1, padx=5, pady=5, sticky="nsew")
        self.button_sil.grid(row=5, column=2, padx=5, pady=5, sticky="nsew")
        self.update_button.grid(
            row=6, column=0, columnspan=3, padx=5, pady=5, sticky="nsew"
        )

        # Veritabanı bilgilerini göstermek için bir metin alanı ekle
        self.veritabani_text = tk.Text(self, height=10, width=50)
        self.veritabani_text.grid(
            row=7, column=0, columnspan=3, padx=10, pady=10, sticky="nsew"
        )

        # Veritabanını başlangıçta güncelle
        self.update_veritabani()

    def update_veritabani(self):
        # Veritabanı sorgusunu gerçekleştir
        limanlar = self.veritabani.limanlari_getir()

        # Veritabanı bilgilerini temizle
        self.veritabani_text.delete("1.0", tk.END)

        # Veritabanı bilgilerini metin kutusuna ekle
        for liman in limanlar:
            self.veritabani_text.insert(tk.END, f"Liman Adı: {liman[0]}\n")
            self.veritabani_text.insert(tk.END, f"Ülke: {liman[1]}\n")
            self.veritabani_text.insert(tk.END, f"Nüfus: {liman[2]}\n")
            self.veritabani_text.insert(
                tk.END, f"Pasaport Gerekli: {'Evet' if liman[3] else 'Hayır'}\n"
            )
            self.veritabani_text.insert(tk.END, f"Demirleme Ücreti: {liman[4]}\n")
            self.veritabani_text.insert(tk.END, "----------------------------------\n")

    def kaydet(self):
        liman_adi = self.entry_liman_adi.get()
        ulke = self.entry_ulke.get()
        nufus = self.entry_nufus.get()
        pasaport_gerekli = (
            True if self.combobox_pasaport_gerekli.get() == "Evet" else False
        )
        demirleme_ucreti = self.entry_demirleme_ucreti.get()

        try:
            liman = Liman(liman_adi, ulke, nufus, pasaport_gerekli, demirleme_ucreti)
            self.veritabani.liman_ekle(liman)
            messagebox.showinfo("Başarılı", "Liman başarıyla eklendi.")
            # Veritabanını güncelle
            self.update_veritabani()
        except Exception as e:
            messagebox.showerror("Hata", f"Bir hata oluştu: {e}")

    def guncelle(self):
        liman_adi = self.entry_liman_adi.get()
        ulke = self.entry_ulke.get()
        nufus = self.entry_nufus.get()
        pasaport_gerekli = (
            True if self.combobox_pasaport_gerekli.get() == "Evet" else False
        )
        demirleme_ucreti = self.entry_demirleme_ucreti.get()

        try:
            liman = Liman(liman_adi, ulke, nufus, pasaport_gerekli, demirleme_ucreti)
            self.veritabani.liman_guncelle(liman)
            messagebox.showinfo("Başarılı", "Liman başarıyla güncellendi.")
            # Veritabanını güncelliyoruz
            self.update_veritabani()
        except Exception as e:
            messagebox.showerror("Hata", f"Bir hata oluştu: {e}")

    def sil(self):
        liman_adi = self.entry_liman_adi.get()
        try:
            self.veritabani.liman_sil(liman_adi)
            messagebox.showinfo("Başarılı", "Liman başarıyla silindi.")
            self.update_veritabani()
        except Exception as e:
            messagebox.showerror("Hata", f"Bir hata oluştu: {e}")


class KaptanForm(tk.Frame):
    def __init__(self, parent, veritabani):
        super().__init__(parent)

        self.veritabani = veritabani

        self.label_id = tk.Label(self, text="ID:")
        self.entry_id = tk.Entry(self)
        self.label_ad = tk.Label(self, text="Ad:")
        self.entry_ad = tk.Entry(self)
        self.label_soyad = tk.Label(self, text="Soyad:")
        self.entry_soyad = tk.Entry(self)
        self.label_adres = tk.Label(self, text="Adres:")
        self.entry_adres = tk.Entry(self)
        self.label_vatandaslik = tk.Label(self, text="Vatandaşlık:")
        self.entry_vatandaslik = tk.Entry(self)
        self.label_dogum_tarihi = tk.Label(self, text="Doğum Tarihi:")
        self.entry_dogum_tarihi = tk.Entry(self)
        self.label_ise_giris_tarihi = tk.Label(self, text="İşe Giriş Tarihi:")
        self.entry_ise_giris_tarihi = tk.Entry(self)
        self.label_lisans = tk.Label(self, text="Lisans:")
        self.entry_lisans = tk.Entry(self)

        self.label_id.grid(row=0, column=0, padx=5, pady=5)
        self.entry_id.grid(row=0, column=1, padx=5, pady=5)
        self.label_ad.grid(row=1, column=0, padx=5, pady=5)
        self.entry_ad.grid(row=1, column=1, padx=5, pady=5)
        self.label_soyad.grid(row=2, column=0, padx=5, pady=5)
        self.entry_soyad.grid(row=2, column=1, padx=5, pady=5)
        self.label_adres.grid(row=3, column=0, padx=5, pady=5)
        self.entry_adres.grid(row=3, column=1, padx=5, pady=5)
        self.label_vatandaslik.grid(row=4, column=0, padx=5, pady=5)
        self.entry_vatandaslik.grid(row=4, column=1, padx=5, pady=5)
        self.label_dogum_tarihi.grid(row=5, column=0, padx=5, pady=5)
        self.entry_dogum_tarihi.grid(row=5, column=1, padx=5, pady=5)
        self.label_ise_giris_tarihi.grid(row=6, column=0, padx=5, pady=5)
        self.entry_ise_giris_tarihi.grid(row=6, column=1, padx=5, pady=5)
        self.label_lisans.grid(row=7, column=0, padx=5, pady=5)
        self.entry_lisans.grid(row=7, column=1, padx=5, pady=5)

        self.button_kaydet = tk.Button(self, text="Kaydet", command=self.kaydet)
        self.button_kaydet.grid(row=9, column=0, columnspan=2, padx=5, pady=5)

    def kaydet(self):
        id = self.entry_id.get()
        ad = self.entry_ad.get()
        soyad = self.entry_soyad.get()
        adres = self.entry_adres.get()
        vatandaslik = self.entry_vatandaslik.get()
        dogum_tarihi = self.entry_dogum_tarihi.get()
        ise_giris_tarihi = self.entry_ise_giris_tarihi.get()
        lisans = self.entry_lisans.get()

        try:
            kaptan = Kaptan(
                id,
                ad,
                soyad,
                adres,
                vatandaslik,
                dogum_tarihi,
                ise_giris_tarihi,
                lisans,
            )
            self.veritabani.kaptan_ekle(kaptan)
            messagebox.showinfo("Başarılı", "Kaptan başarıyla eklendi.")
        except Exception as e:
            messagebox.showerror("Hata", f"Bir hata oluştu: {e}")


class MurettebatForm(tk.Frame):
    def __init__(self, parent, veritabani):
        super().__init__(parent)

        self.veritabani = veritabani

        self.label_id = tk.Label(self, text="ID:")
        self.entry_id = tk.Entry(self)
        self.label_ad = tk.Label(self, text="Ad:")
        self.entry_ad = tk.Entry(self)
        self.label_soyad = tk.Label(self, text="Soyad:")
        self.entry_soyad = tk.Entry(self)
        self.label_adres = tk.Label(self, text="Adres:")
        self.entry_adres = tk.Entry(self)
        self.label_vatandaslik = tk.Label(self, text="Vatandaşlık:")
        self.entry_vatandaslik = tk.Entry(self)
        self.label_dogum_tarihi = tk.Label(self, text="Doğum Tarihi:")
        self.entry_dogum_tarihi = tk.Entry(self)
        self.label_ise_giris_tarihi = tk.Label(self, text="İşe Giriş Tarihi:")
        self.entry_ise_giris_tarihi = tk.Entry(self)
        self.label_lisans = tk.Label(self, text="Lisans:")
        self.entry_lisans = tk.Entry(self)

        self.label_id.grid(row=0, column=0, padx=5, pady=5)
        self.entry_id.grid(row=0, column=1, padx=5, pady=5)
        self.label_ad.grid(row=1, column=0, padx=5, pady=5)
        self.entry_ad.grid(row=1, column=1, padx=5, pady=5)
        self.label_soyad.grid(row=2, column=0, padx=5, pady=5)
        self.entry_soyad.grid(row=2, column=1, padx=5, pady=5)
        self.label_adres.grid(row=3, column=0, padx=5, pady=5)
        self.entry_adres.grid(row=3, column=1, padx=5, pady=5)
        self.label_vatandaslik.grid(row=4, column=0, padx=5, pady=5)
        self.entry_vatandaslik.grid(row=4, column=1, padx=5, pady=5)
        self.label_dogum_tarihi.grid(row=5, column=0, padx=5, pady=5)
        self.entry_dogum_tarihi.grid(row=5, column=1, padx=5, pady=5)
        self.label_ise_giris_tarihi.grid(row=6, column=0, padx=5, pady=5)
        self.entry_ise_giris_tarihi.grid(row=6, column=1, padx=5, pady=5)
        self.label_lisans.grid(row=7, column=0, padx=5, pady=5)
        self.entry_lisans.grid(row=7, column=1, padx=5, pady=5)

        self.button_kaydet = tk.Button(self, text="Kaydet", command=self.kaydet)
        self.button_kaydet.grid(row=8, column=0, columnspan=2, padx=5, pady=5)

    def kaydet(self):
        id = self.entry_id.get()
        ad = self.entry_ad.get()
        soyad = self.entry_soyad.get()
        adres = self.entry_adres.get()
        vatandaslik = self.entry_vatandaslik.get()
        dogum_tarihi = self.entry_dogum_tarihi.get()
        ise_giris_tarihi = self.entry_ise_giris_tarihi.get()
        lisans = self.entry_lisans.get()

        try:
            murettebat = Murettabat(
                id,
                ad,
                soyad,
                adres,
                vatandaslik,
                dogum_tarihi,
                ise_giris_tarihi,
                lisans,
            )
            self.veritabani.murettebat_ekle(murettebat)
            messagebox.showinfo("Başarılı", "Murettebat başarıyla eklendi.")
        except Exception as e:
            messagebox.showerror("Hata", f"Bir hata oluştu: {e}")


class AnaPencere(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Ana Pencere")

        # Veritabanı bağlantısı oluşturur
        self.veritabani = Veritabani(
            "GemiSirketi", "postgres", "787614", "localhost", "5432"
        )

        # Sekmeleri oluşturur
        self.tabControl = ttk.Notebook(self)

        # Gemi sekmesi
        tab_gemi = ttk.Frame(self.tabControl)
        self.tabControl.add(tab_gemi, text="Gemiler")

        # Liman sekmesi
        self.tab_liman = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tab_liman, text="Limanlar")

        self.liman_form = LimanForm(self.tab_liman, self.veritabani)
        self.liman_form.geometry()

        self.tabControl.pack(expand=1, fill="both")
        gemi_form = GemiForm(tab_gemi, self.veritabani)
        gemi_form.pack()

        # Kaptan sekmesi
        tab_kaptan = ttk.Frame(self.tabControl)
        self.tabControl.add(tab_kaptan, text="Kaptanlar")
        kaptan_form = KaptanForm(tab_kaptan, self.veritabani)
        kaptan_form.pack(fill="both", expand=True, padx=5, pady=5)

        tab_murettabat = ttk.Frame(self.tabControl)
        self.tabControl.add(tab_murettabat, text="Murettebat")
        murettaba_form = MurettebatForm(tab_murettabat, self.veritabani)
        murettaba_form.pack(fill="both", expand=True, padx=5, pady=5)


if __name__ == "__main__":
    app = AnaPencere()
    app.mainloop()
