import java.util.Scanner;
public class BOJ_11557 {
    public static void main(String[] args) {
        Scanner in =new Scanner(System.in);
        int t= in.nextInt();//케이스
        for (int i = 0; i < t; i++) {
            int n=in.nextInt();//학교의 숫자 정수 N
            String[] a=new String[n];//학교이름
            int[] b=new int[n];//지난 한 해동안 소비한 술의 양
            for (int j = 0; j < n; j++) {
                a[j]=in.next();
                b[j]=in.nextInt();
            }
            int max=0;
            int s=0;
            for (int j = 0; j < b.length; j++) {
                if(max<b[j]){//b에서 max이면 s=인덱스할당
                    max=b[j];
                    s=j;
                }
            }
            System.out.println(a[s]);//그래서 a에서 s인덱스 출력
        }
        in.close();
        
    }
}