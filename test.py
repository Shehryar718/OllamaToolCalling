import ollama
from tools import functions
from utils import register_function
import argparse

def main(question: str, verbose: bool):
    client = ollama.Client()
    model = "llama3.2"

    # Register all functions dynamically
    tools = [register_function(name, data['description'], data['params']) for name, data in functions.items()]

    # Initialize conversation with the user query
    messages = [{'role': 'user', 'content': question}]

    # First API call: Send the query and function descriptions to the model
    response = client.chat(
        model=model,
        messages=messages,
        tools=tools,
    )

    # Add the model's response to the conversation history
    messages.append(response['message'])

    # Check if the model used a function
    if not response['message'].get('tool_calls'):
        print("The model didn't use a function. Its response was:")
        print(response['message']['content'])

    # Process any function calls made by the model
    if response['message'].get('tool_calls'):
        for tool in response['message']['tool_calls']:
            function_name = tool['function']['name']
            function_to_call = functions[function_name]['func']
            function_args = tool['function']['arguments']
            function_response = function_to_call(**function_args)

            # Add the function response to the conversation
            messages.append({'role': 'tool', 'content': function_response})

    # Second API call: Get the final response from the model
    final_response = client.chat(model=model, messages=messages)
    print(final_response['message']['content'])

    # If verbose flag is set, print final response and messages
    if verbose:
        print("\nVerbose Output:")
        print("Final Response:", final_response)
        print("Messages:", messages)

    return final_response, messages

if __name__ == "__main__":
    # Argument parser to handle command line inputs
    parser = argparse.ArgumentParser(description='Ask a question to the model and get a response.')
    parser.add_argument(
        'question', 
        nargs='?', 
        default='What is 42+4123?', 
        help='The question to ask the model. If not provided, defaults to "What is 42+4123?".'
    )
    parser.add_argument(
        '-v',
        '--verbose',
        action='store_true', 
        help='Enable verbose mode to print the final response and messages.'
    )
    
    args = parser.parse_args()

    # Run main function with parsed arguments
    final_response, messages = main(args.question, args.verbose)
