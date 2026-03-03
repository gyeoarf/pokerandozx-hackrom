# Universal Pokemon Randomizer ZX - Redux Edition

This is a fork of the Universal Pokemon Randomizer ZX (UPR-ZX) designed to support modern ROM hacks, specifically tailored for **Pokemon Blaze Black 2 & Volt White 2 Redux**.

## Supported ROM Hacks
- **Pokemon Blaze Black 2 Redux / Volt White 2 Redux** (Complete support for Version 1.6+)

## Key Features
- **Starter Pokemon Randomization**: Fixed script issues that caused infinite loops or crashes in Redux.
- **Gift Pokemon Randomization**: Supports Redux-exclusive gifts including:
  - Elemental Monkeys (Floccesy Town)
  - Gen 1 Starters (Virbank City)
  - Gen 2 Starters (Castelia City)
  - Gen 3 Starters (Anville Town)
  - Gen 4 Starters (Driftveil City)
  - Eevee (Castelia City)
  - Corsola (Season Research Lab)
- **Static Pokemon**: 29 verified safe vanilla static encounters are enabled (Legendaries, Fossils, etc.).
- **Bypassed Hack ROM Warnings**: No more "Unrecognized ROM Hack" errors.

## How to Use
1.  **Download**: Clone or download this repository.
2.  **Run**: Navigate to the `launcher` folder.
3.  **Launch**: Run `launcher_WINDOWS.bat` (or the equivalent for your OS).
4.  **Randomize**: Select your Redux ROM and choose your desired settings!

## Building from Source
If you wish to build the project yourself:
1. Ensure you have **JDK 1.8** installed.
2. Run `build_jar.bat` to compile the source and package the `PokeRandoZX.jar`.
3. The updated JAR will be available in the root and copied to the `launcher` folder automatically.

---
*Based on the original work by Ajarmar and Dabomstew.*
