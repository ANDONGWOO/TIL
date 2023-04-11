
import java.util.Scanner;
public class BOJ_10871 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int x = in.nextInt();// x 비교
        StringBuilder q = new StringBuilder();
        for(int i=0; i<n; i++){
            int a=in.nextInt();
            if(a<x){
                q.append(a+" ");
            }
        }
        System.out.println(q);
        in.close();
    }
}