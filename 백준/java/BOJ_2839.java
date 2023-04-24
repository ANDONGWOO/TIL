import java.util.Scanner;

public class BOJ_2839 {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int s =in.nextInt();
        int q=0;//설탕 봉지 수

        while (s>=0) {
            if (s%5==0) {//s가5배수 이면 
                q+=s/5;
                System.out.println(q);//설탕 봉지 수
                break;
            }else{//s가3배수 이면 
                s-=3;
                q+=1;
            }   
        }if(!(s>=0)){//s>=0 아니면
            System.out.println(-1);
        } 
        in.close();
    }
}