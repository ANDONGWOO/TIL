import java.util.Scanner;

public class BOJ_5522 {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int s=0;
        for (int i = 0; i < 5; i++) {
            s+=in.nextInt();
        }
        System.out.println(s);
        in.close();
    }
}