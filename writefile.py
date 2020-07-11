file=open('file1.txt','w')
file.write("I am writing some data to the file.\n")
L=["2020 is considered the worst year of this decade.",
   "At first we have a large orest fire in australia in which millions of animals died.\n",
                                                       "Now we are facing corona virus ,this couldn't been worst."]
file.writelines(L)
file.close()