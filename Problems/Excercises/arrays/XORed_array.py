'''
It was encoded into another integer array encoded of length n - 1, such that encoded[i] = arr[i] XOR arr[i + 1].
For example, if arr = [1,0,2,1], then encoded = [1,2,3].
You are given the encoded array. You are also given an integer first, that is the first element of arr, i.e. arr[0].

Return the original array arr. It can be proved that the answer exists and is unique.
'''

def decode(encoded, first):
    ans =[first]
    for i, _ in enumerate(encoded):
        ans.append(ans[i] ^ encoded[i])
    return ans


encoded = [6,2,7,3]
first = 4
print(decode(encoded, first))