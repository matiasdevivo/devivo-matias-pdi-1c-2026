import cv2
import numpy as np

# ══════════════════════════════════════════════════════════════
# Script 1 — Reencuadre con marcas visuales
# Usado en slide 5: Reencuadre y reinterpretación
# ══════════════════════════════════════════════════════════════

img = cv2.imread("../imagenes/originales/autos_espalda.jpg")
h, w = img.shape[:2]

# Definir regiones de recorte
crop_a_x1, crop_a_x2 = 0, w // 2          # Kombi (izquierda)
crop_b_x1, crop_b_x2 = w // 2, w          # Porsche (derecha)
crop_y1,   crop_y2   = int(h * 0.47), h   # Solo la zona con los autos

# Recorte A — Kombi
recorte_a = img[crop_y1:crop_y2, crop_a_x1:crop_a_x2]
cv2.imwrite("../imagenes/procesadas/recorte_a_kombi.jpg", recorte_a)

# Recorte B — Porsche
recorte_b = img[crop_y1:crop_y2, crop_b_x1:crop_b_x2]
cv2.imwrite("../imagenes/procesadas/recorte_b_porsche.jpg", recorte_b)

# Imagen original con marcas de los recortes
img_marcas = img.copy()
cv2.rectangle(img_marcas, (crop_a_x1, crop_y1), (crop_a_x2, crop_y2), (255, 180, 0), 8)
cv2.rectangle(img_marcas, (crop_b_x1, crop_y1), (crop_b_x2, crop_y2), (0, 100, 255), 8)
cv2.putText(img_marcas, "A", (crop_a_x1 + 20, crop_y1 + 80),
            cv2.FONT_HERSHEY_SIMPLEX, 2.5, (255, 180, 0), 6)
cv2.putText(img_marcas, "B", (crop_b_x1 + 20, crop_y1 + 80),
            cv2.FONT_HERSHEY_SIMPLEX, 2.5, (0, 100, 255), 6)
cv2.imwrite("../imagenes/procesadas/original_con_marcas.jpg", img_marcas)

print("Reencuadre completado.")
print(f"Recorte A (Kombi):   {recorte_a.shape[1]}x{recorte_a.shape[0]} px")
print(f"Recorte B (Porsche): {recorte_b.shape[1]}x{recorte_b.shape[0]} px")

# ══════════════════════════════════════════════════════════════
# Script 2 — Comparación RGB → HSV (separación de canales)
# Muestra cómo se separan los canales H, S y V
# ══════════════════════════════════════════════════════════════

img2 = cv2.imread("../imagenes/originales/camara_oscura.jpg")

# Conversión BGR → HSV
hsv = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)
h_ch, s_ch, v_ch = cv2.split(hsv)

# Guardar cada canal por separado
cv2.imwrite("../imagenes/procesadas/canal_H.jpg", h_ch)
cv2.imwrite("../imagenes/procesadas/canal_S.jpg", s_ch)
cv2.imwrite("../imagenes/procesadas/canal_V.jpg", v_ch)

print("\nSeparacion de canales HSV completada.")
print(f"Canal H — rango: {h_ch.min()} a {h_ch.max()}")
print(f"Canal S — rango: {s_ch.min()} a {s_ch.max()}")
print(f"Canal V — rango: {v_ch.min()} a {v_ch.max()}")
