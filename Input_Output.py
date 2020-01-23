"""lets talk about first ouput statement python is very straightforward its like if you want to propose a girl then python will tell direct I LVE YOU instead of saying any boring compliments
okay lets go to the point directly okay python use print function to print an out put"""
##print(values,sep,end,file,flush) this is what a print function consists of
##values: the thing you wanna say its like eg:
print("I love you")
## Sep: it means separator which is used to provide or adding separator into the string provided by the way by default it will take only space but you can give whatever you want
#eg:
print(1,2,3,4,4,sep=" ")##with the values
print('i','love','you',sep="_")##for strings
"""end: after all vallues are printed end will be printed,bydefault it will print new line"""
print("I love you","but as a friend",sep=" " ,end="***fuck")
###file is the object where the values are printed and its default value is sys.stdout(screen)
print("Hello world!", flush=True)
"""The file argument must be an object with a write(string) method; if it is not present or None, sys.stdout will be used. Whether output is buffered is usually determined by file, but if the flush keyword argument is true, the stream is forcibly flushed.
"""
