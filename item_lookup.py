import json
import chardet

with open('char_table.json', 'rb') as file:
    rawdata = file.read()
    result = chardet.detect(rawdata)
    print(result)
encoding = result['encoding']

black_list_id = ['31014','30094','30044','30024', '30135', '30145', '30115']

with open("char_table.json", 'r',encoding=encoding) as f:
    data = json.load(f)

for op in data.values():
    if "skills" in op:
        for n in range(len(op["skills"])):
            skill = op["skills"][n]
            valid = True
            for level in skill["levelUpCostCond"]:
                for cost in level["levelUpCost"]:
                    if cost["id"] in black_list_id and valid:
                        valid = False
                        break
            if valid:
                print(op["name"],n+1,",")
