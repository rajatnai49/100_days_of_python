from art import logo

auction_info = []
auction = True


def add_new_bidder(name, amount):
    bidder = {}
    bidder["bid"] = amount
    bidder["name"] = name
    auction_info.append(bidder)


while auction:
    print(logo)
    print("Welcome to the private bidding auction")
    name = input("what is your name?: ").title()
    bid = float(input("How much you want to bid?: $"))
    add_new_bidder(name=name, amount=bid)

    others = input("Are there any other bidders for auction? [y/n]\n")
    if others == 'n':
        auction = False
        highest = 0
        index = -1
        for bidder in auction_info:
            if bidder["bid"] > highest:
                index += 1
                highest = bidder["bid"]
        winner = auction_info[index]["name"]
        print(f"The highest bidder is {winner} with a ${highest}")
        print("THank you")
