friends = ["gabriel", "bruno", "Joao"]
for friend in friends:
        print "\n hello my friend", friend
        done = raw_input("done? ")
        if done == "done" or done == "yes":
                print "\n okay, have a good day", friend
                continue
        elif done == "no":
                why = raw_input("Why? ")
                if why == "because I'm sad today":
                        print "\n Call someone to drink today with you", friend
                        
                if why == "I don't know":
                        print "\n share a doctor, you need!", friend
        import os
        os.system("cls")

bye = raw_input("bye? ")
quit()

        
