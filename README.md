# Logs-Analysis  

# what  is the project ?

  - You've been hired onto a team working on a newspaper site. The user-facing newspaper site frontend itself, and the database behind it, are already built and running. You've been asked to build an internal reporting tool that will use information from the database to discover what kind of articles the site's readers like.

 - The database contains newspaper articles, as well as the web server log for the site. The log has a database row for each time a reader loaded a web page. Using that information, your code will answer questions about the site's user activity.



### Requirements For Installation:

-  Python3, because the program is written in python3, download it from [here](https://www.python.org/downloads/) , then install it.
- VirtualBox , the software that actually runs the virtual machine. You can download it from [here](https://www.virtualbox.org/wiki/Downloads) , then install it.
- Vagrant, the software that configures the Vitual Machine and lets you share files between your host computer and the VM's filesystem, you can dwnload it from  [here](https://www.vagrantup.com/downloads.html) , then install it.

### What to do after installing ?
 
- download the VM configuration using this github reository:
you can use Github to fork and clone the repository from [here](https://github.com/udacity/fullstack-nanodegree-vm.).

- Either way, you will end up with a new directory containing the VM files. Change to this directory in your terminal with ```cd```. Inside, you will find another directory called vagrant. Change directory to the vagrant directory, then From your terminal, inside the vagrant subdirectory, run the command ```vagrant up```. This will cause Vagrant to download the Linux operating system and install it.

- When ```vagrant up``` is finished running, you will get your shell prompt back. At this point, you can run ```vagrant ssh``` to log in to your newly installed Linux VM!
- Download the data from [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
you should Unzip this file after downloading it. The file inside is called newsdata.sql.
- To run the reporting tool, you will need to load the site's data into your local database. To load the data, use the command
```psql -d news -f newsdata.sql```

### How to run the program ?
From the vagrant directory inside the virtual machine, run logs_analysis.py using:
``$ python3 LogAnalysis.py```
Check the output file for the results Log-Analysis-output.txt

### You should familiar with postgresql , to know more about its commands , please press [here](http://www.postgresqltutorial.com/) .
