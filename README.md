# Botter
Making Various email accounts and storing credentials in a database then using these credentials to leverage account creation
#
#
So far I am working on generating Protonmail email accounts.
Am stuck on Verification section.
I have a theoretical fix for that which has been test.
By using a temporary email for the verification the account can be created.
However there we still need to select the element with the webdriver.
The issue arises because when a radio is selected it completely reloads that area changing the html there.

I could use help figuring out a way around this.

# Dependencies:

python-guerrillamail

selenium

#  Help is wanted

