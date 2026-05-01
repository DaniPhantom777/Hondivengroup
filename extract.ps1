$v6 = Get-Content -Raw -Encoding UTF8 "hondiven_v6 (1).html"
$v6Lines = Get-Content -Encoding UTF8 "hondiven_v6 (1).html"

# CSS block (approx lines 1450-1500)
$cssLines = $v6Lines[1485..1501]
Set-Content -Path "css_patch.txt" -Value ($cssLines -join "
") -Encoding UTF8

# Panel block (approx lines 1535-1546)
$panelLines = $v6Lines[1535..1546]
Set-Content -Path "panel_patch.txt" -Value ($panelLines -join "
") -Encoding UTF8

# Section block (approx lines 2169-2356)
$sectionLines = $v6Lines[2169..2355]
Set-Content -Path "section_patch.txt" -Value ($sectionLines -join "
") -Encoding UTF8

