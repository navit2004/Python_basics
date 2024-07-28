#2  write a program to fill in a letter template given below with name and date.
# letter='''Dear <|Name|>,
#           you are selected!
#           <|Date|> '''

letter='''Dear <|Name|>,
 you are selected!
<|Date|> '''

print(letter.replace("Name","Navit").replace("Date","27 july 2024"))