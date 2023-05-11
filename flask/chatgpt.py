import os
import openai
# define a function to get the response from chatgpt 3.5 turbo using chatgpt api.
def chatgpt(messages):
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",messages=messages)
    text=completion.choices[0].message.content
    return(text)
