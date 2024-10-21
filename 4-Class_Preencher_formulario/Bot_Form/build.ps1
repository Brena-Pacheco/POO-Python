$exclude = @("venv", "Bot_Form.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "Bot_Form.zip" -Force