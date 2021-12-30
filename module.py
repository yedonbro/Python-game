from time import *
answer_yes = ["YES", "Yes", "yes", "y", "Y"]
answer_no = ["NO", "No", "no", "n", "N"]
def terminal():
    commands = ["run", "start", "start>> rungame--0", "!help"]
    var1 = input(">>")
    var2 = var1.lower()
    hall = input(f"{var1.upper()}>>")
    hall2 = input(f"{var2.upper()}>>{hall}>>")


    if "run" == var2 or var2 == "start":


 


        if hall2.lower() == "adventure" or hall2.lower() == "rungame--0":
            run_adventure()
        
        if hall2.lower == ".":
            terminal()
    if var1 == "!help":
        print(f"\nHere are the usable commands:{commands}")
    terminal()
def run_adventure():

    print("""
    WELCOME! LET'S START THE ADVENTURE
    You are standing outside of your house and you see a man running towards you and asking for urgent shelter.
    Will you provide shelter to him? (Yes / No)
    """)
    ans1 = input(f"game>>")
    if ans1 in answer_yes:
        print("\nAfter some time, the  local Police ask you that whether the thief is in your house or not.")
        print(" Will you say (Yes / No)\n")
        if ans1 == ".":
            terminal()
        ans2 = input(f"game>>")
        if ans2 in answer_yes:
            print("\nYou are an honest person. He was a thief.")
        if ans2 == ".":
            terminal()
        if ans2 in answer_no:
            print('\nYou helped a thief. Now, go to Jail.')
            sleep(1)
            escape = input("\nWould you like to escape? Yes/No.")
            sleep(2)
            if escape in answer_yes:
                print("You Escaped!")
                sleep(2)
                print("You were caught escaping!")
                print("GAME OVER")
                terminal()
            elif escape in answer_no:
                print("You were stuck in prison!\nGAME OVER")
                terminal()
            else:
                print("You were stuck in prison!\nGAME OVER")
                terminal()
    if ans1 in answer_yes:
        print("\nNow, he is trying to rob you. Will, you stop his plan? (Yes / No)\n")
        ans3 = input("run>>game>>")
        if ans3 == ".":
            terminal()
        if ans3 in answer_yes:
            print("\nCongrats! He was a thief & You helped the police to catch him with your bravery.")
        elif ans3 in answer_no:
            print("\nSorry! You lost all your money! He was a thief & He robbed you. GAME OVER")
            terminal()
