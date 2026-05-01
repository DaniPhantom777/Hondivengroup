$v6 = Get-Content -Raw -Encoding UTF8 "hondiven_v6 (1).html"
$start = $v6.IndexOf('/* ?
   CONSTRUCCIÓN')
if ($start -eq -1) { $start = $v6.IndexOf('/* 
   CONSTRUCCIÓN') }
if ($start -eq -1) { $start = $v6.IndexOf('CONSTRUCCIÓN - paleta') - 10 }
$end = $v6.IndexOf('</style>', $start)
$cssArgs = $v6.Substring($start, $end - $start)
Set-Content -Path "css_patch.txt" -Value $cssArgs -Encoding UTF8
