# pycmgr
a package for obscuring and hiding credentials in your code

the problem:
I want to use my credentials in my code, but I don't want others to see them.
the script itself is (maybe) publicly readable, so we don't want anyone that 
views the code to have our credentials.

we can keep a file with the secrets in a restricted directory, but what if
some administrator decides to grep things?

we need:
1) a way to keep our credentials database in an obscured way (even encoded using a private key)
2) a way to have the information usable when needed in our script
3) a way to share our script with others without sharing the credentials

NOTE:
if someone can "sudo" run with your user, there isn't much you can do because they can 
just print out the decoded credentials (unless you actively control the access to a hidden
path where the database is kept, and it could only be imported if you know where it is)

generate the database:
<code here>

save the database file in a secure directory and add it (the path) to PYTHON_PATH only for yourself!

use the database:
<code here>
