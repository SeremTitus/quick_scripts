@echo off
"C:\Users\Serem\Development\c\godot\bin\godot.windows.editor.dev.x86_64.exe" --test -ts="*[GDScript]*"
if %ERRORLEVEL% EQU 0 (
    echo Command was successful > "%TEMP%\build_godot_result.txt"
) else (
    echo Command failed with error level %ERRORLEVEL% > "%TEMP%\build_godot_result.txt"
    del "%TEMP%\build_godot_result.txt"
)