
string1="intention"
string2="execution"

string1="acd"
string2="abd"

string1="horse"
string2="ros"

string1="sunday"
string2="saturday"

string1="zoologicoarchaeologist"
string2="zoogeologist"


def editDistance(string1,string2):

    dp=[[0 for j in range(len(string2)+1)] for i in range(len(string1)+1)]

    for i in range(1, len(string1)+1):
      dp[i][0] = i

    for j in range(1, len(string2) + 1):
      dp[0][j] = j

    for i in range(len(string1)):
        for j in range(len(string2)):
            
  
            if string1[i] == string2[j]:
                dp[i+1][j+1] = dp[i][j]

            else:
                a = dp[i][j+1] #insert
                b = dp[i+1][j] #delete
                c = dp[i][j] #replace
                dp[i+1][j+1] = 1 + min(a, b, c) 

    return dp[len(string1)][len(string2)]

print(editDistance(string1,string2))
