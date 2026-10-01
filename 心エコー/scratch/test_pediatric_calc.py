import math

def test_formulas(height, weight, lmca, lad, rca, lvdd, sinus):
    # Haycock BSA
    bsa = 0.024265 * (height ** 0.3964) * (weight ** 0.5378)
    
    # Kobayashi Coronary
    # LMCA
    m_lmca = math.exp(0.384 * math.log(bsa) + 0.942)
    z_lmca = (math.log(lmca) - math.log(m_lmca)) / 0.165
    
    # LAD
    m_lad = math.exp(0.342 * math.log(bsa) + 0.697)
    z_lad = (math.log(lad) - math.log(m_lad)) / 0.170
    
    # RCA
    m_rca = math.exp(0.355 * math.log(bsa) + 0.686)
    z_rca = (math.log(rca) - math.log(m_rca)) / 0.175
    
    # Pettersen Chamber (cm)
    m_lvdd = 3.998 * (bsa ** 0.449) * 10 # mm
    sd_lvdd = 0.284 * (bsa ** 0.285) * 10
    z_lvdd = (lvdd - m_lvdd) / sd_lvdd
    
    m_sinus = 2.052 * (bsa ** 0.485) * 10 # mm
    sd_sinus = 0.180 * (bsa ** 0.300) * 10
    z_sinus = (sinus - m_sinus) / sd_sinus
    
    print(f"Ht={height}cm, Wt={weight}kg -> BSA={bsa:.4f} m2")
    print(f"LMCA={lmca}mm -> Mean={m_lmca:.2f}mm, Z={z_lmca:+.2f}")
    print(f"LAD={lad}mm   -> Mean={m_lad:.2f}mm, Z={z_lad:+.2f}")
    print(f"RCA={rca}mm   -> Mean={m_rca:.2f}mm, Z={z_rca:+.2f}")
    print(f"LVDd={lvdd}mm -> Mean={m_lvdd:.1f}mm, Z={z_lvdd:+.2f}")
    print(f"Sinus={sinus}mm -> Mean={m_sinus:.1f}mm, Z={z_sinus:+.2f}")

test_formulas(75.0, 10.0, 2.2, 3.1, 2.5, 34.0, 19.5)
