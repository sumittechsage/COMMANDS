# GIT CLI :-
'''
1. LOGIN USING WEB BROWSER GIT HUB CREDENTIALS.
2. SSH KEY
3. TOKEN 

# LOGIN 
COMMAND :- gh auth login
'''

# LEVELS OF CONFIGRATION :-
'''
System level: git config --system --list
Global level: git config --global --list
Local level: git config --local --list
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


# CLONE
'''
# CLONING IS JUST MAKING A COPY OF THE REPO. WE FIRST MAKE A REPO ON INTERNET(GITHUB) SO THAT OUR DATA WILL BE SAFE WHEN OUR LOCAL DATA CAN BE DELETED EAISLY. NOW, WHENEVER WE NEED THAT REPO TO WORK ON ANY SYSTEM OR BY ANY TEAM MEMBERS THEY CAN SIMPLY DOWNLOAD A COPY BY CLONING THE REPO. 
COMMAND:-  git clone remote_repo_url

# CLONING A REPO WILL SET THE COPY OF REPO ON YOUR SYSTEM WITH SOME ADDITIONAL SETTINGS :-
1. THE NAME OF REMOTE REPO TO "origin" FROM WHICH WE CLONED OR MADE THE COPY. WE CAN CHANGE THE NAME ANYTIME  
        -- when cloning a repo we can explicitly specifies the name of remote repo like this :- git clone -o anyname clone_url
        -- TO CHECK THE REMOTE NAME :- git remote -v
        -- To change the name after cloning :- git remote rename old_name new_name

2. ALL THE BRANCHES THAT ON REMOTE (WE WILL SEE WHAT IS A BRANCH IN NEXT STEP).

3. ALL THE BRANCHES DUPLICATES TO TRACK REMOTE CHANGES(THEY ARE NAMED AS REMOTE_NAME/BRANCH) e.g :- origin/main, origin/test etc.
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

# HEAD 
'''
# HEAD IS THE MOST IMPORTANT POINTER BUT COVERED BECAUSE OF ABSTRACTION.
# HEAD INITALLY POINTS TO THE POINTER POINTING DEFAULT BRANCH  (HEAD(ptr) -> MAIN(ptr))
# WHATEVER WE DO, CREATING NEW COMMIT, CREATING NEW BRACH, SWITCHING BRANCH OR ANY OTHER OPERATION MOSTLY ALL THESE OPERATIONS REQURIES HEAD TO POINT THEM FIRST.

# HOW TO DEATTACH HEAD ? (MEANS CURRENTLY HEAD IS POINTING TO A BRACH POINTER, IF MAKE OUR HEAD TO POINT TO THE COMMIT WHERE THE BRANCH POINTER IS POINTING OR ANY OTHER COMMIT IT MEANS WE DEATTACHED THE HEAD FROM BRANCH AND NOW WHATEVER OPERATIONS WILL WE MAKE OUR BRANCH WILL NOT FOLLOW INSTEAD THEY WILL BE ON HEAD.)
COMMAND :- git checkout commit_hash
'''

# REMOTE BRANCHES
'''
# Branches that are used to track changes on remote for our local branches.
# e.g :- orign/main, origin/fixes etc. by default they start with remote name and than / and than our branch name
# THAT IS THE REASON WE USALLY SEE THIS WHEN CLONING : local branch "main" set to track remote branch "o/main"
# As remote branches are only meant to track changes on remote they cannot be pointed by HEAD and we cannot checkout to any remote branch that means we can not change the code in the remote branch instead we have to push the code onto remote and they will track those changes.
# so, git checkout origin/main will move our HEAD to the commit pointed by our origin/main branch not to the origin/main  pointer itself.
# It's not necessary that a branch origin/main should track the changes for main branch instead we can rename our create any branch and set its tracking branch however we want.
        A) git checkout -b newbranch origin/main  :- it will create a new branch and set origin/main as the tracking branch for it.
        B) git branch -u origin/main exsistingbranch :- it will set the origin/main  to track the existing branch.
        C) git branch -u origin/main  :- here the origin/main will be set to track the current branch pointed by the HEAD.
'''

# FETCH
'''
# FETCHING IS SIMPLY DOWNLOADING THE CODE/ NEW CODE/ NEW COMMITS FORM THE REMOTE REPO INTO OUR REMOTE BRANCHES.
# THE NEW COMMITS ON MAIN WILL BE ADDED TO origin/main or whatever remote branch is set for tracking main.
# IT DOES NOT CHANGE, OR MERGE OUR CODE INTO OUR LOCAL BRANCHES. IT JUST DOWNLAOD THE CHANGES INTO REMOTE BRANCHES.
# COMMAND :- git fetch                      # all the changes FROM every branch
# COMMAND :- git fetch origin main          # changes FROM main branch only
# COMMAND :- git fetch remote_name source:destination  # now, here we can actually specify the destination as any of our local or remote branch of our local repo. and the source should be the branches on rempte repo
        -- git fetch origin test:main
        -- git fetch origin test:origin/main
        -- git fetch origin test:test
        -- git fetch origin test:origin/test

        -- if we use branch_name as the source than the remote branch set for tracking that branch along with the destination.
            git fetch origin test:main
            than branch main and origin/test both will be updated 

        -- but if we use the commit as the source than only the destination branch will be updated
           git fecth origin commit_hash:main
           than the main branch will be updated.

        -- if we specify a non existing branch as the destination than the new branch will  be created pointing to the last fetched commit.
            git fetch origin main:new
            
    ! IF WE LEAVE THE SOURCE EMPTY  THAN A NEW BRANCH WILL BE CREATED AT THE HEAD.
        e.g  git fetch origin :new              will create a new branch at the HEAD. 
'''

# MERGE
'''
=> MERGE IS  ADDING THE FETCHED CODE FROM REMOTE BRANCES TO THEIR RESPECTIVE LOCAL BRANCHES WHICH THEY ARE TRACKING.

# HOW TO MERGE CHANGES FROM ANOTHER BRANCH TO THE CURRENT BRANCH?

# STEP 1: FIRST SEE THE DIFFERNCE BETWEEN TWO BRANCHES.
COMMAND: git diff branch_to_merge

# STEP 2: MERGE A BRANCH INTO THE CURRENT CHECKOUT BRANCH or COMMIT 
COMMAND: git merge branch_name

# IF we have fetched some changes from the remote than we will do
COMMAND: git fetch origin/mian; git checkout main; git merge origin/main;
'''


# GIT REBASE
'''
=> The second way of combining work between branches is rebasing. Rebasing essentially takes a set of commits, "copies" them, and plops them down somewhere else.

# HOW TO REBASE(MOVE OUR CURRENT BRANCH/COMMIT'S(HEAD'S) WORK ONTO ANOTHER BRANCH/COMMIT(HEAD'S)) ?
COMMAND: git rebase commit_address 

COMMAND: git rebase destination source

COMMAND: git rebase -i destination source   # IT WILL GIVE MORE CONTROL OVER WHICH COMMITS AND ORDER OF COMMITS TO REBASE.
'''


# PULL
'''
=> PULL IS THE COMBINATION OF FETCH AND MERGE. IT FETCHES ALL THE CHANGES FROM REMOTE REPO TO REMOTE BRANCHES IN OUR SYSTEM THAN MERGE THOSE CHANGES WITH THE RESPECTIVE BRANCHES SET FOR TRACKING.
# HOW TO PULL(FETCH AND MERGE) CHANGES FROM REMOTE?
COMMAND: git pull origin main
COMMAND: git pull

=> PULL CAN BE USED WITH REBASE TOO 
COMMAND:- git pull --rebase
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
COMMAND :- git log -1 --pretty=full    # to specifiy number of commits to view

'''

# PUSH Command
'''
# PUSH :- upload local repo latest commit to remote repo.

@ HOW TO PUSH A COMMIT TO REMOTE REPO FROM LOCAL REPO.
$ COMMAND MEANING :- git push original_repo_name(remote repo name) branch_name_in_which_we_want_to_push_cahnges
COMMAND :- git push origin main
COMMAND :- git push -u origin main      (by using this command we have set or main branch as upstream. From now on if we make {git push} it will directly push out code to main with using origin main.)

=> HERE THE main in git push origin main does'nt only specifies which branch we want to push but it also specifies in which branch on remote we to push our main branch and that will be defined by which remote branch is used to track the main branch genereally its origin/main
=> YOU CAN ALSO PUSH TO ANOTHER BRANCH ON REMOTE FROM A DIFFERENT BRANCH ON LOCAL. HOW ?
COMMAND :- git push origin source:destination
            --> HERE source is reference location on our local to push(it can be a commit or branch or head anything) 
            --> HERE destination is branch location on our remote to push
            e.g if we want to push our test branch commits onto main branch of remote assuming origin  in our remote repo name.
            git push origin test:main 

            --> if we leave the souce as empty than the destination branch will be deleted from the remote
            git push origin :test       will delete the test branch from remote and origin/test from our local.

!! NOTE !!
>> origin is the default name given to the remote repo from which we cloned.
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