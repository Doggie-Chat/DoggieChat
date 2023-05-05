import os
import openai
def chatgpt(messages):
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",messages=messages)
    text=completion.choices[0].message.content
    return(text)
