import shutil
import os
import git
from git import Repo
import json
import time

foulderNames = []
cloneURL = []

# Get all url's from the json file and clone the repos 
def init():
        with open('./repos.json', encoding='utf-8') as data_file:
                data = json.loads(data_file.read())

        list(map(lambda a: cloneURL.append(a['clone_url']), data))
        # if os.path.isdir('./lesson1'):
        #         clone()
        # else: 
        #         pull()
        clone()

# Deletes all files that are different than readme.md
def deleteExcessFiles(foulder):
        print('Cleaning extra files')
        for i in range(len(foulder)):
                foulderItems = os.listdir(foulder[i])
                for j in foulderItems:
                        if os.path.isfile(j) and j != 'README.md' and j != '.git':
                                os.remove(f'{os.getcwd()}/{foulder[i]}/{j}')
                        elif j != '.git' and j != 'README.md' and j !='.DS_Store':
                                shutil.rmtree(f'{os.getcwd()}/{foulder[i]}/{j}')  
        mapTextFiles(foulderNames) 

def mapTextFiles(foulders):
        print('Writing on your file')
        newText = open("required_reading.md", 'w')
        paragraph = []
        for i in foulders:
                with open(f'./{i}/README.md') as f:
                                for line in f:
                                        if "## Required reading" in line:
                                                paragraph.append(line)
                                                newText.write(line)
                                                continue
                                        if paragraph and line != '\n' or paragraph:
                                                if line != '\n':
                                                        newText.write(line)
                                                        continue
                                        if line == '\n':
                                                paragraph = []
                                                continue
        newText.close()
        push(newText)

def clone():
        for i in range(len(cloneURL)):
                print(f'Cloning repositories','.' * i)
                foulderNames.append('lesson' + str(i + 1)) 
                Repo.clone_from(cloneURL[i], 'lesson' + str(i + 1))
        deleteExcessFiles(foulderNames)
def pull():
        
        deleteExcessFiles(foulderNames)

def push(textFile):
        if textFile:
                print('Pushing to git')
                try:
                        repo = Repo('./')
                        repo.git.add(update=True)
                        repo.index.commit("new text file")
                        origin = repo.remote(name='origin')
                        origin.push()
                except:
                        print('Some error occured while pushing the code')
                finally:
                        print('Code push from script succeeded')       


                                                        
def main():
        # push()
        init()

if __name__ == '__main__':
        main()