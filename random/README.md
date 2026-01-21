# This is simple challenge of xor decodeing 

    rand = random() but in c it always give same input
    key  = user input so we can provide intizer number

    encode = rand ^ key
    decode = encode ^ key

    In this case we need to decode 
        we have encoded value 0xcafebabe and key

        solution 
            0xcafebabe ^ random = you get the flag
