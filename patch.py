import sys

with open('hondiven_v6 (1).html', 'r', encoding='utf-8') as f:
    v6 = f.read()

with open('hondiven_v5__3_.html', 'r', encoding='utf-8') as f:
    v5 = f.read()

# 1. Extract CSS
css_start = v6.find('/* ?\n   CONSTRUCCIÓN')
if css_start == -1:
    css_start = v6.find('/* \n   CONSTRUCCIÓN')
if css_start == -1:
    css_start = v6.find('CONSTRUCCIÓN - paleta') - 10

css_end = v6.find('</style>', css_start)
css_block = v6[css_start:css_end]
if not css_block:
    print('Failed to find css block')

# 2. Extract HTML Panel
panel_start = v6.find('<div class="sel-panel construccion"')
panel_end = v6.find('</div>\n    </div>', panel_start) + len('</div>\n    </div>')
panel_block = v6[panel_start:panel_end]
if not panel_block:
    print('Failed to find panel block')

# 3. Extract HTML Section
section_start = v6.find('<div id="sec-construccion"')
section_end_str = '</div><!-- end sec-construccion -->'
section_end = v6.find(section_end_str, section_start) + len(section_end_str)
section_block = v6[section_start:section_end]
if not section_block:
    print('Failed to find section block')

# 4. Extract updateBanner logic
banner_logic_start = v6.find("} else if (brand === 'construccion') {")
banner_logic_end = v6.find("} else if (brand === 'gl') {", banner_logic_start)
banner_logic = v6[banner_logic_start:banner_logic_end]

# 5. Extract switchBrand logic
switch_logic_start = v6.find("} else if (brand === 'construccion') {", banner_logic_end + 100)
switch_logic_end = v6.find("  }\n}\n", switch_logic_start)
if switch_logic_end == -1:
    switch_logic_end = v6.find("  }\n}\r\n", switch_logic_start)
switch_logic = v6[switch_logic_start:switch_logic_end]

# === Inject into v5 ===

# Inject CSS
v5 = v5.replace('</style>', css_block + '\n</style>')

# Inject Panel
v5_ceep_panel = '<div class="sel-panel ceep"'
v5 = v5.replace(v5_ceep_panel, panel_block + '\n    ' + v5_ceep_panel)

# Inject Section
v5_ceep_section = '<div id="sec-ceep"'
v5 = v5.replace(v5_ceep_section, section_block + '\n\n  ' + v5_ceep_section)

# Inject JS constants in switchBrand
v5 = v5.replace("const glBgImg   = document.getElementById('gl-bg-img');", "const glBgImg   = document.getElementById('gl-bg-img');\n  const construccionBgImg = document.getElementById('construccion-bg-img');")

# Inject JS reset in switchBrand
v5 = v5.replace("glBgImg.classList.remove('visible');", "glBgImg.classList.remove('visible');\n    if (construccionBgImg) construccionBgImg.classList.remove('visible');")
v5 = v5.replace("ceepBgImg.classList.remove('visible');", "ceepBgImg.classList.remove('visible');\n    if (construccionBgImg) construccionBgImg.classList.remove('visible');")

# Inject updateBanner logic
v5 = v5.replace("} else if (brand === 'gl') {", banner_logic + "} else if (brand === 'gl') {")

# Inject switchBrand logic
v5 = v5.replace("}, 420);\n  }\n}", "}, 420);\n  " + switch_logic + "\n  }\n}")
# Handle windows line endings if needed
v5 = v5.replace("}, 420);\r\n  }\r\n}", "}, 420);\r\n  " + switch_logic + "\r\n  }\r\n}")

with open('hondiven_v5__3_.html', 'w', encoding='utf-8') as f:
    f.write(v5)

print('Script execution complete.')

