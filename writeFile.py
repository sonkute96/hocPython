from sys import argv

script, nameFile_sour, nameFile_des = argv

txt = open(nameFile_sour)
# 'w' se ghi lien tiep va se truncate khi khoi dong lai lenh write.
txt_again = open(nameFile_des,'w')

txt_again.write(txt.read())

txt.close()
