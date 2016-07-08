from html_stripper import strip_tags
import re

with open('./yearly_files/DISNEY_WALT_CO_10-K') as file:
	data=file.read()
	tag_free_string = '|'.join(strip_tags(data))
	space_stripped = re.sub(' +',' ',tag_free_string)
	f = open ('./yearly_files/DISNEY_WALT_CO_10-K_stripped.txt', 'w')
	f.write(space_stripped)
	f.close()
	NI_index = space_stripped.find('NET INCOME')
	new_line = space_stripped.find('\n', NI_index)
	NI_line = space_stripped[NI_index:new_line]
	NI = re.search(r'(\d+(?:(?:\.|\,)\d+)+)', NI_line).group(0)
	print NI