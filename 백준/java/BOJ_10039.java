import java.util.Scanner;

public class BOJ_10039 {

    public static void main(String[] args) {
        Scanner in =new Scanner(System.in);
        int s=0;//총합
        for (int i = 0; i < 5; i++) {//5는 학생수
            int q =in.nextInt();//점수 
            if(q<40){//40미만이면 점수에 40할당
                q=40;
            }
            s+=q;
        }
        System.out.println(s/5);
        in.close();
    }
}