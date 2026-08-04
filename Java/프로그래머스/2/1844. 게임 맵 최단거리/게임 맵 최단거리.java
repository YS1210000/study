import java.util.ArrayDeque;
import java.util.Deque;

class Solution {
    public int solution(int[][] maps) {
        /*
        1)bfs로 탐색
        2)시작점은 0,0
        3)0이 벽, 1이 길
        4)탐색에 걸린 시간을 return
         */

        Deque<int[]> q = new ArrayDeque<>();
        q.push(new int[]{0, 0});

        return bfs(1, maps, q);
    }

    boolean [][] visited = new boolean[100][100];
    int [] nx = {-1, 1, 0, 0};
    int [] ny = {0, 0, -1, 1};

    private int bfs(int count, int[][] maps, Deque<int[]> q){
        Deque<int[]> nextQ = new ArrayDeque<>();

        while(!q.isEmpty()){
            int[] cur = q.poll();
            int maxX = maps[0].length-1;
            int maxY = maps.length-1;

            for(int i = 0; i < 4; i++){
                int nextX = cur[0] + nx[i];
                int nextY = cur[1] + ny[i];


                if(0 <= nextX && nextX <= maxX && 0 <= nextY && nextY <= maxY && !visited[nextX][nextY] && maps[nextY][nextX] == 1){
                    //System.out.println(count+"회 순회 중, {"+nextX+", "+nextY+"} 삽입");

                    if(nextX == maxX && nextY == maxY){
                        return count + 1;
                    }
                    nextQ.push(new int[]{nextX, nextY});
                    visited[nextX][nextY] = true;

                }
            }
        }

        if(nextQ.isEmpty()){
            return -1;
        }
        else{
            return bfs(count + 1, maps, nextQ);
        }


    }
}