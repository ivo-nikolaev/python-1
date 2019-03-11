import shutil
import os
import git
from git import Repo
import json

foulderNames = []
cloneURL = []

# Get all url's from the json file and clone the repos 
def init():
        with open('./repos.json', encoding='utf-8') as data_file:
                data = json.loads(data_file.read())

        list(map(lambda a: cloneURL.append(a['clone_url']), data))
        for i in range(len(cloneURL)):
                foulderNames.append('lesson' + str(i + 1)) 

        if os.path.isdir(f'./{foulderNames[0]}'):
                pull()
        else: 
                clone()

# Deletes all files that are different than readme.md
def deleteExcessFiles():
        print('Cleaning extra files')
        for i in range(len(foulderNames)):
                foulderItems = os.listdir(foulderNames[i])
                for j in foulderItems:
                        if os.path.isfile(j) and j != 'README.md' and j != '.git':
                                os.remove(f'{os.getcwd()}/{foulderNames[i]}/{j}')
                        elif j != '.git' and j != 'README.md' and j !='.DS_Store':
                                shutil.rmtree(f'{os.getcwd()}/{foulderNames[i]}/{j}')  
        mapTextFiles() 

def mapTextFiles():
        print('Writing on your file')
        newText = open("required_reading.md", 'w')
        paragraph = []
        for i in foulderNames:
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
        push()

def clone():
        for i in range(len(cloneURL)):
                print(f'Cloning repositories','.' * i)
                Repo.clone_from(cloneURL[i], 'lesson' + str(i + 1))
        deleteExcessFiles()

def pull():
        for i in range(len(cloneURL)):
                print(f'Pulling from repositories','.' * i)
                repo = git.Repo(f'./{foulderNames[i]}')
                o = repo.remotes.origin
                o.pull()
        deleteExcessFiles()

def push():
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
        push()
        # init()

if __name__ == '__main__':
        main()