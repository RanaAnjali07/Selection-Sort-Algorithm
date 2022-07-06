import sys
S = [30,45,78,90,12,3,21,7]

for i in range(len(S)):
	
	min_idx = i
	for j in range(i+1, len(S)):
		if S[min_idx] > S[j]:
			min_idx = j
			
	
	S[i], S[min_idx] = S[min_idx], S[i]

print ("Sorted array")
for i in range(len(S)):
	print("%d" %S[i],end=" ")
