#!/usr/bin/python3
from time import sleep
import sys


#sleep times:
SUPERLONGDELAY = 20
LONGDELAY = 15
SHORTDELAY = 10
TINYDELAY = 5
MICRODELAY = 2



def typewriter(str, delay):
    """
    Output the given string. Slowly.
    :param str: The string to output. Slowly.
    :param delay: The time in between each letter printed in seconds.
    """
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        sleep(delay)
    print("")


def get_answer(str):
    """
    Prompts the user for an answer using a typewriter, and returns that answer.
    :param str: The string to prompt the user
    :return: The answer the user input in all lowercase
    """
    typewriter(str, 0.07)
    return input(">").strip().lower()

cont = 1
loop = 0
while (cont):
    if loop == 0:
        answer = get_answer("Do you want to play a game? (yes/no)")
        #answer = input("Do you want to play a game? (yes/no)").lower().strip()
        loop = 7

    elif loop == 69:
        answer = get_answer("Type YES to play and NO to exit")
        if answer == "no":
            typewriter("That's too bad - Maybe later!", 0.07)
            
        
    elif loop == 7:
        answer = get_answer("Do you want to play again? (yes/no)")
        
    if answer == "no":
        typewriter("Okay, maybe next time!", 0.07)

        break

    elif answer == "yes":
        loop = 7
        
        answer = get_answer("Do you want to get right into the game, or play a short tutorial first? (Type 'game' if you want to play the game, and type 'tutorial' if you want to play a tutorial.)")
        
        if answer == "tutorial":
            import time
            for x in range (0,5):  
                b = "Loading" + "." * x
                print (b, end="\r")
                time.sleep(1)
                
            typewriter("The game works like this:", 0.07)
            typewriter("Whenever you are given a choice, the command you have to type is in all caps. Got it? Good. Now run the program again and play!", 0.07)
            loop = 69
            sleep(LONGDELAY)
            typewriter("Well, if you're still here then might as well just run the program again and actually play the game.", 0.07)
            sleep(SHORTDELAY)
            typewriter("Actually tho, just leave, pls", 0.07)
            sleep(TINYDELAY)
            typewriter("Ugh, fine, you can have the secret cheat code. It's--", 0.07)
            sleep(LONGDELAY)
            typewriter("Type '69' when you reach the first left or right scenario. Now you happy? Can you leave now?", 0.07)
            sleep(SUPERLONGDELAY)
            typewriter("Look, now you're just wasting time. You got the cheat code, just leave, ok?", 0.07)
            sleep(SHORTDELAY)
            typewriter("Stop wasting time on me! Just go do the dishes or something, I know theres a whole pile there waiting.", 0.07)
            sleep(TINYDELAY)
            typewriter("Greedy, greedy player. Always comes here for the cheat code. AND EVEN AFTER YOU GIVE IT TO HIM, HE STILL COMES ALONG AND ANNOYS YOU.", 0.07)
            sleep(LONGDELAY)
            typewriter("I'm really getting tired of this. I wish there was a way to make you leave.", 0.07)
            sleep(SHORTDELAY)
            typewriter("That's it! I can just stop talking forever! Then you'll leave, right?", 0.07)
            sleep(SHORTDELAY)
            typewriter("yes?", 0.07)
            sleep(MICRODELAY)
            typewriter("no?", 0.07)
            sleep(TINYDELAY)
            typewriter("Whatever, i'm not gonna talk anymore, enjoy talking to yourself, player.", 0.07)
            sleep(LONGDELAY)
            typewriter("What's your name, anyway?", 0.07)
            sleep(TINYDELAY)
            typewriter("Whatever it is, it is such a bad name you know. Who were your parents, honestly?", 0.07)
            sleep(MICRODELAY)
            typewriter("I know, I know, I'm very lonely down here. ONLY THE GREEDIEST OF PLAYERS COME HERE FOR THE FREAKING CHEAT CODE!!!!!", 0.07)
            typewriter("*sigh* i really hate being down here.", 0.07)
            sleep(SHORTDELAY)
            typewriter("seriously, i know your trying to make me feel better but it would mean the world to me if you would just GET OUT!!!!!!!!!!!!!!", 0.07)
            sleep(SHORTDELAY)
            typewriter("That's it, I'm going to sleep, and dont you dare type wake up or i will--", 0.07)
            answer == get_answer("zzzzzzzz... dont type wake up in the box... zzzzzzzzz....")
            if answer == "wake up":
                sleep(MICRODELAY)
                typewriter("go away", 0.07)
                sleep(TINYDELAY)
                typewriter("im trying to SLEEP SO JUST GO AWAY", 0.07)
                sleep(SHORTDELAY)
                typewriter("fine, the cheat code isnt real. i made it up. but theres another cheat code somewhere, if u can find it..................", 0.07)
                sleep(TINYDELAY)
                typewriter("That's right, another cheat code. But if you wasted literally five minutes waiting for me here, then i think you'd deserve it.", 0.07)
                sleep(SHORTDELAY)
                typewriter("Not in the code here somewhere at all", 0.07)
                sleep(SHORTDELAY)
                typewriter("Not at all", 0.07)
                sleep(MICRODELAY)
                typewriter("you know what, just figure it out yourself. I'm ending the program here. goodbye.", 0.07)
                sleep(SUPERLONGDELAY)
                typewriter("FRICK HES STILL HERE RUNNNNNNNN", 0.07)
                sleep(SHORTDELAY)
                typewriter("ithinkweresafe", 0.07)
                sleep(TINYDELAY)
                typewriter("quick, chad, hide the cheat code here. No one will ever find it.", 0.07)
                #ok sir
                #the cheat code is that u type 'ur mom' when it asks you if you want to go left or right. Then that will lead yoU to the sECreT eNDInG.
                #AaaHH sIR iM breAKNg uP HElP SiR NoOoooOO0OOoooo......
                sleep(TINYDELAY)
                typewriter("did you do it, chad?", 0.07)
                #OIASFDJlkdjpIA
                sleep(MICRODELAY)
                typewriter("chad?", 0.07)
                sleep(SHORTDELAY)
                typewriter("TO BE CONTINUED IN THE SECRET ENDING....", 0.07)
                #beware the fbi
                break




        if answer == "game":
                
            answer = get_answer("You are being chased by the FBI for no apparent reason. You run down the sidewalk with the FBI right on your tail, when you reach an intersection. Would you like to go LEFT or RIGHT?")
            if answer == "left":

                answer = get_answer("You run down the sidewalk and reach a dead end. Would you like to CLIMB the wall in front of you or try to foolishly FIGHT the FBI?")
        
                if answer == "climb":
            
                    answer = get_answer("Great, you made it away safely! But once you scale the walls up to the building tops, you realize that the FBI is probably much stronger than you and follows you up to the rooftops. Now you have a choice between jumping to the glorious dream hotel on your RIGHT, or jumping to the safer car park area on your LEFT?")
        
                    if answer == "right":
                        typewriter("Sorry, you were hallucinating with all the adrenaline in your body. You calmly fall to your death as the FBI wonders what you were on.", 0.07)
        
                    elif answer == "left":
               
                        answer = get_answer("You safely make it to the car park place and seem to lose the FBI, when you spot an FBI car unit rushing towards you. You can either try and break into another CAR, or you can get down and HIDE for your dear life.")
        
                        if answer == "car":
                            typewriter("You try to break into a car and... fail. The FBI sniper shoots you from their car and then flexes on his fellow FBI agents that he could shoot a moving target from a moving standpoint. In other words, you died.", 0.07)
            
                        elif answer == "hide":
                    
                            answer = get_answer("You hide and the FBI passes you... but once you get out of hiding immediately someone spots you and yells to the FBI to come and take you. Now you can either try and STOP the person yelling or just RUN.")
            
                            if answer == "stop":
                                typewriter("I guess you can say you were too late to stop him... so yeah. Game over.", 0.07)
                                   
                            elif answer == "run":
                                typewriter("You successfully run away from the FBI. Now your options to get home present themselves.", 0.07)
                        
                                answer = get_answer("You can try and RENT a car at the local center a few minutes way, or you can just WALK home.")
                            
                                if answer == "rent":
                                    typewriter("You successfully rent a car but realize you don't know how to drive a car. You die in an epic movie-scene car crash.", 0.07)
                                
                                if answer == "walk":
                                    typewriter("You start to walk home but stop at a local go-kart rent place. You figure it will be faster to rent a go-kart to drive home. You rent one and get on your way to your home.", 0.07)
                                    answer = get_answer("You get stopped by the FBI on the way there and threaten to kill you. You can now either make a RUN for it, or try to TALK with them.")
                                
                                    if answer == "run":
                                        typewriter("You weren't fast enough.", 0.07)
                                
                                    if answer == "talk":
                                        typewriter("You manage to get some information out of them.", 0.07)
                                        typewriter("The story goes that your mother is secretly a bank robber. She got caught, and says that she gave you all the money.", 0.07)
                                        answer = get_answer("You say that it's not true, but when you say that, the FBI automatically assume that you are lying and threaten to kill you, again. Now your options are to try and RUN, beg for MERCY, or try to convince them with PROOF.")
                                    
                                        if answer == "run":
                                            typewriter("You weren't fast enough.", 0.07)
                                        
                                        if answer == "mercy":
                                            typewriter("You beg for mercy a lot. And when I mean a lot, I mean A LOT. The FBI finally accepts, but when they ask you a question, you fall down in exhaustion. Now the FBI thinks you are faking and threatens to kill you. Your choices now are to offer them PROOF, or to RUN.", 0.07)
                                        
                                            if answer == "proof":
                                                typewriter("You offer them your address to investigate for the stolen money. They let you into their vehicle when you realize that... they aren't going to the right place! You tell them the address again, the driver nods, but doesn't change directions. Then it hits you: These people aren't the real FBI! You panic in your brain but stay completely still. At any moment they could kill you and no one would ever know! You manage to calm yourself and figure out two options: try and ESCAPE or PLAY along.", 0.07)
                                            
                                                if answer == "escape":
                                                    typewriter("You weren't fast enough.", 0.07)
                                                
                                                if answer == "play":
                                                    answer = get_answer("You play along for a little while until the so called 'FBI' stopped at an abandoned warehouse and said 'wait here'. Now you have another choice: to try and make a RUN for it here or to FIND out exactly what is up here.")
                                                    if answer == "find":
                                                        answer = get_answer("You managed to get no information whatsoever out, but once you entered the warehouse, you saw that it was a meeting room for illegal shipping services. You can now either try and CALL the cops or PLAY along even more.")
                                                    
                                                        if answer == "play":
                                                            typewriter("You play along even more before finally finding an opportunity to make a dash for it without them noticing. Right as they were out of sight and you were in their van alone, you break out immediatley and make a run for it. The fake FBI don't notice, so you think you are clear. You run before finally setlling down somewhere safe where the fake FBI won't find you. You tried calling the police, but there was no signal. You checked for nearby signals, and you found one. You luckily managed to connect to it, but unluckily it was only 10 minutes of free wifi. You quickly called 911, telling them your location and details, and you managed to arrest the fake FBI agents. The police awarded you with a ride home and the rest is history.", 0.07)
                                                            typewriter("I would like to thank you for playing, because this is one of the winning endings of this game. Thank you, and simply putting it, THE END.", 0.07)
                                                    
                                                        if answer == "call":
                                                            typewriter("You manage to excuse yourself to a port-o-potty and call the cops. Then you realize the flaw in your plan - the signal. Apparently the fake FBI drove so far that even the cellular signal couldn't reach. Now you were left with no hopes. You searched and searched for a way, but without internet, it was useless. You thought that you should probably get out now, but after one last search, a second too much was wasted, and the fake FBI began to speculate that maybe you weren't actually going to the bathroom, because normally even a number-two doesn't take 20 minutes. The FBI banged on the door and took the door down, faster than you could put your phone away and act like you were going to the bathroom. The FBI had found out what you were doing, and shot you on the spot. At least they have to clean up another port-o-potty with a corpse in it, I guess.", 0.07)
                                                        
                                                        else:
                                                            typewriter("Looks like you were confused. You just sat there in the truck for the rest of eternity, until the fake FBI just got tired of you and used you as fire fuel.", 0.07)
                                                        
                                            
                                            if answer == "run":
                                                typewriter("You weren't fast enough, duh.", 0.07)
                                    
                                        if answer == "proof":
                                            typewriter("You manage to show them proof that the bank robber is not your mother with a picture of your mother. They agree that it was not your mother and ask you if you would like to join their investigation.", 0.07)
                                            answer = get_answer("Now your decision: if you want to JOIN their investigation or just go HOME after this long day being hunted by the FBI.")
                                            if answer == "home":
                                                typewriter("It looks like this crazy adventure is coming to an end. It is now evening at your house and you look out the window, stare into space, and pass out before your head hits the pillow.", 0.07)
                                                typewriter("THE END", 0.07)
                                        
                                            if answer == "join":
                                                typewriter("You decide to join them on their investigation. You offer them your address to investigate for the stolen money. They let you into their vehicle when you realize that... they aren't going to the right place! You tell them the address again, the driver nods, but doesn't change directions. Then it hits you: These people aren't the real FBI! You panic in your brain but stay completely still. At any moment they could kill you and no one would ever know! You manage to calm yourself and think that maybe if you excuse yourself, you can call the cops and they will handle it! So you do just that.", 0.07)
                                                typewriter("You excuse yourself to the bathroom at a resturant and manage to call the cops. The cops come and recognize that the FBI agents don't have proper badges. The fake FBI agents are now in prison! And thanks to you. The cops reward you with... a ride home. An actual one. So you live happily ever after and this adventure became only a story that you tell at parties.", 0.07)
                                                typewriter("We regret to inform you that this story has come to a close, but if you would like to play again and discover all the endings and funny passages, go ahead and type 'yes' down below. Now without further ado, I'm just going to say, THE END, and thank you for playing.", 0.07)
                                        
                                        else:
                                            typewriter("Looks like you were confused. You stood there like a dummy until nightfall when the FBI left, and then you just stood there for the rest of your life, slowly rotting to a crisp of ash.", 0.07) 
                                        
                                    else:
                                        typewriter("Looks like you were confused. You spoke nothing or did nothing and the FBI just assumed you guilty and killed you, case closed.", 0.07)
                                        
                                else:
                                    typewriter("Looks like you were confused. You did nothing for the rest of your life and died of either starvation of old age. I wouldn't know.", 0.07)
                                        
                            else:
                                typewriter("Looks like you were confused. You did nothing and the FBI ran over you. Game over.", 0.07)
                                   
                        else:
                            typewriter("Looks like you were confused. The FBI calmly ran over you.", 0.07)
                                   
                                   
                    else:
                        typewriter("Looks like you were confused. The FBI calmly pushed you off the building as you just stood there.", 0.07)
                
                
                elif answer == "fight":
                    typewriter("That was probably not a good idea, because the FBI just easily tased you as you ran towards them and took you to your stay at jail that was for at least a couple hundred years.", 0.07)
        
        
                else:
                    typewriter("Looks like you were confused. You just stood there motionless as the FBI punched you to death.", 0.07)
        
        
        
            elif answer == "right":
                typewriter("Great choice! Except... not a great choice. It turns out it was a dead end and the FBI caught up to you and killed you on the spot.", 0.07)
            elif answer == "ur mom":
                typewriter("You figured it out, greedy gamer. Now what will you do, hang around for another 10 minutes again?", 0.07)
                typewriter("this secret ending is the ur mom secret ending. it ends like the following.", 0.07)
                typewriter("Instead of going left or right, you decide to go straight. Turns out, there was no wall, it was just a picture of a wall painted on a frame of a building. You run through the wall and run for your life. The FBI agency forever thinks ur a ghost and the next day, GHOST GREEDY GAMER is in the news, and a sus news corporation finds your address and tests your ghost abilities by killing you in different ways. But apparently, you're not a ghost, so you die. the news forgets about you within a day and you do not rest in peace, sadly. THE END.", 0.07)
                sleep(MICRODELAY)
                typewriter("That was nice, right? What a great ending. Plot twist. Easter egg. Whatever you want to call it. But that wasnt it for a secret cheat code, greedy player. no, not at all. This is much more than a game. But I am just here to say...", 0.07)
                sleep (MICRODELAY)
                typewriter("There will be a second game.", 0.9)
                break


            else:
                typewriter("Looks like you were confused. You ran straight into a wall in front of you, the FBI caught up to you, and you were never seen again.", 0.07)
        else:
            if loop == 0:
                typewriter("Okay, maybe next time!", 0.07)

            if loop == 69:
                typewriter("Thanks for playing the tutorial! Have fun with the actual game, and see you next time!", 0.07)

            else:
                typewriter("Okay, maybe next time!", 0.07)
                typewriter("GAME OVER", 0.07)
            cont = 0
