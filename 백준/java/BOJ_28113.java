

import java.util.Scanner;

public class BOJ_28113 {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int a= in.nextInt();
        int b = in.nextInt();
        int c = in.nextInt();
        if(b<c){//100원 동전 n*100  크거나 같다
            System.out.println("Bus");
        }else if(b>c){
            System.out.println("Subway");
        }else{
            System.out.println("Anything");
        }
        in.close();
    }
}