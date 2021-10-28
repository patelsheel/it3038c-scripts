$Rando = 0

$LogFile = "C:\logs\rando.log"
clear-content $LogFile

for($i=0; $i -lt 5; $i++){
    $Rando = Get-Random -Maximum 1000 -Minimum 1
    Write-Host($Rando)
    Add-Content $LogFile "INFO: Random Number is ${RANDO}"
}