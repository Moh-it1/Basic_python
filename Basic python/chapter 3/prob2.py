letter='''
      Dear! <|name|>
      You are selected!
      <|date|>
'''
print(letter.replace("<|name|>", "Mohit").replace ("<|date|>","2026 mar 18"))