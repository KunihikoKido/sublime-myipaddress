# MyIPAddress for Sublime text 3
you can show your ip address in the panel.

It works using  [ifconfig.me](ifconfig.me) or [ifconfig.co](ifconfig.co) etc.

## Installation
To install, clone to your "Packages" directory.

- OS X: ~/Library/Application\\ Support/Sublime\\ Text\\ 3/Packages

```bash
git clone https://github.com/kunihikokido/sublime-myipaddress.git MyIpAddress
```

**Note** MyIpAddress expects to be installed to a directory called "MyIpAddress". Some features like the meny command to open settings will not work if installed somewhere else.

## Using

use shortcut ``Ctrl + Alt + i`` or open the Command Palette (``Shift + Command + P``) and enter ``MyIpAddress``.


## Settings

User Settings (accessible from the *Preferences/Package Settings/MyIpAddress/Settings - User* menu)

```javascript
{
    "ip_lookup_service_domain": "ifconfig.co",
    "curl_command": "curl",
}
```


Setting                       | Description
----------------------------- | ----------------------------------
``ip_lookup_service_domain``  | ip address lookup service domain. e.g, ifconfig.me, ifconfig.co, Default: ``ifconfig.io``
``curl_command``              | path to the curl command. If curl is on you path, you should not need to change this. Windows users will need to use forward slashes in the path. Default: ``curl``

