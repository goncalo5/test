
number = 5


print(type(range(10)))


def main(number):
    newlist = []
    for n in range(number):
        newlist.append(n**2)
    return newlist


print sum(main(number))


def main1(number):
    return (n ** 2 for n in range(number))


print sum(main1(number))

#print(map(str.upper, oldlist))

import time
start_time = time.time()
# main(number)
print("--- %s seconds ---" % (time.time() - start_time))


start_time = time.time()
main1(number)
print("--- %s seconds ---" % (time.time() - start_time))
