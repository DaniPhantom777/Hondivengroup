#!/usr/bin/env python3
"""
Reorder sections in sec-hondiven:
Required order:
  1. Hero (lines before que-es-hondiven section start, including metrics)
  2. ¿Qué es HONDIVEN? + metrics (id="que-es-hondiven")
  3. PROPUESTA/EBITDA (id="ebitda-section")
  4. PROBLEMAS (id="problemas-section")
  5. RESULTADOS (id="resultados-section")
  6. PORTAFOLIO (id="portafolio-section")
  7. ¿POR QUÉ HONDIVEN? (id="por-que-hondiven")
  8. CÓMO TRABAJAMOS (id="como-trabajamos")
  9. Clients + rest (from <!-- CLIENTES --> to end of sec-hondiven)
"""

import re

with open(r"d:\Trabajos\compu2024\HONDIVEN\pagina 2\hondiven_v5__3_.html", 'r', encoding='utf-8') as f:
    content = f.read()

lines = content.split('\n')

# Find line numbers (0-indexed) for key markers
def find_line(pattern, start=0):
    for i in range(start, len(lines)):
        if re.search(pattern, lines[i]):
            return i
    return -1

# Key markers (0-indexed)
sec_hondiven_start = find_line(r'<div id="sec-hondiven"')
print(f"sec-hondiven starts at line {sec_hondiven_start + 1}")

que_es_start = find_line(r'<div id="que-es-hondiven"', sec_hondiven_start)
print(f"que-es-hondiven starts at line {que_es_start + 1}")

metrics_start = find_line(r'<div class="metrics"', sec_hondiven_start)
print(f"metrics starts at line {metrics_start + 1}")

portafolio_start = find_line(r'<div id="portafolio-section"', sec_hondiven_start)
print(f"portafolio-section starts at line {portafolio_start + 1}")

resultados_start = find_line(r'<div id="resultados-section"', sec_hondiven_start)
print(f"resultados-section starts at line {resultados_start + 1}")

por_que_start = find_line(r'<div id="por-que-hondiven"', sec_hondiven_start)
print(f"por-que-hondiven starts at line {por_que_start + 1}")

como_start = find_line(r'<div id="como-trabajamos"', sec_hondiven_start)
print(f"como-trabajamos starts at line {como_start + 1}")

ebitda_start = find_line(r'<div id="ebitda-section"', sec_hondiven_start)
print(f"ebitda-section starts at line {ebitda_start + 1}")

problemas_start = find_line(r'<div id="problemas-section"', sec_hondiven_start)
print(f"problemas-section starts at line {problemas_start + 1}")

clientes_comment = find_line(r'<!--.*CLIENTES', sec_hondiven_start)
print(f"CLIENTES comment starts at line {clientes_comment + 1}")

# Also need the comment lines before each section
# For ebitda, the comment is at line 2731 (0-idx: 2730)
ebitda_comment = find_line(r'<!--.*PROPUESTA.*EBITDA', sec_hondiven_start)
print(f"EBITDA comment at line {ebitda_comment + 1}")

problemas_comment = find_line(r'<!--\s*[¿]?\s*', problemas_start - 5)
# Search more carefully for the problemas comment
for i in range(problemas_start - 5, problemas_start):
    print(f"  Line {i+1}: {lines[i][:80]}")

# portafolio comment
portafolio_comment = find_line(r'<!--.*PORTAFOLIO', sec_hondiven_start)
print(f"PORTAFOLIO comment at line {portafolio_comment + 1}")

resultados_comment = find_line(r'<!--.*RESULTADOS', sec_hondiven_start)
print(f"RESULTADOS comment at line {resultados_comment + 1}")

por_que_comment = find_line(r'<!--.*POR QU', sec_hondiven_start)
print(f"POR QUE comment at line {por_que_comment + 1}")

como_comment = find_line(r'<!--.*C.MO TRABAJAMOS', sec_hondiven_start)
print(f"COMO TRABAJAMOS comment at line {como_comment + 1}")

print("\nLines around que-es end / metrics start:")
for i in range(que_es_start, metrics_start + 3):
    print(f"  {i+1}: {lines[i][:80]}")
