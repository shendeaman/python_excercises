test_tup1 = (7,2)
test_tup2 = (7,8)

def combinationsFunc(collections1,collections2):
	lst = []
	for ele in test_tup1:
		tup1,tup2 = (ele,test_tup2[0]),(ele,test_tup2[1])
		lst.extend([tup1,tup2])
	for ele in test_tup2:
		tup1,tup2 = (ele,test_tup1[0]),(ele,test_tup1[1])
		lst.extend([tup1,tup2])		
	return lst
	
ret_value = combinationsFunc(test_tup1, test_tup2)
print(f"ret_value : {ret_value}")