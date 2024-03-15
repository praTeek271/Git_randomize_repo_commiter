@REM run 40 times notepad in loop


@echo off

setlocal enabledelayedexpansion

set /a count=0

:loop
start "" https://www.youtube.com/watch?v=KfRRznwcvsY&t=64s 
set /a count+=1
if !count! lss 40 goto loop

endlocal








