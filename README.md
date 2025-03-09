# Code Delicious, an Open-Source Plant-Based Cookbook

Welcome to Code Delicious! In this repository, we are attempting to create an open-source Plant-Based cookbook that anyone can submit recipes to! All recipes in this repository will be viewable on the live site, [https://multiplemonomials.github.io/Code-Delicious/](https://multiplemonomials.github.io/Code-Delicious/).

All recipes in this repo must have been tested and verified by me (Jamie) or another contributor to the project. So, you can trust that the recipes here actually work, and produce food that is worth your time to cook. And I'm a programmer, and I think about recipes as programs as much as anything else. So, you have my guarantee that the steps in each recipe will be written as cleanly and clearly as I can manage.

Why a GitHub repo? Well, even as we have entered the digital age, recipes and how they are distributed haven't changed much: whether through a cookbook or a website, one person will test and publish recipes, and others have to use those recipes as is, without any ability to make fixes or suggestions. Using a distributed version control system such as GitHub is a natural evolution to this process. Find something that's unclear, or figure out a way to make one of these recipes better? Leave an issue or submit a pull request! I can't promise that every change will be accepted, but GitHub does provide an elegant way to submit and discuss feedback.

There's also another reason. As humanity's struggles with our climate get worse, and as the damage that large scale agriculture is causing to the environment becomes more apparent, I believe it is more important than ever that people eat as much plant-based food as possible. If there was ever a time to get possessive about recipes, that time has long passed. I hope that by sharing high-quality, well-tested vegan recipes with anyone who accesses this site, it will make at least a tiny difference.

## Submission Criteria

Anyone can propose a recipe to include in this site by making a pull request that adds the recipe (in markdown format) to the `content` folder of this repository. For inclusion, recipes must be vegan.

Also, simply transcribing existing recipes from cookbooks is NOT allowed. While almost every recipe is inspired by something else, recipes must be materially different in some way from their original source to be eligible for inclusion here.

## Setup Instructions

Create a venv and install pelican into it:
```shell
python3 -m venv venv # on Windows use python instead of python3
source venv/bin/activate.sh # on Windows with Powershell, run 'venv\Scripts\Activate.ps1'
pip install -r requirements.txt
```

## Building the Site Locally

In Bash:
```shell
pelican -r -l -e SITEURL='"http://127.0.0.1:8000"'
```

In cmd:
```batch
pelican -r -l -e "SITEURL=""http://127.0.0.1:8000"""
```

In PowerShell:
```ps
pelican -r -l -e 'SITEURL=\"http://127.0.0.1:8000\"'
```