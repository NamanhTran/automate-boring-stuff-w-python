import os
import random

# Import capitals dictionary data
import capitals

# Max number of quizzes user wants to generate
def MAX_QUIZZES():
    return 35

# Max number of choices for a question
def MAX_CHOICES():
    return 3

def main():
    # If quizzes directory doesn't exist then create
    if not os.path.isdir('./quizzes'):
        os.makedirs('./quizzes')

    # If answers directory doesn't exist then create
    if not os.path.isdir('./answers'):
        os.makedirs('./answers')

    # Change directory to quizzes
    os.chdir('./quizzes')

    # Set data to a variable
    quizData = capitals.capitals

    # Iterate through loop until MAX_QUIZZES amount is reached
    for i in range(MAX_QUIZZES()):
        # Create file name
        fileName = 'quiz' + str(i + 1)

        # Creates/opens the file to write in
        quizFile = open(f'{fileName}.txt', 'w')
        
        # Header of the quiz file
        quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
        quizFile.write((' ' * 20) + f'State Capitals Quiz (Version {i + 1})')
        quizFile.write('\n\n')

        # Get the list of states in the dictionary
        statesList = list(quizData.keys())

        # Shuffle the statesList
        random.shuffle(statesList)

        # Initalize the answerKey dictonary
        answerKey = {}

        # Loops through entire states list and create a question for each
        for num, states in enumerate(statesList):
            # Write the question to the file
            quizFile.write(f"{num + 1}) What is the capital of {states}?\n")

            # Find the answer to the question
            answer = quizData[states]

            # Create 3 choices also containing answer
            choices = createChoices(quizData, answer)

            # Write the choices to the file
            quizFile.write(f"\tA) {choices[0]}\n\tB) {choices[1]}\n\tC) {choices[2]}\n\n")

            # Add answer to the answerKey dictionary
            answerKey[num] = choices.index(answer)

        # Close the quiz file
        quizFile.close()

        # Create answer key file for the current quiz
        createKey(answerKey, i)

# Generates the choices for the quiz's questions
def createChoices(dict, answer):
    # Create a list already containing the answer
    choices = [answer]

    # Get the list of capitials in the quiz data dictonary
    listValue = list(dict.values())

    # Loop through until MAX_CHOICES is reached
    for i in range(MAX_CHOICES() - 1):
        # Randomly choose from the list values
        randomVal = random.choice(listValue)

        # If choices in the list already exist then keep randomizing
        while randomVal == answer or randomVal in choices:
            randomVal = random.choice(listValue)

        # Add choice to the list
        choices.append(randomVal)
    
    # Shuffle the list one more time
    random.shuffle(choices)

    # Return the choices list
    return choices

# Creates answer key for the quizzes
def createKey(answerKey, quizNum):
    # Change directory to the answers directory
    os.chdir('../answers')

    # Create/open the quiz's answer key file
    answerFile = open(f'quiz_answer_{quizNum + 1}.txt\n', 'w')

    # Loops through each key in the answerKey
    for key in answerKey:
        # Convert from asii value
        letterAns = chr(answerKey[key] + 65)

        # Write the answer to the file
        answerFile.write(f'{key + 1}) {letterAns}\n')

    # Closes the answer key file
    answerFile.close()

    # Change the directory back to quizzes
    os.chdir('../quizzes')

if __name__ == "__main__":
    main()