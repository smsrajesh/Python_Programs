








def sock_pairs(pairs,wash_cycles):
    actual_socks=pairs*2
    res_2=wash_cycles//2
    # print(actual_socks,wash_cycles,res_1)
    res_3=wash_cycles//3
    # print(actual_socks,wash_cycles,res_2)
    res_5=wash_cycles//5
    # print(actual_socks,wash_cycles,res_3)
    res_10=wash_cycles//10
    # print(actual_socks,wash_cycles,res_4)


    total=actual_socks-abs((res_2*-1)+(res_3*1)+(res_5*-1)+(res_10*2))
    # print(total)
    final_result=total//2 if total>=0 else 0

    return final_result
    # pass


print(sock_pairs(2,5))
print(sock_pairs(1,2))
print(sock_pairs(5,11))
print(sock_pairs(6,25))
print(sock_pairs(1,8))

