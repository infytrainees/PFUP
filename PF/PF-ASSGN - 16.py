#PF-Assgn-16
def make_amount(rupees_to_make,no_of_five,no_of_one):
    five_needed=0
    one_needed=0
    if (((no_of_five*5) + no_of_one) < rupees_to_make):
        print(-1)
    else:
        five_needed = int (rupees_to_make/5)
        if (no_of_five<five_needed):
            five_needed=no_of_five
        rupees_to_make=rupees_to_make-(five_needed*5)
        one_needed = rupees_to_make
        if (one_needed>no_of_one):
            print(-1)
        else:
            print("No. of Five needed :", five_needed)
            print("No. of One needed  :", one_needed)
    #Start writing your code here
    #Populate the variables: five_needed and one_needed
    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work
    #Provide different values for rupees_to_make,no_of_five,no_of_one and test your program
make_amount(280,8,5)
