def solution(name):
    answer = 0
    alphabet = {}
    name_location = []
    location_map = []
    current_position = 0
    step_count = 0
    forwarding_Fast = False

    #dictionary 초기화
    for i in range(26):
        alphabet[chr(ord('A')+i)] = i
    
    #해당 알파벳 alphabet 참조 후 13(중간)이상이면 26-값으로 return
    for i in range(len(name)):
        location = alphabet[name[i]]
        if location > 13:
            location = 26-location

        name_location.append(location)
        if location > 0 and i > 0:
            location_map.append(i)
    

    while sum(name_location)>0:
        

        answer += name_location[current_position]
        name_location[current_position] = 0

        if location_map:
            forward_position = (len(name_location) + location_map[0] - current_position) % len(name_location)
            backward_position = (len(name_location) + current_position - location_map[-1])%len(name_location)


            if forward_position <= backward_position:
                current_position = location_map.pop(0)
                step_count += forward_position
            else:
                current_position = location_map.pop()
                step_count += backward_position
    

        if step_count > len(name_location):
            forwarding_Fast = True
            break

    if forwarding_Fast:
        answer = sum(name_location)+len(name_location)-1

    else:
        answer+= step_count

    return answer

print(solution("JEROEN"))
print(solution("JAN"))