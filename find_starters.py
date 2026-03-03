import ndspy
import ndspy.rom
import ndspy.narc

def find_starter_offsets(rom_path):
    print("Loading ROM:", rom_path)
    rom = ndspy.rom.NintendoDSRom.fromFile(rom_path)
    
    # a/0/5/6 is the scripts NARC
    # Wait, how to find the NARC by path?
    # Actually, ndstool or just ndspy gives us the file ID.
    # UPR-ZX uses a/0/5/6, which is exactly how ndstool shows it.
    
    # We can just iterate through file names if we have ndspy.rom
    # But wait, ndspy doesn't store true path names for all games natively unless using the FAT.
    # a/0/5/6 Narc in B2W2 is known. I can use the raw file ID from UPR if needed, or ndspy's rom.filenames
    scripts_narc_id = rom.filenames.idOf('a/0/5/6')
    print("Scripts NARC file ID:", scripts_narc_id)
    narc_data = rom.getFileByName('a/0/5/6')
    
    scripts = ndspy.narc.NARC(narc_data)
    
    # The starter script in B2W2 is file 854
    f854 = scripts.files[854]
    
    print("File 854 length:", len(f854))
    
    # Search for Snivy (495 = 0x01EF), Tepig (498 = 0x01F2), Oshawott (501 = 0x01F5)
    # usually 2 bytes, little endian: EF 01, F2 01, F5 01
    snivy_pattern = b'\xEF\x01'
    tepig_pattern = b'\xF2\x01'
    oshawott_pattern = b'\xF5\x01'
    
    # Also I'll list all occurrences of each, to guess which are the StarterOffsets
    print("Snivy occurrences:")
    idx = 0
    while True:
        idx = f854.find(snivy_pattern, idx)
        if idx == -1: break
        print(f"  Snivy at 0x{idx:X}")
        idx += 1

    print("Tepig occurrences:")
    idx = 0
    while True:
        idx = f854.find(tepig_pattern, idx)
        if idx == -1: break
        print(f"  Tepig at 0x{idx:X}")
        idx += 1

    print("Oshawott occurrences:")
    idx = 0
    while True:
        idx = f854.find(oshawott_pattern, idx)
        if idx == -1: break
        print(f"  Oshawott at 0x{idx:X}")
        idx += 1

find_starter_offsets("..\\BlazeBlack2Redux.nds")
