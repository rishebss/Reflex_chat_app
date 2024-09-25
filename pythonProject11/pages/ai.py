# import google.generativeai as genai
#
#
# OPENAI_MODEL="gpt-4o-mini"
# OPENAI_API_KEY="AIzaSyAcr5MCA00fk4QX7QxyZnWml2jyeQ6HToU"
# def get_client():
#     return OpenAI(api_key=OPENAI_API_KEY)
#
# # client = OpenAI()
# def get_llm_response(gpt_messages):
#     client=get_client()
#     completion = client.chat.completions.create(
#       model=OPENAI_MODEL,
#       messages=gpt_messages
#     )
#     return completion.choices[0].message.content


import google.generativeai as genai

# Configure the GenAI API key (replace with your actual key)
genai.configure(api_key="your_api_key")

def get_llm_response(gpt_messages):
    # Convert the messages to a single prompt format for GenAI
    # Combine messages with role and content into a readable format for GenAI
    prompt = "\n".join([f"{msg['role']}: {msg['message']}" for msg in gpt_messages])

    # Define generation configuration
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }

    # Initialize the model
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
    )

    # Start a chat session (no history needed as it is incorporated in the prompt)
    chat_session = model.start_chat(
        history=[]  # Empty history for now
    )

    # Send the formatted prompt and get the response
    response = chat_session.send_message(prompt)

    # Return the AI-generated text
    return response.text

# Example usage with your get_gpt_messages function
gpt_messages = [
    {"role": "system", "message": "You are great."},
    {"role": "user", "message": "Hello, how can I assist you today?"}
]

response_text = get_llm_response(gpt_messages)



