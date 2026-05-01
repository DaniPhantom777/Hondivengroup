$v6 = Get-Content -Encoding UTF8 "hondiven_v6 (1).html"
$v5 = Get-Content -Encoding UTF8 "hondiven_v5__3_.html"

$cssLines = $v6[1454..1499]
$panelLines = $v6[1535..1545]
$sectionLines = $v6[2169..2355]
$bannerLogic = $v6[2376..2382]
$switchConst = $v6[2427]
$switchLogic = $v6[2472..2486]

$newV5 = @()

for ($i = 0; $i -lt $v5.Length; $i++) {
    $line = $v5[$i]
    $trimmed = $line.Trim()

    if ($trimmed -eq "</style>") {
        $newV5 += $cssLines
    }

    if ($line -match '<div class="sel-panel ceep"') {
        $newV5 += $panelLines
    }

    if ($line -match '<div id="sec-ceep"') {
        $newV5 += $sectionLines
        $newV5 += ""
        $newV5 += "  <!-- =============================== -->"
        $newV5 += "  <!-- SECCION CEEP                    -->"
        $newV5 += "  <!-- =============================== -->"
        # Wait, the v5 file does not have those comments exactly, but I can just append it before sec-ceep.
    }

    if ($trimmed -eq "} else if (brand === 'gl') {" -and $newV5[-1] -match "cta\.textContent = 'Medir ahora") {
        $newV5 += $bannerLogic
    }

    if ($line -match "const glBgImg") {
        $newV5 += $line
        $newV5 += $switchConst
        continue
    }

    if ($line -match "glBgImg.classList.remove\('visible'\);" -or $line -match "ceepBgImg.classList.remove\('visible'\);") {
        $newV5 += $line
        # Insert if next line is not another remove
        $next = $v5[$i+1]
        if (-not ($next -match "glBgImg.classList.remove") -and -not ($next -match "ceepBgImg.classList.remove")) {
             $newV5 += "    if (construccionBgImg) construccionBgImg.classList.remove('visible');"
        }
        continue
    }

    $newV5 += $line

    if ($inSwitch -and $trimmed -eq "}" -and $v5[$i+1].Trim() -eq "") {
        # End of switch logic
    }
}

# The switchBrand function injection at the end.
$finalV5 = @()
$inSwitch = $false
for ($i = 0; $i -lt $newV5.Length; $i++) {
    $line = $newV5[$i]
    if ($line -match "function switchBrand") {
        $inSwitch = $true
    }
    if ($inSwitch -and $line.Trim() -eq "}" -and $newV5[$i+1].Trim() -eq "}") {
        $finalV5 += $switchLogic
        $inSwitch = $false
    }
    $finalV5 += $line
}

Set-Content -Path "hondiven_v5__3__modified.html" -Value $finalV5 -Encoding UTF8
