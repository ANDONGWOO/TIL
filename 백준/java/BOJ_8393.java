import java.util.Scanner;

public class BOJ_8393 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        short n = in.nextShort();
        int s=0;
        for(int i=0; i<=n;i++ ){
            s+=i;
        }
        System.out.println(s);
        in.close();
    }
}
// n 10000이하 short