import cv2
import numpy as np
import matplotlib.pyplot as plt

# ── Cargar imagen ─────────────────────────────────────────────────────────
img_bgr = cv2.imread("../imagenes/originales/camara_oscura.jpg")

# ── Convertir BGR → HSV y separar canales ────────────────────────────────
hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)

# ── Ecualizar únicamente el canal V (brillo) ─────────────────────────────
v_eq = cv2.equalizeHist(v)

# ── Recomponer la imagen en HSV y reconvertir a BGR ──────────────────────
hsv_eq = cv2.merge([h, s, v_eq])
img_eq_bgr = cv2.cvtColor(hsv_eq, cv2.COLOR_HSV2BGR)

# ── Guardar imagen ecualizada ─────────────────────────────────────────────
cv2.imwrite("../imagenes/procesadas/camara_oscura_ecualizada.jpg", img_eq_bgr)

# ── Histogramas antes / después ───────────────────────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(8, 3))

axes[0].hist(v.ravel(), bins=256, range=(0, 255), color="#2ECC71", alpha=0.85)
axes[0].set_title("Canal V — Original")
axes[0].set_xlabel("Intensidad")
axes[0].set_ylabel("Frecuencia")

axes[1].hist(v_eq.ravel(), bins=256, range=(0, 255), color="#1A6B40", alpha=0.85)
axes[1].set_title("Canal V — Ecualizado")
axes[1].set_xlabel("Intensidad")
axes[1].set_ylabel("Frecuencia")

plt.tight_layout()
plt.savefig("../imagenes/procesadas/histograma_v.png", dpi=150, bbox_inches="tight")
plt.show()

print("Proceso completado.")
print(f"V original  — min: {v.min()}  max: {v.max()}  media: {v.mean():.1f}")
print(f"V ecualizado — min: {v_eq.min()}  max: {v_eq.max()}  media: {v_eq.mean():.1f}")
