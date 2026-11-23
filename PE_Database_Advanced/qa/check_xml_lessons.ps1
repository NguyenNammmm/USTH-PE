$ErrorActionPreference = 'Stop'
$root = (Resolve-Path (Join-Path $PSScriptRoot '../../..')).Path
$md68 = Get-Content -Raw -Encoding UTF8 (Join-Path $root 'output/database-advanced/lessons/AD68.md')
$md16 = Get-Content -Raw -Encoding UTF8 (Join-Path $root 'output/database-advanced/lessons/AD16.md')
$blocks = [regex]::Matches($md68, '(?s)```xml\r?\n(.*?)\r?\n```')
$shop = ($blocks | Where-Object { $_.Groups[1].Value.StartsWith('<shop ') })[0].Groups[1].Value
$xsd = ($blocks | Where-Object { $_.Groups[1].Value.StartsWith('<xs:schema ') })[0].Groups[1].Value
$recursiveXsd = ($blocks | Where-Object { $_.Groups[1].Value.StartsWith('<xs:schema ') -and $_.Groups[1].Value.Contains('name="PartType"') })[0].Groups[1].Value
$catalog = ($blocks | Where-Object { $_.Groups[1].Value.StartsWith('<catalog>') -and $_.Groups[1].Value.Contains('<name>') })[0].Groups[1].Value
$dtd = [regex]::Matches($md68, '(?s)```dtd\r?\n(.*?)\r?\n```') | Where-Object { $_.Groups[1].Value.StartsWith('<!ELEMENT catalog ') }
$dtdBody = $dtd[0].Groups[1].Value
$dtdDoc = ($blocks | Where-Object { $_.Groups[1].Value.StartsWith('<catalog>') -and $_.Groups[1].Value.Contains('refs=') })[0].Groups[1].Value
$checks = [System.Collections.Generic.List[object]]::new()
function Check($name, $condition, $detail) {
    $checks.Add([pscustomobject]@{ name=$name; passed=[bool]$condition; detail=$detail })
    if (-not $condition) { throw "Failed: $name ($detail)" }
}
function ValidateXml($text, $type, $schemaText) {
    $issues = [System.Collections.Generic.List[string]]::new()
    $settings = [System.Xml.XmlReaderSettings]::new()
    $settings.XmlResolver = $null
    $settings.DtdProcessing = [System.Xml.DtdProcessing]::Parse
    $settings.ValidationType = $type
    if ($schemaText) {
        $sr = [System.Xml.XmlReader]::Create([System.IO.StringReader]::new($schemaText))
        [void]$settings.Schemas.Add('', $sr)
        $sr.Dispose()
    }
    $settings.add_ValidationEventHandler({ param($sender,$eventArgs) $issues.Add($eventArgs.Message) }.GetNewClosure())
    $reader = [System.Xml.XmlReader]::Create([System.IO.StringReader]::new($text), $settings)
    $doc = [System.Xml.XmlDocument]::new()
    $doc.PreserveWhitespace = $true
    $doc.XmlResolver = $null
    try { $doc.Load($reader) } finally { $reader.Dispose() }
    return [pscustomobject]@{ doc=$doc; errors=@($issues) }
}
$good = ValidateXml $catalog Schema $xsd
Check 'XSD-full-catalog-valid' ($good.errors.Count -eq 0) 'Complete authored XSD compiled and accepted authored catalog.'
$mutations = @(
    @('negative-money', $catalog.Replace('10.50','-1')),
    @('missing-name', $catalog.Replace('<name>But</name>','')),
    @('wrong-sequence', $catalog.Replace('<name>But</name><price>10.50</price>','<price>10.50</price><name>But</name>')),
    @('duplicate-key', $catalog.Replace('sku="B"','sku="A"')),
    @('missing-keyref', $catalog.Replace('<purchase sku="A"','<purchase sku="C"')),
    @('zero-quantity', $catalog.Replace('qty="2"','qty="0"'))
)
foreach ($case in $mutations) {
    $r = ValidateXml $case[1] Schema $xsd
    Check ('XSD-reject-'+$case[0]) ($r.errors.Count -gt 0) ($r.errors -join ' | ')
}
$part = '<part><name>P</name><component><part><name>Q</name><component><part><name>R</name></part><qty>3</qty></component></part><qty>2</qty></component></part>'
$r = ValidateXml $part Schema $recursiveXsd
Check 'XSD-recursive-part-valid' ($r.errors.Count -eq 0) 'Compiled recursive PartType and accepted P -> Q -> R.'
foreach ($case in @(
    @('qty-zero', $part.Replace('<qty>3</qty>','<qty>0</qty>')),
    @('name-required', $part.Replace('<name>Q</name>','')),
    @('component-sequence', '<part><name>P</name><component><qty>2</qty><part><name>Q</name></part></component></part>')
)) {
    $r = ValidateXml $case[1] Schema $recursiveXsd
    Check ('XSD-recursive-reject-'+$case[0]) ($r.errors.Count -gt 0) ($r.errors -join ' | ')
}
$dtdText = '<!DOCTYPE catalog [' + $dtdBody + ']>' + $dtdDoc
$r = ValidateXml $dtdText DTD $null
Check 'DTD-IDs-and-refs-valid' ($r.errors.Count -eq 0) 'p1/p2 ID values; refs p2 p1.'
Check 'DTD-default-currency' ($r.doc.SelectSingleNode('/catalog/purchase').GetAttribute('currency') -eq 'VND') 'Default currency materialized by validating reader.'
$bad = ValidateXml ($dtdText.Replace('refs="p2 p1"','refs="p3"')) DTD $null
Check 'DTD-reject-missing-ref' ($bad.errors.Count -gt 0) ($bad.errors -join ' | ')
$bad = ValidateXml ($dtdText.Replace('code="p2"','code="p1"')) DTD $null
Check 'DTD-reject-duplicate-ID' ($bad.errors.Count -gt 0) ($bad.errors -join ' | ')
$bad = ValidateXml '<!DOCTYPE n [<!ELEMENT n ANY>]><n><undeclared/></n>' DTD $null
Check 'DTD-ANY-requires-declared-elements' ($bad.errors.Count -gt 0) ($bad.errors -join ' | ')
$r = ValidateXml $dtdText DTD $null
Check 'XPath1-id-is-ID-typed-document-order' (($r.doc.SelectNodes('id("p2 p1")') | ForEach-Object { $_.GetAttribute('code') }) -join ',' -eq 'p1,p2') 'DTD-typed IDs returned in document order despite reference-token order.'
$doc = [System.Xml.XmlDocument]::new()
$doc.PreserveWhitespace = $true
$doc.XmlResolver = $null
$doc.LoadXml($shop)
$ns = [System.Xml.XmlNamespaceManager]::new($doc.NameTable)
$ns.AddNamespace('p','urn:pe:shop')
Check 'XPath1-count-items' ($doc.SelectNodes('/p:shop/p:order[@id="o1"]/p:item',$ns).Count -eq 2) 'Native .NET XPath 1.0 subset only.'
Check 'XPath1-qty-filter' ($doc.SelectSingleNode('/p:shop/p:order/p:item[p:qty>1]/@sku',$ns).Value -eq 'A') 'Expected sku A.'
$note = $doc.SelectSingleNode('/p:shop/p:order/p:note',$ns)
Check 'XPath1-mixed-content-child-count' ($note.SelectNodes('node()',$ns).Count -eq 3) 'text, em element, text.'
Check 'XPath1-text-direct-only' ($note.SelectNodes('text()',$ns).Count -eq 2) 'Direct text() excludes text nested in em.'
Check 'XPath1-existence' ($doc.SelectNodes('/p:shop/p:order[p:item and not(p:item[p:qty<=0])]',$ns).Count -eq 1) 'Only o1.'
Check 'XPath1-nested-union' ($doc.SelectNodes('(/p:shop/p:order[@id="o1"] | /p:shop/p:order[@id="o2"])/p:customer',$ns).Count -eq 2) 'Parenthesized union can feed another path.'
$o2 = $doc.SelectSingleNode('/p:shop/p:order[@id="o2"]',$ns)
$item = $doc.CreateElement('item','urn:pe:shop')
$item.SetAttribute('sku','C')
[void]$o2.AppendChild($item)
Check 'XPath1-position-per-parent' ($doc.SelectNodes('/p:shop/p:order/p:item[1]',$ns).Count -eq 2) 'One first item per order.'
Check 'XPath1-position-global' ($doc.SelectNodes('(/p:shop/p:order/p:item)[1]',$ns).Count -eq 1) 'One first item for complete sequence.'
$small = [System.Xml.XmlDocument]::new()
$small.LoadXml('<order><note><item/></note><item/></order>')
Check 'DOM-descendants-versus-child' (($small.DocumentElement.GetElementsByTagName('item').Count -eq 2) -and ($small.SelectNodes('/order/item').Count -eq 1)) 'getElementsByTagName finds descendants; /order/item selects direct children.'
$small.LoadXml('<n a="x"><![CDATA[<b/>]]></n>')
Check 'CDATA-not-markup' (($small.SelectNodes('/n/b').Count -eq 0) -and ($small.DocumentElement.InnerText -eq '<b/>')) 'CDATA content is character data, no b element.'
$small.LoadXml('<n a="x">A<b/>B</n>')
Check 'XPath1-attribute-axis-is-not-child' (($small.SelectNodes('/n/child::node()').Count -eq 3) -and ($small.SelectNodes('/n/attribute::node()').Count -eq 1)) 'Children are text A, b, text B; attribute a is selected separately.'
$result = [ordered]@{
    date='2026-11-05'
    scope=@('AD16','AD68')
    kind='actual-.NET-XML-validation-and-XPath1-smoke-checks'
    engine=[System.Environment]::Version.ToString()
    allPassed=($checks.Where({-not $_.passed}).Count -eq 0)
    xqueryExecuted=$false
    sqlXmlExecuted=$false
    xpath2Or3Executed=$false
    checks=@($checks)
    lessonHashes=@{
      AD16=(Get-FileHash (Join-Path $root 'output/database-advanced/lessons/AD16.md') -Algorithm SHA256).Hash.ToLower()
      AD68=(Get-FileHash (Join-Path $root 'output/database-advanced/lessons/AD68.md') -Algorithm SHA256).Hash.ToLower()
    }
}
$result | ConvertTo-Json -Depth 7 | Set-Content -Encoding UTF8 (Join-Path $root 'output/database-advanced/research/semantic-xml-checks.json')
Write-Output ("Passed {0} XML checks. XQuery/SQLXML execution not performed." -f $checks.Count)
