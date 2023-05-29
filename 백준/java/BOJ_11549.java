import java.util.Scanner;

public class BOJ_11549 {
    public static void main(String[] args) {
        Scanner in =new Scanner(System.in);
        int q=in.nextInt();
        int a=in.nextInt();
        int b=in.nextInt();
        int c=in.nextInt();
        int d=in.nextInt();
        int f=in.nextInt();
        int s=0;
        if (a==q) {
            s+=1;
        }
        if (b==q) {
            s+=1;
             
        }
        if (c==q) {
            s+=1;
        }
        if (d==q) {
            s+=1; 
        }
        if (f==q) {
            s+=1; 
        }
        System.out.println(s);
        in.close();
    }
}
