"""
Authors: Tien Nguyen, Meghana Ravi, Nicholas Bottomley

Create a markov model from a provided text document.
"""
import numpy as np

def nth_states(states: list, order: int) -> list:
    """
    Takes in list of first order states and converts them into
    a list of nth order states
    
    Args:
        states (list): list of first order states
        order (int): desired order of states output
    
    Returns:
        list: list of tuples where each tuple length, n, is a nth order state
    """
    # TODO implement this func
    nth_order_states = []
    for ind, state in enumerate(states):
        # Separate case for first order to generate single element tuple
        if order != 1:
            nth_order_states.append(tuple(states[ind:ind+order]))

        # Generate tuple states size = order
        else:
            nth_order_states.append((states[ind],))
        if ind + order == len(states):
            break
    
    return nth_order_states

def build_markov_model(markov_model: dict, new_text: str, order: int = 1) -> dict:
    '''
    Function to build or add to a 1st order Markov model given a string of text
    We will store the markov model as a dictionary of dictionaries
    The key in the outer dictionary represents the current state
    and the inner dictionary represents the next state with their contents containing
    the transition probabilities.
    Note: This would be easier to read if we were to build a class representation
           of the model rather than a dictionary of dictionaries, but for simplicitiy
           our implementation will just use this structure.
    
    Args: 
        markov_model (dict of dicts): a dictionary of word:(next_word:frequency pairs)
        new_text (str): a string to build or add to the moarkov_model

    Returns:
        markov_model (dict of dicts): an updated markov_model
        
    Pseudocode:
        Add artificial states for start and end
        For each word in text:
            Increment markov_model[word][next_word]
        
    '''
    # TODO: file implementation needs read-in func

    # Split string of words into list of states
    states_string = "*S* " * order + new_text
    states = states_string.split()

    # Create list of nth order states from states list
    states = nth_states(states, order)

    # Loop through states until all states viewed
    current_state = states[0]
    
    for ind, next_state in enumerate(states):
        if ind == 0:
            continue
        # Check if current state in markov dict else add
        if current_state not in markov_model:
            markov_model[current_state] = {}
        
        # Get next string from next_state tuple
        next_word = next_state[-1]

        # Check if next word in current state transition dict 
        # Add 1 to frequency if is else create transition w/ freq 1
        if next_word in markov_model[current_state]:
            markov_model[current_state][next_word] += 1
        else:
            markov_model[current_state][next_word] = 1

        if ind == len(states) - 1:
            if next_state not in markov_model:
                markov_model[next_state] = {}
            markov_model[next_state]["*E*"] = 1

        current_state = next_state

    return markov_model


def get_next_word(current_word, markov_model, seed=42):
    '''
    Function to randomly move a valid next state given a markov model
    and a current state (word)
    
    Args: 
        current_word (tuple): a word that exists in our model
        markov_model (dict of dicts): a dictionary of word:(next_word:frequency pairs)

    Returns:
        next_word (str): a randomly selected next word based on transition probabilies
        
    Pseudocode:
        Calculate transition probilities for all next states from a given state (counts/sum)
        Randomly draw from these to generate the next state
        
    '''
    # Define current word dictionary of transitions from markov_model
    states = markov_model[current_word]

    # Count total transition frequency
    total_transitions = 0
    for transition in states:
        total_transitions += states[transition]
    
    # Find transition probability for each possible next state
    transitions = []
    probabilities = []
    for transition in states:
        transitions.append(transition)
        probabilities.append(states[transition] / total_transitions)

    # TODO: Remove debug logic
    # print(sum(probabilities))

    return np.random.choice(a=transitions, p=probabilities)

def generate_random_text(markov_model, seed=42):
    '''
    Function to generate text given a markov model
    
    Args: 
        markov_model (dict of dicts): a dictionary of word:(next_word:frequency pairs)

    Returns:
        sentence (str): a randomly generated sequence given the model
        
    Pseudocode:
        Initialize sentence at start state
        Until End State:
            append get_next_word(current_word, markov_model)
        Return sentence
        
    '''
    # Set current_state to start state
    current_state = list(markov_model.keys())[0]

    # Initialize next_word variable
    next_word = None
    end_word = "*E*"
    sentence = ""

    # Loop until transition to end state
    while True:
        next_word = get_next_word(current_state, markov_model)

        # Break loop if next_word is end state
        if next_word == end_word:
            break

        # Concatenate sentence with next_word
        sentence += f"{next_word} "

        # Current is ("*S*", "*S*") next is "string" -> ("*S*", "string")
        # Update current state
        current_state_update = []
        for ind, word in enumerate(current_state):
            if ind + 1 == len(current_state):
                current_state_update.append(next_word)
                current_state = tuple(current_state_update)
                break
            current_state_update.append(current_state[ind + 1])
    

    return sentence

if __name__ == "__main__":
    text = "one fish two fish red fish blue fish"
    n = 3
    mark = build_markov_model({}, text, order=n)
    print(mark)
    print(generate_random_text(mark))


