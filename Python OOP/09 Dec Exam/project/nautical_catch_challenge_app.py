from project.divers.base_diver import BaseDiver
from project.divers.free_diver import FreeDiver
from project.divers.scuba_diver import ScubaDiver
from project.fish.base_fish import BaseFish
from project.fish.deep_sea_fish import DeepSeaFish
from project.fish.predatory_fish import PredatoryFish


class NauticalCatchChallengeApp:
    VALID_DIVERS = {"FreeDiver": FreeDiver, "ScubaDiver": ScubaDiver}
    VALID_FISH = {"PredatoryFish": PredatoryFish, "DeepSeaFish": DeepSeaFish}

    def __init__(self):
        self.divers: list[BaseDiver] = []
        self.fish_list: list[BaseFish] = []

    def dive_into_competition(self, diver_type: str, diver_name: str):
        already_diver = next((d for d in self.divers if d.name == diver_name), None)

        if diver_type not in self.VALID_DIVERS.keys():
            return f"{diver_type} is not allowed in our competition."
        if already_diver:
            return f"{diver_name} is already a participant."
        self.divers.append(self.VALID_DIVERS[diver_type](diver_name))
        return f"{diver_name} is successfully registered for the competition as a {diver_type}."

    def swim_into_competition(self,fish_type: str, fish_name: str, points: float):
        already_fish = next((f for f in self.fish_list if f.name == fish_name), None)

        if fish_type not in self.VALID_FISH.keys():
            return f"{fish_type} is forbidden for chasing in our competition."
        if already_fish:
            return f"{fish_name} is already permitted."
        self.fish_list.append(self.VALID_FISH[fish_type](fish_name, points))
        return f"{fish_name} is allowed for chasing as a {fish_type}."

    def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool):
        diver = next((d for d in self.divers if d.name == diver_name), None)
        fish = next((f for f in self.fish_list if f.name == fish_name), None)
        if not diver:
            return f"{diver_name} is not registered for the competition."
        if not fish:
            return f"The {fish_name} is not allowed to be caught in this competition."
        if diver.has_health_issue:
            return f"{diver_name} will not be allowed to dive, due to health issues."

        has_missed = False
        has_hit = False
        if diver.oxygen_level < fish.time_to_catch:
            diver.miss(fish.time_to_catch)
            has_missed = True
        elif diver.oxygen_level == fish.time_to_catch:
            if is_lucky:
                diver.hit(fish)
                has_hit = True
            else:
                diver.miss(fish.time_to_catch)
                has_missed = True
        else:
            diver.hit(fish)
            has_hit = True
        if diver.oxygen_level <= 0:
            diver.update_health_status()
        if has_hit:
            return f"{diver_name} hits a {fish.points}pt. {fish_name}."
        if has_missed:
            return f"{diver_name} missed a good {fish_name}."

    def health_recovery(self):
        counter = 0
        for d in self.divers:
            if d.has_health_issue:
                d.update_health_status()
                d.renew_oxy()
                counter += 1
        return f"Divers recovered: {counter}"

    def diver_catch_report(self, diver_name: str):
        result = [f'**{diver_name} Catch Report**']
        diver = next((d for d in self.divers if d.name == diver_name), None)
        for f in diver.catch:
            result.append(f.fish_details())
        return '\n'.join(result)

    def competition_statistics(self):
        divers_issues = [d for d in self.divers if not d.has_health_issue]
        sorted_divers = sorted(divers_issues, key=lambda x: (-x.competition_points, -len(x.catch), x.name))
        result = ["**Nautical Catch Challenge Statistics**"]
        for d in sorted_divers:
            result.append(d.__str__())
        return '\n'.join(result)
