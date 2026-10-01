import math

def pettersen_lvdd_mean_sd(bsa):
    """
    Pettersen et al. JASE 2008
    Predicted Mean = a * (BSA ** b)
    LVDd (cm): a = 3.998, b = 0.449 (2D parasternal short axis / long axis)
    Residual SD = c * (BSA ** d) or constant
    """
    # Pettersen式パラメータ例
    mean = 3.998 * (bsa ** 0.449)
    # SDモデル（概算）
    sd = 0.28 * (bsa ** 0.3)
    return mean, sd

# 1歳児（BSA = 0.464 m2）のLVDd基準値
bsa_1y = 0.4635
mean_cm, sd_cm = pettersen_lvdd_mean_sd(bsa_1y)
print(f"Age 1yo (BSA {bsa_1y:.3f} m2):")
print(f"LVDd Predicted Mean: {mean_cm*10:.1f} mm")
print(f"LVDd +2SD (Z=+2.0): {(mean_cm + 2*sd_cm)*10:.1f} mm")

# 実測値 35.0 mm だった場合のZスコア
measured_mm = 35.0
measured_cm = measured_mm / 10.0
z = (measured_cm - mean_cm) / sd_cm
print(f"Measured LVDd: {measured_mm:.1f} mm -> Z-score: {z:+.2f}")
