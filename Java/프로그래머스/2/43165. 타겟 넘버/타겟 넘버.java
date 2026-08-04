import java.util.Stack;

class Solution {
    public int solution(int[] numbers, int target) {
        int answer = 0;

        /*
        1) numbers에서 dfs
        2) dfs를 진행할 때 덧셈, 뺄셈 2가지를 stack에 삽입
        3)


        1) numbers에서 순서대로 값을 받음(i)
        2) 이전의 값은 모두 preSt에 삽입해뒀다가, 하나씩 빼면서 numbers[i]를 더하거나 뺀 값을 stack에 삽입
        3) numbers[i]와 연산을 마친 값들은 curSt을 통해 관리
        4) 다음 순회에서는 curSt를 preSt자리에 넘겨줌
        */

        Stack <Integer> st = new Stack<>();
        st.push(numbers[0]);
        st.push(-numbers[0]);
        st = dfs(1, st, numbers);

        for(int isTarget : st){
            //System.out.println(isTarget);
            if(isTarget == target){
                answer++;
            }
        }




        return answer;
    }

    public static Stack<Integer> dfs(int v, Stack<Integer> preSt, int[] numbers){
        Stack <Integer> curSt = new Stack<>();

        while(!preSt.empty()){
            int cur = preSt.pop();
            //System.out.println("현재"+(v+1)+"번째 시행."+cur+"에 "+numbers[v]+"를 더하거나 뺄 예정");
            curSt.push(cur + numbers[v]);
            curSt.push(cur - numbers[v]);
        }

        if(v+1 < numbers.length){
            return dfs(v+1, curSt, numbers);
        }
        else{
            return curSt;
        }


    }
}