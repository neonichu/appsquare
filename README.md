# appsquare

Import [Foursquare][1] check-ins to your [Ohai][2] [ADN][3] journal. 

This is **alpha** software, I am not responsible for any issues with it, but I am glad to help with them :). Be aware that the script imports **all** of your checkins. 

The script is just a couple of lines of Python and you can tackle stuff from the TODO list if you want to help out - just send a pull request.

## Installation

    $ brew install python
    $ sudo easy_install pip
    $ sudo pip install requests foursquare
    $ git submodule update --init --recursive

## Requirements

You will need to obtain API tokens for [Foursquare][1] and [ADN][3].
Those will need to be inserted into the *appsquare.py* script.

For Foursquare:

1. Go to <https://foursquare.com/developers/apps>.
2. Create an application.
3. Insert *FOURSQUARE_CLIENT_ID* and *FOURSQUARE_CLIENT_SECRET* into the script.
4. On first run of the script, you will need to go through an OAuth process in your browser.
5. The token that comes from OAuth needs to end up in the variable *FOURSQUARE_USER_TOKEN*.

For ADN:

If you have a developer account:

1. Go to <https://account.app.net/developer/apps/> and create an app.
2. Click on 'Generate a user token for yourself' and copy that into the *APP_TOKEN* variable.
3. We need permissions for messages and public\_messages.

If you don't:

1. Go to <http://dev-lite.jonathonduerig.com>, make sure 'Messages' and 'Public messages' are checked.
2. Click 'Authorize', authorize the app, get the token and copy it into the *APP_TOKEN* variable.

[1]: http://foursquare.com
[2]: http://ohaiapp.net
[3]: http://app.net
