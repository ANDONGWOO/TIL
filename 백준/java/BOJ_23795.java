import java.util.Scanner;

public class BOJ_23795 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int s=0;
        while (true) {
            int q=in.nextInt();
            if (q==-1) {
                break;
            }
            s+=q;
        }
        System.out.println(s);
        in.close();
    }
}
