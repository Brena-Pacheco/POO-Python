$exclude = @("venv", "BotLivros.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "BotLivros.zip" -Force