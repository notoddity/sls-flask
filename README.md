## Getting started

### Required cli's
- `npm` For installing nodejs packages to extend serverless
- `pip` For installing pything packages and creating your microservice

### Amazon Web Services
While I won't go through how to setup a AWS account once you have an account
read this to find out how to get your access key and secret then run the
following to store your credentials for serverless
```
export AWS_ACCESS_KEY_ID=1234-your-key-here
export AWS_SECRET_ACCESS_KEY=5678-your-secret-here
```

## Creating Flask microservices
Creating a flask microservice with serverless and this template is relatively easy
```
$ sls install --name my_new_microservice --url https://github.com/NotOddity/sls-flask.git
$ cd my_new_microservice
$ npm install
```

To run your new flask microservice locally
```
$ sls wsgi serve
 * Running on http://localhost:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 123-456-789
```

## Deploying your microservice to Amazon Web Services

## Multiple endpoints for the same service

## Adding a custom url to your microservice

## Automatic deployment of certain stages with CodePipeline