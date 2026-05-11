$inputPath = "d:\Trabajos\compu2024\HONDIVEN\pagina 2\hondiven_v5__3_.html"
$content = Get-Content $inputPath -Encoding UTF8

$newCss = @"
/* ════════════════════════════════════
   HONDIVEN LUXURY CORPORATE TECH PALETTE
════════════════════════════════════ */
#sec-hondiven {
  background: #04152D;
  --accent: #D4A84F;
  --accent-bright: #F5D38A;
  --accent-dark: #A17F3B;
  --tech-blue: #007BFF;
  --dark-bg: #0A0A0A;
  font-family: 'Montserrat', sans-serif;
}

#sec-hondiven h1, #sec-hondiven h2, #sec-hondiven h3, 
#sec-hondiven .sec-title, #sec-hondiven .hook-title {
  font-family: 'Montserrat', sans-serif !important;
}

#sec-hondiven .hook-tag { color: var(--accent); }
#sec-hondiven .hook-tag::before { background: var(--tech-blue); box-shadow: 0 0 8px rgba(0,123,255,0.5); }
#sec-hondiven .hook-cta { border-color: var(--accent); color: #fff; }
#sec-hondiven .hook-cta:hover { color: var(--accent); border-color: var(--accent); box-shadow: 0 0 10px rgba(212,168,79,0.3); }

#sec-hondiven .metric-card.accent {
  background: linear-gradient(135deg, #04152D 0%, #0A0A0A 100%) !important;
  border-left: 3px solid var(--accent);
  box-shadow: 0 4px 20px rgba(0,123,255,0.1);
}
#sec-hondiven .metric-card.accent .metric-val { color: var(--accent); text-shadow: 0 0 10px rgba(212,168,79,0.4); }
#sec-hondiven .metric-card.accent .metric-label { color: rgba(255,255,255,0.7); }
#sec-hondiven .metric-card:not(.accent):hover { background: rgba(0,123,255,0.05); border-left-color: var(--tech-blue); }

#sec-hondiven .service-num { color: var(--accent); opacity: 1; text-shadow: 0 0 8px rgba(212,168,79,0.3); }
#sec-hondiven .service-row:hover { background: linear-gradient(90deg, rgba(0,123,255,0.05) 0%, transparent 100%); }
#sec-hondiven .service-row:hover .service-name { color: var(--tech-blue); text-shadow: 0 0 8px rgba(0,123,255,0.4); }
#sec-hondiven .service-kpi { color: var(--accent); }

#sec-hondiven .rtab.active { color: #fff; border-bottom-color: var(--tech-blue); box-shadow: 0 2px 10px rgba(0,123,255,0.2); }
#sec-hondiven .result-num { color: var(--accent); text-shadow: 0 0 10px rgba(212,168,79,0.3); }

#sec-hondiven .how-step { color: var(--accent); }
#sec-hondiven .how-step::before { background: var(--tech-blue); color: #fff; box-shadow: 0 0 8px rgba(0,123,255,0.4); }
#sec-hondiven .how-card:not(:last-child)::after { color: rgba(212,168,79,0.3); }
#sec-hondiven .how-card:hover { background: linear-gradient(135deg, rgba(0,123,255,0.05) 0%, transparent 100%); }

#sec-hondiven .diff-eyebrow { color: var(--accent); }
#sec-hondiven .diff-pillar-bar { background: var(--tech-blue); box-shadow: 0 0 8px rgba(0,123,255,0.5); }

#sec-hondiven .sec-link:hover { color: var(--tech-blue); text-shadow: 0 0 8px rgba(0,123,255,0.4); }
#sec-hondiven .client-pill:hover { color: var(--tech-blue); background: rgba(0,123,255,0.05); border-color: var(--tech-blue); }

#sec-hondiven .closing-sub { color: var(--accent); }
#sec-hondiven .btn-primary {
  background: linear-gradient(135deg, #D4A84F 0%, #A17F3B 100%);
  color: #0A0A0A;
  border: 1px solid #D4A84F;
  box-shadow: 0 4px 15px rgba(212,168,79,0.3);
}
#sec-hondiven .btn-primary:hover {
  background: linear-gradient(135deg, #007BFF 0%, #0056b3 100%);
  color: #fff;
  border-color: #007BFF;
  box-shadow: 0 4px 15px rgba(0,123,255,0.4);
}

#sec-hondiven .contact-badge { border-color: rgba(212,168,79,0.3); color: var(--accent); }
#sec-hondiven .contact-title span { color: var(--tech-blue); text-shadow: 0 0 10px rgba(0,123,255,0.3); }
#sec-hondiven .form-input:focus,
#sec-hondiven .form-select:focus,
#sec-hondiven .form-textarea:focus { border-color: var(--tech-blue); box-shadow: 0 0 8px rgba(0,123,255,0.2); background: rgba(4,21,45,0.8); }
#sec-hondiven .form-submit { background: linear-gradient(135deg, #04152D, #0A0A0A) !important; color: var(--accent); border: 1px solid var(--accent); }
#sec-hondiven .form-submit:hover { background: linear-gradient(135deg, #D4A84F, #A17F3B) !important; color: #0A0A0A; box-shadow: 0 4px 15px rgba(212,168,79,0.4); }
"@

$newContent = @()
$inOldCss = $false

foreach ($line in $content) {
    # 1. Update Google Fonts
    if ($line -match '<link href="https://fonts.googleapis.com/css2\?family=Barlow\+Condensed') {
        $line = '<link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:ital,wght@0,400;0,600;0,700;0,800;0,900;1,700;1,900&family=Barlow:wght@300;400;500;600&family=Montserrat:wght@400;600;800;900&display=swap" rel="stylesheet">'
    }
    
    # 2. Update the inline style of sec-hondiven
    if ($line -match '<div id="sec-hondiven" class="brand-section active"') {
        $line = '  <div id="sec-hondiven" class="brand-section active" style="--accent:#D4A84F;--form-accent:#D4A84F;background:#04152D">'
    }

    # 3. Replace CSS Block
    if ($line -match 'HONDIVEN SILVER PALETTE') {
        $inOldCss = $true
        # Write the new CSS before skipping the rest
        $newContent += $newCss
        continue
    }
    if ($inOldCss -and $line -match 'selector left panel stays neutral') {
        $inOldCss = $false
        # Write the line we matched since we want to keep it
        $newContent += $line
        continue
    }

    if (-not $inOldCss) {
        $newContent += $line
    }
}

$newContent | Set-Content $inputPath -Encoding UTF8
Write-Output "Applied new Corporate Tech Palette."
