# PowerShell script to reorder sections in sec-hondiven
$inputPath = "d:\Trabajos\compu2024\HONDIVEN\pagina 2\hondiven_v5__3_BACKUP.html"
$outputPath = "d:\Trabajos\compu2024\HONDIVEN\pagina 2\hondiven_v5__3_.html"

# Read file as array of lines
$lines = Get-Content $inputPath -Encoding UTF8

# Add the prefix
$prefix = $lines[0..1920]

$hero         = $lines[1921..2050]   # lines 1922-2051
$queEs        = $lines[2051..2193]   # lines 2052-2194
$portafolio   = $lines[2194..2385]   # lines 2195-2386
$resultados   = $lines[2386..2522]   # lines 2387-2523
$porQue       = $lines[2523..2639]   # lines 2524-2640
$como         = $lines[2640..2729]   # lines 2641-2730
$ebitda       = $lines[2730..3051]   # lines 2731-3052
$problemas    = $lines[3052..3159]   # lines 3053-3160
$rest         = $lines[3160..($lines.Length-1)]  # lines 3161..end

# Required new order:
# 1. Hero
# 2. ¿Qué es HONDIVEN? (queEs includes metrics)
# 3. PROPUESTA/EBITDA
# 4. PROBLEMAS
# 5. RESULTADOS REALES
# 6. PORTAFOLIO DE SERVICIOS
# 7. ¿POR QUÉ HONDIVEN?
# 8. CÓMO TRABAJAMOS
# 9. Clients + rest

$newContent = $prefix + $hero + $queEs + $ebitda + $problemas + $resultados + $portafolio + $porQue + $como + $rest

# Verify sizes
Write-Output "Original lines: $($lines.Length)"
Write-Output "New content lines: $($newContent.Length)"

# Write output
$newContent | Set-Content $outputPath -Encoding UTF8
Write-Output "Done! File reordered and saved."
