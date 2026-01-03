#File Discriptor Challenge

Mommy! What is a file discriptor in Linux?
    *try to play the wargame your self but if you are absolute beginner follow this tutorial link: https://youtu.be/971eZhMHQQw

    Credentials to play this ctf

    ssh fd@pwnable.kr -p2222 (pw:guest)

    #This Challenge is easy to solve ther are three file discriptors 
        
        stdin=0
        stdout=1
        stderr=2

    The program ask some user input, Then it change that into intiger value then it subtract that number and provide to read 

        The subtract value is 0x1234 lets think like this 

          - 0x1234
            0x1234
            ------
                0
        so now the read will ready to accept user input ,Once ask input let give this LETMEWIN
        then the Challenge read the flag and print to the string
