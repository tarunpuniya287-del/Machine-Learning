letter='''
   Dear<|Name|>
   You are selected!
   <|Date|>'''

print(letter.replace("<|Name|>" , "Tarun").replace("<|Date|>" , "24 sept"))
print(letter)