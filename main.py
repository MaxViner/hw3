import math
import random
import time


def odd_index_sum():
    random_int_list=[]
    summ = 0
    for i in range(0,random.randint(5,10)):
        random_int_list.append(random.randint(0,21))
        if (i % 2 == 1):
            summ = summ + random_int_list[i]
            i += 1
        else:
            i += 1
    print('cлучайно сгенерированный список чисел : \n',random_int_list)
    print("сумма элементов на нечетных индексах: ",summ)

def pairs_num_multiply():
    random_int_list=[]

    product = []
    width = random.randint(5, 10)
    for i in range(0, width):
        random_int_list.append(random.randint(0,21))
    print('cлучайно сгенерированный список чисел : \n',random_int_list)
    for i in range(0, math.ceil(width/2)):
        product.append(random_int_list[i]*random_int_list[width-i-1])
    print(product)


def float_minimax():
    random_float_list = []
    fractional_list = []
    for i in range(0, random.randint(5, 10)):
        random_float_list.append(random.random()*10)
        fractional_list.append(random_float_list[i]%1)

    print(f"\nслучайно сгенерированный список:\n:"
          f"{random_float_list}\n"
          f"\nразница между\nмаксимальной {max(fractional_list)} и \n"
          f"минимальной {min(fractional_list)} дробной частью равна \n"
          f"={max(fractional_list)-min(fractional_list)}")


def deli_na_dwa():
    int_didgit=int(input("введите целое числ\n-->"))
    binar_didgit = ""
    while int_didgit > 0:
        binar_didgit = str(int_didgit % 2) + binar_didgit
        int_didgit = int_didgit//2
    print(binar_didgit)


def Fibonachi():
    N=int(input("сколько чисел Фибоначи вывести на экран?\n-->"))
    Positive_fibonachi=[]
    Negative_fibonachi=[]


    for i in range(0, N):

        if i in (0,1):
            Positive_fibonachi.append(1)
            Negative_fibonachi.append(-1)

        else:
            Positive_fibonachi.append (Positive_fibonachi[i-2]+Positive_fibonachi[i-1])
            Negative_fibonachi.append\
                ((-1)*(Positive_fibonachi[i - 2] + Positive_fibonachi[i - 1]))

    Negative_fibonachi.reverse()
    Negative_fibonachi.append(0)
    print(f"\nпервые {N} чисел Фибоначи: \n"
          f"{Negative_fibonachi+Positive_fibonachi}")


def go_escho():
    input("нажмите ENTER для продолжения")
    main()


def main():
    Task_number=int(input("какое задание будем проверять?: \n"
                          "\n0-выйти из программы"
                          "\n1-Задайте список из нескольких чисел. Напишите программу, "
                          "которая найдёт сумму элементов списка, стоящих на нечётной идексах."
                          "\n2-Напишите программу, которая найдёт произведение пар чисел списка. "
                          "Парой считаем первый и последний элемент, второй и предпоследний и т.д."
                          "\n3-Задайте список из вещественных чисел. Напишите программу, "
                          "которая найдёт разницу между максимальным и минимальным значением дробной части элементов."
                          "\n4-Напишите программу, которая будет преобразовывать десятичное число в двоичное."
                          "\n5-Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов."
                          "\n-->"))
    if Task_number == 1:
        odd_index_sum()

    elif Task_number ==2:
        pairs_num_multiply()
    elif Task_number ==3:
        float_minimax()
    elif Task_number ==4:
        deli_na_dwa()
    elif Task_number ==5:
        Fibonachi()
    elif Task_number == 0:
        print("goodbay...")
        time.sleep(3)
        exit()
    else:
        print("oh..something wrong")
    go_escho()

if __name__=="__main__" :
    main()