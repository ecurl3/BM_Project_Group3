#!/usr/bin/env python3
import sys
import random
from functions import print_preferences_before, gen_random_preference, print_engagements_after
from Gale_Shapley import algo

__authors__ = "BM_GROUP_3 coders: Jacob, Tyler, Emily"

# main function
def main():

    if (len(sys.argv) != 2):
        print("Execute with './main.py <number>'")
        sys.exit(0)

    n = int(sys.argv[1])

    preference = []
    preference = gen_random_preference(n)

    print_preferences_before(preference)

    result = algo(preference)

    print_engagements_after(result)


if __name__ == '__main__':
    sys.exit(main())
