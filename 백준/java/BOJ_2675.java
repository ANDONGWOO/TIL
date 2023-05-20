
import java.util.Scanner;

public class BOJ_2675 {
    public static void main(String[] args) {
        Scanner in =new Scanner(System.in);
        int t=in.nextInt();
        for (int i = 0; i <t; i++) {
            int a = in.nextInt();
            String b=in.next();
            
            for (int k = 0; k < b.length(); k++) {
                for (int j = 0; j <a; j++) {
                    System.out.print(b.charAt(k));
                }
            }
            System.out.println();
        }
        in.close();
    }
}