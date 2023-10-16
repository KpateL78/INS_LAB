def euclidean_algo(a, b):
    if b == 0:
        return a
    else:
        return euclidean_algo(b, a % b)

if __name__ == "__main__":
    a = int(input("Enter A: "))
    b = int(input("Enter B: "))
    
    if a < b:
        ans = euclidean_algo(b, a)
    else:
        ans = euclidean_algo(a, b)
    
    print(ans)
