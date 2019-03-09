import shutil
import os
from git import Repo
import json

# Get all url's from the json file and clone the repos 
def init():
        with open('./repos.json', encoding='utf-8') as data_file:
                data = json.loads(data_file.read())
        cloneURL = []
        foulderNames = []
        list(map(lambda a: cloneURL.append(a['clone_url']), data))
        for i in range(len(cloneURL)):
                foulderNames.append('lesson' + str(i + 1)) 
                Repo.clone_from(cloneURL[i], 'lesson' + str(i + 1))
        deleteExcessFiles(foulderNames)

# Deletes all files that are different than readme.md
def deleteExcessFiles(foulder):
        for i in range(len(foulder)):
                foulderItems = os.listdir(foulder[i])
                for j in foulderItems:
                        if os.path.isfile(j) and j != 'README.md' and j != '.git':
                                os.remove(f'{os.getcwd()}/{foulder[i]}/{j}')
                        elif j != '.git' and j != 'README.md' and j !='.DS_Store':
                                shutil.rmtree(f'{os.getcwd()}/{foulder[i]}/{j}')   
def main():
        init()

if __name__ == '__main__':
        main()