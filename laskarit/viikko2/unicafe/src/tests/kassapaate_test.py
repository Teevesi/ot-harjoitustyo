import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()

    def test_kassapaatteen_alkusaldo_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kassapaatteen_myydyt_lounaat_alussa_nolla(self):
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_syo_edullisesti_kateisella_kun_maksu_riittaa(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(vaihtoraha, 60)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_syo_edullisesti_kateisella_kun_maksu_ei_riita(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(vaihtoraha, 200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_syo_maukkaasti_kateisella_kun_maksu_riittaa(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(vaihtoraha, 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_syo_maukkaasti_kateisella_kun_maksu_ei_riita(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(300)
        self.assertEqual(vaihtoraha, 300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_syo_edullisesti_kortilla_kun_saldo_riittaa(self):
        kortti = Maksukortti(500)
        onnistui = self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertTrue(onnistui)
        self.assertEqual(kortti.saldo, 260)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_syo_edullisesti_kortilla_kun_saldo_ei_riita(self):
        kortti = Maksukortti(200)
        onnistui = self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertFalse(onnistui)
        self.assertEqual(kortti.saldo, 200)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_syo_maukkaasti_kortilla_kun_saldo_riittaa(self):
        kortti = Maksukortti(500)
        onnistui = self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertTrue(onnistui)
        self.assertEqual(kortti.saldo, 100)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_syo_maukkaasti_kortilla_kun_saldo_ei_riita(self):
        kortti = Maksukortti(300)
        onnistui = self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertFalse(onnistui)
        self.assertEqual(kortti.saldo, 300)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_lataa_rahaa_kortille_kun_summa_positiivinen(self):
        kortti = Maksukortti(500)
        self.kassapaate.lataa_rahaa_kortille(kortti, 2000)
        self.assertEqual(kortti.saldo, 2500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 102000)

    def test_lataa_rahaa_kortille_kun_summa_negatiivinen(self):
        kortti = Maksukortti(500)
        self.kassapaate.lataa_rahaa_kortille(kortti, -500)
        self.assertEqual(kortti.saldo, 500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kassassa_rahaa_euroina(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.00)
    