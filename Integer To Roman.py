def intToRoman(num):
    Z = ""
    n = len(str(num))
    o = num%10
    num = (num//10)*10

    if n > 1:
        for i in range(n-1, 0, -1):
            num_ = num//(10**i)
            if i == 3:
                Z += 'M'*num_
            elif i == 2:
                if 1 <= num_ < 4:
                    Z += 'C'*num_
                elif num_ == 4:
                    Z += 'CD'
                elif num_ == 5:
                    Z += 'D'
                elif num_ == 9:
                    Z += 'CM'
                elif 5 < num_ < 9:
                    Z += 'D' + 'C'*(num_-5)
            elif i == 1:
                if 1 <= num_ < 4:
                    Z += 'X'*num_
                elif num_ == 4:
                    Z += 'XL'
                elif num_ == 5:
                    Z += 'L'
                elif num_ == 9:
                    Z += 'XC'
                elif 5 < num_ < 9:
                    Z += 'L' + 'X'*(num_-5)
            num = num%(10**i)
    
    if 1 <= o < 4:
        Z += 'I'*o
    elif o == 4:
        Z += 'IV'
    elif o == 5:
        Z += 'V'
    elif o == 9:
        Z += "IX"
    elif 5 < o < 9:
        Z += 'V' + 'I'*(o-5)
    print(Z)
intToRoman(345)
