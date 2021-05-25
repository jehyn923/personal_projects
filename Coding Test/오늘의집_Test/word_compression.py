# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
from collections import OrderedDict
string = raw_input()

text_compressor = OrderedDict()

for i in range(len(string)):
	if string[i].isdigit():
		continue
		
	if string[i].isalpha():
		temp_num_txt = ''
		#다음 알파벳이 나올 때까지 반복
		for j in range(i+1, len(string)):
			if string[j].isalpha():
				break
			temp_num_txt += string[j]
		
		#문자열에 이미 해당 알파벳이 나왔다면
		if string[i] in text_compressor.keys():
			text_compressor[string[i]] += int(temp_num_txt)
			#나오지 않았다면 그냥 매칭
		else:
			text_compressor[string[i]] = int(temp_num_txt)


#compressed 문자열 만들기
compressed_txt = ''
for k,v in text_compressor.items():
	compressed_txt += k + str(v)

print(compressed_txt)