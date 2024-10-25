def this_is_dec(func):
    def coaching():
        print("Entering into Ocean Academy")
        func()
        print("Thanks for visiting Ocean Academy")
    return coaching
def Ocean():
    print("welcome to Ocean Academy...Welcome again")
Ocean=this_is_dec(Ocean) 
Ocean()   

