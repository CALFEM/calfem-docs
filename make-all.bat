@echo OFF

REM Command file to build all documentation formats

call make-matlab.bat %1
call make-python.bat %1
