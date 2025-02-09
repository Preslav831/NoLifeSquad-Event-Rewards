import random


#Ideas
# Add method to pick from several rewards listed
# Add staff description in difficulty
# Include player names
# Add method only one place
# Add manual render with set difficulty for method
# separate the Rewards render from difficulty and rewards render
# Make a file with given rewards and player names


# Values are in minutes


class Event:
    def __init__(self, event_name,):
        self.event_name = event_name


# class Difficulty(Event):
#     def __init__(self, difficulty, event_name):
#         self.difficulty = difficulty
#         super().__init__(event_name)
#
#
#     def pick_difficulty(self, minutes):
#         if minutes <= 5:
#             self.difficulty = "easy"
#
#         elif minutes <= 10:
#             self.difficulty = "medium"
#
#         else:
#             self.difficulty = "hard"
#
#         return f"Event {self.event_name.upper()} is flagged as {self.difficulty.upper()}."


class RenderRewards(Event):
    def __init__(self, first_place, second_place, third_place,difficulty, event_name):
        self.first_place = first_place
        self.second_place = second_place
        self.third_place = third_place
        self.difficulty = difficulty
        super().__init__(event_name)

    def pick_difficulty(self, minutes):
        if minutes <= 5:
            self.difficulty = "easy"

        elif minutes <= 10:
            self.difficulty = "medium"

        else:
            self.difficulty = "hard"

        return f"Event {self.event_name.upper()} is flagged as {self.difficulty.upper()}."

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



legendary_rewards = ["Miner Minion", "General 7d", "God Crate Key", "Tier III Flare", "Admiral Rank Седмица", "7 Extra mod"]
rare_rewards = ["2x Ultra Keys", "2x Tag Keys", "3x Tag Keys", "Collector Minion", "Pathfinder 7d", "Stargater 7d"]
uncommon_rewards = ["Explorer 7d", "5x Boss Reward Key", "5x Vote Key", "100,000 XP", "Tier III Mod Key", "Chunk Loader 1w"]
common_rewards = ["1500 MobCoins", "1000 Сиренца", "2500 Сиренца"] # taken out 500 cheese and Totem of Undying  and Amulet


event_name = input()
input_minutes = int(input())
first_place_var = ""
second_place_var = ""
third_place_var = ""
difficulty_var = ""


render_rewards_object = RenderRewards(first_place_var,second_place_var,third_place_var, difficulty_var, event_name)
print(render_rewards_object.pick_difficulty(input_minutes))
print(render_rewards_object.render())
print(render_rewards_object.print_rendered())


# obj1 = Event("Maze")
# define_param_child_difficulty = Difficulty("","Maze")
# print(define_param_child_difficulty.pick_difficulty(input_minutes))
# define_param_child_render_rewards = RenderRewards(first_place_var,second_place_var,third_place_var,difficulty, event_name)
# print(define_param_child_render_rewards.print_rendered())
#
#
#
#
# print(define_param_child_difficulty.pick_difficulty(input_minutes))







