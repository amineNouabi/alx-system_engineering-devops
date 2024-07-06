![img](https://assets.imaginablefutures.com/media/images/ALX_Logo.max-200x150.png)
  > shell variable expansion

## Intro
Have you ever found yourself writing a shell script and wanting to incorporate the value of a variable into a command or string? Or maybe you've wanted to manipulate the value of a variable before using it in your script. If so, then you'll want to learn about shell variable expansion. Lets take a deep dive into this powerful feature of the shell and explore some of the various ways you can use it to make your scripts more flexible and efficient

## Resources
Read or watch. 
1. [Expansions](http://linuxcommand.org/lc3_lts0080.php)
2. [Shell arithmetic](https://www.gnu.org/software/bash/manual/html_node/Shell-Arithmetic.html)
3. [Variables](https://tldp.org/LDP/Bash-Beginners-Guide/html/sect_03_02.html)
4. [Shell init files](https://tldp.org/LDP/Bash-Beginners-Guide/html/sect_03_01.html)
5. [The alias command](https://tldp.org/LDP/Bash-Beginners-Guide/html/sect_03_01.html)
6. [Technical writting](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/misc/2021/6/9112669886fd446a2aa3113c31319d1f468dc160.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230107%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230107T205221Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=c01637fc9adee4b178a6e71b5628c99b434f6f79f3aca4137a3331f94b85dccc)

## Man or Help
* ```printenv```
* ```set```
* ```unset```
* ```export```
* ```alias```
* ```unalias```
* ```.```
* ```source```
* ```printf```


## Learning objectives
By the end of this project, you should be able to [explain to anyone](https://fs.blog/feynman-learning-technique/?fbclid=IwAR2K5_BGPVo0QjJXkOIIqNsqcXK4lTskPWJvA0asKQIGtCPWaQBdKmj1Ztg) __Without the help of google__ the following concepts

### General
* [X] What happens when you type $ ```ls -l *.txt```

### Shell intialization files
* [X] What are the ```/etc/profile``` file and the ``` /etc/profile.d``` directory
* [X] What is the ```~/.bashrc``` file

### Variables
* [X] What is the difference between a local and a global variable
* [X] What is a reserved variable
* [X] How to create, update and delete shell variables
* [X] What are the roles of the following reserved variables: ```HOME```, ```PATH```, ```PS1```
* [X] What are special parameters
* [X] What is the special parameter ```$??```

### Expansions
* [X] What is expansion and how to use them
* [X] What is the difference between single and double quotes and how to use them properly
* [X] How to do command substitution with ```$()``` and backticks

### Shell Arithmetic
* [X] How to perform arithmetic operations with the shell

### The ```alias``` command

* [X] How to create an alias
* [X] How to list aliases
* [X] How to temporarily disable an alias

### Other help pages
* [X] How to execute commands from a file in the current shell

### More info
Read your ``` /etc/profile```, ```/etc/inputrc ```and ```~/.bashrc ``` files.

Look at some files in the ```/etc/profile.d``` directory.

Note: You do not have to learn about ```awk```, ```tar```, ```bzip2```, ```date```, ```scp```, ```ulimit```, ```umask```, or shell scripting, yet.

## Tasks

0. [\<o>](./0-alias) : A script that creates an alias.
   - Name of alias: `ls`
   - Value: `rm *` 
1. [Hello you](./1-hello_you) : A script that prints `hello user`, where user is the current Linux user.
2. [The path to success is to take massive, determined action](./2-path) : A script that adds `/action` to the `PATH`. `/action` should be the last directory the shell looks into when looking for a program.
3. [If the path be beautiful, let us not ask where it leads](./3-paths) : A script that counts the number of directories in the `PATH`.
4. [Global variables](./4-global_variables) : A script that prints all the enviroment variables.
5. [Local variables ](./5-local_variables) : A script that lists all local variables and enviroment variables, and functions.
   - Name of variable : `HOLBERTON`
   - Value : `Betty`
6. [Local variable](./6-create_local_variable) : A script that creates a new local variable.
7. [Global variable](./7-create_global_variable) : A script that creates a new global variable.
   - Name of variable : `HOLBERTON`
   - Value : `Betty`
8. [Every addition to true knowledge is an addition to human power](./8-true_knowledge) : A script that prints the results of the addition of 128 with the value stored in the enviroment variable `TRUEKNOWLEDGE`, followed by a new line.
   - Remember to export variable TRUEKNOWLEDGE : `export TRUEKNOWLEDGE=1209`
   - Run command this way: `./8-true_knowledge | cat -e`
9. [Divide and rule](./9-divide_and_rule) : A script that prints the result of `POWER` divide by `DIVIDE`, followed by a new line.
   - `POWER` and `DIVIDE` are environment variables.
   - Variables values;
    - export POWER=42784
    - export DIVIDE=32
   - Run command this way: `./9-divide_and_rule | cat -e`
10. [Love is anterior to life, posterior to death, initial of creation, and the exponent of breath](./10-love_exponent_breath) : A script that displays the result of `BREATH` to the power of `LOVE`.
    - `BREATH` and `LOVE` are enviroment variables.
    - The script should display the result, followed by a new line.
11. [There are 10 types of people in the world -- Those who understand binary, and those who don't](./11-binary_to_decimal) : A script that converts a number from base 2 to base 10.
    - The number in base 2 is stored in the enviroment variable `BINARY`.
    - The script should display the number in base 10, followed by a new line.
12. [Combination](./12-combinations) : A script that prints all possible combinations of two letters, except `oo`.
    - Letters are lower cases, from `a` to `z`.
    - One combination per line.
    - The output should be alpha ordered, starting with `aa`.
    - Do not print `oo`.
    - Your script file should contain maximum 64 characters.
13. [Floats](./13-print_float) : A script that prints a number with two decimal places, followed by a new line.
    - The number will be stored in the enviroment variable `NUM`.
14. [Decimal to Hexadecimal](./100-decimal_to_hexadecimal) : A script that converts a number from base 10 to base 16.
    - The number is base 10 is stored in the enviroment variable `DECIMAL`.
    - The script should display the number in base 16, followed by a new line.
15. [Everyone is a proponent of strong encryption](./101-rot13) : A script that encodes and decodes text using the rot13 encryption. Assume ASCII.
16. [The eggs of the brood need to be an odd number](./102-odd) : A script that prints every other line from the input, starting with the first line.
17. [I'm an instant star. Just add water and stir.](./103-water_and_stir) : A script that adds the two numbers stored in the enviroment variables `WATER` and `STIR` and prints the results.
    - `WATER` is in base `water`.
    - `STIR` is in base `stir`.
    - The result should be in base `behlnort`.
