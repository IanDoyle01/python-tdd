from byotest import *

usd_coins = [100, 50, 25, 10, 5, 1] #US Dollar Coin Denominations
eur_coins = [200, 100, 50, 20, 10, 5, 2, 1] #Euro Coin Denominations

def get_change(amount, coins=eur_coins): #defaults to euro coins
    
    change = [] #empty list to hold change
    
    for coin in coins:
        while coin <= amount:
            amount -= coin
            change.append(coin)
            
    return change

#Tests
test_are_equal(get_change(0),[])
test_are_equal(get_change(1),[1])
test_are_equal(get_change(2),[2])
test_are_equal(get_change(5),[5])
test_are_equal(get_change(10),[10])
test_are_equal(get_change(20),[20])
test_are_equal(get_change(50),[50])
test_are_equal(get_change(100),[100])
test_are_equal(get_change(200),[200])
test_are_equal(get_change(3),[2, 1])
test_are_equal(get_change(7),[5, 2])
test_are_equal(get_change(9),[5, 2, 2])
test_are_equal(get_change(35, usd_coins),[25,10])

print("All tests passed")