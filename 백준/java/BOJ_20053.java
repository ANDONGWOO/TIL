import java.util.Scanner;

public class BOJ_20053 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int t=in.nextInt();
        for (int  i = 0; i < t; i++) {
            int n =in.nextInt();
            int max=-1000000;
            int min=1000000;
            for (int j = 0; j < n; j++) {
                int q=in.nextInt();
                if (q>max){
                    max = q;
                }
                if (q<min) {
                    min = q;
                }
            }
            System.out.println(min+" "+max);
        }
        in.close();
    }
}
//최소값 최대값