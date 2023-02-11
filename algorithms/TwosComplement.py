"""Python Program that takes in two decimal number and returns the binary of the sums of twos complement"""


def inttobinary(decimal):
    decimal = int(decimal.replace('-',''))
    b = bin(decimal).split('b')[1][-7:]
    p = '0' if decimal >= 0 else '1'
    return p + format(b, '>07')


def toTwosComplement(binarySequence):
    convertedSequence = [0] * len(binarySequence)
    carryBit = 1
    # INVERT THE BITS
    for i in range(0, len(binarySequence)):
        if binarySequence[i] == '0':
            convertedSequence[i] = 1
        else:
            convertedSequence[i] = 0

    # ADD BINARY DIGIT 1

    if convertedSequence[-1] == 0: #if last digit is 0, just add the 1 then there's no carry bit so return
            convertedSequence[-1] = 1
            return ''.join(str(x) for x in convertedSequence)

    for bit in range(0, len(binarySequence)):
        if carryBit == 0:
            break
        index = len(binarySequence) - bit - 1
        if convertedSequence[index] == 1:
            convertedSequence[index] = 0
            carryBit = 1
        else:
            convertedSequence[index] = 1
            carryBit = 0

    return ''.join(str(x) for x in convertedSequence)

def binarysum(input1,input2):
    if input1[0] == '-':
        a=toTwosComplement(inttobinary(input1)) # If number is negative, find twos compliment of positive
    else:
        a=inttobinary(input1)

    if input2[0] == '-':
        b=toTwosComplement(inttobinary(input2))
    else:
        b=inttobinary(input2)

    # add two binary numbers.
    max_len = max(len(a), len(b))
    a = a.zfill(max_len) #Zfill adds 0s until a specific length, in this case 8 bits
    b = b.zfill(max_len)

    # Initialize the result
    result = ''

    # Initialize the carry
    carry = 0

    # Traverse the string
    for i in range(max_len - 1, -1, -1):
        r = carry
        r += 1 if a[i] == '1' else 0
        r += 1 if b[i] == '1' else 0
        result = ('1' if r % 2 == 1 else '0') + result

        # Compute the carry.
        carry = 0 if r < 2 else 1

    print("The sum of the two's complement is "+ result.zfill(max_len))

if __name__ == '__main__':
    print("Program that takes in two decimal numbers and returns the sum of the Twos complement")
    while True:
        input1= input("Enter an integer:")
        input2= input("Enter a second integer:")
        
        binarysum(input1,input2)
    
