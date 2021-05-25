# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
num_people = int(raw_input())

#돌아가야 하는 사람들
people = []

for i in range(num_people):
	speed = int(input())
	people.append(speed)

people.sort()

#다리를 한번에 건널 수 있는 최대인원 2명이기 때문에 플래시를 돌려주는 빠른 인원 2명 고정
moveable = (people[0],people[1])
arrived = []
time = 0 

#대기 중인 사람이 없어질 때까지 반복
while people:
	move = []
	people.sort()
		
	
	if arrived:
		#빠르게 돌아올 수 있는 2명이 없을 경우
		if arrived[0] == moveable[0] or arrived[0] == moveable[1]:
			move.extend(people[-2:])
			del people[-2:]
			
		#빠르게 돌아올 수 있는 2명이 없을 경우
		else:
			move.extend(people[:2])
			del people[:2]
	#도착한 인원이 없을 떄
	else:
		move.extend(people[:2])
		del people[:2]
	
	#도착 인원에 추가
	arrived.extend(move)
	time += max(move)
	arrived.sort()
	if len(arrived) != num_people:
		#돌아오는 로직
		back = arrived.pop(0)
		people.append(back)
		time += back
		del move
    
print(time)
  

