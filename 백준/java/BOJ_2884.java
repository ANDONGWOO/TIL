import java.util.Scanner;
public class BOJ_2884 {

    public static void main(String[] args) {
        Scanner in =new Scanner(System.in);
        int a = in.nextInt();
        int b = in.nextInt();
        if(b<45){
            //b가45보다 작다면
            //시에서 분으로 추가(+60)
            if(a==0){
                //a(24)가 0이면
                //a=24-1
                //b에 60분 추가 
                a=23;
                b=b+60;    
            }else{
                // 0아니면
                //a=24-1
                //b에 60분 추가 
                a=a-1;
                b=b+60;
            }
        }
        System.out.println(a+" "+(b-45));
        in.close();
    }
}