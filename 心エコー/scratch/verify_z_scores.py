import math

def calc_bsa_haycock(height_cm, weight_kg):
    """Haycock式: BSA (m^2) = 0.024265 * height^0.3964 * weight^0.5378"""
    return 0.024265 * (height_cm ** 0.3964) * (weight_kg ** 0.5378)

def calc_bsa_du_bois(height_cm, weight_kg):
    """Du Bois式: BSA (m^2) = 0.007184 * height^0.725 * weight^0.425"""
    return 0.007184 * (height_cm ** 0.725) * (weight_kg ** 0.425)

def calc_z_score_kobayashi(internal_diameter_mm, bsa, branch="LMCA"):
    """
    小林式（Kobayashi et al. Circ J 2006 / 2016）：
    ln(Predicted diameter) = a + b * ln(BSA)
    Z = (ln(Measured) - ln(Predicted)) / SD(residual)
    または実寸モデルでの計算。
    ここでは文献標準の小林式パラメータを検証
    """
    pass

# 小児典型例（1歳、75cm、10kg）のBSA計算
h, w = 75.0, 10.0
bsa_h = calc_bsa_haycock(h, w)
bsa_d = calc_bsa_du_bois(h, w)
print(f"Age 1yo (75cm, 10kg):")
print(f"Haycock BSA: {bsa_h:.4f} m2")
print(f"DuBois  BSA: {bsa_d:.4f} m2")
print(f"Difference: {abs(bsa_h - bsa_d)/bsa_h * 100:.2f}%")

# 年齢別・体格別のBSA基準テーブル
cases = [
    ("6M", 66.0, 7.5),
    ("1Y", 75.0, 10.0),
    ("2Y", 86.0, 12.0),
    ("3Y", 95.0, 14.0),
    ("5Y", 110.0, 18.0)
]
print("\n--- BSA Comparison Table ---")
for age, height, weight in cases:
    bh = calc_bsa_haycock(height, weight)
    bd = calc_bsa_du_bois(height, weight)
    print(f"{age:3s} (Ht {height:5.1f}cm, Wt {weight:4.1f}kg) -> Haycock: {bh:.3f} m2, DuBois: {bd:.3f} m2")
