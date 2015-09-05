# 
# 
# README
# 
# The code is too long. I ran it with key size = 4
# Then replaced the most frequent letter in a column by 
# the most freq in english dictionary.
# the code works. Then I subtracted the change of substitions 
# example: if q is most common in first column, i would replace it 
# with 'e' which is the most common in english dictionary. 
# So, q == 17 and e == 5
# 17 - 5 + 1 = 13 which is "m" 
# That is why i would get the shift of m in first column, 
# Similarly, i would get the shift of "o" in second column.
# 

el = ['e','t','a','o','n','s','r','h','l','d','c','u','m','f','p','g','w','y','b','v','k','x','j','q','z']
x,key = "ofbxfcjzmdkgugdjqoxbutxteierqqwbagwcpmlpadhixzrnkcxatcxtpphinzhbapummywpugwwkqlxtsummgltkwxaqrwpqgxzzopmatrcdduqyspqzwvbqfdafvhsqmzwdrwpqfhumwqqzuvmzhhvosvidsmcehwwqbvcdswpmhbwgqdvnfhiwhkqehhffsdauzbqrhkmxsqofvrnfvhkudkmdhhffwvvahhvaijpfvhvqjhvfvhbamfqbvhzeqdvnskidrwwnfhiwtrzqldubzhizcwpqftcqgwqablvfvlatcpmicusmgnakcxbagkwihkifhkmevlnfqlxtsuqedhzrsfbxmvmoiumutrvxmrvqqkidofbqflaqbfzkdwmpivqzulbfvlaugdoacgbuahbafhipoewghwpqhzwfmsmeciifhdkwgzmpwvkggvmpwqbtsftmgv", "modi"
k = input("What is the key size?")
chunks = len(x)
divided_by_key_size = [ x[i:i+k] for i in range(0, chunks) ]

import collections
import operator

divided_by_key_size = divided_by_key_size[:-3] #removed last three strings
t=0
while t<len(divided_by_key_size[0]):
	s=[]
	for i in divided_by_key_size:
		s+= i[t]
		if len(s) == 460: 
			print s
			freq = collections.Counter(s)
			for ind in xrange(10):
				f = max(freq.iteritems(), key=operator.itemgetter(1))[0]
				freq[f] = 0
				s = ''.join(s)
				print f
				s.replace(f,el[ind])
			s=[]
	t+=1
print  "key is : " + key
