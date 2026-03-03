import com.dabomstew.pkrandom.newnds.NDSRom;

public class GetDiagnostic {
    public static void main(String[] args) throws Exception {
        System.out.println("Processing " + args[0]);
        NDSRom rom = new NDSRom(args[0]);
        rom.getARM9();
        for (int i : new int[] { 36, 162, 166, 167, 168, 284, 294, 316 }) {
            rom.getOverlay(i);
        }
        rom.printRomDiagnostics(System.out);
    }
}
