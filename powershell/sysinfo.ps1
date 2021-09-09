#Function to get IP Address
function getIP
    {
        (Get-NetIPAddress).IPv4Address | Select-string "192"
        }
$IP= getIP
#Write-Host("This machine's IP is $IP")  #Code Here
#Write-Host("This machine's IP is {0}" -f $IP)  #Code Here

#Function to get Powershell Version
function getPshellVersion{
($PSVersionTable.PSVersion).Major}
$Version = getPshellVersion
#Write-Host("PowerShell version is  $Version")  #Code Here

#Function to get today's date.
function getDate {
Get-Date -Format "dddd, MM/dd/yyyy" }
$Date = getDate
#Write-Host("Today's date is $Date")  #Code Here

#Function to get hostname 
function getHostName { hostname }
$hName = getHostName
#Write-Host("Host name is $hName")  #Code Here

#Function to get a Username
function getUsrName { $env:USERNAME }
$userName = getUsrName
#Write-Host("User name is $userName")  #Code Here

#Code to display it all together.
$Body = "This machine's IP is $IP. User is $userName.
 Hostname is $hName. PowerShell version is $Version.
  Today's date is $Date."
  

 Send-MailMessage -From "sheelpatel1801@gmail.com" -Subject "IT3038C Windows SysInfo" -To "botheaj@ucmail.uc.edu" -Body $Body -SmtpServer smt.gmail.com -Port 587 -UseSsl -Credential (Get-Credential)