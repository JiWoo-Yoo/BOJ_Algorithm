class Solution {
    public int solution(int[] bandage, int health, int[][] attacks) {

        //기본 체력바 <- 체력 초과 치료 방지
        int standard = health;
        //시전 시간
        int casTime = bandage[0];
        //초당 회복량
        int heal = bandage[1];
        //추가 회복량
        int addHeal = bandage[2];

        //마지막 공격 제외하고 데미지 계산
        for(int i = 0; i < attacks.length-1; i++){
            //공격 받을 경우 -> 데미지만큼 체력을 제외
            health -= attacks[i][1];

            //만약 체력 0이하 -> 죽음
            if(health <= 0){
                return -1;
            }

            //공격 간의 term 측정(이때 마지막 공격까지 고려)
            int term = attacks[i+1][0] - attacks[i][0];

            //term 사이 치료하기
            if(term > 1){
                health += heal*(term-1);
            }

            //추가 치유
            if(term > casTime){
                //추가 치유가 두 번 이상 이루어질 경우
                health += ((term-1)/casTime)*addHeal;
            }

            //체력 바 이상 초과 치료 방지
            if(health > standard){
                health = standard;
            }
        }

        //마지막 공격 맞기
        health -= attacks[attacks.length-1][1];


        int answer = 0;

        if(health > 0){
            answer = health;
        }else{
            answer = -1;
        }

        return answer;
    }
}