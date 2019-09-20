from playsound import playsound
import random


while(1):
    seq_len = input("请输入序列长度：")
    if len(seq_len) > 0:
        seq_len = int(seq_len)
        break

while(1):
    sequence = []
    for i in range(seq_len):
        num = random.randint(0, 9)
        sequence.append(num)

    for i in sequence:
        filename = "number_audios/audio_%d.mp3"%(i)
        playsound(filename)

    sequence_test= list(map(int, list(input("请输入听到的数字序列："))))

    print("实际值：" + "".join(list(map(str, sequence))))
    print("测量值：" + "".join(list(map(str, sequence_test))))

    print("测试结果：" + str(sequence_test == sequence))

    control = input("继续Y/退出n:")
    if control == "" or control == "Y" or control == "y":
        continue
    else:
        break
