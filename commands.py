# Global Account Config :-

'''
(set the account to make changes for all the changes made on the system)

@ SET USERNAME ?
COMMAND :- git config --global user.name "gamersumit"

@ SET EMAIL ?
COMMAND :- git config --global user.email "s*****.com"

@ HOW TO SEE THE CURRENT ACCOUNT SET UP ?
COMMAND :- git config --list
'''


# CLONE:

'''
# local :- Repos/folder on our system/pc
# remote :- Repos on  remote/github


@ CLONE A REPO THROUGH GITHUB URL ON OUR LOCAL MACHINE/SYSTEM/PC
COMMAND :- git clone clone_url
>> By this command "origin" will be set as the name of remote repo from which we are cloning will be set as origin on our local machine or system.

COMMAND :- git clone -o gamer clone_url
>> By this command "gamer" is the name for remote repo on our local machine or system.
$ cd(change dir) TO THE CLONED REPO.

'''

# STATUS:

'''
#  THERE ARE 4 TYPES OF STATUS :-
    1. UNTRACKED :- IF A NEW FILE OR DIR IS ADDED INSIDE THE REPO WHICH IS NOT COMMITTED EVER BEFORE
    2. MODIFIED :- IF SOME LINE OF CODE IS ADDED OR CHANGED IN A FILE
    3. STAGED :- THE FILE IS READY TO BE COMMITTED.
        !! BEFORE STAGE LET'S UNDERSTAND COMMIT FIRST. 
        >> COMMITNG CHANGES IS A TWO STEP PROCESS :-
            a) WE HAVE TO "ADD" THE CHANGES FIRST WHICH WE WANT TO COMMIT. e.g :- IF THERE ARE 5 CHANGES IN DIFFERENT FILES AND YOU ONLY HAVE TO COMMIT.
            b) WE HAVE TO COMMIT CHANGES ON OUR SYSTEM(THESE ARE NOT ON GITHUB YET BUT TRACKED BY GIT ON OUR SYSTEM.)
        
        >> AFTER ADDING THE CHANGES OF A FILE. IT IS READY TO BE COMMITED. AND THIS STATE IS KNOWN AS STAGED.
    
    4. UNMODIFIED :- NO CHANGES IN THE FILE.

    
@ HOW TO CHECK GIT STATUS FOR CURRENT REPO ?
COMMAND :- git status
'''


# ADD & COMMIT:-
'''
@ How to add a single file to the staging files ?
COMMAND :- git add file name
$ e.g :- git add requirements.txt

@ HOW TO ADD ALL THE CHANGED FILE IN STAGING AREA ?
COMMAND :- git add .

@ HOW TO COMMIT CHANGES? :-
COMMAND :- git commit -m "message"

# EVERY COMMIT HAS A UNIQUE ID KNOWN AS COMMIT HASH.

@HOW TO VIEW COMMITS INFORMATION?
COMMAND :- git log

'''

# PUSH Command
'''
# PUSH :- upload local repo latest commit to remote repo.

@ HOW TO PUSH A COMMIT TO REMOTE REPO FROM LOCAL REPO.
$ COMMAND MEANING :- git push original_repo_name(remote repo name) branch_name_in_which_we_want_to_push_cahnges
COMMAND :- git push origin main
COMMAND :- git push -u origin main      (by using this command we have set or main branch as upstream. From now on if we make {git push} it will directly push out code to main with using origin main.)

!! NOTE !!
>> origin is the default name given to the remote repo from which we cloned.
'''

# INIT COMMAND
'''
# INIT :- COMMAND IS USED TO CREATE A NEW GIT REPO FROM OUR SYSTEM/LOCAL MACHINE.

COMMANDS :- 
1. git init                         (initialize current folder as git folder)
2. git remote add origin link       (to add the remote repo into our existing project)
3. git remote -v                    (to verify remote repo name and url)
4. git branch                       (current git branch)
5. git branch -M main               (rename a branch)
6. git push origin branch           (push command)
'''

# BRANCHEs
'''
# HOW TO CREATE A NEW BRANCH ?
COMMAND :- git checkout -b branch_name


# HOW TO CHANGE THE CURRENT BRANCH ON OUR SYSTEM ?
COMMAND :- git checkout branch_name

# HOW TO DELETE ANY BRACH EXCEPT FOR THE CURRENT BRANCH ?
COMMAND :- git branch -d branch_name
'''

# UNDO CHANGES
'''
# UNDO STAGED CHANGES
COMMAND :- git reset filename
COMMNAD :- git reset .


# UNDO COMMITED CHANGES
COMMAND :- git reset HEAD~1
COMMAND :- git reset commit_hash   (changes will be removed from git but remain in system/vscode and will need to stage and commit them again.)
COMMAND :- git reset --hard commit_hash   (changes after the hash_commit will be removed from the system too.)
'''


# MERGE AND PULL CODE
'''
# HOW TO MERGE CHANGES FROM ANOTHER BRANCH TO THE CURRENT BRANCH?

# STEP 1: FIRST SEE THE DIFFERNCE BETWEEN TWO BRANCHES.
COMMAND: git diff branch_to_merge

# STEP 2: MERGE
COMMAND: git merge branch_name

# HOW TO PULL(FETCH AND MERGE) CHANGES FROM REMOTE?
COMMAND: git pull origin main
'''