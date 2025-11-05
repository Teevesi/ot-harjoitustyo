import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_oikein(self):
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.00)

    def test_lataaminen_kasvattaa_saldoa(self):
        self.maksukortti.lataa_rahaa(2500)
        self.assertEqual(self.maksukortti.saldo_euroina(), 35.00)

    def test_rahan_ottaminen_toimii_kun_saldo_riittaa(self):
        onnistui = self.maksukortti.ota_rahaa(500)
        self.assertTrue(onnistui)
        self.assertEqual(self.maksukortti.saldo_euroina(), 5.00)

    def test_rahan_ottaminen_ei_toimi_kun_saldo_ei_riita(self):
        onnistui = self.maksukortti.ota_rahaa(1500)
        self.assertFalse(onnistui)
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.00)

    def test_raha_nakyy_oikeassa_muodossa(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")


