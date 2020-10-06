# saesite2020
## How to Contribute: 

1. Fork the project.
2. Make any changes in your forked repo
3. On this repo, click `Pull Requests` and raise a `Pull Request` selecting your fork on the right drop down

Questions can be asked by raising an `Issue`.

## How to clone repo and make changes locally: ✂📋

```
  click on the clone button (green in colour). This gives you a copy of the project. Its now yours to play around with
```

- Using git on your local machine. Do this to download the forked copy of this repo to your computer

```
  git clone https://github.com/yourGitHubUsername/saesite2020.git
```
cd saesite2020

- Make a new branch. Your name would make a good branch because it's unique

```
  git checkout -b <name of new branch>
```

-activate virtualenv
  ```
  Scripts\activate
  ```
-Do the required changes.
- Stage your changes
  - For example, if you have added 1 file
    ``` 
    git add ".location/filename" 
    ```
  - If there are many files, to add all the files use 
    ``` 
    git add .
    ```

- Commit the changes

```
  git commit -m "Initial commit"
```

- Check the status of your repository

```
  git status
```

- Pushing your repository to github

```
  git push origin <name of your branch>
```

- Pulling your request. Click on the Pull requests tab on the forked github repository.
  - ***Note : A pull request allows your changes to be merged with the original project.***

```
  Click on Pull Request
```

- Wait for your changes to be merged

