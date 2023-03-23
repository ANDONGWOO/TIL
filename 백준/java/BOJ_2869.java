import java.util.Scanner;
public class BOJ_2869 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int a = in.nextInt();
        int b = in.nextInt();
        int c = in.nextInt();
        int q= (c-b) / (a-b);
        if ((c-b) % (a-b) !=0)
        q++;
        System.out.println(q);
        in.close();
    }
}
