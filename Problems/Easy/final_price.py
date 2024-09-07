'''
'''
def finalPrices(prices):
    ans = []
    for i in range(0, len(prices)):
        for j in range(i+1,len(prices)):
            if prices[i] >= prices[j]:
                ans.append(prices[i] - prices[j])
                break
        else:
            ans.append(prices[i])
    return ans

prices = [1,2,3,4,5]
print(finalPrices(prices))