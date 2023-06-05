import java.util.Scanner;

public class BOJ_10808 {
    public static void main(String[] args) {
        Scanner in =new Scanner(System.in);
        String q=in.next();

        int[] s = new int[26];//알파벳26

        for (int i = 0; i < q.length(); i++) {
            char w=q.charAt(i);
            s[w-97]++;//아스키 a 97
        }
        // for (int i = 0; i < 26; i++) {
        //     System.out.print(s[i]+" ");
        // }
        for (int i : s) {
            System.out.print(i+" ");
        }
        in.close();
    }
}
