@echo off
copy /Y src\com\dabomstew\pkrandom\config\gen5_offsets.ini bin\com\dabomstew\pkrandom\config\gen5_offsets.ini
javac -encoding UTF-8 -d bin @sources.txt
java -cp bin com.dabomstew.pkrandom.newgui.NewRandomizerGUI cli -s "..\settings.rnqs" -i "..\BlazeBlack2Redux.nds" -o "..\Randomized Redux.nds"
