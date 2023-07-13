import random

easter_eggs = {'meow': 'Woof-woof'}

def askForInput():
    user_input = input('HUMAN => ')
    return user_input

def reply(answer):
    print('CAT => {0}.'.format(answer))
    analyse(askForInput())

def buildReply():
    answer = 'Meow'
    meow_count = random.randrange(1, 9)
    i = 0
    while i <= meow_count:
        comma_rate = random.randrange(1, 5)
        if comma_rate == 1 and i != meow_count:
            answer += ','
        answer += ' meow'
        i+=1
    reply(answer)

def analyse(user_input):
    if user_input.lower() in easter_eggs:
        reply(easter_eggs[user_input.lower()])
    else:
        buildReply()

print('[ Meow v1.0.0 ]\n\nAsk something to the cat:')
analyse(askForInput())