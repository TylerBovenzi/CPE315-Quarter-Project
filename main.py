import subprocess
CMD = ["rm", "temp.txt"]
process = subprocess.Popen(CMD, stdout=subprocess.PIPE)

for i in range(2,27):
	CMD = ["perf", "stat", "-e", "L1d_cache_refill", "-e", "l2d_cache_refill", "-x"," ", "-o", "temp.txt", "--append", "./main", str(i) ]
	process = subprocess.Popen(CMD, stdout=subprocess.PIPE)
	process.wait()

		
temp_file = open("temp.txt", "r")
temp_lines = temp_file.readlines()
L1_file = open("L1.txt", "w")
L1_lines = []
L2_file = open("L2.txt", "w")
L2_lines = []
for i in range(0, 25):
	line = ((temp_lines[(i*4)+2]).split(" ", 1))  
	L1_lines.append(str(i+2) + " " + line[0] + "\n")
	line = ((temp_lines[(i*4)+3]).split(" ", 1))
        L2_lines.append(str(i+2) + " " + line[0] + "\n")

L1_file.writelines(L1_lines)
L2_file.writelines(L2_lines)

output, error = process.communicate()


