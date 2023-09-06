$files = Get-ChildItem | Where-Object { $_.Length -gt 1024 }

$files | ForEach-Object {
    Write-Output "Nombre: $($_.Name), Tamaño: $($_.Length) bytes"
}
Read-Host "Presiona Enter para salir..."