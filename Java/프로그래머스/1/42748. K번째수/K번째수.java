import java.util.*;

class Solution {
    public LinkedList<Integer> solution(int[] array, int[][] commands) {
        LinkedList<Integer> answer = new LinkedList<>();
        for(int[] sentence : commands){
            LinkedList<Integer> list = new LinkedList<>();

            for(int i = sentence[0]-1; i < sentence[1]; i++){
                list.addLast(array[i]);
            }

            Collections.sort(list);

            System.out.println(list);

            answer.addLast(list.get(sentence[2]-1));


        }

        return answer;
    }
}