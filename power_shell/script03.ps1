param(
    [Parameter(Mandatory=$true)]
    [int]$umbralEspacioLibreGB
)

$discos = Get-WmiObject Win32_LogicalDisk | Where-Object { $_.DriveType -eq 3 -and $_.FreeSpace / 1GB -lt $umbralEspacioLibreGB }

if ($discos.Count -eq 0) {
    Write-Host "No se encontraron discos que cumplan con el criterio."
} else {
    $discos | ForEach-Object {
        $letraUnidad = $_.DeviceID
        $espacioLibre = [math]::Round($_.FreeSpace / 1GB)
        $tamanoTotal = [math]::Round($_.Size / 1GB)
        Write-Host "Unidad $letraUnidad - Espacio libre: $espacioLibre GB de $tamanoTotal GB"
    }
}

Read-Host "Presiona Enter para salir..."