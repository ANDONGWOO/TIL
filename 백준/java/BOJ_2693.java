
import java.util.Arrays;
import java.util.Scanner;

public class BOJ_2693 {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int[] a = new int[10];//a원소 저장
        int[] w = new int[n];//7번째 배열값 저장
        for (int i = 0; i < n; i++) {
            for (int j = 0; j <10; j++) {
                a[j]= in.nextInt();//배열에 저장
            }
            Arrays.sort(a);//정렬하고 
            w[i]=a[7];//7번째 배열값 저장
        }
        for (int z : w) {//w에 저장한 7번째 배열값 출력 
            System.out.println(z);
        }
        in.close();
    }
}