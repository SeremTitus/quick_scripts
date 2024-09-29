@echo off
REM ninja=true
scons module_text_server_fb_enabled=yes warnings=extra verbose=yes strict_checks=yes tests=true dev_build=true debug_symbols=true dev_mode=true werror=yes -j8%*
REM Check if the scons command was successful
if %ERRORLEVEL% EQU 0 (
    echo Command was successful > "%TEMP%\build_godot_result.txt"
) else (
    echo Command failed with error level %ERRORLEVEL% > "%TEMP%\build_godot_result.txt"
    del "%TEMP%\build_godot_result.txt"
)