import timeit


def find_coins_greedy(cash):
    dont_be_so_greedy = greedy_function(cash)
    return dont_be_so_greedy


def greedy_function(cash):
    coins = [50, 25, 10, 5, 2, 1]
    temp = cash
    res = {}
    if cash <= 0:
        return res

    for coin in coins:
        par1, par2 = divmod(temp, coin)
        if par2 != 0 and par1 != 0:
            res[coin] = par1
            temp = par2

        if par2 == 0 and par1 != 0:
            res[coin] = par1
            temp = par2

    return res


def find_min_coins(cash):
    nominals = recursion_min_function(cash)
    return nominals


def recursion_min_function(cash):
    coins = [1, 2, 5, 10, 25, 50]
    res = {1: 0, 2: 0, 5: 0, 10: 0, 25: 0, 50: 0}

    def internal_recursion_function(n, k=5):
        par1, par2 = divmod(n, coins[k])

        if n <= 0:
            return res

        elif par2 != 0 and par1 != 0:
            res[coins[k]] = par1
            k -= 1
            return internal_recursion_function(par2, k)

        elif par2 != 0 and par1 == 0:
            res.pop(coins[k])
            k -= 1
            return internal_recursion_function(par2, k)

        elif par2 == 0 and par1 == 0:
            res.pop(coins[k])
            k -= 1
            return internal_recursion_function(par2, k)

        # last element
        res[coins[k]] = par1
        if res[1] == 0:
            res.pop(1)
        return res

    return internal_recursion_function(cash)


input_cash = 113
t1 = timeit.timeit(f"output={find_coins_greedy(input_cash)}")
t2 = timeit.timeit(f"output={find_min_coins(input_cash)}")
print(input_cash, t1, t2)

input_cash = 1190
t3 = timeit.timeit(f"output={find_coins_greedy(input_cash)}")
t4 = timeit.timeit(f"output={find_min_coins(input_cash)}")
print(input_cash, t3, t4)

input_cash = 12133
t5 = timeit.timeit(f"output={find_coins_greedy(input_cash)}")
t6 = timeit.timeit(f"output={find_min_coins(input_cash)}")
print(input_cash, t5, t6)

input_cash = 20012133
t7 = timeit.timeit(f"output={find_coins_greedy(input_cash)}")
t8 = timeit.timeit(f"output={find_min_coins(input_cash)}")
print(input_cash, t7, t8)

input_cash = 2560012133
t9 = timeit.timeit(f"output={find_coins_greedy(input_cash)}")
t10 = timeit.timeit(f"output={find_min_coins(input_cash)}")
print(input_cash, t9, t10)


input_cash = 113
dict_greedy = find_coins_greedy(input_cash)
print("Жадібний алгоритм:", dict_greedy)
dict_min_coins = find_min_coins(input_cash)
print("Динамичне прогромуапння:", dict_min_coins)
