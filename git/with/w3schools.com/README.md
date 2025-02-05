# Git cli commands for used.



### list shortly the status.
```shell
git status --short # or -s
```

### create and select new branch
this command will be create and select halona branch.
```shell
git checkout -b halona
```

### delete branch
this command will be deleted halona branch if exists.
```shell
git checkout -d halona
```

### merge files another branch to current branch.
this command will be merged halona branch to current branch (main).
```shell
git merge halona
```

# remote
```shell
git remote add origin [url] &&
git push --set-upstream origin master
```

git pull is combination of fetch and merge.