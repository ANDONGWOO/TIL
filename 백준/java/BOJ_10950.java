import java.util.Scanner;

public class BOJ_10950 {
    public static void main(String[] args) {
        Scanner in =new Scanner(System.in);
        int n = in.nextInt();

        for(int i = 0; i<n; i++ ){
            byte a = in.nextByte();
            byte b = in.nextByte();
            System.out.println(a+b);
        }
        in.close();
    }
}
// n int 조건 없음 
// a,b (0 < A, B < 10) byte
