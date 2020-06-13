# class Solution:
# 	def firstUniqChar(self, s: str) -> int:
# 		hashmap = dict()

# 		# enumerate string, store the number of each letter
# 		for c in s:
# 			if c not in hashmap:
# 				hashmap[c] = 1
# 			else:
# 				hashmap[c] +=1
# 		# since we store it in order, so enumerate it, return the index when the value == 1
# 		for k, v in hashmap.items():
# 			if v==1:
# 				return s.index(k)
				
# 		# didn't find it, return -1 
# 		return -1


from collections import OrderedDict, Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
	# Explaination: Ordered Dict will save the characters it encounters in
	# same sequence as the original string. Hence it becomes easy to catch hold of the first
	#unique character. Then according to the counter variable, whenever the first 1 is encountered
	# the corresponding dict.key's index is returned from the original String.
        for i,j in OrderedDict(Counter(s)).items():
            if j == 1:
                return s.index(i)
        return -1
