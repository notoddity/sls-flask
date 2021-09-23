# Serverless Flask Template

### Why?
I previously forked serverless-flask which was good to learn from but I wanted to create a new template for
myself and other to use on a Seperate project. I wanted clear documentation on how to setup and deploy a
new flask microservice.

### Index
- [Getting Started](https://github.com/NotOddity/sls-flask#getting-started)
- [Creating a flask microservice](https://github.com/NotOddity/sls-flask#creating-flask-microservices)
- [Deploying your microservice to Amazon Web Services](https://github.com/NotOddity/sls-flask#creating-flask-microservices)
- [Adding a custom domain to your microservice](https://github.com/NotOddity/sls-flask#adding-a-custom-domain-to-your-microservice)

## Getting started

### Required
- `npm` For installing nodejs packages to extend serverless. [How to install nodejs & npm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm)
- `npm install -g serverless` This is the serverless cli (`npm` must be installed)
- `python` The primary language of a flask microservice. [How to install](https://wiki.python.org/moin/BeginnersGuide/Download)
- `pip` For installing pything packages and creating your microservice [How to install](https://packaging.python.org/tutorials/installing-packages/#requirements-for-installing-packages)

### Amazon Web Services
While I won't go through how to setup an AWS account, once you have an account
[read this](https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html)
to find out how to get your access key and secret.
Then run the following to store your credentials for serverless to use when deploying:
```
export AWS_ACCESS_KEY_ID=1234-your-key-here
export AWS_SECRET_ACCESS_KEY=5678-your-secret-here
```

## Creating a flask microservice

Generating your first Flask microservice with serverless is realatively easy and straight forward. As long as you meet all the above requirements
you will only need to run a few lines to serve your first GET request.

### Creating a flask microservice
```
$ sls install --name my_new_microservice --url https://github.com/NotOddity/sls-flask.git
$ cd my_new_microservice
```

### Creating virtual environment and installing dependencies
```
$ npm install
$ python3 -m venv .venv
$ source .venv/bin/activate
(venv)$ pip install -r requirements.txt 
```

### To run your flask microservice locally
```
$ sls wsgi serve
 * Running on http://localhost:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 123-456-789
```
### Test your microservice is responding
```
$ curl http://localhost:5000/
{"message": "Hello World!"}
```

## Deploying your microservice to Amazon Web Services

Serverless makes this super simple, just run `sls deploy` (This can take a while)

You should get this
```
Service Information
service: sls-flask
stage: dev
region: us-east-1
stack: sls-flask-dev
resources: 13
api keys:
  None
endpoints:
  ANY - https://ucpykgtlf2.execute-api.us-east-1.amazonaws.com/dev
  ANY - https://ucpykgtlf2.execute-api.us-east-1.amazonaws.com/dev/{proxy+}
functions:
  api: sls-flask-dev-api
```

Lets test your new aws endpoint
```
$ curl https://ucpykgtlf2.execute-api.us-east-1.amazonaws.com/dev
{"message": "Hello World!"}
```

## Adding a custom domain to your microservice

### Requirements
1. Ensure you have the domain you wish to use avaiable on your AWS Console 
- [Registering a new domain](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/domain-register.html)
- [Making Route 53 the DNS service for a domain that's in use](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/migrate-dns-domain-in-use.html)
2. Once you have a domain you need to request a certificate
- [Requesting a public certificate](https://docs.aws.amazon.com/acm/latest/userguide/gs-acm-request-public.html)

### Install serverless-domain-manager
- `npm install serverless-domain-manager`

### Add your custom domain to your serverless.yml
```
custom:
  customDomain:
    createRoute53Record: true
    domainName: my-domain.com
    certificateName: my-domain.com
    stage: dev
    basePath: api
```

### Re-deploy with your new custom domain
Again to deploy (or re-deploy) just type `sls deploy` and give it a while

Result:
```
Service Information
service: sls-flask
stage: dev
region: us-east-1
stack: sls-flask-dev
resources: 13
api keys:
  None
endpoints:
  ANY - https://my-domain.com/
  ANY - https://my-domain.com/{proxy+}
functions:
  api: sls-flask-dev-api
```

Lets test just to make sure
```
$ curl https://my-domain.com/
{"message": "Hello World!"}
```

## Multiple endpoints for the same service

## Using git branches to control staging

## Automatic deployment of certain stages with CodePipeline automatically (or with manual approval)