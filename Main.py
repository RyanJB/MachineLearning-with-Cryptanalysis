#==============================================================================
# Ryan Brown - Using Machine Learning optimisation techniques to decipher a polyalphabetic cipher.
#==============================================================================

import random, math, time
import Deciphering as dc
#Used matplotlib and plotly for graphs
import numpy as np
import matplotlib.pyplot as plt

#fitness scoring using quadgrams(Practical Cyrptography (2009))
import ngram_score as ns
fitness = ns.ngram_score('english_quadgrams.txt')

#default values at start   |   expected key is 'WINSTON'
keySize = 7
#cipher = 'KCESVQBQVGKLVBSBUSMHUAAVLNOGEWAAGGCWQAALRRPMEAHFNPQAYTBQPPNLMVRLMAAGGHHIVKGCGBIEXKCZPPRKMOERIGAHBCKQALTBBBNRJUMLKCGGWCYAWHLYCBZUBFMVOUUBFMVFKTBFZOFPPRQDSRLWHLHTGDMJSKAVCPGTXRRYQFAOSFIIYDMVVJOFVHBBPKBMGHAKENFWHUEAVKTHVIMSGKJRNGCDTWAPIYCMCGDMZLASBYKHHTHVKVOQZSEIIAQHTOKBUKBRROWSLASFPZNAMGJKCYVUSNCZVWOCHOIQVBHVKVGGHIEJIISEGGNIVFTZEAIQQLSIAZRLASTAZZSGGJKCYVLCBJPNNXPNPBRJBSFSWECBBTXGESWWBZQEWVHVKVSAGRVJOJZBQUSWHDWQYKARLASFPZNAMGOKBUTRBVCPGSGRQWGJAMVNIIWGKQNIXNAZBQADRDHDVJOVFMVRAIFLXFAIMQAMSENIAWTBNJLAWXRBBZRAGTBNKREXBGWVQKNDCHGBXHIEWZZAXGGDMEWTZYNWHFWHUAKNHXKRYWHDWBBPKBFMSZLTNLXOAUUVDBHNNGNUMWBJWALASZWQADTBQWBBJGSNNBUWLHEWQGKMVRNWPCHTTEJESEHNNEVDEGGWVQSECACAVWZSOQBJZTHVOBUWZCBZWSLAOGENJWVOAJWGMLSGDMUSKPBQZBJIOFOBUWLHEWQGKHBPAQAEHFBYKBLASTAZZSGGJETYOHFXOWHLAOAZCOGTHFWVQSBFPNISLPWYHABGGPRKXRJTHVJOSJHAPWANTEOAYINFWRNGIEAGSRZVBLFFCNMFAWSAPMADTFTACCGGHUABEGNPYABUALKVHTPSNGRPWHKHFNLXEGTQUKNGJHIOHMGGMVRSMFLXFADMZALDUAZROXAHOBTSBBNOUHUAHVIMNKICFOQODX'
cipher = 'KPZALHLAGRGYHUAUBMGHNEVOWECJGMRHVOEANHDPOGYPBXFMONWGZXFFOWHDLOAZAUGNZQPPRKDMOANVDESQSQGZYWEAIAVLABGMXWXDJWBPZBBTKDRJWIEEVFKHBVBBUALWFPWRFWWABQEWMVRJERKACHHLNDEPHNVGGZSGDMEOTHPDBUWYZNIMFUEWZXPVYAWAPWGZXBVCPGUTZYEVTGNHSKZGZXFBLMFWGHOUIAVPSJETYOTHPDBUWYZNIMFTNFAKVNFWCAPPREHIAPIVFLWQAPRQTBQENJWLVBQTQVBSGKVVYAHGDMAOXGUKCYVTZYZQRLHURPPRJKOVOMNYEOFOWSOBBRBWELASYWAGLBARYIYDBBTKCGXHFGDMEGISCNMCSKSNOEROBZYSIGUAHUANYSFSFXCEFHBNJLBFMVRIWHFMOVJAVVXRROWYSMWBJKBEXGHLWALASFGGAGPWFAMSAKSVJAVVXHUAUBMGHNEVVKXSSEZRTNFAEVTLASGNMRKTBQEARWYWEAPBDECJEVTKHIYOIAVBGRANVJXPYKWQAGHUAJEWXNRWVQAACCABUSMMBQTYJXARIJRJFSBDAUGNZQIGCWHDYANNDEHUAVFMKSYUQYDWCGDMFSFSPKVSAGSQEVZGNBGWQAZTZYOERYHHGKWPDHGRPWGZXTYWURUTZYEVTGNHSWBUWKVBHLSSLHNJLJWPWYHENLVVGDMSDTAROJHJGCAWVQGGHUAUBMGHNEVFAWSQAABDTHVKVPGFSFQXBFMVROSLFHKVOMRXBFREVFAWSGDMZGNBGWQAALSRBQEWUIEJQAYMVRPZRWLOAZQFWXTVNMUGEZBSQAYLCHHANFWWFAMSAKSOHWBVBBGDMOJXSMAIAVBVBLMGZTHLKCYDKSZAUOWKARWVQAYHUAVVYAHVOJHJGWACQJAEZPKDRJFMRUMFXHFVBBUWWOEGZRLNFAOBUWGALXZBLASEOEVDERVAIAVTGGDMFCRGSWTYAGUQKEAAMQEWAUWWWAPWGZBGYKVRDRHBSVNFWKVPPGZTHFDIQGPICKVGZXUEKCAVBVRWZZQISBLTRKVFRWUVFZCHPVBOBGRANVJXWAOQQWMVRIWHFMOVJQFWXTVNMOMKBVJOGZXHEAMFSGRVOMRXBFRDWYDHKVJOFGNZFWVQALSRBQEWUZBKLVFMVRXZRWSSVOMRXBFRKPLGNYAKEVKTKNYQGQUIEJQAYYWEAIAVBGRANVJXTRATGZXVRWBHHHBZUAXAGTVNMNFWWFAMSAKSSEZRSGRVOMRXBFRXCEFHBNJLBFTBQIWHFMOVJAFAWS'

dictionary_keys = {}
best_keys_dictionary = {}

#calculates a score from the decipherment of key and ciphertext
def fitness_score(problem, sol):
    
    decipher = dc.deciphering(problem,sol)
    decipher.startDecryption()
    message = decipher.getDecryptedMessage()
    
    score = fitness.score(message)
    
    return score
    
#some code used from collective intelligence (Segeran, 2007)
def hillclimb(problem, rstarts=1000, random_startkeys = {}):
    
    print "Hill Climbing Algorithm Starting....\n"
    
    start_time = time.time()#time the algorithm's performance completion
    
    hillClimbScores = [] #collecst all the best scores

    #number of random starts
    for random_start in range(1,rstarts):

        #start of the index of keyword. changes as it progresses through decipher
        key_indicator = 0

        # Create a random solution
        sol=[chr(random.randint(0,25)+65) for i in range(keySize)]

        while 1: # Main loop

          currentSol = fitness_score(problem,sol)
          best = currentSol

          #two random solutions made from solution
          prevSol = [sol[p] for p in range(len(sol))]
          nextSol = [sol[n] for n in range(len(sol))]

          if key_indicator < keySize: #if index of key is less than the size of key

              getnum = ord(sol[key_indicator])

              #from alphabet of 0 to 25 (1 to 26) change to ascii uppercase letters (add 65. 65 being 'A' in ascii alphabet)
              #previous neighbour
              prevChar = chr(getnum - 1)
              prevNum = ord(prevChar)

              if prevNum >= 65 and prevNum <= 90:
                  prevSol[key_indicator] = prevChar
              elif prevNum < 65:
                  #assign Z as A - 1 goes to Z
                  prevSol[key_indicator] = chr(90)

              #from alphabet of 0 to 25 (1 to 26) change to ascii uppercase letters (add 65. 65 being 'A' in ascii alphabet)
              #next neighbour
              nextChar = chr(getnum + 1)
              nextNum = ord(nextChar)

              if nextNum >= 65 and nextNum <= 90:
                  nextSol[key_indicator] = nextChar
              elif nextNum > 90:
                  #assign A as Z + 1 goes back to start of alphabet A.
                  nextSol[key_indicator] = chr(65)

          elif key_indicator >= keySize: #if index of key is greater than size of key
              break #break out of the while loop 

          neighbour = [prevSol, nextSol] #assign two neighbours together

          for j in range(len(neighbour)): #check neighbours to see if their better than solution

              current_score = fitness_score(problem,neighbour[j])

              #if current score is greater (so closer to 0) then
              if current_score > best:
                  best=current_score
                  sol=neighbour[j]
                  hillClimbScores.append(best)

          if best == currentSol:
              key_indicator = key_indicator + 1

        random_startkeys[''.join(sol)] = best

    best_of = None
    num = 0
    best_of_sol = []

    #run through the best random iterations and find the best result 
    for item in random_startkeys:

        if num == 0:
            best_of = random_startkeys[item]
            best_of_sol = list(item)
            num += 1

        else:
            current = random_startkeys[item]

            if current > best_of:
                best_of = current
                best_of_sol = list(item)
                
    end_time = time.time()
    print "\nHill Climbing time (seconds):\t" + str(end_time - start_time) + "\n"

    create_graphs(hillClimbScores, 'Hill Climbing', 'r')

    print "Number of best solutions found:\t" + str(len(hillClimbScores))
    print "Hill Climbing Algorithm Completed....\n"
    print str(''.join(best_of_sol)) + "\n" + str(best_of)
    
    return hillClimbScores

#some code used from collective intelligence (Segeran, 2007)
def geneticoptimize(problem, popsize=100, step=1, mutprod=0.6, elite=0.4, maxiter=120):
      
      print "Genetic Algorithm Starting....\n"
      
      start_time = time.time() #time the algorithm's performance completion
      
      geneScores = [] #collects the best scores
      
      # Mutation Operation
      def mutate(vec):
          
        i = random.randint(0, keySize-1) #choose random index to mutate
        
        if random.random()<0.5 and len(vec[i])>0:
            
          newNum = ord(vec[i]) - step #find neighbour alphabet to change
    
          if newNum >= 65 and newNum <= 90: #If character is in the Alphabet
              newChr = vec[0:i]+[chr(ord(vec[i])-step)]+vec[i+1:] #mutation
          elif newNum < 65: #If character is less than the character A assign Z
              newChr = vec[0:i]+[chr(90)]+vec[i+1:]
              
          return newChr
      
        elif len(vec[i])<keySize:
            
          newNum = ord(vec[i]) + step #find neighbour alphabet to change
    
          if newNum >= 65 and newNum <= 90:#If character is in the Alphabet
              newChr = vec[0:i]+[chr(ord(vec[i])+step)]+vec[i+1:] #mutation
          elif newNum > 90: #If character is more than the character Z assign A
              newChr = vec[0:i]+[chr(65)]+vec[i+1:]
            
          return newChr

      # Crossover Operation
      def crossover(r1,r2):
        i = random.randint(1,len(r1)-2) #index of key to changeover
        cross = r1[0:i]+r2[i:]  #crossover the two elite
        return cross

      pop=[] #Initialise the starting population
      
      for i in range(popsize): #create a number of random keys
        sol = [chr(random.randint(0,25)+65)for i in range(keySize)]
        pop.append(sol)

      topelite = int(elite*popsize) #find the number of elite in the population

      for i in range(maxiter): #start of main nloop
        
        scores=[(fitness_score(problem,v),v) for v in pop] #find fitness scores of population
        scores.sort(reverse=True) #make best results show first
        ranked=[v for (s,v) in scores] #rank these scores

        # Start with the pure winners and overwrite existing list of better population
        pop = ranked[0:topelite]

        # Add mutated and bred forms of the winners
        while len(pop)<popsize:
          if random.random()<mutprod:
            # Mutation changes a specific character to a different result
            chosenElite = random.randint(0,topelite)
            mutation = mutate(ranked[chosenElite])
            pop.append(mutation)
            
            geneScores.append(fitness_score(problem, mutation))
            
          else:
            # Crossover is the point in which one best key is copied to another
            chosenElite1 = random.randint(0,topelite)
            chosenElite2 = random.randint(0,topelite)
            cross_element = crossover(ranked[chosenElite1],ranked[chosenElite2])
            pop.append(cross_element)
            geneScores.append(fitness_score(problem, cross_element))
            
      end_time = time.time()
      print "\nGenetic Algorithm time (seconds):\t" + str(end_time - start_time) + "\n"

      create_graphs(geneScores, 'Genetic Algorithm', 'b') #create graphs from resultss
      
      print "Number of best solutions found:\t" + str(len(geneScores))
      print "Genetic Algorithm Completed....\n"
      print str(''.join(scores[0][1])) + "\n" + str(scores[0][0])
      
      return geneScores

#some code used from collective intelligence (Segeran, 2007)
def randomoptimize(problem, riterations=7000):
    
      print "Random Optimize Starting....\n"
      
      #time the algorithm's performance completion
      start_time = time.time()
      
      randomScores = []
    
      best = -999999999 #best is the largest number possible first (number is less than 0)
      best_result = None
      
      for i in range(0,riterations):
          
        # Create a random solution of a key of the size key set
        sol=[chr(random.randint(0,25)+65)for i in range(keySize)]
        
        score = fitness_score(problem,sol)# Get the fitness score of the current solution
        
        # Compare the current fitness score with the best. If so, update new best.
        if score > best:
          best = score
          best_result = sol 
          randomScores.append(best)
      
      end_time = time.time() #
      print "\nRandom Optimize time (seconds):\t" + str(end_time - start_time) + "\n"

      create_graphs(randomScores, 'Random Optimize', 'g')
        
      print "Number of best solutions found:\t" + str(len(randomScores))
      print "Random Optimize Completed....\n"
      print str(''.join(best_result)) + "\n" + str(best)
      
      return randomScores

#some code used from collective intelligence (Segeran, 2007)
def annealingoptimize(problem, T=100000.0, cool=0.9995, step=1):
    
      print "Simulated Annealing Starting....\n"
      
      #time the algorithm's performance completion
      start_time = time.time()
      
      best_sol_score = None
      annealingScores = []
    
      # create a random solution of a key with the given size
      sol=[chr(random.randint(0,25)+65) for i in range(keySize)]

      while T > 0.1:

        # randomise the chosen index
        i = random.randint(0, keySize-1)
    
        # edit the index of character
        dir = random.choice([1,-1])
        
        # Create a new list with one of the values changed
        current_sol = sol[:]
        newChar = current_sol[i]
        
        newNum = ord(newChar) + dir
        
        if newNum >= 65 and newNum <= 90: #if new character is part of Alphabet
            current_sol[i] = chr(newNum)
        elif newNum < 65: #if new character is less than A then assign Z
            current_sol[i] = chr(90)
        elif newNum > 90: #if new character is more than Z then assign A
            current_sol[i] = chr(65)
    
        # Calculate the current cost and the new cost
        best_sol_score = fitness_score(problem, sol)
        current_sol_score = fitness_score(problem, current_sol)
        
        #find the probability from results. The lower the probability the less errors can be accepted.
        probability = pow(math.e,(current_sol_score - -best_sol_score) / T)    
        
        if (current_sol_score > best_sol_score or random.random() < probability):
            sol=current_sol      
            best_sol_score = current_sol_score
            annealingScores.append(best_sol_score)
    
        # Decrease the temperature
        T = T * cool
        
      end_time = time.time()
      print "\nSimulated Annealing time (seconds):\t" + str(end_time - start_time) + "\n"

      create_graphs(annealingScores, 'Simulated Annealing', 'y')
        
      print "Number of best solutions found:\t" + str(len(annealingScores))
      print "Simulated Annealing Completed....\n"
      print str(''.join(sol)) + "\n" +str(best_sol_score)

      return annealingScores
  
def create_graphs(score, title_name='Graph', color_line='r'):
    
    #create graph to represent all best solutions found
    plt.figure(1)
    line_amount = np.linspace(0, len(score), len(score))
    plt.subplot(111)
    s = plt.plot(line_amount, score, 'k')
    plt.setp(s, 'color', color_line, 'linewidth', 1.0)
    plt.title(title_name)
    
    plt.subplots_adjust(top=0.92, bottom=0.08, left=0.01, right=0.99, hspace=0.40, wspace=0.50)
    
    plt.show()
    
    #create a histogram graph from results
    m_values, m_base = np.histogram(score, bins=15)
    m_cumulative = np.cumsum(m_values)
    plt.plot(m_base[:-1], m_cumulative, c=color_line)
    plt.title(title_name)
    plt.ylabel('No. of Best Solutions')
    plt.xlabel('Scores')
    plt.show()
    
# RESULTS OF ALGORITHMS

hill_climbing_score = hillclimb(cipher)

genetic_score = geneticoptimize(cipher)

random_score = randomoptimize(cipher) 

simulated_annealing_score = annealingoptimize(cipher)

    
def hillClimb_ptesting():
    
    start_time = time.time()
    hillclimb(cipher, 100)
    end_time = time.time()
    print "\nHill Climbing 1 time (seconds):\t" + str(end_time - start_time) + "\n"
    
    start_time = time.time()
    hillclimb(cipher, 500)
    end_time = time.time()
    print "\nHill Climbing 2 time (seconds):\t" + str(end_time - start_time) + "\n"
    
    start_time = time.time()
    hillclimb(cipher, 1000)
    end_time = time.time()
    print "\nHill Climbing 3 time (seconds):\t" + str(end_time - start_time) + "\n"

def genetic_ptesting():
    
    start_time = time.time()
    geneticoptimize(cipher, 50, 1, 0.2, 0.1, 80)
    end_time = time.time()
    print "\nGenetic Algorithm time (seconds):\t" + str(end_time - start_time) + "\n"
    
    start_time = time.time()
    geneticoptimize(cipher, 70, 1, 0.4, 0.2, 100)
    end_time = time.time()
    print "\nGenetic Algorithm time (seconds):\t" + str(end_time - start_time) + "\n"
    
    start_time = time.time()
    geneticoptimize(cipher, 100, 1, 0.6, 0.4, 120)
    end_time = time.time()
    print "\nGenetic Algorithm time (seconds):\t" + str(end_time - start_time) + "\n"
    
def random_ptesting():
    
    start_time = time.time()
    randomoptimize(cipher, 3000) 
    end_time = time.time()
    print "\nRandom Optimize time (seconds):\t" + str(end_time - start_time) + "\n"
    
    start_time = time.time()
    randomoptimize(cipher, 5000) 
    end_time = time.time()
    print "\nRandom Optimize time (seconds):\t" + str(end_time - start_time) + "\n"
    
    start_time = time.time()
    randomoptimize(cipher, 7000) 
    end_time = time.time()
    print "\nRandom Optimize time (seconds):\t" + str(end_time - start_time) + "\n"
    
def annealing_ptesting():
    
    start_time = time.time()
    score = annealingoptimize(cipher, 100000.0, 0.9995, 1)
    end_time = time.time()
    print "\nSimulated Annealing time (seconds):\t" + str(end_time - start_time) + "\n"

    create_graphs(score, 'Simulated Annealing')
    
    start_time = time.time()
    score = annealingoptimize(cipher, 1000000.0, 0.995, 1)
    end_time = time.time()
    print "\nSimulated Annealing time (seconds):\t" + str(end_time - start_time) + "\n"
    
    create_graphs(score, 'Simulated Annealing')
    
    start_time = time.time()
    score = annealingoptimize(cipher, 100000000.0, 0.9995, 1)
    end_time = time.time()
    print "\nSimulated Annealing time (seconds):\t" + str(end_time - start_time) + "\n"
    
    create_graphs(score, 'Simulated Annealing')
    




