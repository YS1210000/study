import java.util.*;

class Solution {
    public int solution(int[] people, int limit) {
        Arrays.sort(people);
        int answer = 0;

        int front = 0;
        int end = people.length-1;

        //구현할 내용 : 두 개의 포인터가 각각 앞, 뒤에서 탐색하며 2명을 한번에 태울 수 있는지 검사
        //단, 한번에 2명을 태울 수 없는 인원이 발생할 경우 단독으로 태워야함
        while(front < end){

            if (people[front] + people[end] <= limit){
                front++;
                end--;
                answer++;
            }
            else{ //무거운 사람을 태울 수 없을 때는 단독으로 태워야함
                end--;
                answer++;
            }
        }

        if(front == end){ //홀수명일 때
            answer++;
        }

        return answer;
    }
}