@echo off
cd "C:\Users\ADMIN\Development\c_workroom\godot"
scons target=editor vsproj=yes dev_build=yes -j2 %*