
if __name__ == '__main__':
    def my_bin_2_dec(list_):
        decimal = 0
        power_2 = 1
        l = len(list_)
        decimal += list_[ l -1 ] *power_2
        for i in range(1 ,len(list_)):
            power_2 *= 2
            decimal += list_[- i -1] * power_2
        return decimal

    test_case_1 = [1, 1, 1]
    print(my_bin_2_dec(test_case_1))
    print(my_bin_2_dec([1 ,0 ,1]))

    def my_dec_2_n_base(input_, n):
        divisor = 1
        str_binary = ""
        while divisor != 0:
            divisor = (input_ // n)
            remainder = input_ % n
            # if remainder == 10:
            #     str_binary += "A"
            # elif remainder == 11:
            #     str_binary += "B"
            # elif remainder == 12:
            #     str_binary += "C"
            # elif remainder == 13:
            #     str_binary += "D"
            # elif remainder == 14:
            #     str_binary += "E"
            # elif remainder == 15:
            #     str_binary += "F"
            # else:
            #     str_binary += str(remainder)
            if remainder >= 10:
                str_binary += chr(remainder + 55)
            else:
                str_binary += str(remainder)
            input_ = divisor

        str_binary = str_binary[::-1]
        return str_binary

    print(my_dec_2_n_base(1607859 ,20))
