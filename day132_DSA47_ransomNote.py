'''
LeetCode 383: Ransom Note

Problem statement: You are given two strings ransomNote and magazine. Return True if you can build ransomNote using letters from magazine. Each letter in magazine can be used only once. Otherwise return False.

Expected output:
“a”, “b” -> False (magazine has no ‘a’)
“aa”, “ab” -> False
“aa”, “aab” -> True
“”, “abc” -> True
'''

def canBuild(ransomNote,magazine):
	mag_list = list(magazine)

	for i in ransomNote:
		if i in mag_list:
			mag_list.remove(i)
		else:
			return False
	return True
print(canBuild("a","b"))
print(canBuild("aa","ab"))
print(canBuild("aa","aab"))
print(canBuild("","abc"))

