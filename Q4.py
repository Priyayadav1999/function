def reverse_str(a):
    i=1
    sum=" "
    while i<=len(a):
        sum=sum+a[-i]
        i+=1
    print(sum)

string="1234a69007bcd"
reverse_str(string)