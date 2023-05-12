def solutionA(lines):
  total_calories = 0
  top_calories = 0
  mid_calories = 0
  bot_calories = 0
  calories = 0
  for line in lines:
    if not line:
         calories = 0
    else:
        calories += int(line)

    if calories > top_calories:
        bot_calories = mid_calories
        mid_calories = top_calories
        top_calories = calories 
    total_calories = top_calories + mid_calories + bot_calories
  return total_calories


def solutionB(lines):
  # TODO: replace with code solving the problem
  return -2 # Dummy result, deliberately wrong


# Helper function for loading the problem data
def load_data(fileName):
  with open(fileName, "r") as input_data:
    lines = input_data.readlines()
  for i in range(len(lines)):
    lines[i] = lines[i].strip()
  return lines


if __name__ == "__main__":
  input_file_name = "dummy-input.txt"
  # TODO: Uncomment line below to use real input
  # input_file_name = "input.txt" 
  
  print("Loading data")
  lines = load_data(input_file_name)
  
  resultA = solutionA(lines)
  print(f"Solution for part A: {resultA}")

  resultB = solutionB(lines)
  print(f"Solution for part B: {resultB}")