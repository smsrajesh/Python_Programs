import os


print("***** Welcome to Silent_Auction_Program *****")


bidding_dict=dict()
def SAP():
    name=input("Enter your name? : ")
    bid=int(input("Enter your bidding : "))
    bidding_dict[name]=bid
    anymore=input("Are there any other bidders ? Type 'yes' or 'no' : ")
    if anymore.lower()=='yes':
        os.system('cls')
        SAP()
    else:
        max_val=max(bidding_dict.values())
        """
        next() returns the first match.
        None is the default if the value is not found.
        """
        b_name=next((k for k,v in bidding_dict.items() if v==max_val),None)
        print(f"The Winner is {b_name} with a bid of {max_val}")

        """
        It returns all the different bidders who won the item
        """

        keys = [k for k, v in bidding_dict.items() if v == max_val]
        print(f"The Winner is {keys} with a bid of {max_val}")

SAP()
