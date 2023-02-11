$folder = Get-Location
$pythonpath = (get-command python.exe).Path
$action = New-ScheduledTaskAction -Execute $pythonpath -Argument "main.py" -WorkingDirectory $folder
$trigger = New-ScheduledTaskTrigger -AtLogon
$principal = New-ScheduledTaskPrincipal -UserId $env:UserDomain'\'$env:UserName
$settings = New-ScheduledTaskSettingsSet -ExecutionTimeLimit 0
$task = New-ScheduledTask -Action $action -Principal $principal -Trigger $trigger -Settings $settings
Register-ScheduledTask horizon -InputObject $task