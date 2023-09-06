$fecha = Get-Date -Format "yyyyMMdd"
Get-ChildItem -Filter *.jpg | ForEach-Object {
    $nuevoNombre = "$fecha-$($_.Name)"
    Rename-Item -Path $_.FullName -NewName $nuevoNombre
}
Read-Host "Ejecutado el Script, Presiona Enter para salir..."