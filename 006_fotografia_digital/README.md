# TP 006 — De la cámara oscura a la imagen intencional

**Materia:** Procesamiento Digital de Imágenes / PLN  
**Instituto:** IFTS N° 24  
**Alumno:** De Vivo, Matias  
**Fecha:** 13 de mayo de 2026  

---

## Descripción

Trabajo práctico integrador sobre fotografía digital. Combina principios ópticos, captura fotográfica, composición visual y postprocesamiento digital con Python y OpenCV.

---

## Estructura del repositorio

```
006_fotografia_digital/
│
├── README.md               ← este archivo
├── presentacion.pdf        ← entrega principal
│
├── imagenes/
│   ├── originales/         ← fotografías capturadas sin procesar
│   ├── procesadas/         ← resultados del postproceso
│   └── descartes/          ← imágenes descartadas (slide 8)
│
├── codigo/
│   ├── ecualizacion_hsv.py ← ecualización del canal V en espacio HSV
│   ├── escala_grises.py    ← conversión a escala de grises
│   └── otros_scripts.py    ← reencuadre y scripts auxiliares
│
└── recursos/
    └── referencias_opcionales/
```

---

## Contenido de la presentación

| Slide | Tema |
|-------|------|
| 1 | Portada |
| 2 | Construcción y registro de la cámara oscura |
| 3 | Captura con cámara oscura + Ecualización HSV |
| 4 | Fotografía de simplicidad visual |
| 5 | Reencuadre y reinterpretación |
| 6 | Punto de vista y construcción narrativa |
| 7 | Fotografía basada en la luz |
| 8 | Selección crítica |
| 9 | Reflexión final |

---

## Scripts

### `ecualizacion_hsv.py`
Toma la imagen capturada con la cámara oscura, convierte a HSV, ecualiza solo el canal V (brillo) y guarda la imagen resultante junto con los histogramas comparativos.

```bash
cd codigo/
python ecualizacion_hsv.py
```

### `escala_grises.py`
Convierte una imagen a escala de grises. Usado para la slide de simplicidad visual.

```bash
cd codigo/
python escala_grises.py
```

### `otros_scripts.py`
Scripts auxiliares: reencuadre con marcas visuales y comparación de puntos de vista.

```bash
cd codigo/
python otros_scripts.py
```

---

## Dependencias

```bash
pip install opencv-python matplotlib numpy
```

---

## Cómo ejecutar

1. Colocar las imágenes originales en `imagenes/originales/`
2. Ejecutar los scripts desde la carpeta `codigo/`
3. Los resultados se guardan automáticamente en `imagenes/procesadas/`
