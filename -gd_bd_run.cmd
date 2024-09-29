@echo off
rem Delete all folders except the "editor" folder
for /d %%i in ("C:\Users\Serem\Development\godot_projects\gdtrait-tests\.godot\*") do (
    if /i not "%%i"=="C:\Users\Serem\Development\godot_projects\gdtrait-tests\.godot\editor" (
        rmdir /s /q "%%i"
    )
)

rem Delete all files except "editor_layout.cfg"
for %%i in ("C:\Users\Serem\Development\godot_projects\gdtrait-tests\.godot\editor\*") do (
    if /i not "%%i"=="C:\Users\Serem\Development\godot_projects\gdtrait-tests\.godot\editor\editor_layout.cfg" (
        del /q "%%i"
    )
)
"C:\Users\Serem\Development\c\godot\bin\godot.windows.editor.dev.x86_64.exe" "--path" "C:\Users\Serem\Development\godot_projects\gdtrait-tests" "-e"
if %ERRORLEVEL% EQU 0 (
    echo Command was successful > "%TEMP%\build_godot_result.txt"
) else (
    echo Command failed with error level %ERRORLEVEL% > "%TEMP%\build_godot_result.txt"
    del "%TEMP%\build_godot_result.txt"
)