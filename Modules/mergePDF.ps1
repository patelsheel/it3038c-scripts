$FilePath1 = "$PSScriptRoot\Example01_Simple.pdf"
$FilePath2 = "$PSScriptRoot\Example02_Simple.pdf"

$OutputFile = "$PSScriptRoot\Output\OutputDocument.pdf" 

Merge-PDF -InputFile $FilePath1, $FilePath2 -OutputFile $OutputFile