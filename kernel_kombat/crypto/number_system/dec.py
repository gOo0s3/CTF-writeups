encoded_flag = "3a_2}3pyhr_1_nc135_7_7_0ul4_830_fyu_n471rpm07_0t015_n1_7y553rbm3_nta{umklobneKre"

new_flag = ''
for i in range(0, len(encoded_flag), 5):
        new_flag += encoded_flag[i+4]
        new_flag += encoded_flag[i]
        new_flag += encoded_flag[i+3]
        new_flag += encoded_flag[i+1]
        new_flag += encoded_flag[i+2]

print(new_flag[::-1])
