def print_formatted(number):
    # your code goes here
    #Octal
    i=1
    l='';
    while i<=number:
        o=str(oct(i));h=str(hex(i));b=str(bin(i));
        o1=str(o[2:]);h1=str(h[2:]);b1=str(b[2:]);
        l=l+str(i)+'  '+o1+'  '+h1+'  '+b1+'\n'
        i+=1
    print(l)
    return
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
