#!/bin/zsh

cd ~/markdeep
git status

echo "开始git add ."
git add .

echo -n "输入commit 描述:"
read input

echo -n "开始commit:"
git commit -m $input

echo -n "开始push:"
git push

exit
