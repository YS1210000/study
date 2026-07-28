import java.util.*;

class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        PriorityQueue<Integer> pQ = new PriorityQueue<>();

        for(int c : scoville){
            pQ.add(c);
        }

        /*
        1)가장 낮은 음식 2개를 선별(우선순위 큐를 통해 자동으로 꺼내짐)
        2)newVal = firstVal + 2 * secondVal
        3)다시 q에 넣음
        4)q에서 1개를 꺼내서 스코빌을 확인
        5)스코빌이 k이상이 되지 않았으면 다시 넣고 루프 반복
         */

        while (pQ.size() >= 2){
            if(pQ.peek() >= K){
                return answer;
            }
            int firstVal = pQ.poll();
            int secondVal = pQ.poll();
            int newVal = firstVal + 2 * secondVal;
            pQ.add(newVal);

            answer += 1;

        }
        
        if(pQ.peek() >= K){
            return answer;
        }

        

        return -1;
    }
}