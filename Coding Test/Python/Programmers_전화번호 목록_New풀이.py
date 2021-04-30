#효율성 바꾸기 
#배운점, 문자열을 sort하면 길이로 sorting 안됨
#문자열 key=len으로 문자열 길이대로 정렬 가능함
#내가 참고한 그 페이지는 문제가 있는 것이다.
#합쳐도 괜찮을 듯

def solution(phone_book):
    answer = True
    phone_dic = dict()
    phone_book.sort(key=len)
    
    for i in range(len(phone_book)-1):
        try:
            phone_dic[len(phone_book[i])][phone_book[i]] = 1
        
        except:
            phone_dic[len(phone_book[i])]=dict()
            phone_dic[len(phone_book[i])][phone_book[i]] = 1
        
        for k in phone_dic:
            if k < len(phone_book[i+1]):
        #기존의 문제풀이에서 list 자료구조를 dict로 만들어 O(N)에서 O(1)로 바꿈
                if phone_dic[k].get(phone_book[i+1][:k]):
                    return False
                
                
    return answer
    
    
print(solution(["119", "97674223", "1195524421"]))
print(solution(["123","456","789"]))
print(solution(["12","123","1235","567","88"]))
