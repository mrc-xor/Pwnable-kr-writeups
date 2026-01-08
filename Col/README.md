#This challenge teach me about some md5 hash collision

*credential to login

    ssh col@pwnable.kr -p2222 (pw:guest)

    In this vulnarable program , It ask user input of 20 characters then simply it check with defined hashcode

    hashcode = 0x21DD09EC
    divide_value = int(hashcode/5)
    solution:
                If we devide this hash into 5 we get 20 bytes
                
                then payload will be (divide_value + divide_value + divide_value + divide_value +divide_value+4) now we got out payload
