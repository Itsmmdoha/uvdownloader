
# Uvdownloader

Uvdownloader is flask web app that allows user to download videos from Udvash or Unmesh courses.


- screenshot:
![screenshots](https://raw.githubusercontent.com/Itsmmdoha/uvdownloader/main/screenshot.png)



## Run Locally

Clone the project

```bash
  git clone https://github.com/itsmmdoha/uvdownloader
```

Go to the project directory

```bash
  cd uvdownloader
```

Install dependencies

```bash
  pip Install -r requirements.txt
```

Start the server

```bash
  gunicorn app:app
```

Open [http://localhost:8000](https://localhost:8000)

Done!


## How it works

It logs in to your udvash account from the back-end and fetches required video data. The video data cannot be fetched without loging in, that's why you need to provide the "Registration Number" and "Password" of your udvash account.

After downloading the video you will be logged from your browser. But don't worry, nobody is stealing your information it's just because udvash doesn't allow multi device login. Heck, it's even open source!


## 🚀 About Me
I'm a enthusiast.
I have a youtube [channel](https://youtube.com/@HoundSec)

