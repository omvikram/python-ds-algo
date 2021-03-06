## KMP Pattern Search works on the Pattern Creation
## It works on the theory that if the Pattern has prefix and suffix then their search will skip some characters
## Time Complexity O(m+n) where m and n are the length of the test and pattern respec. 
## txt[] => search text string
## pat[] => search text pattern
## lps[] => longest proper Prefix which is also Suffix

# Python program for KMP Algorithm 
def KMPSearch(pat, txt): 
	M = len(pat) 
	N = len(txt) 

	# create lps[] that will hold the longest prefix suffix 
	# values for pattern 
	lps = [0]*M 
	j = 0 # index for pat[] 

	# Preprocess the pattern (calculate lps[] array) 
	computeLPSArray(pat, M, lps) 

	i = 0 # index for txt[] 
	while i < N: 
		if pat[j] == txt[i]: 
			i += 1
			j += 1

		if j == M: 
			print "Found pattern at index " + str(i-j) 
			j = lps[j-1] 

		# mismatch after j matches 
		elif i < N and pat[j] != txt[i]: 
			# Do not match lps[0..lps[j-1]] characters, they will match anyway 
			if j != 0: 
				j = lps[j-1] 
			else: 
				i += 1

# This function creates the lps list which will help in case search pattern
# has prefix == suffix to reduce the search on searchable text
def computeLPSArray(pat, M, lps): 
	len = 0 # length of the previous longest prefix suffix 

	lps[0] # lps[0] is always 0 
	i = 1

	# the loop calculates lps[i] for i = 1 to M-1 
	while i < M: 
		if pat[i]== pat[len]: 
			len += 1
			lps[i] = len
			i += 1
		else: 
			# This is tricky. Consider the example. 
			# AAACAAAA and i = 7. The idea is similar to search step.
			# Also, note that we do not increment i here 
			if len != 0: 
				len = lps[len-1] 
			else: 
				lps[i] = 0
				i += 1

txt = "ABABDABACDABABCABAB"
pat = "ABABCABAB"
KMPSearch(pat, txt)
