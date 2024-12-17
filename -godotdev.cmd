@echo off
cls
cd "C:\Users\Serem\Development\c\godot"
(
pre-commit run
echo Number of runs: %*
-gd_bd
if exist "%TEMP%\build_godot_result.txt" (
    cls
    "C:\Users\Serem\Development\c\godot\bin\godot.windows.editor.dev.x86_64.exe" "--doctool"
    cls
    -gd_bd_run
    if exist "%TEMP%\build_godot_result.txt" (
        cls
        "C:\Users\Serem\Development\c\godot\bin\godot.windows.editor.dev.x86_64.exe" "--headless" "--print-filenames" "--gdscript-generate-tests" "C:\Users\Serem\Development\c\godot\modules\gdscript\tests\scripts"
        -gd_bd
        if exist "%TEMP%\build_godot_result.txt" (
            pause
            cls
        ) else (
            goto error
        )
        -gd_bd_test_gd
        if exist "%TEMP%\build_godot_result.txt" (
            @REM cls
            pause
        ) else (
            powershell -c "[console]::Beep(1000, 1000)"
            echo Godot test error -- any key to continue
            pause
        )
    ) else (
        powershell -c "[console]::Beep(1000, 1000)"
        echo Godot crash -- any key to continue
        pause
    )
) else (
    :error
    powershell -c "[console]::Beep(1000, 1000)"
    echo Build failed -- any key to continue
    pause
)
)



