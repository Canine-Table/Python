#!/usr/bin/python3

if __name__ != "__main__":

    def my_animal_lists():

        return [num for elem in [
                ["oryx","bat","mouse","panda","dormouse","woodchuck","octopus","pig","jackal","opossum"],
                ["dung beetle","guanaco","parakeet","coati","wolf","prairie dog","starfish","lynx","musk deer","lion"],
                ["bull","budgerigar","gnu","koala","jaguar","eland","squirrel","waterbuck","lovebird","mink"]
            ] for num in elem]
