@echo off
scons dev_mode=true dev_build=true debug_symbols=yes tests=true optimize=debug verbose=yes warnings=extra werror=yes module_text_server_fb_enabled=yes strict_checks=yes debug_symbols=yes windows_subsystem=console dev_build=yes -j8 %*
REM Check if the scons command was successful
if %ERRORLEVEL% EQU 0 (
    echo Command was successful > "%TEMP%\build_godot_result.txt"
) else (
    echo Command failed with error level %ERRORLEVEL% > "%TEMP%\build_godot_result.txt"
    del "%TEMP%\build_godot_result.txt"
)