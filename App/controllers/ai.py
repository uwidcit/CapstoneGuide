import os
import openai
from App.controllers import add_evaluation, get_last_proposal, get_lecturer

openai.api_key = "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"


def set_struct(sentence):
    j = 0
    rubric = [0, 0, 0, 0, 0, 0]
    for i in range(len(sentence)):
        if sentence[i] == ":":
            rubric[j] = int(sentence[i + 2])
            j += 1
            if j >= 6:
                break
            
    add_evaluation(sentence, rubric[0], rubric[1], rubric[2], rubric[3], rubric[4], rubric[5], get_last_proposal().id,101)
    return sentence

#openai.Completion.create(model="ada", prompt=query)
def get_ai_evaluation(proposal_nm, problem_desc, audience, solution_desc, approach, num_members, functionalities, technologies, goals, benifit, sustain, notes):
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[
        {"role": "system", "content": "Evaluate the following capstone project proposal based on the following"
                                      "Rubric: novelty, relevance, feasibility, impact, sustainability, use of technology"
                                      "Also give overall comments"
                                      "In summary grade the proposal on each of the points in the rubric 0-9"
                                      "If you cannot understand, assign a score of 0 to the points in the rubric"},
        {"role": "user", "content": "Proposal Name: " + proposal_nm + "\nProblem Description: " + problem_desc + audience + 
                                    "\nSolution Description: " + solution_desc + approach + "\nNumber of Members: " + num_members
                                    + "\nRequirements: "+ functionalities + "\nTechnical Skills: "+ technologies +
                                    "\nGoals: "+ goals + benifit + "\nSustainability: "+ sustain + "\nAdditional Information: "+ notes}])
    
    comment = str(response.choices[0].message.content).replace("\n", "")
    print(comment)
    comment = comment.replace("/9", " ")
    # f = open("App/tests/ai_dictionary.jsonl", "a")
    # f.write('{"prompt": "' + proposal_nm + '", "completion": "' + comment)
    # f.close()
    set_struct(comment)
