import java.util.Scanner;

public class BOJ_1546 {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n=in.nextInt();
        float[] s=new float[n];
        float q=0;
        float max = s[0];
        for (int i = 0; i < s.length; i++) {
            s[i]=in.nextInt();
            if (max<s[i]) {
                max=s[i];
            }
        }
        for (float f : s) {
            q+=f/max*100;
        }
        System.out.println(q/n);
        in.close();
    }
}