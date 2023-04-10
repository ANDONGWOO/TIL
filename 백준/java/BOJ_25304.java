import java.util.Scanner;
public class BOJ_25304 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        int x= in.nextInt();//총금액
        int n= in.nextInt();//종류의 수
        int s=0;
        for(int i =0; i<n; i++){
            int a = in.nextInt();
            int b = in.nextInt();
            s+=a*b;//a와b 곱하고 s더하고
        }
        if(x==s){//x과s 비교 
            System.out.println("Yes");
        }else{
            System.out.println("No");
        }
        in.close();
    }
}
