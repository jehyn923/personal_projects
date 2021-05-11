function solution(n,lost,reserve){
    var answer = 0;
    var borrowed =[];
    var lended =[];
    var cnt = 0;
    for(var i = 1 ; i< n+1;i++){
        //original 하게 갖고 있는 친구들 case

        //잃어버린 case
        if(lost.includes(i)){
            if(reserve.includes(i)){
                //lost 더 이상 아님 체크 안해도댐
                lost.splice(lost.indexOf(i),1);
                //여분 없음 빌려줄수 없음
                reserve.splice(reserve.indexOf(i,1));
                cnt ++;

            }
            //내 앞에 애가 여분이 있더라
            else if(reserve.includes(i-1)){
                lost.splice(lost.indexOf(i),1);
                reserve.splice(reserve.indexOf(i-1,1));
                cnt ++;
            }
            else if(reserve.includes(i+1)){
                lost.splice(lost.indexOf(i),1);
                reserve.splice(reserve.indexOf(i+1,1));
                cnt ++;
            }
        }
        else{
            cnt ++;
        }
        
        //그 중 내가 여분이 있던 case
        //내 앞이 여분이 있던 case
        //내 뒤가 여분이 있던 case
        

    }
    answer = cnt;
    console.log(lost);
    return answer;
}


console.log(solution(5,[2,4],[1,3,5]));
console.log(solution(5,[2,4],[3]));
console.log(solution(3,[3],[1]));
console.log(solution(4,[1],[4]))