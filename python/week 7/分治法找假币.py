# 有一堆共n枚硬币，其中一枚是假币，外观上无法区分，只知道假币的重量稍轻。要求仅使用一个天平，使用最少的重量比较次数找出假硬币。


# 将n个硬币分成数量相同的两堆，如果n为偶数，每堆的硬币个数为n/2；

# 如果n为奇数，每堆的硬币个数为(n-1)/2，两堆之外还会剩余一个硬币。

# 将两堆硬币上天平比较重量，如果有一堆较轻，那么假的硬币必然在轻的那一堆中。如果两堆硬币重量相等，且两堆之外有一个剩余硬币，则那个剩余硬币就是假硬币。如果两堆硬币重量相等，且两堆之外没有剩余硬币，则查找任务失败，未发现假硬币。


# 编写函数findFalseCoin(coins,start,n)并调用

# 实现"在读入的coins列表中，从下标start开始的n个硬币中查找假硬币"



def Sum(coins, start, n):
    sum = 0
    k = 0
    for i in coins[start:]:
        k += 1
        if n >= k:
            sum += i
    return sum


def findFalseCoin(coins, start, n):
    if n == 1:
        print('Fake coin:{}'.format(int(start)))
        return
    elif n % 2 == 0:
        if Sum(coins, int(start), int(n/2)) < Sum(coins, int(start+n/2), int(n/2)):
            return findFalseCoin(coins, int(start), int(n/2))
        elif Sum(coins, int(start), int(n/2)) > Sum(coins, int(start+n/2), int(n/2)):
            return findFalseCoin(coins, start+n/2, n/2)
        else:
            print('Fake coin is not found')
            return
    elif n % 2 != 0:
        if Sum(coins, int(start), int(n//2)) < Sum(coins, int(start+n//2), int(n//2)):
            return findFalseCoin(coins, int(start), int(n//2))
        elif Sum(coins, int(start), int(n//2)) > Sum(coins, int(start+n//2), int(n//2)):
            return findFalseCoin(coins, int(start+n//2), int(n//2))
        else:
            print('Fake coin:{}'.format(start+n-1))
            return


k = 0
a = list(map(int, input().split(',')))
for i in a:
    k += 1
findFalseCoin(a, 0, k)
