import re

total_sum = 0

for i, line in enumerate(open('./testes_python/regular_expression/arquivo_texto2.txt')):
    all_nums_s = re.findall('[0-9]+', line)
    all_nums = [ int(x) for x in all_nums_s ] 
    line_sum = sum(all_nums)
    total_sum += line_sum

print('total: ' + total_sum)