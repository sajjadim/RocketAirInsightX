import requests
import json
url = 'https://api.openai.com/v1/completions'
global prompt
fueltypes = ['Kerosene','Cryogenic','Solid','Hypergolic','liquid']
def ChatEnchancementSuggestion(template,arguments,predictionResult):
    if template == 0:
        prompt = (f''' The rocket's maximum altitude is {arguments[2]} km, with a total fuel mass of {arguments[3]} kg 
        and Total Propellant Mass of {arguments[1]} kg. The fuel type is {fueltypes[arguments[0]]} and  The rocket is launched from {arguments[4]}.
           Unfortunately, the rocket produces {predictionResult} of pollution during each launch. . Can you please provide suggestions on how to
        improve the rocket's performance and efficiency while also reducing pollution? I am looking for ways to minimize the
        environmental impact of the rocket's launch. ''')
    

    headers = {'Authorization': 'Bearer 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'}
    payload = {"model": "text-davinci-003", "prompt": prompt, "temperature": 0, "max_tokens": 700}
    response = requests.post(url, headers=headers, json=payload)
    
    # print(response.json()['choices'][0])
    # f = open("res.txt","a")
    # f.write(response.text)
    return response.json()

def ChatWritingOverview(template,arguments):
    if template == 0:
        prompt = (f''' I have some information about a rocket that I would like to share with you. The rocket uses {fueltypes[arguments[0]]} as its fuel,
         with a total fuel mass of {arguments[3]}. Its maximum altitude is {arguments[2]},
          and its Total Propellant Mass is {arguments[1]}.
            can you write an overview about this rocket? ''')
    elif template == 1:
        prompt = (f''' Hello, I am interested in learning more about a specific rocket. Can you please provide me with an overview of the rocket's design, capabilities, and any notable achievements? The name of the rocket I am interested in is {arguments[0]}. Thank you! ''')


    headers = {'Authorization': 'Bearer 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'}
    payload = {"model": "text-davinci-003", "prompt": prompt, "temperature": 0, "max_tokens": 5}
    response = requests.post(url, headers=headers, json=payload)
    
    print(response.json()['choices'][0])
    f = open("res.txt","a")
    f.write(response.text)
    return response.text




