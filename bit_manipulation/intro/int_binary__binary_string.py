def int_binary(integer):
    binary=''
    while integer!=1:
        binary+=str(integer%2)
        integer=integer//2
    if integer==1:
        binary+='1'
    binary=binary[::-1]
    return binary
def binary_int(binary):
    integer=0
    for i in range(1,len(binary)+1):
        num=int(binary[-i])
        integer=integer+num*(2**(i-1))
    return integer
def int_binary_simple(integer):
    return bin(integer)[2:]
def binary_int_simple(binary):
    return int(binary,2)


if __name__=='__main__':
    integer=int(input())
    print(f"integer to binary of {integer} is {int_binary(integer)}")
    binary=input()
    print(f"binary to integer of {binary} is {binary_int(binary)}")
    print(f"integer to binary of {integer} is {int_binary_simple(integer)}")
    print(f"binary to integer of {binary} is {binary_int_simple(binary)}")

