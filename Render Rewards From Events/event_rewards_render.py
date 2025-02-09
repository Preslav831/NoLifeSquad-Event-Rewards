import random


#Ideas
# Include player names
# Make a file with given rewards and player names


class Event:
    def __init__(self, event_name):
        self.event_name = event_name


class Rewards(Event):
    def __init__(self):
        self.difficulty = ""
        self.first_place = ""
        self.second_place = ""
        self.third_place = ""
        super().__init__(event_name)


    def pick_difficulty(self, minutes):
        if minutes <= 5:
            self.difficulty = "easy"

        elif minutes <= 10:
            self.difficulty = "medium"

        else:
            self.difficulty = "hard"

        return f"Event {self.event_name.upper()} is on {self.difficulty.upper()} difficulty. The event lasted {minutes} minutes"

    def difficulty_setter(self, value):
        self.difficulty = value
        return ""

    def render(self):
        if self.difficulty == "hard":
            self.first_place  = random.choice(legendary_rewards)
            self.second_place = random.choice(rare_rewards)
            self.third_place = random.choice(uncommon_rewards)

        elif self.difficulty == "medium":
            self.first_place  = random.choice(rare_rewards)
            self.second_place = random.choice(uncommon_rewards)
            self.third_place = random.choice(common_rewards)

        elif self.difficulty == "easy":
            self.first_place  = random.choice(uncommon_rewards)
            self.second_place = random.choice(common_rewards)
            self.third_place = random.choice(common_rewards)
        # NEEDS REWORK
        return ""


    def print_rendered(self):
        return f"First Place: {self.first_place}\nSecond place: {self.second_place}\nThird place: {self.third_place}"


    def pick_one_winner(self):
        if self.difficulty == "hard":
            self.first_place = random.choice(legendary_rewards)

        else:
            self.first_place = random.choice(rare_rewards)

        return f"One Place: {self.first_place}"




legendary_rewards = ["Miner Minion", "General 7d", "God Crate Key", "Tier III Flare", "Admiral Rank 7d", "7 Extra mod"]
rare_rewards = ["Tier II Flare", "Tier III Mod Key", "Collector Minion", "Pathfinder 7d", "Stargater 7d"]
uncommon_rewards = ["Explorer 7d", "5x Boss Reward Key", "6x Vote Key", "130,000 XP", "Tier II Mod Key", "Chunk Loader 1w"]
common_rewards = ["3x Boss Reward Key", "3x Ultra Keys", "2000 Сиренца", "100,000 XP"] # taken out 500 cheese and Totem of Undying  and Amulet




# classes instances

event_name = input("Enter event name: ")
input_minutes = int(input("Enter how much minutes the event lasted: "))
only_one_place_condition = input("Input y or n for one winner: ")
manual_difficulty = input("If you want to set manual difficulty type the difficulty, if not leave blank: ")
print("")



event_instance = Event(event_name)
rewards_instance = Rewards()

if manual_difficulty == "hard" or  manual_difficulty == "medium" or  manual_difficulty == "easy":
    print(rewards_instance.difficulty_setter(manual_difficulty))
else:
    print(rewards_instance.pick_difficulty(input_minutes))

if only_one_place_condition == "y":
    print(rewards_instance.pick_one_winner())

else:
    print(rewards_instance.render())
    print(rewards_instance.print_rendered())