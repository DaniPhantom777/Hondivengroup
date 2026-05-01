$v6 = Get-Content -Encoding UTF8 "hondiven_v6 (1).html"
$v5 = Get-Content -Encoding UTF8 "hondiven_v5__3_.html"

$css_add = $v6[1454..1498]
$panel_add = $v6[1535..1546]
$section_add = $v6[2169..2355]
$banner_add = $v6[2376..2382]
$switch_add = $v6[2472..2486]

$newV5 = @()

for ($i = 0; $i -lt $v5.Length; $i++) {
    $line = $v5[$i]
    
    if ($line -match "^\s*</style>") {
        $newV5 += $css_add
    }
    
    if ($line -match '<div class="sel-panel ceep"') {
        $newV5 += $panel_add
    }
    
    if ($line -match '<div id="sec-ceep"') {
        $newV5 += $section_add
    }

    if ($line -match "} else if \(brand === 'gl'\) {") {
        if ($v5[$i-1] -match "cta\.textContent") {
             $newV5 += $banner_add
        }
    }

    if ($line -match "const glBgImg") {
        $newV5 += $line
        $newV5 += "  const construccionBgImg = document.getElementById('construccion-bg-img');"
        continue
    }

    if ($line -match "glBgImg\.classList\.remove\('visible'\);" -or $line -match "ceepBgImg\.classList\.remove\('visible'\);") {
        $newV5 += $line
        # To avoid duplicating if multiple matches
        $nextLine = $v5[$i+1]
        $isLastRemove = $true
        if ($nextLine -match "glBgImg\.classList\.remove\('visible'\);" -or $nextLine -match "ceepBgImg\.classList\.remove\('visible'\);") {
            $isLastRemove = $false
        }
        if ($isLastRemove -and -not ($nextLine -match "construccionBgImg")) {
            $newV5 += "    if (construccionBgImg) construccionBgImg.classList.remove('visible');"
        }
        continue
    }

    $newV5 += $line

    if ($v5[$i-2] -match "ceepBgImg\.classList\.remove\('visible'\);" -and $v5[$i-1] -match "setTimeout\(\(\) => {" -and $line -match "const content = document\.getElementById\('content'\);") {
         # Ensure we're in the right place to add switch_add. Actually, it's safer to just look for the end of the gl block in switchBrand:
    }
}

# The switchBrand addition is best placed at the end of the gl block.
# Let's find it more specifically.
$newV5Final = @()
$inSwitchBrand = $false
for ($i = 0; $i -lt $newV5.Length; $i++) {
    $line = $newV5[$i]
    if ($line -match "function switchBrand") {
        $inSwitchBrand = $true
    }
    if ($inSwitchBrand -and $line -match "^  }$" -and $newV5[$i+1] -match "^}$") {
        # This is the end of switchBrand
        $newV5Final += $switch_add
        $inSwitchBrand = $false
    }
    $newV5Final += $line
}

Set-Content -Path "test_patch.html" -Value $newV5Final -Encoding UTF8

