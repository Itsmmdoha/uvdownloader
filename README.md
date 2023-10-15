# Uvdownloader

Uvdownloader is a Flask web app that allows users to download videos from Udvash or Unmesh courses.
Access the app [here](https://uvdownloader.onrender.com)

- Screenshot:
![3-devices-black](https://github.com/Itsmmdoha/uvdownloader/assets/70005698/9ae35a9f-1def-46ba-a8e2-f9dc1b05982b)



## Run Locally

Clone the repository

```bash
  git clone https://github.com/itsmmdoha/uvdownloader
```
Go to the project directory

```bash
  cd uvdownloader
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  gunicorn app:app
```

Open [http://localhost:8000](https://localhost:8000)

Done!


## How it works

It logs in to your Udvash account from the back-end and fetches the required video data. The video data cannot be fetched without logging in, that's why you need to provide the "Registration Number" and "Password" of your Udvash account.

After downloading the video, you will be logged out from your browser. But don't worry, nobody is stealing your information; it's just because Udvash doesn't allow multi-device login.


## 🚀 About Me
I'm an enthusiast.
I have a youtube channel named [HoundSec](https://youtube.com/@HoundSec)

contact me at: <the_doha@protonmail.com>
