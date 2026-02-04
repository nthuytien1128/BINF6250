# Introduction
This project implements an n-th order Markov text generator that learns word-level transition probabilities from an input text document and uses them to generate new, probabilistically similar text.

# Pseudocode
```
FUNCTION: build_markov_model(markov_model:dict, new_text:str) -> dict:
INPUT:
    markov_model : dictionary mapping word → dictionary of next_word → count
    new_text     : string of space-separated words

OUTPUT:
    markov_model : updated Markov model with transition counts

ALGORITHM:
    1. Split new_text into a list of words by " "
    2. Add artificial start and end tokens:
           augmented_states ← ["*S*"] + words + ["*E*"]

    3. For each index i from 0 to length(augmented_states) − #order:
           current_state ← augmented_states[i]
           next_state ← augmented_states[i + 1]

           If current_state is not in markov_model:
               initialize markov_model[current_state] as an empty dictionary

           If next_state is not in markov_model[current_state]:
               initialize markov_model[current_state][next_state] to 0

           Increment markov_model[current_state][next_state] by 1

    4. Return the updated markov_model
    
    
    
FUNCTION: def build_markov_model(markov_model: dict, text: str, order: int) -> dict:   
INPUT:
    markov_model : dictionary mapping n-gram tuples → dictionary of next_word → count
    text         : input string of space-separated words
    order        : integer specifying the Markov order (n)

OUTPUT:
    markov_model : updated Markov model with transition counts

ALGORITHM:
    1. Split the input text into a list of words by " "

    2. Create a list of states by:
           - Prepending 'order' number of start tokens "*S*"
           - Appending a single end token "*E*"
       states ← ["*S*"] * order + words + ["*E*"]

    3. For each index i from 0 to length(states) − order − 1:
           current_state ← tuple of states from i to i + order − 1
           next_state ← states[i + order]

           If current_state is not in markov_model:
               initialize markov_model[current_state] as an empty dictionary

           If next_state is not in markov_model[current_state]:
               initialize markov_model[current_state][next_state] to 0

           Increment markov_model[current_state][next_state] by 1

    4. Return the updated markov_model
    
    
    
FUNCTION: get_next_word(current_word, markov_model, seed=42)
INPUT:
    current_word : tuple representing the current n-gram state
    markov_model : dictionary mapping state → dictionary of next_word → count

OUTPUT:
    next_word : randomly selected next word based on transition probabilities

ALGORITHM:
    1. If current_word is not a key in markov_model:
           return end token "*E*"

    2. Retrieve the dictionary of next-word counts for current_word

    3. Convert the counts to a numeric array

    4. Compute the total number of transitions

    5. If total is less than or equal to zero:
           return end token "*E*"

    6. Compute transition probabilities by dividing each count by the total

    7. Randomly select and return a next word using the computed probabilities
    
    

FUNCTION: generate_random_text(markov_model, seed=42)

INPUT:
    markov_model : dictionary mapping n-gram states → transition dictionaries
    seed         : integer used to seed the random number generator

OUTPUT:
    sentence : a randomly generated sequence of words

ALGORITHM:
    1. Seed the random number generator using the provided seed

    2. Define start token "*S*" and end token "*E*"

    3. Determine the Markov order by inspecting the length of any state in the model

    4. Initialize the current state as a tuple containing 'order' start tokens

    5. Initialize an empty list to store generated words

    6. While True:
           a. Select the next word using get_next_word(current_state, markov_model)

           b. If the next word is the end token:
                  break the loop

           c. Append the next word to the word list

           d. Update the current state by removing the oldest word
              and appending the newly generated word

    7. Join the generated words into a single string and return it
```

# Successes
- Understood the concept of Markov model
- Upgraded to the nth order
- Able to generate random text that is similar to the input file

# Struggles
- Struggled to find a way to generate more complex text file.
- Simplified the function using available functions/modules.
- Transforming data from dict to tuple, converting data in general between steps.

# Personal Reflections
## Tien Nguyen (Group Leader)
Working on this project helped me better understand the Markov model and how to apply it in practice. I gained insight into the importance of clean iteration logic, reproducibility through random seeding, and defensive handling of edge cases. In addition to the algorithm used in the functions, I also learned about using a .venv virtual environment and why a requirements.txt file is created to manage required modules. Through screen sharing with my teammates, we were able to collaboratively run, debug, and understand each function line by line using VS Code, which strengthened both my technical skills and my ability to communicate and troubleshoot code effectively.

## Nicholas Bottomley
This project was my first real exposure to markov models, so it was very educational to take the time to work through it. Although the concepts make sense and seem relatively straightforward, the implementation took a little longer to get down. It was very rewarding to see the generate_random_text() outputs after building the model and developing logic for output. I struggled a little with understanding and developing logic from reading in and generating one line of text to reading in and generating paragraphs as well, but was able to understand it thanks to help from my groupmates. Overall, this was a great new experience that I believe has greatly improved the depth of my algorithmic ability.

## Meghana Ravi
Working on this assignment helped me understand Markov Models better and reinforced the concepts we discussed in class. Starting with a single line of text and first-order models was especially helpful because it gave us a solid foundation. As we moved on to nth order models and using entire files to build the model, the complexity increased significantly and I found it a little challenging, but having base code from the first-order model and adding logic as the concepts became more complex made the process less overwhelming than if we started with nth order models or full text files directly. This project has helped me develop a more step-by-step approach to planning which has improved how I work through complex problems.

# Generative AI Appendix
ChatGPT was used to help me understand the usage of NumPy functions, including np.array, for processing and normalizing data in this project.