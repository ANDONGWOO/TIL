
import java.util.Scanner;

public class BOJ_4470 {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n=Integer.parseInt(in.nextLine());
        for (int i = 1; i < n+1; i++) {
            System.out.println(i+". "+in.nextLine());
        }
        in.close();
    }
}