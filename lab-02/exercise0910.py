def myfunction(filename, num_lines):
    #return error if the filename is less than 4 - length
    if len(filename) > 4:
#copies arg2 number of lines of arg1 into home dir
        f = open(filename)
        f2 = f.read(filename)
        home_dir_file = []
        home_dir_file = f2.split("\n")
        print home_dir_file
 #to slice to number of line - use colon
        #n = int(num_lines)
        print_this = home_dir_file[:num_lines]
        for each in print_this:
            print each
       
# ~/devopstraining/ansible/
myfunction("/Users/localadmin/devopstraining/ansible/mylogfile.log", 3)
print "error"
