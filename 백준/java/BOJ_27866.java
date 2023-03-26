import java.util.Scanner;

public class BOJ_27866 {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String a = in.nextLine();
        System.out.println(a.charAt(in.nextInt()-1));
        in.close();
    }
}