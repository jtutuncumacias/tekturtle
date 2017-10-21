#Mad Libs

#Concepts:
#-input
#-functions

lib1 = "Today I went to the zoo. I saw a "
lib2 = " jumping up and down in its tree. He "
lib3 = " through the large tunnel that led to its "
lib4 = ". I got some peanuts and passed them through the cage to a gigantic gray "
lib5 = " towering above my head. Feeding it made me hungry. I went to get a "
lib6 = " scoop of ice cream. It filled my stomach. Afterwards I "
lib7 = " to catch our bus. When I got home I told my mom about my "
lib8 = " day at the zoo."

def getNoun():
    noun = input("Please enter a noun: ")
    return noun

def getVerb():
    verb = input("Please enter a verb in the past tense: ")
    return verb

def getAdjective():
    adjective = input("Please enter an adjective: ")
    return adjective

print(lib1 + getAdjective() + " " + getNoun() + lib2 + getVerb() + lib3 +
      getNoun() + lib4 + getNoun() + lib5 + getAdjective() + lib6 + getVerb() +
      lib7 + getAdjective() + lib8)


