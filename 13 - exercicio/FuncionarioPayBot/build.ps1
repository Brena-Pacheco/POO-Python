$exclude = @("venv", "FuncionarioPayBot.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "FuncionarioPayBot.zip" -Force