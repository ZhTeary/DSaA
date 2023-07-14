def sameele(s: str):
    n = len(s)
    k = int(input("please input k , -n<=k<0: "))
    print("s[k] = ", s[k])
    j = n + k
    print(s[j])


sameele("abcde")
