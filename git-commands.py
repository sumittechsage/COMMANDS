# GIT CLI :-
'''
1. LOGIN USING WEB BROWSER GIT HUB CREDENTIALS.
2. SSH KEY
3. TOKEN 

# LOGIN 
COMMAND :- gh auth login
'''


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


# HEAD 
'''
# HEAD IS THE MOST IMPORTANT POINTER BUT COVERED BECAUSE OF ABSTRACTION.
# HEAD INITALLY POINTS TO THE POINTER POINTING DEFAULT BRANCH  (HEAD(ptr) -> MAIN(ptr))
# WHATEVER WE DO, CREATING NEW COMMIT, CREATING NEW BRACH, SWITCHING BRANCH OR ANY OTHER OPERATION MOSTLY ALL THESE OPERATIONS REQURIES HEAD TO POINT THEM FIRST.

# HOW TO DEATTACH HEAD ? (MEANS CURRENTLY HEAD IS POINTING TO A BRACH POINTER, IF MAKE OUR HEAD TO POINT TO THE COMMIT WHERE THE BRANCH POINTER IS POINTING OR ANY OTHER COMMIT IT MEANS WE DEATTACHED THE HEAD FROM BRANCH AND NOW WHATEVER OPERATIONS WILL WE MAKE OUR BRANCH WILL NOT FOLLOW INSTEAD THEY WILL BE ON HEAD.)
COMMAND :- git checkout commit_hash
'''


# BRANCHEs
'''
=> A BRANCH IS JUST A POINTER POINITING TO A COMMIT. 

# TO CREATE A NEW BRANCH ?
COMMAND :- git branch branch_name

# HOW TO DELETE ANY BRACH EXCEPT FOR THE CURRENT BRANCH ?
COMMAND :- git branch -d branch_name

----------------------------- CHECKOUT OPERATIONS WORKS ON DEATTACHING AND ATTACHING THE HEAD -------------------------

# HOW TO CHANGE THE HEAD POINTER TO ANOTHER BRANCH FROM CURRENT BRANCH ON OUR SYSTEM ?
# COMMAND :- git checkout branch_name

# HOW TO CREATE A NEW BRANCH FROM THE COMMIT POINTED BY THE HEAD AND CHECKOUT TO THE CURRENTLY CREATED BRANCH?
COMMAND :- git checkout -b branch_name

'''


# MERGE AND PULL CODE
'''
=> MERGE US TO CREATE A COMMIT WHICH WILL HAVE TWO UNIQUE COMMITS AS ITS PARENTS.

# HOW TO MERGE CHANGES FROM ANOTHER BRANCH TO THE CURRENT BRANCH?

# STEP 1: FIRST SEE THE DIFFERNCE BETWEEN TWO BRANCHES.
COMMAND: git diff branch_to_merge

# STEP 2: MERGE A BRANCH INTO THE CURRENT CHECKOUT BRANCH 
COMMAND: git merge branch_name

# HOW TO PULL(FETCH AND MERGE) CHANGES FROM REMOTE?
COMMAND: git pull origin main
'''

# GIT REBASE
'''
=> The second way of combining work between branches is rebasing. Rebasing essentially takes a set of commits, "copies" them, and plops them down somewhere else.

# HOW TO REBASE(MOVE OUR CURRENT BRANCH/COMMIT'S(HEAD'S) WORK ONTO ANOTHER BRANCH/COMMIT(HEAD'S)) ?
COMMAND: git rebase commit_address

'''

# MOVE HEAD AND BRANCH POINTER
'''
# MOVING HEAD (changes are there we are just making our head points to the previous commit) BY MOVING YOUR POINTER TO THE PRECIOUS COMMIT
# SITUATION :- If we want to go to the one commit back in our MAIN branch.

# HOW COMMAND TAKES ARGS HERE :- after the keyword checkout the arg should be the commit where we want our head to point. here it is main^ means the commit previous to the commit pointed by main branch.
COMMAND :- git checkout main^     :- IT WILL MOVE OUR HEAD POINTER TO  THE ONE COMMIT BACK FROM THE COMMIT POINTED BY OUR MAIN POINTER. 


# MOVING BRANCH POINTER
# MOVING BRANCH POINTER (changes are there just our branch pointer is pointing to another/previous commit)

# here main is the branch pointer which want to move and followed by commit which we want to point which is HEAD~3(commit which is 3 commits behind the commit pointed by HEAD)
COMMAND :- git branch -f main HEAD~3
'''

# UNDO CHANGES
'''
1. BY RESET :-  RESET WORKS GREAT FOR THE LOCAL MACHINE BUT ON REMOTE REPO USED BY OTHER IT WON'T AFFECT
    # MODES OF RESETTING  
         --soft: Moves the branch pointer to the specified commit but leaves the index and working directory unchanged.
        --mixed (default): Moves the branch pointer to the specified commit and resets the index, but leaves the working directory unchanged. This means changes between the specified commit and the current HEAD will be unstaged.
       --hard: Moves the branch pointer to the specified commit and resets both the index and working directory to match the specified commit. All changes in the working directory are discarded.

    # ONE CAN FORCE CHANGES ONTO REMOTE MADE BY RESET BY FORCE PUSHING, BUT THIS SHOULD BE DONE WITH CAUTION AS THE OTHER COLLOBORATERS MIGHT BE AFFECTED AND THE CHANGES WILL BE LOST FOREVER.  
       

2. BY REVERT :- RESET CHANGES AND SHARE THOSE CHANGES WITH OTHERS

# UNDO STAGED CHANGES
COMMAND :- git reset filename
COMMNAD :- git reset .


# UNDO COMMITED CHANGES BY RESETTING
COMMAND :- git reset HEAD~1
COMMAND :- git reset commit_hash   (changes will be removed from git but remain in system/vscode and will need to stage and commit them again.)
COMMAND :- git reset --hard commit_hash   (changes after the hash_commit will be removed from the system too.)

# UNDO CHANGES AND SHARE WITH OTHER MAKE A NEW COMMIT FROM THE COMMIT WE WANT TO MOVE AND ADD IT AHEAD OF THE COMMIT WE WANT TO REMOVE. KEEPS THE RECORD.
COMMAND :- git revert commit   


# UNDO CHANGES IN A UNSTAGED BUT TRACKED FILE
COMMAND :- git checkout -- file_path

# UNDO CHANGES IN MULTIPLE UNSTAGED BUT TRACKED FILES
COMMAND :- git checkout -- file1.txt file2.txt file3.txt
'''

# CHERRY PICK
'''
# It's a very straightforward way of saying that you would like to copy a series of commits below your current location (HEAD)
SYNTAX :- git cherry-pick <Commit1> <Commit2> <...>


# INTERACTIVE REBASE
=> When you hit the REABSE COMMAND with -i, an interactive rebase window will appear. Reorder some commits around see the result!
COMMAND :- git rebase -i HEAD~4
'''


# ADD NEW REMOTE URL/ CHANGED/ RENAMED REPO ON REMOTE
'''
# HOW TO SET UPDATED REMOTE URL TO CURRENT REPO
COMMAND :- git remote set-url origin new-url
'''