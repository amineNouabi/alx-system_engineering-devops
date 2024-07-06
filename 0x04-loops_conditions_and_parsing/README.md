# Shell Loops, Conditions,
![](https://phoenixnap.com/kb/wp-content/uploads/2021/12/individual.sh-for-loop-script.png)

## Use this command to generate RSA key `ssh-keygen -t rsa`

## Learning objectives

- How to create SSH keys
- What is the advantage of using `#!/usr/bin/env` bash over `#!/bin/bash`
- How to use `while`, `until` and `for` loops
- How to use `if`, `else`, `elif` and case condition statements
- How to use the `cut` command
- What are files and other comparison operators, and how to use them

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted on `Ubuntu 20.04 LTS`
- All your files should end with a new line
- A README.md file, at the root of the folder of the project, is mandatory
- All your Bash script files must be executable
- You are not allowed to use `awk`
- Your Bash script must pass `Shellcheck` (version 0.7.0) without any error
- The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of all your Bash scripts should be a comment explaining what the script doing

## Concepts

- `env`
- `cut`
- `for`
- `while`
- `until`
- `if`

## Tasks

<details>
<summary><a href="./0-RSA_public_key.pub">0. Create a SSH RSA key pair</a></summary><br>
<a href='https://postimages.org/' target='_blank'><img src='https://i.postimg.cc/HkVtBRMg/image.png' border='0' alt='image'/></a><br>
<ul>
  <li>Links from screenshot
  <ul>
      <li><a href="https://askubuntu.com/questions/61557/how-do-i-set-up-ssh-authentication-keys">Linux and Mac OS users</a></li>
      <li><a href="https://docs.rackspace.com/support/how-to/generating-rsa-keys-with-ssh-puttygen/">Windows users</a></li>
      <li><a href="https://www.youtube.com/watch?v=iuqXFC_qIvA&t=46s">data centers</a></li>
  </ul>
  </li>
</ul>
</details>

<details>
<summary><a href="./1-for_best_school">1. For Best School loop</a></summary><br>
<a href='https://postimages.org/' target='_blank'><img src='https://i.postimg.cc/XYvX60Nr/image.png' border='0' alt='image'/></a>
</details>

<details>
<summary><a href="./2-while_best_school">2. While Best School loop</a></summary><br>
<a href='https://postimages.org/' target='_blank'><img src='https://i.postimg.cc/KcfDJy01/image.png' border='0' alt='image'/></a>
</details>

<details>
<summary><a href="./3-until_best_school">3. Until Best School loop</a></summary><br>
<a href='https://postimages.org/' target='_blank'><img src='https://i.postimg.cc/y8jvVtx4/image.png' border='0' alt='image'/></a>
</details>

<details>
<summary><a href="./4-if_9_say_hi">4. If 9, say Hi!</a></summary><br>
<a href='https://postimages.org/' target='_blank'><img src='https://i.postimg.cc/vBCCykBL/image.png' border='0' alt='image'/></a>
</details>

<details>
<summary><a href="./5-4_bad_luck_8_is_your_chance">5. 4 bad luck, 8 is your chance</a></summary><br>
<a href='https://postimages.org/' target='_blank'><img src='https://i.postimg.cc/SxMkcYGF/image.png' border='0' alt='image'/></a><br>
<ul>
  <li>Links from screenshot
  <ul>
      <li><a href="https://freakonomics.com/2006/07/05/lucky-8s-in-china/">8 in the Chinese culture</a></li>
      <li><a href="https://en.wikipedia.org/wiki/Chinese_numerology#Four">4 in the Chinese culture</a></li>
  </ul>
  </li>
</ul>
</details>

<details>
<summary><a href="./6-superstitious_numbers">6. Superstitious numbers</a></summary><br>
<a href='https://postimages.org/' target='_blank'><img src='https://i.postimg.cc/XvHdRPT0/image.png' border='0' alt='image'/></a>
</details>

<details>
<summary><a href="./7-clock">7. Clock</a></summary><br>
<a href='https://postimages.org/' target='_blank'><img src='https://i.postimg.cc/YqRc5vMR/image.png' border='0' alt='image'/></a>
</details>

<details>
<summary><a href="./8-for_ls">8. For ls</a></summary><br>
<a href='https://postimages.org/' target='_blank'><img src='https://i.postimg.cc/wjzrjgTv/image.png' border='0' alt='image'/></a>
</details>

<details>
<summary><a href="./9-to_file_or_not_to_file">9. To file, or not to file</a></summary><br>
<a href='https://postimages.org/' target='_blank'><img src='https://i.postimg.cc/RFwsBY5f/image.png' border='0' alt='image'/></a>
</details>

<details>
<summary><a href="./10-fizzbuzz">10. FizzBuzz</a></summary><br>
<a href='https://postimages.org/' target='_blank'><img src='https://i.postimg.cc/85bsJLq3/image.png' border='0' alt='image'/></a>
</details>

<details>
<summary><a href="./100-read_and_cut">11. Read and cut</a></summary><br>
<a href='https://postimages.org/' target='_blank'><img src='https://i.postimg.cc/FHQyLVqF/image.png' border='0' alt='image'/></a>
</details>

<details>
<summary><a href="./101-tell_the_story_of_passwd">12. Tell the story of passwd</a></summary><br>
<a href='https://postimages.org/' target='_blank'><img src='https://i.postimg.cc/g0vNZG3x/image.png' border='0' alt='image'/></a>
<ul>
  <li>Links from screenshot
  <ul>
      <li><a href="https://www.cyberciti.biz/faq/understanding-etcpasswd-file-format/">Understanding /etc/passwd</a></li>
      <li><a href="https://tldp.org/LDP/abs/html/internalvariables.html">IFS (internal field separator)</a></li>
  </ul>
  </li>
</ul>
</details>

<details>
<summary><a href="./102-lets_parse_apache_logs">13. Let's parse Apache logs</a></summary><br>
<a href='https://postimg.cc/rDm2Zg6H' target='_blank'><img src='https://i.postimg.cc/P5bfxFSd/image.png' border='0' alt='image'/></a>
<ul>
  <li>Links from screenshot
  <ul>
      <li><a href="https://en.wikipedia.org/wiki/Apache_HTTP_Server">Apache HTTP Server</a></li>
      <li><a href="https://en.wikipedia.org/wiki/List_of_HTTP_status_codes">HTTP status codes</a></li>
      <li><a href="https://www.the-art-of-web.com/system/logs/">System: Analyzing Apache log Files</a></li>
  </ul>
  </li>
</ul>
</details>

<details>
<summary><a href="./103-dig_the-data">14. Dig the data</a></summary><br>
<a href='https://postimages.org/' target='_blank'><img src='https://i.postimg.cc/T2WBc5gs/image.png' border='0' alt='image'/></a>
</details>
