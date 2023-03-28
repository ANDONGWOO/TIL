import java.util.Scanner;
public class BOJ_2754 {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String q = in.next();
        double s=0;
        switch (q) {
            case "A+":
            s=4.3;
            break;
            case "A0":
            s=4.0;
            break;
            case "A-":
            s=3.7;
            break;
            case "B+":
            s=3.3;
            break;
            case "B0":
            s=3.0;
            break;
            case "B-":
            s=2.7;
            break;
            case "C+":
            s=2.3;
            break;
            case "C0":
            s=2.0;
            break;
            case "C-":
            s=1.7;
            break;
            case "D+":
            s=1.3;
            break;
            case "D0":
            s=1.0;
            break;
            case "D-":
            s=0.7;
            break;
            case "F":
            s=0.0;
            break;
        }
        in.close();
        System.out.println(s);
    }
}