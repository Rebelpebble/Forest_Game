from sys import exit
import random

my_health = 20
weapon = "hands"
monster = "werewolf"

#### Main Game ####
def start():
    print "You begin your journey in a eerie forest."
    print "A heavy mist surrounds you and winds throughout the trees."
    print "You come upon a sign pointing to your left and right."
    print "Which way do you choose?"
    print "(1) Left"
    print "(2) Right"

    choice = raw_input("> ")

    if choice == "1":
        left(1)
    elif choice == "2":
        right(2)

########

#### Fighting ####
def fight(my_health, monster, weapon):

    monster_health = choose_monster_health(monster)

    print "A %s appeared!" % monster
    print "Your HP:    ", "-" * my_health
    print "Monster HP: ", "-" * monster_health

    while monster_health > 0:
        print "Will you attack (1) or run (2)?"

        choice = raw_input("> ")

        if choice == "1":
            my_attack = choose_weapon(weapon)
            monster_health = monster_health - my_attack
            monster_attack = choose_monster_attack(monster)
            my_health = my_health - monster_attack

            print "You did %d damage." % my_attack
            print "The monster did %d damage.\n" % monster_attack
            print "Your HP:    ", "-" * my_health
            print "Monster HP: ", "-" * monster_health

            die(my_health)

        else:
            return my_health
            exit(0)


def choose_weapon(weapon):
    if weapon == "iron":
        return random.randrange(1, 6)
    elif weapon == "steel":
        return random.randrange(5, 15)
    else:
        return random.randrange(0, 2)


def choose_monster_health(monster):
    if monster == "goblin":
        return 20
    elif monster == "werewolf":
        return 25
    elif monster == "basilisk":
        return 30
    else:
        print "That is not a monster."
        exit(0)


def choose_monster_attack(monster):
    if monster == "goblin":
        return random.randrange(0, 3)
    elif monster == "werewolf":
        return random.randrange(0, 6)
    elif monster == "basilisk":
        return random.randrange(0, 10)
    else:
        print "That is not a monster."
        exit(0)


def die(my_health):
    if my_health <= 0:
        print "\n\nYou were killed!"
        print "GAME OVER\n\n"
        exit(0)


########

fight(my_health, monster, weapon)
