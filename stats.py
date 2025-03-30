def get_num_words(txt):
	count = 0
	for word in txt.split():
		count += 1
	return count

def get_characters(txt):
	split_txt = list(txt)
	split_txt.pop(0) # pop off the dickhead unicode BOM
	txtd = {}

	for c in split_txt:
		try:
			txtd[c.lower()] +=1
		except:
			txtd[c.lower()] = 1
	return txtd

def sort_characters(input):
	rtn = {}

	input_sort = {k: v for k, v in sorted(input.items(), key=lambda item: item[1])}
	
	for k in reversed(list(input_sort.keys())):
		rtn[k] = input_sort[k]

	del rtn[" "] # strip out the useless space counter

	print(rtn)

	return rtn