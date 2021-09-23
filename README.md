## Requirements

## Getting started

## Creating Flask microservices
### Creating Flask microservices
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