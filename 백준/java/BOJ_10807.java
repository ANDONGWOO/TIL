import java.util.Scanner;

public class BOJ_10807 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int t=in.nextInt();//배열 수
        int[] q= new int[t];//배열
        int s=0;
        for(int i=0; i<t; i++){
            q[i]=in.nextInt();
        }
        int w= in.nextInt();//배열에서 찾으려고 하는 정수
        for(int i=0; i<q.length; i++){
            if(w==q[i]){
                s++;
            }
        }
        System.out.println(s);
        in.close();
    }
}
