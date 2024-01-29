#1.
#test_list = [[('Gfg', 3)], [('best', 1)]] 
#cus_eles = [1, 2]
#2.
test_list = [[('Gfg', 6), ('Gfg', 3)]]
cus_eles = [7]
output = []


for cnt,ele in enumerate(test_list):
	sample_list = []
	if cnt==len(test_list)-1 and len(cus_eles)==1:
		print(f"ele : {ele}")
		for e in ele:
			lst = []
			a = list(e)
			b = cus_eles[0]
			a.append(b)
			lst.append(tuple(a))
			output.append(lst)
	else:
		print(f"I am in else...")
		a = list(ele[0])
		b = cus_eles[cnt]
		a.append(b)
		sample_list.append(tuple(a))
		output.append(sample_list)

#if len(test_list)==len(cus_eles) and len(test_list[0])>:

print(f"output : {output}")