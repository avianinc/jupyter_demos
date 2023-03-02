# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 12:51:58 2023

@author: jdehart
"""
import PySimpleGUI as psg
psg.set_options(font=("Arial Bold",14))
treedata = psg.TreeData()


data = '''{
    "id": 0,
    "name": "root",
    "children": [
        {
            "id": 1,
            "name": "child 1",
            "children": []
        },
        {
            "id": 2,
            "name": "child 2",
            "children": [
                {
                    "id": 3,
                    "name": "grandchild 1",
                    "children": []
                },
                {
                    "id": 4,
                    "name": "grandchild 2",
                    "children": []
                }
            ]
        }
    ]
}'''


rootnodes=[
   ["","MH", "Maharashtra", 175, 150, 200],
   ["MH", "MUM", "Mumbai", 100, 100,100],
   ["MH", "PUN", "Pune", 30, 20, 40],
   ["MH", "NGP", "Nagpur", 45, 30, 60],
   ["","TEL", "Telangana", 120, 80, 125],
   ["TEL", "HYD", "Hyderabad", 75, 55, 80],
   ["TEL", "SEC", "Secunderabad", 25, 15, 30],
   ["TEL", "NZB", "Nizamabad", 20, 10, 15]
]

for row in rootnodes:
   treedata.Insert( row[0], row[1], row[2], row[3:])
tree=psg.Tree(data=treedata,
   headings=['Product A','Product B','Product C' ],
   auto_size_columns=True,
   select_mode=psg.TABLE_SELECT_MODE_EXTENDED,
   num_rows=10,
   col0_width=5,
   key='-TREE-',
   show_expanded=False,
   enable_events=True,
   expand_x=True,
   expand_y=True,
)
layout=[[tree]]
window=psg.Window("Tree Demo", layout, size=(715, 200), resizable=True)
while True:
   event, values = window.read()
   print ("event:",event, "values:",values)
   if event == psg.WIN_CLOSED:
      break