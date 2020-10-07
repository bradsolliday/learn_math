import os

MIN_SCORE = 0.0
PROFILES_DIR = "saved_profiles"

class Profile:

    # Loads and returns existing profile of string profile_name
    def __init__(self, profile_name):
        self.profile_name = profile_name

        with open(os.path.join(PROFILES_DIR, profile_name + ".txt"), "r") as f:
            addition_data, multiplication_data = f.read().split("|")[1::2]

        def extract_data(data):
            output = [[0] * 12] * 12
            #for operand1, operand2, score in data.split("\n")[0:-1]:
            for triple in data.split("\n")[0:-1]:
                operand1, operand2, score = triple.split(",")
                output[int(operand1)][int(operand2)] = float(score)

        self.addition = extract_data(addition_data)
        self.multiplication = extract_data(multiplication_data)



    # Creates a new profile with name profile_name
    @classmethod
    def new(cls, profile_name):
        obj = cls.__new__(cls)
        obj.profile_name = os.path.split(profile_name)[1]
        obj.addition = [[MIN_SCORE for oper2 in range(1, 13)]
                            for oper1 in range(1, 13)]
        obj.multiplication = obj.addition.copy()
        return obj

    # Saves profile to "saved_profiles/[profile_name]"
    def save(self):
        relative_path = os.path.join(PROFILES_DIR, self.profile_name + ".txt")
        if not os.path.exists(os.path.dirname(relative_path)):
            os.makedirs(os.path.dirname(relative_path))

        def write_scores(file, score_list):
            for operand1, op2_list in enumerate(score_list):
                for operand2, score in enumerate(op2_list):
                    file.write(f"{operand1},{operand2},{score}\n")

        with open(relative_path, "w") as f:
            f.write("Addition Scores (operand1,operand2,score)\n|")
            write_scores(f, self.addition)
            f.write("|multiplication Scores (operand1,operand2,score)\n|")
            write_scores(f, self.multiplication)

def profile_list():
    if os.path.isdir(PROFILES_DIR):
        return [os.path.splitext(f)[0] for f in os.listdir(PROFILES_DIR)
                    if os.path.isfile(os.path.join(PROFILES_DIR, f))]
    return []


# Creates a new save file with name new_profile_name
# precondition: new_profile_name is not the empty string
def create_profile(new_profile_name):
    new_profile = Profile.new(new_profile_name)
    new_profile.save()

def delete_profile(profile_name):
    os.remove(os.path.join(PROFILES_DIR, profile_name + ".txt"))

