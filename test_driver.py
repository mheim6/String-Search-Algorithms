####################################
#
# Monica Heim
# Driver Code
# Automata Algorithms and Complexity
# Assignment 3
####################################

import kmp as third_script
import naive_multi_ocurrance as first_script
import rkm as second_script
import time

def test(testString, sub):
    print("----------------------------------")
    print("Test string: " + testString)
    print("Sub string: " + sub)
    print("Naive multi-ocurrance string search: ")
    print(first_script.finder(sub, testString))
    print("Rabin-Karp multi-ocurrance search: ")
    print(second_script.rabin_karp(testString, sub))
    print("Knuh-Morris-Pratt multi-ocurrance seach: ")
    third_script.KMP(sub, testString)
    print("----------------------------------\n")
    
def timer():
    average = "pneumonoultramicroscopicsilicovolcanoconiosis"
    sub = "amicroscopi"
    print("average time for NAIVE:" )
    start_time = time.time()
    first_script.finder(sub,average)
    print(str(round(time.time() - start_time, 5)) + " seconds to finish the search string")
    print("Worst case for NAIVE:" )
    worst = "xxxxxxxxxxxxxxxxxxxxxxx"
    sub = "xxxx"
    start_time = time.time()
    first_script.finder(sub,worst)
    print(str(round(time.time() - start_time, 5)) + " seconds to finish the search string")
    print("------------------------------------------------\n")
    average = "pneumonoultramicroscopicsilicovolcanoconiosis"
    sub = "scopicsil"
    print("average time for RKM:" )
    start_time = time.time()
    second_script.rabin_karp(average, sub)
    print(str(round(time.time() - start_time, 5)) + " seconds to finish the search string")
    print("Worst case for RKM:" )
    worst = "xxxxxxxxxxxxxxxxxxxxxy"
    sub = "xy"
    start_time = time.time()
    second_script.rabin_karp(worst, sub)
    print(str(round(time.time() - start_time, 5)) + " seconds to finish the search string")
    print("------------------------------------------------\n")
    average = "pneumonoultramicroscopicsilicovolcanoconiosis"
    sub = "scopicsil"
    print("average time for KMP:" )
    start_time = time.time()
    third_script.KMP(sub,average)
    print(str(round(time.time() - start_time, 5)) + " seconds to finish the search string")
    print("Worst case for KMP:" )
    worst = "xyxyxyxyxyxyyxyxy"
    start_time = time.time()
    third_script.KMP(sub,worst)
    print(str(round(time.time() - start_time, 5)) + " sseconds to finish the search string")
    print("------------------------------------------------\n")
    
print("TEST CASE 1")   
# test case 1
testString = "pneumonoultramicroscopicsilicovolcanoconiosis" #literally a real word 
sub = "a"
test(testString,sub)
sub = "covo"
test(testString,sub)
sub = "covol"
test(testString,sub)
sub = "croscopicsilicovolcanoconiosis"
test(testString,sub)
sub = "oscopicsilicovolcanocon"
test(testString,sub)



print("TEST CASE 2") 
testString = "esternocleidooccipitomastoideos"
sub = "a"
test(testString,sub)
sub = "oclei"
test(testString,sub)
sub = "xxxxxxxxx"
test(testString,sub)

timer()