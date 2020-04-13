#!/bin/zsh

cd ~/markdeep
git status

git add .

read input

git commit -m $input

git push

exit
