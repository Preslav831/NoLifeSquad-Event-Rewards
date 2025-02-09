import random

class Event:
    def __init__(self, event_name,):
        self.event_name = event_name


class Difficulty(Event):
    def __init__(self, difficulty, event_name):
        self.__difficulty = difficulty
        super().__init__(event_name)


    def pick_difficulty(self, minutes):
        if minutes <= 5:
            self.__difficulty = "easy"

        elif minutes <= 10:
            self.__difficulty = "medium"

        else:
            self.__difficulty = "hard"

        return f"Event {self.event_name.upper()} is flagged as {self.__difficulty.upper()}."

#
# class RenderRewards(Difficulty):
#     def __init__(self, first_place, second_place, third_place, event_name, difficulty):
#         self.first_place = first_place
#         self.second_place = second_place
#         self.third_place = third_place
#         super().__init__(event_name,difficulty)
#
#     def render(self):
#         if self.__difficulty == "hard":
#             self.first_place  = random.choice(legendary_rewards)
#             self.second_place = random.choice(rare_rewards)
#             self.third_place = random.choice(uncommon_rewards)
#
#         elif self.__difficulty == "medium":
#             self.first_place  = random.choice(rare_rewards)
#             self.second_place = random.choice(uncommon_rewards)
#             self.third_place = random.choice(common_rewards)
#
#         elif self.__difficulty == "easy":
#             self.first_place  = random.choice(uncommon_rewards)
#             self.second_place = random.choice(common_rewards)
#             self.third_place = random.choice(common_rewards)
#         # NEEDS REWORK
#         return ""
#
#
#     def print_rendered(self):
#         return f"First Place: {self.first_place}\nSecond place: {self.second_place}\nThird place: {self.third_place}"
#
#
#
# legendary_rewards = ["Miner Minion", "General 7d", "God Crate Key", "Tier III Flare", "Admiral Rank Седмица", "7 Extra mod"]
# rare_rewards = ["2x Ultra Keys", "2x Tag Keys", "3x Tag Keys", "Collector Minion", "Pathfinder 7d", "Stargater 7d"]
# uncommon_rewards = ["Explorer 7d", "5x Boss Reward Key", "5x Vote Key", "100,000 XP", "Tier III Mod Key", "Chunk Loader 1w"]
# common_rewards = ["1500 MobCoins", "1000 Сиренца", "2500 Сиренца"] # taken out 500 cheese and Totem of Undying  and Amulet
#
#





# event_name = input()
# input_minutes = int(input())
# first_place_var = ""
# second_place_var = ""
# third_place_var = ""
# difficulty_var = ""
#
# event_object = Event(event_name)
# render_rewards_object = RenderRewards(first_place_var,second_place_var,third_place_var, difficulty_var,e)
# print(render_rewards_object.pick_difficulty(input_minutes))
# print(render_rewards_object.render())
# print(render_rewards_object.print_rendered())