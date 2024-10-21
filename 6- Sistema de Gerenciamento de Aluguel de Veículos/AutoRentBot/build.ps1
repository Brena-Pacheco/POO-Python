$exclude = @("venv", "AutoRentBot.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "AutoRentBot.zip" -Force