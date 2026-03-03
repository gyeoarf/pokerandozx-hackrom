@echo off
echo === Building PokeRandoZX.jar (Redux Fork) ===

echo [1/4] Cleaning bin directory...
if exist bin rmdir /s /q bin
mkdir bin

echo [2/4] Compiling Java sources...
javac -encoding UTF-8 -d bin @sources.txt
if errorlevel 1 (
    echo ERROR: Compilation failed!
    pause
    exit /b 1
)

echo [3/4] Copying resources...
xcopy /s /y /q src\com\dabomstew\pkrandom\config bin\com\dabomstew\pkrandom\config\
xcopy /s /y /q src\com\dabomstew\pkrandom\newgui\*.properties bin\com\dabomstew\pkrandom\newgui\
xcopy /s /y /q src\com\dabomstew\pkrandom\patches bin\com\dabomstew\pkrandom\patches\

echo [4/4] Packaging JAR...
cd bin
jar cfe ..\PokeRandoZX.jar com.dabomstew.pkrandom.newgui.NewRandomizerGUI .
cd ..

echo.
echo === Build complete! ===
echo JAR created: PokeRandoZX.jar
echo.
echo To use with GUI: double-click launcher\launcher_WINDOWS.bat
echo   (make sure PokeRandoZX.jar is in the same folder as the launcher)
echo.
echo To use via CLI:
echo   java -Xmx4096M -jar PokeRandoZX.jar cli -s settings.rnqs -i input.nds -o output.nds
pause
