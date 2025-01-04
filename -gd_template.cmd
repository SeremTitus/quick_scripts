@echo off
scons target=template_release tests=true verbose=yes warnings=extra werror=yes module_text_server_fb_enabled=yes strict_checks=yes
if %ERRORLEVEL% EQU 0 (
    echo Command was successful > "%TEMP%\build_godot_result.txt"
) else (
    echo Command failed with error level %ERRORLEVEL% > "%TEMP%\build_godot_result.txt"
    del "%TEMP%\build_godot_result.txt"
)