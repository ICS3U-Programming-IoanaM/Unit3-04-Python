#!/usr/bin/env python3
# Copyright (c) 2022 Ioana Marinescu All rights reserved.
# Created By: Ioana Marinescu
#
# Date: Oct. 12, 2022
# tell you if a number is positive, negative, or null


def main():
    # variables
    user_num = int(input("Enter any number: "))

    # checks if number is null (equal to 0)
    if user_num == 0:
        print("0 is a null number.")

    # check if number is negative
    elif user_num < 0:
        print(f"{user_num} is a negative number.")

    # if number is positive
    else:
        print(f"{user_num} is a positive number")


if __name__ == "__main__":
    main()
