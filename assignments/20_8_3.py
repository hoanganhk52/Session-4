file=open("alice.txt","r")
text = file.read().split()
##print(type(text))
sorted(text)
##print(text)
wordcount={}

for word in text:
    wordcount[word] = wordcount.get(word, 0) + 1
    
print("{0:30}  {1}".format("Word","Count"))
print("=======================================")
for key,value in sorted(wordcount.items()):    
    print("{0:30}  {1}".format(key,value))









