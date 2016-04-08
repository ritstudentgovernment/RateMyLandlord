# RateMyLandlord
Landlord and property rating site designed for the Rochester community. Next: the world. 

## Motivation
Rate My Landlord was created to empower students seeking housing in the Rochester community. 

## Project Organization
Coming soon...

## Developers - Installation
- Create virtual environment for the python application, with >= python 3.4
- run `pip install -r requirements.txt`
- run `ln -s -f hooks/pre-commit .git/hooks/pre-commit`

## Workflow - how to push code

In an attempt to ensure some type of quality control, we'll be using a 
pull-request, review and then merge workflow. 


```
$ git branch user-dev-branch        # specify your working branch
// do code
// test personally
$ git add --all                     
$ git commit -m "message"           # commit your work, with a helpful commit message!
$ git push origin user-dev-branch   # will push to a remote branch
```

Using the Github website, you can then make a pull request against 
the current master-working branch. The current master-working branch is `dev`.
A travisCI build will be triggered. 

Once a pull request has been made <b> please wait for two reviews before merging </b> as well
as a successful travis build.

## Contributing
This project was built based on the [Requirements Doc](https://docs.google.com/document/d/1BlJj_FgGth0pj5qa73X4nh9E8uXhNqFFHVbEO_nVxFU/edit?usp=sharing). The project was started at RIT Student Government and is part of our commitment to open source. 

Pull requests welcome! Check out the issues for anything marked as "bug" or "help wanted". 

## Installation

Coming soon...

## License
This project is released under the MIT license. 
