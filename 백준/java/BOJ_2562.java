import java.util.Scanner;

public class BOJ_2562 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int[] num = {in.nextInt(),in.nextInt(),in.nextInt(),
            in.nextInt(),in.nextInt(),in.nextInt(),
            in.nextInt(),in.nextInt(),in.nextInt()};
        in.close();
        int m=0;//max값
        int s=0;//칸수
        for(int i=0; i<9; i++){
            if(num[i]>m){
                m=num[i];
                s=i+1;
            }
        }

        System.out.println(m+"\n"+s);

    }
}
