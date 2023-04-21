import java.util.Scanner;

public class BOJ_10953 {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int s= in.nextInt();
        for(int i = 0; i<s; i++){
            String[] q= in.next().split(",");
            System.out.println(Integer.parseInt(q[0])+Integer.parseInt(q[1]));
        }
        in.close();
    }
}