import json
from difflib import get_close_match

def get_knowledge_base (file_path:str)->dict:
  with open (file_path, 'r') as file:
   data:json. load(file)
  return data

def save_knowledge_base (file_path : str,data:dict):
  with open (file_path,'w')as file:
    json. dump (data,file, indent=2)

def find_best_match (user_question: str ,question: list[str])->str |None:
  matches: list = get_close_matches (user_question, question = 1 , cutoff = 0.6)

def get_answer_for_question (question: str knowledge_base.dict)-> str |None:

  for q in knowledge_base ["question"]

  if q["question"] = question :
    return q["answer"]

def chat_bot ():
  knowledge_base:dict=knowledge_base (knowledge_base.json)

 while True:
   user_input: str = input ('> ')

 if user_input.lower()='quit':
   break

best_match : str|None =find_best_match (user_input q["question"] for q in knowledge_base ["question"]
if best_match:
       answer: str = get_answer_for_question(best_match, knowledge_base)
     print(f'Bot:{answer}')
else:
    print(f'Bot:I don\'t know the answer.can you teach me?'):
       new_answer:str=input('Type the answer or "skip" to skip:')



if new_answer.lower():!= 'skip':
  knowledge_base["questions"].append ({"question":user_input, "answer": new_answer})
save_knowledge_base('knowledge_base.json',knowledge_base)
   print(f'Bot:Thank you for teaching me!')
                    
                    
if name_='_main_':
  chatbot()



