# Challenge 1
#  Write a solution that prints the numbers from 1 to 100. 
# But for multiples of three print "Planit" instead of the number and for the multiples of five print "Testing". 
# For numbers which are multiples of both three and five print "PlanitTesting".


def planit():
    i=1
    while i<101:
        if i%15 == 0:
            print('PlanitTesting')
        elif i%5 ==0 :
            print('Testing')
        elif i%3 == 0:
            print('Plaint')
        else:
            print(i)
        i += 1

planit()

# test result
# 1
# 2
# Plaint
# 4
# Testing
# Plaint
# 7
# 8
# Plaint
# Testing
# 11
# Plaint
# 13
# 14
# PlanitTesting
# 16
# 17
# Plaint
# 19
# Testing
# Plaint
# 22
# 23
# Plaint
# Testing
# 26
# Plaint
# 28
# 29
# PlanitTesting
# 31
# 32
# Plaint
# 34
# Testing
# Plaint
# 37
# 38
# Plaint
# Testing
# 41
# Plaint
# 43
# 44
# PlanitTesting
# 46
# 47
# Plaint
# 49
# Testing
# Plaint
# 52
# 53
# Plaint
# Testing
# 56
# Plaint
# 58
# 59
# PlanitTesting
# 61
# 62
# Plaint
# 64
# Testing
# Plaint
# 67
# 68
# Plaint
# Testing
# 71
# Plaint
# 73
# 74
# PlanitTesting
# 76
# 77
# Plaint
# 79
# Testing
# Plaint
# 82
# 83
# Plaint
# Testing
# 86
# Plaint
# 88
# 89
# PlanitTesting
# 91
# 92
# Plaint
# 94
# Testing
# Plaint
# 97
# 98
# Plaint
# Testing