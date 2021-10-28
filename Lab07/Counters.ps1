$Machines = 'patel7sa-win'
$LogFile = "C:\logs\cpu.log"
Clear-Content($LogFile)

Foreach($machine in $Machines)
{
    $RCounters = Get-Counter -ListSet * -ComputerName $machine
    "There are {0} counters on {1}" -f $RCounters.count, ($machine)

    $pt = (Get-Counter -Counter "\Processor(_Total)\% Processor Time" -SampleInterval 1 -MaxSamples 10).CounterSamples.CookedValue
    $sample = 1
    foreach ($p in $pt){
        $date = Get-date -Format g
        "{3} - Sample {0}: CPU is at {1}% on {2} " -f [int]$sample, [int]$p, $machine, $date | out-file -Append $LogFile
        $sample++
    } 
}