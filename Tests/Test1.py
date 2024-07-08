import math
import unittest

def treibstoffmasse(hoehe, ve, m_leer):
    # Typische delta-v für den Erdorbit
    delta_v = 9400  # in m/s

    # Anfangsmasse der Rakete inklusive Treibstoff
    m_0 = m_leer * math.exp(delta_v / ve)

    # Treibstoffmasse
    m_treibstoff = m_0 - m_leer

    return m_treibstoff

class TestTreibstoffmasse(unittest.TestCase):

    def test_treibstoffmasse_typical(self):
        hoehe = 200000  # Höhe in Meter (z.B. 200 km für LEO - Low Earth Orbit)
        ve = 4500  # Ausströmgeschwindigkeit des Treibstoffs in m/s (z.B. für Kerosin/LOX)
        m_leer = 50000  # Leermasse der Rakete in kg (ohne Treibstoff)
        
        result = treibstoffmasse(hoehe, ve, m_leer)
        expected = 50000 * (math.exp(9400 / 4500) - 1)
        
        self.assertAlmostEqual(result, expected, places=2)

    def test_treibstoffmasse_high_empty_mass(self):
        hoehe = 200000
        ve = 4500
        m_leer = 100000
        
        result = treibstoffmasse(hoehe, ve, m_leer)
        expected = 100000 * (math.exp(9400 / 4500) - 1)
        
        self.assertAlmostEqual(result, expected, places=2)
    
    def test_treibstoffmasse_low_empty_mass(self):
        hoehe = 200000
        ve = 4500
        m_leer = 10000
        
        result = treibstoffmasse(hoehe, ve, m_leer)
        expected = 10000 * (math.exp(9400 / 4500) - 1)
        
        self.assertAlmostEqual(result, expected, places=2)
    
    def test_treibstoffmasse_high_exhaust_velocity(self):
        hoehe = 200000
        ve = 5000
        m_leer = 50000
        
        result = treibstoffmasse(hoehe, ve, m_leer)
        expected = 50000 * (math.exp(9400 / 5000) - 1)
        
        self.assertAlmostEqual(result, expected, places=2)
    
    def test_treibstoffmasse_low_exhaust_velocity(self):
        hoehe = 200000
        ve = 4000
        m_leer = 50000
        
        result = treibstoffmasse(hoehe, ve, m_leer)
        expected = 50000 * (math.exp(9400 / 4000) - 1)
        
        self.assertAlmostEqual(result, expected, places=2)

if __name__ == "__main__":
    unittest.main()
