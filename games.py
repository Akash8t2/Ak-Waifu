import random

def get_truth():
    truths = ["What is your biggest fear?", "Who was your first crush?"]
    return random.choice(truths)

def get_dare():
    dares = ["Do 10 push-ups!", "Sing a song loudly!"]
    return random.choice(dares)

def roll_dice():
    return random.randint(1, 6)

def toss_coin():
    return random.choice(["Heads", "Tails"])

def rock_paper_scissors():
    return random.choice(["Rock", "Paper", "Scissors"])