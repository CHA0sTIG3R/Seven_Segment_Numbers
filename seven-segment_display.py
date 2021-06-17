layout = ["###\n# #\n# #\n# #\n###", "#\n#\n#\n#\n#",
          "###\n  #\n###\n#  \n###", "###\n  #\n###\n  #\n###",
          "# #\n# #\n###\n  #\n  #", "###\n#  \n###\n  #\n###",
          "###\n#  \n###\n# #\n###", "###\n  #\n  #\n  #\n  #",
          "###\n# #\n###\n# #\n###", "###\n# #\n###\n  #\n###"]
uin = input("Enter Numbers: ")
newlst = []
disp = ''
for i in uin:
    if i == "0":
        newlst.append(layout[0].strip('\n').split('\n'))
    if i == "1":
        newlst.append(layout[1].strip('\n').split('\n'))
    if i == "2":
        newlst.append(layout[2].strip('\n').split('\n'))
    if i == "3":
        newlst.append(layout[3].strip('\n').split('\n'))
    if i == "4":
        newlst.append(layout[4].strip('\n').split('\n'))
    if i == "5":
        newlst.append(layout[5].strip('\n').split('\n'))
    if i == "6":
        newlst.append(layout[6].strip('\n').split('\n'))
    if i == "7":
        newlst.append(layout[7].strip('\n').split('\n'))
    if i == "8":
        newlst.append(layout[8].strip('\n').split('\n'))
    if i == "9":
        newlst.append(layout[9].strip('\n').split('\n'))
for r in range(5):
    for l in range(len(newlst)):
        disp += (newlst[l][r] + " ")
    disp += "\n"

print(disp) 
