import sys


class game:
    def __init__(self, name="blank", death=0, sword=0):
        self.name = name
        self.deathcount = death
        self.swordcount = sword

    def start(self, name):
        print(
            f"Greetings, {name}, my name is Ishmuth, the King of Goldenpine Nation")
        input("Press Enter\n")
        print("As you have also heard, our nation is currently in great danger.")
        print("The Dragon, which came to our country about an year ago, has best our country with danger")
        input("Press Enter\n")
        while True:
            ready = input(
                f"{name}, are you ready to go on an adventure to save our country? (type Yes, yes, y, or Y to begin): ")
            if ready in ["yes", "Yes", "y", "Y"]:
                break
            else:
                print("Not a valid input. Either type 'yes', 'Yes', 'y', 'Y'")
        GAME.check_yes(ready)

    def check_yes(self, ready):
        self.ready = ready
        if self.ready in ["yes", "Yes", "y", "Y"]:
            print("\ngood, it is this direction")
            input("Press Enter\n")
            print(f"{name} starts to go on an adventure!")
            GAME.space(name)
        else:
            sys.exit("I never assumed that you would make this choice")

    def space(self, name):
        print(f"After walking for some time, {name} arrives at the room.")
        input("Press Enter\n")
        while True:
            move_answer = input(f"what is {name} going to do? ")
            if move_answer.lower() in ["fight", "search", "left", "right", "front", "back", "help"]:
                break
            else:
                print("Not a valid input. Type 'help' for available actions")
        GAME.space_action(name, move_answer)

    def space_action(self, name, action_answer):
        do = action_answer.lower()
        if do == "fight":
            print(f"{name} was killed trying to kill a monster with bear hands")
            input("Press Enter\n")
            GAME.death(name)
        elif do == "right":
            GAME.room(name)
        elif do == "front":
            GAME.boss(name)
        elif do == "back":
            GAME.loser(name)
        elif do == "search":
            print("nothing to search here")
            input("Press Enter\n")
            GAME.space(name)
        elif do == "left":
            GAME.meme(name)
        elif do == "help":
            GAME.help()

    def meme(self, name):
        print("You've been trolled")

    def boss(self, name):
        print(f"{name} meet the boss, ghost of the Goldenpine Nation")
        if self.swordcount == 1:
            print(f"{name} defeated the boss using the secret sword")
            input("Press Enter\n")
            GAME.victory(self.deathcount)
        elif self.swordcount == 0:
            print(f"{name} died instantly by the boss")
            input("Press Enter\n")
            GAME.death(self.deathcount)

    def room(self, name):
        print(f"\n {name} is at a deeper room, where he sees something shine")
        while True:
            move2_answer = input(f"what is {name} going to do? ")
            if move2_answer in ["fight", "search", "left", "right", "front", "back", "help"]:
                break
            else:
                print("Not a valid input. Type 'help' for available actions")
        GAME.action_room(name, move2_answer)

    def action_room(self, name, action_answer2):
        does = action_answer2.lower()
        if does == "fight":
            print(f"{name} was killed trying to kill a wall with bear hands")
            input("Press Enter\n")
            GAME.death(name)
        elif does == "left":
            GAME.space(name)
        elif does == "right":
            print(f"{name} tried to swim on lava")
            input("Press Enter\n")
            GAME.death(self.deathcount)
        elif does == "search":
            self.swordcount = 1
            print(
                f"{name} has found the secret sword! Now head to the boss and defeat him")
            GAME.room(name)
        elif does == "back":
            GAME.back_rooms(name)
        elif does == "help":
            GAME.help_deeper_room()

    def back_rooms(name):
        print(
            f"{name} is sent to the backrooms. He does not know how he would escape....")
        print("to be continued")

    def death(self, name):
        self.deathcount += 1
        if self.deathcount == 1:
            order = "st"
        elif self.deathcount == 2:
            order = "nd"
        elif self.deathcount == 3:
            order = "rd"
        print(f"{name}, the {self.deathcount}{order} adventurer, fought bravely but faced death during his adventure")
        input("Press Enter\n")
        print("I Ishmuth, pray for him")
        input("Press Enter\n")
        GAME.ask_again(self.deathcount)

    def ask_again(self, count):
        while True:
            again_answer = input(f"do you want to try again?")
            if again_answer.lower() in ["yes", "Yes", "y", "Y", "end"]:
                break
            else:
                print(
                    "Not a valid input. Either type 'yes', 'Yes', 'y', 'Y', or end the game by typing'end'")
        if again_answer.lower() in ["yes", "Yes", "y", "Y"]:
            GAME.start(name)
        elif again_answer.lower() in ["end", "no"]:
            GAME.end(count)

    def end(self, count):
        if count == 1:
            time_times = "time"
        else:
            time_times = "times"
        print(f"Well played, you died {count} {time_times}")

    def victory(self, count):
        if count == 1:
            death_deaths = "death"
        else:
            death_deaths = "deaths"
        print(f"congrats! you cleared the game after {count} {death_deaths}")

    def loser(self, name):
        print(
            f"{name} decided to cowardly turn back and return. He was deemed as a loser, forever")
        input("Press Enter\n")
        sys.exit

    def help(self):
        print("You can either choose to fight, search, go left, go right, go front, or go back")
        input("Press Enter\n")
        print("Each commands are the following: fight, search, left, right, front, back")
        input("Press Enter\n")
        print("You will now be directed back to the first room, good luck")
        input("Press Enter\n")
        help_pause = input("Press Any Key\n")
        GAME.space(name)

    def help_deeper_room(self):
        print("You can either choose to fight, search, go left, go right, go front, or go back")
        input("Press Enter\n")
        print("Each commands are the following: fight, search, left, right, front, back")
        input("Press Enter\n")
        print("You will now be directed back to the previous room, good luck")
        input("Press Enter\n")
        help_pause = input("Press Any Key\n")
        GAME.room(name)


GAME = game()
name = input("What is the name of the Adventurer? \n")
GAME.start(name)
