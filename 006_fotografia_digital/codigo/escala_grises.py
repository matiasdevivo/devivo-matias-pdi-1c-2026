import cv2

# ── Cargar imagen ─────────────────────────────────────────────────────────
img = cv2.imread("../imagenes/originales/simplicidad.jpg")

# ── Convertir a escala de grises ──────────────────────────────────────────
gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# ── Guardar resultado ─────────────────────────────────────────────────────
cv2.imwrite("../imagenes/procesadas/simplicidad_grises.jpg", gris)

print("Conversion completada.")
print(f"Imagen original:  {img.shape[1]}x{img.shape[0]} px, 3 canales (BGR)")
print(f"Imagen en grises: {gris.shape[1]}x{gris.shape[0]} px, 1 canal")
