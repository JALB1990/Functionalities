[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

function Show-Menu {
    Write-Host "Menu:"
    Write-Host "1. Listar los servicios arrancados."
    Write-Host "2. Mostrar la fecha del sistema."
    Write-Host "3. Ejecutar el Bloc de notas."
    Write-Host "4. Ejecutar la Calculadora."
    Write-Host "5. Salir."
}

function List-Services {
    Get-Service | Where-Object { $_.Status -eq "Running" } | Format-Table DisplayName, Status -AutoSize
}

$choice = 0
while ($choice -ne 5) {
    Show-Menu
    $choice = Read-Host "Selecciona una opcion (1-5)"

    switch ($choice) {
        1 {
            List-Services
        }
        2 {
			(Get-Date).ToString()
        }
        3 {
            Start-Process notepad
        }
        4 {
            Start-Process calc
        }
        5 {
            Write-Host "Saliendo del programa."
        }
        default {
            Write-Host "Opcion no valida, por favor selecciona una opcion valida (1-5)."
        }
    }
}