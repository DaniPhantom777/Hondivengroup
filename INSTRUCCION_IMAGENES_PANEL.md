# 🎨 INSTRUCCIÓN — IMÁGENES DE FONDO AL HACER CLIC EN PANEL
## Archivo: `hondiven_v4 (1).html`
## Ejecutar en Antigravity — modo agente

---

## LÓGICA EXACTA A IMPLEMENTAR

| Estado | Panel CEEP | Panel Grounding Lab |
|---|---|---|
| Sin selección (hero completo) | Solo gradiente naranja | Solo gradiente rojo |
| Clic en CEEP | Imagen ingeniero visible (fade in) | Solo gradiente rojo (sin imagen) |
| Clic en Grounding Lab | Solo gradiente naranja (sin imagen) | Imagen ejecutivo visible (fade in) |
| Volver a HONDIVEN | Sin imagen en ningún panel | Sin imagen en ningún panel |

---

## ARCHIVOS DE IMAGEN

```
Carpeta: misma ubicación que el HTML
- backgroun_ceep.png      → ingeniero con casco naranja (panel CEEP)
- background_grounding.png → ejecutivo de traje rojo (panel Grounding Lab)
```

> ⚠️ Verificar que los archivos estén en la misma carpeta que el HTML antes de ejecutar.

---

## CAMBIO 1 — Agregar divs de imagen dentro de cada panel

### 🔍 Buscar en el HTML:
```html
<div class="sel-panel ceep" onclick="switchBrand('ceep')">
      <div class="pbg"></div>
      <div class="pcontent">
```

### ✏️ Reemplazar por:
```html
<div class="sel-panel ceep" onclick="switchBrand('ceep')">
      <div class="pbg"></div>
      <div class="panel-bg-img" id="ceep-bg-img"></div>
      <div class="pcontent">
```

---

### 🔍 Buscar en el HTML:
```html
<div class="sel-panel gl" onclick="switchBrand('gl')">
      <div class="pbg"></div>
      <div class="pcontent">
```

### ✏️ Reemplazar por:
```html
<div class="sel-panel gl" onclick="switchBrand('gl')">
      <div class="pbg"></div>
      <div class="panel-bg-img" id="gl-bg-img"></div>
      <div class="pcontent">
```

---

## CAMBIO 2 — CSS para las imágenes de fondo

### 🔍 Buscar en el CSS (dentro del bloque `<style>`), justo antes del cierre `</style>`:

### ✏️ Agregar este bloque nuevo:
```css
/* ═══════════════════════════════
   PANEL BACKGROUND IMAGES
═══════════════════════════════ */
.panel-bg-img {
  position: absolute;
  inset: 0;
  z-index: 3;
  background-size: cover;
  background-position: center bottom;
  background-repeat: no-repeat;
  opacity: 0;
  transition: opacity 0.6s cubic-bezier(0.22, 1, 0.36, 1);
  pointer-events: none;
}

/* Imágenes específicas por panel */
#ceep-bg-img {
  background-image: url('backgroun_ceep.png');
  background-position: center bottom;
  background-size: cover;
}

#gl-bg-img {
  background-image: url('background_grounding.png');
  background-position: center bottom;
  background-size: cover;
}

/* Visible cuando el panel está activo */
.panel-bg-img.visible {
  opacity: 1;
}

/* En nav minimizada, ocultar siempre las imágenes */
#selector.minimized .panel-bg-img {
  opacity: 0 !important;
  transition: none;
}
```

---

## CAMBIO 3 — JS: mostrar/ocultar imagen según la marca seleccionada

### 🔍 Buscar la función `switchBrand` en el `<script>`.

### ✏️ Agregar estas 2 líneas al inicio de la función, justo después de `const selLogo`:

```javascript
const ceepBgImg = document.getElementById('ceep-bg-img');
const glBgImg   = document.getElementById('gl-bg-img');
```

### ✏️ Luego en el bloque `if (brand === 'hondiven')`, agregar:
```javascript
ceepBgImg.classList.remove('visible');
glBgImg.classList.remove('visible');
```

### ✏️ En el bloque `else if (brand === 'ceep')`, agregar:
```javascript
ceepBgImg.classList.add('visible');
glBgImg.classList.remove('visible');
```

### ✏️ En el bloque `else if (brand === 'gl')`, agregar:
```javascript
glBgImg.classList.add('visible');
ceepBgImg.classList.remove('visible');
```

---

## RESULTADO ESPERADO — función switchBrand completa

Para referencia, así debe quedar la función entera:

```javascript
function switchBrand(brand) {
  const selector  = document.getElementById('selector');
  const sections  = document.querySelectorAll('.brand-section');
  const panels    = document.querySelectorAll('.sel-panel');
  const selLogo   = document.querySelector('.sel-logo');
  const ceepBgImg = document.getElementById('ceep-bg-img');
  const glBgImg   = document.getElementById('gl-bg-img');

  sections.forEach(s => s.classList.remove('active'));
  bannerShown = false;
  bannerClosed = false;
  document.getElementById('sticky-banner').classList.remove('visible');
  updateBanner(brand);

  if (brand === 'hondiven') {
    document.getElementById('sec-hondiven').classList.add('active');
    selector.classList.remove('minimized');
    panels.forEach(p => p.classList.remove('active-brand'));
    selLogo.classList.remove('brand-active');
    ceepBgImg.classList.remove('visible');
    glBgImg.classList.remove('visible');
    window.scrollTo({ top: 0, behavior: 'smooth' });

  } else if (brand === 'ceep') {
    document.getElementById('sec-ceep').classList.add('active');
    selector.classList.add('minimized');
    panels.forEach(p => p.classList.remove('active-brand'));
    document.querySelector('.sel-panel.ceep').classList.add('active-brand');
    selLogo.classList.add('brand-active');
    ceepBgImg.classList.add('visible');
    glBgImg.classList.remove('visible');
    setTimeout(() => {
      const content = document.getElementById('content');
      const top = content.getBoundingClientRect().top + window.scrollY - 72;
      window.scrollTo({ top, behavior: 'smooth' });
    }, 420);

  } else if (brand === 'gl') {
    document.getElementById('sec-gl').classList.add('active');
    selector.classList.add('minimized');
    panels.forEach(p => p.classList.remove('active-brand'));
    document.querySelector('.sel-panel.gl').classList.add('active-brand');
    selLogo.classList.add('brand-active');
    glBgImg.classList.add('visible');
    ceepBgImg.classList.remove('visible');
    setTimeout(() => {
      const content = document.getElementById('content');
      const top = content.getBoundingClientRect().top + window.scrollY - 72;
      window.scrollTo({ top, behavior: 'smooth' });
    }, 420);
  }
}
```

---

## ✅ VERIFICAR EN NAVEGADOR

```
[ ] Estado inicial: solo gradiente naranja y rojo, SIN imágenes
[ ] Clic en CEEP → ingeniero aparece con fade suave sobre el naranja
[ ] Clic en Grounding Lab → ejecutivo aparece con fade suave sobre el rojo
[ ] Panel opuesto siempre queda sin imagen
[ ] Clic en logo HONDIVEN → ambas imágenes desaparecen
[ ] En nav minimizada: no se ven las imágenes (solo color)
[ ] Las transiciones duran ~0.6s, suaves y sin parpadeo
```

---

*Instrucción imágenes de panel — HONDIVEN v4 — 2026*
