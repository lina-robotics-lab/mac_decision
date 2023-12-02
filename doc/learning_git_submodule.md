# Learning git submodule
## Basics
[Major reference](https://git-scm.com/book/en/v2/Git-Tools-Submodules)
- Create a submodule
    ```bash
    git submodule add $URL
    ```
- commit the submodule

- Cloning with submodule
  
  If directly clone the parent dict, the submodule dict will be cloned but empty. Run this to get the code
  ```bash
  git submodule init
  git submodule update
  ```

## Working with submodule
- Every time changing the submodule, parent module will also have a change. You need to also commit the parent module.

- Updating the submodule 
  ```bash
  git submodule update --remote $REPO_NAME
  ```
  tracking the change of *default* branch.

  If would like to track other branch, do 

  Then the `.gitmodules` file will change to
  ```
  [submodule "src/SafeMaC"]
	path = src/SafeMaC
	url = https://github.com/mahaitongdae/SafeMaC.git
	branch = dev_demo
  ```