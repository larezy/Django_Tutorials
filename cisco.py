# my_list = [1,2,3,4,5,6,7,8,9]
#
# def even_bool(num):
#     return num % 2 == 0
#
#
# evens = filter(even_bool, my_list)
# print(list(evens))







def arck(nums):
    for i in range(len(nums)-2):
        if nums[i] ==1 and nums[i+1] ==2 and nums[i+2]==3:
            print(f"i = {i} -- nums[i] = {i}, nums[i+1] = {i+1}, nums[i+2] = {i+2}")

            return True
        print(i)

checker = arck([1 , 1, 2, 3, 1])
print(checker)


def arraycheck (nums):
    if (1 and 2 and 3) in nums:
        return True
    else:
        return False

checker = arraycheck([1 , 1, 2, 1, 2, 3])
print(checker)


def string_bits(str):
    print(str[::2])


string_bits("Hello")
string_bits("Hi")
string_bits("Heeololeo")


def end_other(a,b):
    a,b.lower()
    print(a, b)
    return a in b

print(end_other('Hiabc','abc'))





# [1 , 1, 2, 3, 1]

def chek (nums):
    for  i in range (len(nums)-2):
        print(f"Start.... At {i} == 0")
        if nums[i] == 1 and nums[i + 1]==2 and nums[i + 2] == 3:
            print(f"At: {i}, >>> {i} == 1  && >>> {i + 1} == 2 , && >>> {i + 2} == 3 ")
            return True
    return False



chek([1 , 1, 2, 3, 1])







def end_other(a,b):
    a = a.lower()
    b = b.lower()
    print(f" start... \n len of A: {len(a)}, >>> len of B: {len(b)} ")
    print(f"first: {a[-(len(b)):]}, second: {b[-len(a):]}")
    return a[-(len(b)):] == b or a == b[-(len(a)):]

print(end_other('Hiabc', 'abc'))
print(end_other('AbC', 'HiaBc'))
print(end_other('abc', 'abXabc'))

hold = "Hiabc"
print(f"Exact negative: {hold[-3:]}")
print(f"Excess: {hold[-7:]}")
