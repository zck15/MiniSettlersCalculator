import json

crafting_table = [
    # 建筑名                产物名          输入物品名称列表                        输入与输出比例列表  建筑冷却时间
    # Settlement
    ['House_level1',        'Population',   ['Water', 'Apple', 'Chair'],            [1, 1, 1, 24],      50],
    ['House_level2',        'Population',   ['Juice', 'Bread', 'Paper', 'Sofa'],    [1, 1, 1, 1, 108],  50],
    ['House_level3',        'Population',   ['Milk', 'Sandwich', 'Book', 'Luxury'], [1, 1, 1, 1, 330],  60],
    # Water
    ['Water_Well',          'Water',        [],                                     [1],                7],
    ['Water_Pump',          'Water',        ['Bread'],                              [1, 3],             5],
    ['Sea_Water_Filter',    'Water',        ['Coal'],                               [1, 2],             20],
    # Food
    ['Apple_Farm',          'Apple',        ['Water'],                              [1, 2],             10],
    ['Juice_Maker',         'Juice',        ['Board', 'Apple'],                     [1, 1, 2],          15],
    ['Wheat_Farm',          'Wheat',        ['Water'],                              [1, 2],             10],
    ['Bakery',              'Bread',        ['Wheat', 'Coal'],                      [2, 1, 2],          20],
    ['Cow_Farm',            'Cow',          ['Water', 'Wheat'],                     [1, 1, 2],          15],
    ['Milk_Factory',        'Milk',         ['Cow', 'Glass'],                       [1, 1, 2],          20],
    ['Butcher',             'Meat',         ['Cow', 'Iron_Tool'],                   [1, 1, 2],          20],
    ['Restaurant',          'Sandwich',     ['Bread', 'Meat'],                      [1, 1, 2],          20],
    # Wood Work
    ['Lumber_Camp',         'Lumber',       ['Apple', 'Tree'],                      [1, 1, 1],          15],
    ['Sawmill',             'Log',          ['Lumber'],                             [1, 2],             10],
    ['Forester',            'Tree',         ['Water'],                              [1, 1],             10],
    ['Carpenter_Workshop',  'Board',        ['Log', 'Stone_Tool'],                  [1, 1, 2],          25],
    ['Charcoal_Maker',      'Coal',         ['Apple', 'Lumber'],                    [1, 1, 2],          15],
    ['Wood_Factory',        'Log',          ['Bread', 'Tree'],                      [1, 1, 2],          20],
    ['Wood_Beam_Workshop',  'Wood_Beam',    ['Iron_Tool', 'Board'],                 [1, 1, 2],          40],
    # Ores
    ['Stone_Quarry',        'Stone',        ['Apple'],                              [1, 2],             20],
    ['Stone_Mine',          'Stone',        ['Bread'],                              [1, 3],             10],
    ['Coal_Quarry',         'Coal',         ['Apple'],                              [1, 2],             20],
    ['Coal_Mine',           'Coal',         ['Bread'],                              [1, 3],             10],
    ['Iron_Quarry',         'Iron_Ore',     ['Bread'],                              [1, 2],             20],
    ['Iron_Mine',           'Iron_Ore',     ['Bread'],                              [1, 3],             10],
    ['Sand_Collector',      'Sand',         ['Juice'],                              [1, 1],             20],
    ['Diamond_Mine',        'Diamond',      ['Meat', 'Steel_Tool'],                 [1, 1, 3],          10],
    # Tools
    ['Stone_Tool_Maker',    'Stone_Tool',   ['Stone', 'Log'],                       [1, 1, 2],          7],
    ['Iron_Tool_Maker',     'Iron_Tool',    ['Iron', 'Stone_Tool'],                 [1, 1, 2],          10],
    ['Steel_Tool_Maker',    'Steel_Tool',   ['Steel', 'Iron_Tool'],                 [1, 1, 2],          15],
    # Furniture
    ['Wood_Furniture_Maker',    'Chair',    ['Lumber', 'Stone_Tool'],               [1, 1, 2],          15],
    ['Leather_Furniture_Maker', 'Sofa',     ['Leather', 'Chair'],                   [1, 1, 1],          15],
    ['Luxury_Furniture_Maker',  'Luxury',   ['Diamond', 'Sofa'],                    [1, 1, 1],          25],
    # Factories
    ['Stone_Blocker',       'Stone_Block',  ['Stone', 'Stone_Tool'],                [1, 1, 2],          25],
    ['Stone_Masonry',       'Slate',        ['Iron_Tool', 'Stone_Block'],           [1, 1, 2],          40],
    ['Iron_Smelter',        'Iron',         ['Coal', 'Iron_Ore'],                   [1, 2, 2],          15],
    ['Paper_Factory',       'Paper',        ['Log', 'Iron_Tool'],                   [1, 1, 2],          30],
    ['Leather_Maker',       'Leather',      ['Cow', 'Iron_Tool'],                   [1, 1, 2],          20],
    ['Glass_Maker',         'Glass',        ['Sand', 'Coal'],                       [1, 1, 2],          25],
    ['Steel_Smelter',       'Steel',        ['Coal', 'Iron'],                       [1, 1, 1],          20],
    ['Library',             'Book',         ['Leather', 'Paper', 'Steel_Tool'],     [1, 1, 1, 2],       25],
]


with open('buildings.json', 'w') as file:
    json.dump(crafting_table, file)