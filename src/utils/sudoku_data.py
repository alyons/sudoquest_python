import xml.etree.ElementTree as ET
import json
tree = ET.parse('./assets/data/SudokuPuzzles.xml')
root = tree.getroot()

sudoku_dictionary: dict[str, list[str]] = dict()

# for item in root[0]:
#     print(f'{item.tag}')

print(f'{root[0][0][0].tag}: {root[0][0][0].text}')
print(f'{root[0][0][1].tag}: {root[0][0][1].text}')

print(root[0][0].__len__())

for item in root[0]:
    puzzle = item[0].text
    difficulty = item[1].text

    if not difficulty in sudoku_dictionary:
        sudoku_dictionary[difficulty] = []
    
    sudoku_dictionary[difficulty].append(puzzle)

data = json.dumps(sudoku_dictionary)

with open('sudoku_data.json', 'w') as f:
    f.write(data)

