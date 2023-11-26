# Introduction to FastAPI

Introduction to FastAPI: Building Data Science Projects with Python

[Workshop Slide Decks](https://docs.google.com/presentation/d/1fioyhI3dzY6aydqD9Qak4OM8k1i4x3udPLuCy0TurTY/edit?usp=sharing)

[[_TOC_]]

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development, testing purposes and as well as in production machine.

## 📦 Installation

### Prerequisite

> Before you start, make sure you have a installed [`Poetry`](https://python-poetry.org/)


### How do I get set up?

Clone the code repository.

```python
git clone git@github.com:porimol/intro2fastapi.git

cd intro2fastapi
poetry install
```

### Model Training

To training the model, run the following command.

```bash
python intro2fastapi/models/training.py
```
Once, model training successfully done, the pickled model will be stored in `intro2fastapi/models/` folder.

### API Serving

Run the following command to serving API.

```bash
poetry run uvicorn intro2fastapi.api:app --reload
```

Now, see the console and you will get the output something like following.

```bash
INFO:     Will watch for changes in these directories: ['/Users/opt/intro2fastapi']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [33179] using StatReload
INFO:     Started server process [33205]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

## API Usage

To access one of the country properties available, you'll need to use one of the API methods listed below and pass a country in either way.

**API URIs:**

Home URI:

```bash
http://127.0.0.1:8000/
```

API Request Method: GET

API Request Body:

```bash
{
    "message": "Welcome to the California Housing Price Prediction API. Use POST /predict/ endpoint for predictions."
}
```

Prediction URI:

```bash
http://127.0.0.1:8000/predict
```

API Request Method: POST

API Request Body:

```bash
{
    "MedInc": 0.02,
    "HouseAge": 2.5,
    "AveRooms": 3.2,
    "AveBedrms": 6.7,
    "Population": 4.0,
    "AveOccup": 5.0,
    "Latitude": 2.0,
    "Longitude": 2.0
}
```

Prediction Response:

```bash
{
    "predicted_price": 1.852310299999999
}
```


## Contributing

See the list of [contributors](https://github.com/porimol/intro2fastapi/contributors) who participated in this project.


### How to become a contributor

If you want to contribute to `intro2fastapi` and make it better, your help is very welcome.
You can make constructive, helpful bug reports, feature requests and the noblest of all contributions.
If like to contribute in a good way, then follow the following guidelines.

#### How to make a clean pull request

* Create a personal fork on Github.
* Clone the fork on your local machine.(Your remote repo on Github is called `origin`.)
* Add the original repository as a remote called `upstream`.
* If you created your fork a while ago be sure to pull upstream changes into your local repository.
* Create a new branch to work on! Branch from `dev`.
* Implement/fix your feature, comment your code.
* Follow `intro2fastapi`'s code style, including indentation(4 spaces).
* Write or adapt tests as needed.
* Add or change the documentation as needed.
* Push your branch to your fork on Github, the remote `origin`.
* From your fork open a pull request to the `dev` branch.
* Once the pull request is approved and merged, please pull the changes from `upstream` to your local repo and delete your extra branch(es).


## Disclaimer

This is being maintained in the contributor's free time, and as such, may contain minor errors in regards to some countries.
Most of the information included in this library is what is listed on Wikipedia. If there is an error,
please let me know and I will do my best to correct it.

## License

### [The Apache License](LICENSE.txt)
