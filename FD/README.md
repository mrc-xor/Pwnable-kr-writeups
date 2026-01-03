#File Discriptor Challenge

Mommy! What is a file discriptor in Linux?
    *try to play the wargame your self but if you are absolute beginner follow this tutorial link: https://youtu.be/971eZhMHQQw

    Credentials to play this ctf

    ssh fd@pwnable.kr -p2222 (pw:guest)

    #This Challenge is easy to solve ther are three file discriptors 
        
        stdin=0
        stdout=1
        stderr=2

    The program ask some user input, Then it change that value into intiger,
    Then is subtract (user input and 0x1234)

        The subtract value is 0x1234 lets think like this 

          - 0x1234
            0x1234
            ------
                0
        len = read(fd,buf,32) now fd is point to stdin we can give input to the program
        Once the program ask user input,It compare with LETMEWIN strin using (strcmp) provide LETMEWIN input field
        
        If(!stcmp("LETMEWIN",buf)) give some user input based on this if conndition ,we can get the flag
        
