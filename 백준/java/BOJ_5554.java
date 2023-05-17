import java.util.Scanner;


public class BOJ_5554 {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int s=0;
        for (int i = 0; i < 4; i++) {
            s+=in.nextInt();
        }
        int a=s/60;
        int b=s%60;
        System.out.println(a);
        System.out.println(b);
        in.close();
    }
}