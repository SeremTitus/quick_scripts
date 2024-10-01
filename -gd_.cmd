@echo off

for /l %%i in (1,1,1000000) do (    
    cls
    cd "C:\Users\Serem\Development\c\godot"

    -gd_bd
    

    if exist "%TEMP%\build_godot_result.txt" (
        echo Build was successful
        -gd_bd_run
        if exist "%TEMP%\build_godot_result.txt" (
            echo good
        ) else (
            powershell -c "[console]::Beep(1000, 1000)"
            echo Godot crash -- any key to continue
            pause
        )
        -gd_bd_test_gd
    ) else (
        powershell -c "[console]::Beep(1000, 1000)"
        echo Build failed -- any key to continue
        pause
    )
)


