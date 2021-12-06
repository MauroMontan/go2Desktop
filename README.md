

# Go2Desktop



## Features

- tray icon app
- prevent runnig multiple instances
- Cross platform
- windows app in releases
- linux release binary



If you dont want to install the development version, go to releases and install your os compatible app version


## Installation



Install my-project with npm

Clone the repository and go to go2Desktop

```bash
  $ git clone https://github.com/MauroMontan/go2Desktop.git
  $ cd go2Desktop
```

Install dependencies
```bash
  $ pip install -r requirements.txt
```

Running

Once you have installed all the dependencies, make sure that the script is running

```bash
  $ python go2Desktop.py
```

## Configuration
Inside go2Desktop directory you will found a "settings.json" file, here is where the app settings go2Desktop

```json
    {
        "url":"here goes your url app",
        "windowname":"here goes your app name",
        "windowicon":"here goes your icon path",
        windowgeometry:[
            800,
            500,
        ]
    }

```
Is recommended put the icon on the app folder. 

### now create every app you need by copying and renaming the go2Desktop folder


## Example



this is an example of how a notion web app looks like

![Notion example](https://i.imgur.com/cEgPu4B.png)


## Authors

- [@MauroMontan](https://github.com/MauroMontan)

