import java.util.Scanner;

public class BOJ_2480 {
    public static void main(String[] args) {
        int s=0;
        Scanner in =new Scanner(System.in);
        int a =in.nextInt();
        int b =in.nextInt();
        int c =in.nextInt();
        if (a==b && c==a){
            s=10000+(a*1000);
        }else if(a==b || a==c){//2번 조건
            s=1000+(a*100);
        }else if(b==c){//2번 조건
            s=1000+(b*100);
        }else{
            int z=a;//a b c max
            if(b>z){
                z=b;
            }
            if(c>z){
                z=c;
            }
            s=z*100;
        }
        in.close();
        System.out.println(s);
    }
}
