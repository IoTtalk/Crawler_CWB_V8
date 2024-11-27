# 交通部中央氣象局V8版網頁爬蟲


* 需安裝 selenium module

* 須將對應Chrome版本的webdriver( chromedriver.exe ) 放到 crawl_weather_V8.py 相同目錄內
*  進入此頁面選擇下載Chromedriver：
```
http://chromedriver.storage.googleapis.com/index.html
```

## For windows:
```
    pip3 install selenium beautifulsoup4 lxml
```
正常訊息

例如:DevTools listening on ws://127.0.0.1:58955/devtools/browser/39b821ce-f499-45bb-b93e-ce423911e4b9 

版本不對可能的訊息1: (可忽略)

selenium.common.exceptions.SessionNotCreatedException: ERROR:browser_switcher_service.cc(238)] XXX Init()

版本不對可能的訊息2: (必須要更換成對應的版本)

selenium.common.exceptions.SessionNotCreatedException: Message: session not created: This version of ChromeDriver only supports Chrome version 83

Reference:
```
https://www.itread01.com/content/1543109607.html
```

## For Ubuntu:

安裝Chrome
```
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
    sudo dpkg -i google-chrome-stable_current_amd64.deb
```
如果報錯:

Errors were encountered while processing:

 google-chrome-stable

執行以下命令後再次安裝Chrome:
```
    sudo apt-get install -f
```

進入此頁面選擇下載Chromedriver：http://chromedriver.storage.googleapis.com/index.html
```
    wget https://chromedriver.storage.googleapis.com/83.0.4103.39/chromedriver_linux64.zip
    unzip chromedriver_linux64.zip
    chmod +x chromedriver
    sudo mv chromedriver /usr/bin/
```   


純console，沒有X-window時，可以利用虛擬視窗環境Xvfb解決:

You can try with Xvfb. it does not require additional hardwares.

#Install Xvfb if you din't install yet and do the following steps.

#Dependencies to make "headless" chrome/selenium work:

    sudo apt-get -y install xorg xvfb gtk2-engines-pixbuf 
    sudo apt-get -y install dbus-x11 xfonts-base xfonts-100dpi xfonts-75dpi xfonts-cyrillic xfonts-scalable

#Optional but nifty: For capturing screenshots of Xvfb display:

    sudo apt-get -y install imagemagick x11-apps

#Make sure that Xvfb starts everytime the box/vm is booted:

    Xvfb -ac :99 -screen 0 1280x1024x16 & export DISPLAY=:99
