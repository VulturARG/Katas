#Método greedy
def change_greedy(coins,amount):
    if len(coins) == 0: return [[amount,-1]]
    returnCoins = []
    coin = coins.pop()
    numberCoin = amount//coin
    if numberCoin != 0:
         returnCoins.append([coin,numberCoin])
    if numberCoin * coin == amount:
        return returnCoins
    else:
        returnCoins.extend(change_greedy(coins,amount%coin))
    
    return returnCoins

coins = [1,5,10,25,50] #Coins debe estar ordenado de mayor a menor
print(change_greedy(coins,126))