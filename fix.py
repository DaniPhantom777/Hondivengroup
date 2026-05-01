import sys
import re

file_path = r'd:\Trabajos\compu2024\HONDIVEN\pagina 2\hondiven_v5__3_.html'

try:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
except Exception as e:
    with open(file_path, 'r', encoding='ISO-8859-1') as f:
        content = f.read()

# Make sure to handle special characters carefully if using ASCII/UTF-8 bytes mismatch.
# 1. Hero Buttons
content = content.replace('<button class="pcta" aria-label="Ver más sobre Construcción">Saber más</button>', '<button class="pcta" aria-label="Ver más sobre Construcción" onclick="setTimeout(() => document.getElementById(\'contacto-construccion\').scrollIntoView({behavior: \'smooth\'}), 100);">Saber más</button>')
content = content.replace('<button class="pcta" aria-label="Ver más sobre CEEP">Saber más</button>', '<button class="pcta" aria-label="Ver más sobre CEEP" onclick="setTimeout(() => document.getElementById(\'contacto-ceep\').scrollIntoView({behavior: \'smooth\'}), 100);">Saber más</button>')
content = content.replace('<button class="pcta" aria-label="Ver más sobre Grounding Lab">Saber más</button>', '<button class="pcta" aria-label="Ver más sobre Grounding Lab" onclick="setTimeout(() => document.getElementById(\'contacto-gl\').scrollIntoView({behavior: \'smooth\'}), 100);">Saber más</button>')

# 2. Add IDs to Contact Forms / Sections
content = content.replace('<div class="contact-section" style="--form-accent:#E8550A">', '<div id="contacto-hondiven" class="contact-section" style="--form-accent:#E8550A">', 1)

content = content.replace('<!-- FORMULARIO CONSTRUCCIÓN -->\n    <div class="contact-section">', '<!-- FORMULARIO CONSTRUCCIÓN -->\n    <div id="contacto-construccion" class="contact-section">')

content = content.replace('<!-- FORMULARIO CEEP -->\n  <div class="contact-section" style="--form-accent:#E8550A">', '<!-- FORMULARIO CEEP -->\n  <div id="contacto-ceep" class="contact-section" style="--form-accent:#E8550A">')

content = content.replace('<!-- CLOSING FINAL -->\n  <div class="closing" style="background:#F2EAE3; border-top:1px solid rgba(19,18,17,0.1); border-bottom:1px solid rgba(19,18,17,0.1);">', '<!-- CLOSING FINAL -->\n  <div id="contacto-gl" class="closing" style="background:#F2EAE3; border-top:1px solid rgba(19,18,17,0.1); border-bottom:1px solid rgba(19,18,17,0.1);">')


# 3. Replace all CTAs in proper sections
# sec-construccion
content = content.replace('<a href="#" class="btn-primary">Cotizar proyecto</a>', '<a href="#contacto-construccion" class="btn-primary">Cotizar proyecto</a>')
content = content.replace('<a href="#" class="btn-outline">Solicitar evaluación</a>', '<a href="#contacto-construccion" class="btn-outline">Solicitar evaluación</a>')
content = content.replace('<a href="#" class="btn-primary">Solicitar Evaluación de Proyecto →</a>', '<a href="#contacto-construccion" class="btn-primary">Solicitar Evaluación de Proyecto →</a>')
content = content.replace('<a href="#" class="btn-outline">Agendar Reunión →</a>', '<a href="#contacto-construccion" class="btn-outline">Agendar Reunión →</a>')

# sec-ceep
content = content.replace('<a href="mailto:central.ceep@eficienciaenergetica.com.pe" class="hook-cta" aria-label="Solicitar Diagnóstico Energético Gratuito">Diagnóstico', '<a href="#contacto-ceep" class="hook-cta" aria-label="Solicitar Diagnóstico Energético Gratuito">Diagnóstico')
content = content.replace('<a href="mailto:central.ceep@eficienciaenergetica.com.pe" class="btn-primary" style="background:#E8550A;color:#fff" aria-label="Solicitar Diagnóstico CEEP">Solicitar', '<a href="#contacto-ceep" class="btn-primary" style="background:#E8550A;color:#fff" aria-label="Solicitar Diagnóstico CEEP">Solicitar')
content = content.replace('<a href="mailto:central.ceep@eficienciaenergetica.com.pe" class="btn-outline" aria-label="Agendar reunión CEEP">Agendar', '<a href="#contacto-ceep" class="btn-outline" aria-label="Agendar reunión CEEP">Agendar')

# sec-gl
content = content.replace('<a href="mailto:contacto@groundinglab.pe" class="btn-primary" style="background:#FF073A;color:#fff;border:none;">QUIERO GENERAR INGRESOS</a>', '<a href="#contacto-gl" class="btn-primary" style="background:#FF073A;color:#fff;border:none;">QUIERO GENERAR INGRESOS</a>')
content = content.replace('<a href="mailto:contacto@groundinglab.pe" class="btn-outline" style="color:#131211;border:1px solid #131211;background:transparent;">AGENDA DIAGNÓSTICO</a>', '<a href="#contacto-gl" class="btn-outline" style="color:#131211;border:1px solid #131211;background:transparent;">AGENDA DIAGNÓSTICO</a>')
content = content.replace('<a href="mailto:contacto@groundinglab.pe" class="btn-primary" style="background:#FF073A;color:#fff;width:100%;text-align:center;justify-content:center;font-size:18px;padding:24px;" aria-label="AGENDA TU DIAGNÓSTICO">AGENDA TU DIAGNÓSTICO →</a>', '<a href="#contacto-gl" class="btn-primary" style="background:#FF073A;color:#fff;width:100%;text-align:center;justify-content:center;font-size:18px;padding:24px;" aria-label="AGENDA TU DIAGNÓSTICO">AGENDA TU DIAGNÓSTICO →</a>')

# sec-hondiven CTAs
content = content.replace('<a href="mailto:info@hondiven.com" class="btn-primary" aria-label="Solicitar Diagnóstico Ejecutivo">Solicitar', '<a href="#contacto-hondiven" class="btn-primary" aria-label="Solicitar Diagnóstico Ejecutivo">Solicitar')
content = content.replace('<a href="mailto:info@hondiven.com" class=\"btn-outline\" aria-label=\"Agendar reunión\">Agendar', '<a href="#contacto-hondiven" class=\"btn-outline\" aria-label=\"Agendar reunión\">Agendar')


# Try regular expressions where specific class needs replacement
content = re.sub(r'<a href="#contacto" class="quien-card-cta">', r'<a href="#contacto-hondiven" class="quien-card-cta">', content)
content = re.sub(r'<a href="#contacto" class="service-expand-cta">', r'<a href="#contacto-hondiven" class="service-expand-cta">', content)


# 4. Sticky banner href update
update_banner_code_old = """  if (brand === 'ceep') {
    b.classList.add('banner-ceep');
    b.style.setProperty('--banner-accent','#E8550A');
    msg.innerHTML = 'Si no estás midiendo tu energía en <em>tiempo real</em>, estás perdiendo dinero <em>todos los meses</em>.';
    cta.style.background = '#E8550A';
    cta.textContent = 'Medir ahora →';
  } else if (brand === 'construccion') {
    b.classList.add('banner-construccion');
    b.style.setProperty('--banner-accent','#0045e6');
    msg.innerHTML = 'Si su proyecto no tiene <em>control total</em>, está perdiendo inversión <em>hoy mismo</em>.';
    cta.style.background = '#0045e6';
    cta.style.color = '#fff';
    cta.textContent = 'Evaluar proyecto →';
  } else if (brand === 'gl') {
    b.classList.add('banner-gl');
    b.style.setProperty('--banner-accent','#D0103A');
    msg.innerHTML = 'Si no estás midiendo tu pipeline comercial en <em>tiempo real</em>, estás dejando ingresos sobre la mesa <em>hoy</em>.';
    cta.style.background = '#D0103A';
    cta.textContent = 'Auditar ahora →';
  } else {
    b.classList.add('banner-hondiven');
    b.style.setProperty('--banner-accent','#A8B4BC');
    msg.innerHTML = 'Si no estás midiendo tu operación en <em>tiempo real</em>, estás perdiendo dinero <em>todos los meses</em>.';
    cta.style.background = '#A8B4BC';
    cta.style.color = '#0a0a0a';
    cta.textContent = 'Medir ahora →';
  }"""

update_banner_code_new = """  if (brand === 'ceep') {
    b.classList.add('banner-ceep');
    b.style.setProperty('--banner-accent','#E8550A');
    msg.innerHTML = 'Si no estás midiendo tu energía en <em>tiempo real</em>, estás perdiendo dinero <em>todos los meses</em>.';
    cta.style.background = '#E8550A';
    cta.textContent = 'Medir ahora →';
    cta.href = '#contacto-ceep';
  } else if (brand === 'construccion') {
    b.classList.add('banner-construccion');
    b.style.setProperty('--banner-accent','#0045e6');
    msg.innerHTML = 'Si su proyecto no tiene <em>control total</em>, está perdiendo inversión <em>hoy mismo</em>.';
    cta.style.background = '#0045e6';
    cta.style.color = '#fff';
    cta.textContent = 'Evaluar proyecto →';
    cta.href = '#contacto-construccion';
  } else if (brand === 'gl') {
    b.classList.add('banner-gl');
    b.style.setProperty('--banner-accent','#D0103A');
    msg.innerHTML = 'Si no estás midiendo tu pipeline comercial en <em>tiempo real</em>, estás dejando ingresos sobre la mesa <em>hoy</em>.';
    cta.style.background = '#D0103A';
    cta.textContent = 'Auditar ahora →';
    cta.href = '#contacto-gl';
  } else {
    b.classList.add('banner-hondiven');
    b.style.setProperty('--banner-accent','#A8B4BC');
    msg.innerHTML = 'Si no estás midiendo tu operación en <em>tiempo real</em>, estás perdiendo dinero <em>todos los meses</em>.';
    cta.style.background = '#A8B4BC';
    cta.style.color = '#0a0a0a';
    cta.textContent = 'Medir ahora →';
    cta.href = '#contacto-hondiven';
  }"""

content = content.replace(update_banner_code_old, update_banner_code_new)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print('success')
