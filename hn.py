#!/usr/bin/env python

def compare(l1,l2):
	count=0
	for elem1 in l1:
		for elem2 in l2:
			if LCSubstr_len(elem1,elem2):
				print elem1
				print elem2
				count+=1
				break;
	return count

#source: http://en.wikibooks.org/wiki/Algorithm_implementation/Strings/Longest_common_substring#Python
def LCSubstr_len(S, T):
     m = len(S); n = len(T)
     L = [[0] * (n+1) for i in xrange(m+1)]
     lcs = 0
     for i in xrange(m):
         for j in xrange(n):
             if S[i] == T[j]:
                 L[i+1][j+1] = L[i][j] + 1
                 lcs = max(lcs, L[i+1][j+1])
             else:
                 L[i+1][j+1] = max(L[i+1][j], L[i][j+1])
     return  (lcs > 0.35 * (m + n))
 

