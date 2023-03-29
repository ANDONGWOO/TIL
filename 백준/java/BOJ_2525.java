import java.util.Scanner;

public class BOJ_2525 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int h = in.nextInt();
        int m = in.nextInt();
        int q = in.nextInt();

        int s=h*60+m+q;
        h=s/60;
        m=s%60;
        if(h>=24){
            h=h-24;
        }
        System.out.println(h+" "+m);
        in.close();
    }
}
