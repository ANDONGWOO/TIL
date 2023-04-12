import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class BOJ_2751 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        StringBuilder e = new StringBuilder();
        int n = in.nextInt();
        ArrayList<Integer> q = new ArrayList<>();
        for(int i=0; i<n; i++){
            q.add(in.nextInt());
        }
        Collections.sort(q);
        for(Integer w : q ){
            e.append(w+"\n");
        }
        System.out.println(e);
        in.close();
    }
}