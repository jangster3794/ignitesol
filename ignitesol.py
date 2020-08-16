def answer_1(arr, N):
    # Finding Rem as after every Len(arr) rotations, arr is back to the initial value and effective rotation will be for rem number of times only
    rem = N%len(arr)
    return arr[-rem::] + arr[:-rem]

print("Answer 1: ",answer_1([1,2,3,4,5,6,7,8,9], 34))

# Answer 2
# "0" == 0  = True Because, "0" due to possible coercion will operate as 0 === 0 (Checking value as well as type)
# "" == 0 = True because on coercion this will become empty === 0 (Boolean of both being False would result True)
# "" == "0" = False, In this case, empty === "0" would be false because now boolean of "0" is True as it is of type string that contains a value.

# Answer 3
def sort(arr):
    # Key function will find smallest length first and sort accordingly
    return sorted(arr, key=lambda s: len(s))

print("Answer 3: ", sort(["You", "are", "beautiful", "looking"]))

# Answer 4
# function weird(x) {
#     var tmp = 3;
#     return function(y) {
#         return x + y + ++tmp;
#     }
# }
# var funny = weird(2);
# var final_answer = funny(10);
# final_answer value = 16;
# funny = weird(2)

# ANSWER : Funny Returns a function reference that says function(y) { x+y+ ++tmp} i.e. {6+y} as y is 10. funny returns 16

# Answer 5
def solve(text):
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    possible_char_len = len(alphabets)
    solved_text = ""
    text_split = list(text)
    # Looping through the characters in text to replace them with the value they are pointing towards
    # Replacing character in reverse, like D is pointing to A
    for t in text_split:
        try:
            #finding the index of char in alphates to replace with the one its pointing at
            position_a = alphabets.index(t.lower()) - 3
            solved_text += alphabets[position_a]
        except ValueError:
            # This is in case of special characters as they wont be in alphates list and to be put as is
            solved_text += t
    return solved_text
print("Answer 5: ", solve("Vrphwklqj phdqlqjixo"))

# question 6
# print(solve("""Zulwh d surjudp (lq Sbwkrq, MdydVfulsw ru Uxeb) wr srsxodwh dqg wkhq vruw d
# udqgrpob glvwulexwhg olvw ri 1 ploolrq lqwhjhuv, hdfk lqwhjhu kdylqj d ydoxh >= 1 dqg <=
# 100 zlwkrxw xvlqj dqb exlowlq/hawhuqdo oleudub/ixqfwlrq iru vruwlqj.
# Brxu surjudp vkrxog fduhixoob frqvlghu wkh lqsxw dqg frph xs zlwk wkh prvw hiilflhqw
# vruwlqj vroxwlrq brx fdq wklqn ri. Surylgh wkh vsdfh dqg wlph frpsohalwb ri brxu dojrulwkp"""))

# Answer 6

# write a program (in python, javascript or ruby) to populate and then sort a
# randomly distributed list of 1 million integers, each integer having a value >= 1 and <=
# 100 without using any builtin/external library/function for sorting.
# your program should carefully consider the input and come up with the most efficient
# sorting solution you can think of. provide the space and time complexity of your algorithm

def answer_6(list_len, start_val, end_val):
    import random
    int_list = []
    for i in range(list_len):
        int_list.append(random.randint(start_val,end_val))
    # Total number of possible values = 100 so making 100 buckets for each value, 
    # and first value will be ignored later on and 0 is count of values at that position
    buckets = [0]*(end_val-start_val + 2)
    for i in int_list:
        buckets[i] += 1
    final_list = []
    # Index represents the integer value and value is the count of occurences per integer
    # Time Complexity here is O(N+M) , N is total number of values in the list, 1mn and M is total number of possible values, i.e. 100
    for i in range(1,len(buckets)):
        final_list += [i]*buckets[i]
    return final_list

# print(answer_6(1000000, 1, 100))

def answer_7(sntc):
    sntc_len = len(sntc)
    final_string = ""
    delimiters = [" ", ",", ".", "@", ";", "!"] # Can add more special characters if needed for example: (,),{,},_,%,# etc
    #starting from 0 index and breaking at the delimeter and reversing from starting index to current and set starting index to the next char index
    i = 0
    for j in range(0, sntc_len):
        if sntc[j] in delimiters:
            final_string += sntc[i:j][::-1] + sntc[j]
            i = j+1
        #for last word
        elif j+1==sntc_len:
            final_string += sntc[i:j+1][::-1]
    return final_string
print("Answer 7: ", answer_7(sntc = "We are at Ignite Solutions! Their email-id is careers@ignitesol.com"))