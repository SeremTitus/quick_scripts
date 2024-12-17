@echo off
cls
cd "C:\Users\Serem\Development\c\godot"
pip install scons
pip install ninja
pip install pre-commit
pre-commit install
for /l %%i in (1,1,1000000) do (
    -godotdev %%i
)