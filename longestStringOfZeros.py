#!/usr/local/bin/python3

# a binary gap is the longest string of zeros in the binary representation of a number where
# there are 1s on both ends of the gap


def binaryGap(myint):
	binaryrep=str(format(myint,'b'))
	print(binaryrep)

	longest=0
	count=0
	for i in range(len(binaryrep)):
		if (binaryrep[i] == "1"):
			if (count > longest):
				longest=count
			count=0
		else:
			count=count + 1
	return(longest)

n=1041
n=561892
longest=binaryGap(n)
print ("longest binary gap in " + str(n) + " is "  + str(longest))

#for n in range(32):
#	longest=binaryGap(n)
#	print ("longest binary gap in " + str(n) + " is "  + str(longest))
