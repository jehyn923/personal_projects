#효율성 실패
def solution(phone_book):
    answer = True
    shortest = 0
    phone_book_searcher = 0 
    phone_dic = dict()
    
    for i in range(len(phone_book)):
        
        try:
            phone_dic[len(phone_book[i])].append(phone_book[i])
        except: 
            phone_dic[len(phone_book[i])]=list()
            phone_dic[len(phone_book[i])].append(phone_book[i])
            
    for book_searcher in range(len(phone_book)):
        #상수 개
        for k in phone_dic:
            if k >= len(phone_book[book_searcher]):
                continue
            else:
                if phone_book[book_searcher][:k] in phone_dic[k]:
                    return False
            
    return answer
    
    
print(solution(["119", "97674223", "1195524421"]))
print(solution(["123","456","789"]))
print(solution(["12","123","1235","567","88"]))