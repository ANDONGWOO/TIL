import java.util.Scanner;

public class BOJ_2438 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int s=in.nextInt();
        for(int i=1; i<=s; i++){
            for (int j = 1; j <=i; j++) {
                System.out.print("*");
            }
            System.out.println();
        }
        in.close();
    }
}
