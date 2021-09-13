import random
import time

def enemyTurn():
    enemyHitChance = random.randint(1,3)

    if enemyHitChance < 3:
        damage = random.randint(2,5)

        global playerHealth
        playerHealth -= damage
        print('> The enemy hits, dealing', damage, 'damage')

    else:
        print('> The enemy misses')


def enemyEncounter():

    global playerHealth
    playerHealth = 20

    global enemyHealth
    enemyHealth = 20

    weapon = 'fists'
    bandages = 2
    healTurn = 0

    print('> You see an enemy!')
    print('> Type a to attack. You can attack every turn')
    print('> Type h to heal. You must wait 3 turns to heal again')
    print('> ')

    while True == True:
        if healTurn <= 0:
            healTurn = 0

        if playerHealth > 20:
            playerHealth = 20

        if playerHealth <= 0:
            print('> ')
            print('> You die')
            return

        if enemyHealth <= 0:
            print('> ')
            print('> You defeated the enemy')
            return




        print('> ')
        print('> You: ', playerHealth, '     ', 'Enemy: ', enemyHealth)
        print('--------------------------------------------------------------')

        userAction = input('> ')


        if userAction == 'a':
            healTurn -= 1

            hitChance = random.randint(1,3)

            if hitChance < 3:
                damage = random.randint(2,5)
                enemyHealth -= damage
                print('> ')
                print('> You hit with', weapon, 'dealing', damage, 'damage')
                print('> ')
                enemyTurn()


            else:
                healTurn -= 1
                print('> ')
                print('> You miss')
                print('> ')
                enemyTurn()


        elif userAction == 'h':
            if healTurn == 0:
                if bandages > 0:
                    healTurn = 3
                    bandages -= 1
                    heals = random.randint(5,8)
                    playerHealth += heals
                    print('> ')
                    print('> You use 1 bandage and heal for', heals)
                    print('> ')
                    enemyTurn()
                else:
                    print('You are out of bandages')
            else:
                print('> You need to wait', healTurn, 'turns')





def main():

    while True == True:

        chance = input()
        if chance == 'r':
            num = random.randint(1,1)

            if num == 1:
                enemyEncounter()

            else:
                print('There are no enemies')

        else:
            print('Type r')








main()
