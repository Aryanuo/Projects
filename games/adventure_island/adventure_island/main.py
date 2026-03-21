import sys
import time
import random

# GAME STATE

corruption = 0
will = 5
awareness = 5
fatigue_stage = 0


# UTILITY FUNCTIONS

def slow(text, d=0.02):
    for c in text:
        print(c, end="", flush=True)
        time.sleep(d)
    print()

def pause(t=0.8):
    time.sleep(t)

def transition(text):
    slow("\n" + text)
    pause()

def end_game(msg):
    slow("\n" + msg)
    slow("\nThe forest remains. It always does.")
    sys.exit()


# CONSUMPTION CHECK

def check_consumption():
    global corruption, will, awareness
    if corruption >= 15:
        slow("""
You keep walking.

At some point, the idea of choosing disappears.
Your body moves without asking you.
""")
        end_game("🌑 ENDING: THE FOREST WALKS YOU (Early Consumption) 🌑")


# FOREST VOICE

def forest_whisper():
    if corruption <= 1:
        slow("The forest is quiet.")
    elif corruption <= 3:
        slow("🌫️ 'You’ve walked far enough.'")
    elif corruption <= 5:
        slow("🌫️ 'You don’t need to think so hard.'")
    else:
        slow("🌫️ 'Let me carry you.'")


# DIALOGUE CONDITIONS

def always(): return True
def can_observe(): return awareness >= 2
def can_question(): return awareness >= 4
def can_refuse(): return will >= 4
def can_assert(): return will >= 6 and awareness >= 6

def present_options(options):
    valid = [(k, t) for k, t, c in options if c()]
    if not valid:
        slow("You cannot find the right words.")
        return None
    for k, t in valid:
        print(f"{k}. {t}")
    return input("> ")


# FATIGUE

def fatigue_check():
    global will, fatigue_stage
    fatigue_stage += 1

    if fatigue_stage == 1:
        slow("Your steps feel heavier than before.")
    elif fatigue_stage == 2:
        slow("Each step now requires intention.")
    elif fatigue_stage == 3:
        slow("Stopping sounds reasonable. Dangerous — but reasonable.")
    else:
        slow("Walking happens without thought.")

    will = max(0, will - 1)
    forest_whisper()
    check_consumption()


# JOURNEY

def long_walk():
    global awareness
    slow("""
You walk.

The forest subtly rearranges itself.
Time stretches.
""")
    awareness += 1

# SCENES

def lost_clearing():
    global awareness, corruption, will
    slow("""
The trees part suddenly.

A clearing.
Open sky.
No wind.

You are certain you have been here before.
""")

    choice = present_options([
        ("1", "Mark the ground", can_observe),
        ("2", "Walk straight ahead", always),
        ("3", "Sit and think", can_refuse)
    ])

    if choice == "1":
        awareness += 1
        slow("The mark fades as soon as you turn away.")
    elif choice == "2":
        corruption += 1
        slow("The clearing appears again behind you.")
    elif choice == "3":
        corruption += 1
        will -= 1
        slow("Thoughte forest grows patient.")

    check_consumption()

def wounded_beast():
    global corruption, awareness, will
    slow("""
A wounded beast blocks the path.
Its eye follows you.
""")

    choice = present_options([
        ("1", "Touch the wound", always),
        ("2", "Observe", can_observe),
        ("3", "End its suffering", can_refuse)
    ])

    if choice == "1":
        corruption += 2
        awareness -= 1
        slow("The wound tightens around your fingers.")
    elif choice == "2":
        awareness += 1
        slow("The beast dissolves into roots.")
    elif choice == "3":
        will += 1
        corruption += 1
        slow("The forest recoils.")

    check_consumption()

def watcher_encounter():
    global awareness, will, corruption
    slow("""
Between the trees,
something watches.

It does not hide.
""")

    choice = present_options([
        ("1", "Stare back", can_refuse),
        ("2", "Pretend not to notice", can_observe),
        ("3", "Speak", always)
    ])

    if choice == "1":
        will += 1
        slow("The presence withdraws slightly.")
    elif choice == "2":
        awareness += 1
        slow("You feel yourself being recorded.")
    elif choice == "3":
        corruption += 1
        slow("Your words do not echo.")

    check_consumption()

def campfire():
    global corruption, will, awareness
    slow("""
A campfire burns ahead.
Warm. Recent.
No one around.
""")

    choice = present_options([
        ("1", "Rest", always),
        ("2", "Scatter the fire", can_refuse),
        ("3", "Move on", can_observe)
    ])

    if choice == "1":
        corruption += 2
        slow("The ground feels too welcoming.")
    elif choice == "2":
        will += 1
        slow("You deny comfort.")
    elif choice == "3":
        awareness += 1
        slow("You leave the warmth behind.")

    check_consumption()

def moss_shrine():
    global corruption, will
    slow("""
A moss-covered shrine leans inward.
The ground remembers kneeling.
""")

    choice = present_options([
        ("1", "Kneel", always),
        ("2", "Circle it", can_observe),
        ("3", "Deface it", can_refuse)
    ])

    if choice == "1":
        corruption += 2
    elif choice == "2":
        will += 1
    elif choice == "3":
        corruption += 1
        will -= 1

    check_consumption()

def village():
    global corruption, awareness
    slow("""
Lanterns glow ahead.
A village.
Too orderly.
""")

    choice = present_options([
        ("1", "Enter", always),
        ("2", "Watch", can_observe)
    ])

    if choice == "1":
        corruption += 2
    else:
        awareness += 1

    check_consumption()

def village_food():
    global corruption, awareness, will
    slow("A villager offers bread.")

    choice = present_options([
        ("1", "Eat", always),
        ("2", "Refuse", can_refuse),
        ("3", "Ask about it", can_question)
    ])

    if choice == "1":
        corruption += 2
    elif choice == "2":
        will += 1
    elif choice == "3":
        awareness += 1

    check_consumption()

def river():
    global corruption, awareness, will
    slow("""
A black river blocks your path.
It murmurs futures.
""")

    choice = present_options([
        ("1", "Drink", always),
        ("2", "Cross carefully", can_refuse),
        ("3", "Follow upstream", can_observe)
    ])

    if choice == "1":
        corruption += 3
    elif choice == "2":
        will += 1
    elif choice == "3":
        awareness += 1

    check_consumption()

def heart_tree():
    global corruption, will, awareness
    slow("""
The Heart Tree towers before you.
The forest waits.
""")

    choice = present_options([
        ("1", "Kneel", always),
        ("2", "Walk calmly", can_refuse)
    ])

    if choice != "2":
        corruption += 2
    else:
        will += 1
        awareness += 1

    check_consumption()
    final_choice()


# FINAL CHOICE (WEIGHTED ENDINGS: 10% / 30% / 30% / 30%)

def final_choice():
    global corruption, will, awareness
    slow("""
The forest offers stillness.
What is your final choice?
""")

    choice = present_options([
        ("1", "Accept the stillness (Submit to the forest's peace)", always),
        ("2", "Refuse the stillness (Assert your independence)", can_assert)
    ])

    # If the player cannot assert (Will < 6 or Awareness < 6), they are forced to 'Accept'.
    if choice != "2":
        # --- PATH 1: ACCEPTANCE (60% Total Probability) ---
        
        # This path is split 50/50 between two endings to achieve 30% each.
        
        # Roll a single number (0.0 to 1.0) to decide the 50/50 split
        roll = random.random()
        
        # ENDING 1: THE EMBRACE (Target 30%)
        if roll < 0.5:
            # We use high corruption OR low resistance (Will + Awareness) to push to this ending.
            if corruption >= 5 or (will + awareness < 10):
                end_game("🌲 ENDING 1: THE EMBRACE (You found peace in submission) 🌲")
            # If corruption is low AND resistance is high, we push to Rooted Will (the other 30% path)
            else:
                end_game("🌑 ENDING 2: ROOTED WILL (Your resolve was consumed slowly) 🌑")
        
        # ENDING 2: ROOTED WILL (Target 30%)
        else:
            # We use high resistance (Will + Awareness) OR low corruption to push to this ending.
            if corruption < 5 or (will + awareness >= 10):
                end_game("🌑 ENDING 2: ROOTED WILL (Your resolve was consumed slowly) 🌑")
            # If corruption is high AND resistance is low, we push to The Embrace (the other 30% path)
            else:
                end_game("🌲 ENDING 1: THE EMBRACE (You found peace in submission) 🌲")
    
    else:
        # --- PATH 2: REFUSAL (40% Total Probability) ---
        
        # Check if the player meets the high stat, low corruption threshold.
        true_ending_threshold = (will >= 7 and awareness >= 7 and corruption < 5)
        
        # ENDING 3: TRUE ENDING (Target 10%)
        # If threshold is met, roll a 25% chance to hit the 10% target (10% is 25% of the 40% pool).
        if true_ending_threshold and random.random() < 0.25:
            slow("🌿 ENDING 3: THE ONE WHO WAS NEVER CONSUMED (True Victory) 🌿")
            sys.exit()
        
        # ENDING 4: THE CONSUMED REFUSAL (Target 30%)
        # This is the catch-all for refusal attempts that fail the True Ending roll.
        else:
            end_game("❌ ENDING 4: THE CONSUMED REFUSAL (Your will broke against the final weight) ❌")

# GAME FLOW

def main():
    slow("🌲 THE FOREST OF CURSED ELVES 🌲")
    input("\nPress Enter to step into the forest...")

    long_walk()
    lost_clearing()
    transition("The forest closes behind you.")

    fatigue_check()
    wounded_beast()
    transition("You walk on, unsettled.")

    long_walk()
    watcher_encounter()
    transition("The watching fades. Or pretends to.")

    campfire()
    fatigue_check()

    moss_shrine()
    transition("You do not look back.")

    long_walk()
    village()
    village_food()

    fatigue_check()
    long_walk()
    river()

    transition("The sound of water fades.")

    long_walk()
    heart_tree()

# START

if __name__=="__main__":
    main()