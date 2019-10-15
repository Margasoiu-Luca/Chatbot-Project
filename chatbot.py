import os
sentence = input('lets talk about something! ' )
path = ('C:/University/4006CEM(programming Project)/Topics')
os.chdir(path)
dir_path = os.path.dirname(path)
for root ,dirs, files, in os.walk(dir_path):
    for file in files:
        if file.endswith('.txt'):
            #print(file)
            topic = '{}'.format(file)
            name = open(file)
            topic = list((name.read().split(',')))
counter  = 0
sentence_list = list(sentence.split(" "))
for i in sentence_list:
    print (i)
    if i in topic:
        counter  = counter+1
        print(counter)
      
