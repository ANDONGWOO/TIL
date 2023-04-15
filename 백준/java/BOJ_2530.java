import java.util.Scanner;

public class BOJ_2530 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int a = in.nextInt();//시
        int b = in.nextInt();//분
        int c = in.nextInt();//초

        int d = in.nextInt();//필요한 시간
        c+=d;
        b+=c/60;
        a+=b/60;
        System.out.println(a%24+" "+b%60+" "+c%60);
        in.close();
    }
}
