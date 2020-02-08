import sys


if __name__ == "__main__":
    r = list()
    c = list()
    c_list = list()
    r_sum = 0
    c_sum = 0
    result = list()
    ans = 0
    possible = False
    overflow = False
    with open("input.txt","r") as f:
        contents = f.readlines()
        n = int(contents[0])
        r_s = contents[1]
        c_s = contents[-1]
        for num in r_s.split(','):
            if int(num) > n:
                overflow = True
            r.append(int(num))
            r_sum += int(num)
        for num in c_s.split(','):
            if int(num) > n:
                overflow = True
            c.append(int(num))
            c_list.append(int(num))
            c_sum += int(num)
    if c_sum == r_sum and overflow == False: 
        possible = True
    c.sort(reverse=True)
    if possible == True:
        for i in range(n):
            row = [0]*n
            col = [True]*n
            number = r[i]
            if number > n:
                ans = 0
                break
            for j in range(number):
                index = c_list.index(c[j])
                if col[index] == True:
                    col[index] = False
                else: 
                    while col[index] == False:
                        index = c_list.index(c[j], index+1)
                    col[index] = False
                row[index] = 1
                c[j] = c[j] - 1
                c_list[index] = c_list[index ] - 1
            c.sort(reverse=True)
            result.append(row)
        ans = 1
    with open("output.txt","w") as f:
        if ans == 1:
            f.write(str(ans)+"\n")
            for i in range(len(result)):
                string = ','.join(str(x) for x in result[i])
                if i == len(result)-1:
                    f.write(string)
                else:
                    f.write(string + "\n")
        else:
            f.write(str(ans))


    
