from html_stripper import strip_tags

with open('./quarterly_files/NICHOLAS_FINANCIAL_INC') as file:
	data=file.read().replace('\n', '')
	print strip_tags(data)