# Uvdownloader

Uvdownloader is a Flask web app that allows users to download videos from Udvash or Unmesh courses.
Access the app [here](http://uvd.houndsec.net/)

- preview:

![thumbnail meterial (1)](https://github.com/Itsmmdoha/uvdownloader/assets/70005698/a70d4b2f-5492-4123-ab8d-7347fe4bc3fc)


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

## Docker

There's a prebuilt image available on dockerhub, you can run it using the the following command,

```bash
docker run -p 8000:8000 houndsec/uvdownloader
```
or

```bash
docker run -p 8000:8000 houndsec/uvdownloader
```
To run in detached mode

Then open [http://localhost:8000](http://localhost:8000)

### Build Locally
1. Clone the repo

```bash
  git clone https://github.com/itsmmdoha/uvdownloader
```
2. change directory
```bash
cd uvdownloader
```
3. Build the image

```bash
docker build -t houndsec/uvdownloader .
```
4. Rut it
```bash
docker run -p 8000:8000 houndsec/uvdownloader
```
or

```bash
docker run -p 8000:8000 houndsec/uvdownloader
```
To run in detached mode
Then open [http://localhost:8000](http://localhost:8000)


## How it works

It logs in to your Udvash account from the back-end and fetches the required video data. The video data cannot be fetched without logging in, that's why you need to provide the "Registration Number" and "Password" of your Udvash account.

After downloading the video, you will be logged out from your browser. But don't worry, nobody is stealing your information; it's just because Udvash doesn't allow multi-device login.

## LICENSE Update
## License Change Notice

I am changing the license for this repository from the MIT license to the Creative Commons Attribution-ShareAlike (CC BY-SA) license. This change is being made to prevent unauthorized use of my code, including the use of ads and the lack of proper attribution.

Under the CC BY-SA license, users are permitted to:

* Use, reuse, and adapt the code for any purpose, including commercial purposes.
* Share the code with others, but they must give credit to the original author and distribute the code under the same license.

Users are not permitted to:

* Remove or change any copyright notices or other legal notices in the code.
* Claim ownership of the code or make it appear that they are the original author.
* Use the code to promote or support any illegal or harmful activities.

I hope that this change will help to protect my work and ensure that it is used in a responsible and ethical manner.


## 🚀 About Me
I'm an enthusiast.
I have a youtube channel called [HoundSec](https://youtube.com/@HoundSec)

contact me at: <the_doha@protonmail.com>
