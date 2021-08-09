[![pbaboutlabel](https://github.com/pbdata/pbaboutlabel/actions/workflows/python-app.yml/badge.svg)](https://github.com/pbdata/pbaboutlabel/actions/workflows/python-app.yml)

# Part 1 - Model Build
Please refer to [pitchbook.ipynb](https://github.com/pbdata/pbaboutlabel/blob/main/pitchbook.ipynb)

# Part 2 - Model Deploy
a) Using API Gateway and Lambda sitting in front of Sagemaker endpoint to process the request in real-time.  API URL is [here](https://kprzr6eot5.execute-api.us-east-1.amazonaws.com/prod/predictaboutlabel) and sample data format is in JSON {"data": "SeatGeek is the leading mobile-focused ticket platform that enables fans to buy and sell tickets for sports, concert, and theater events."}

![alt text](https://github.com/pbdata/pbaboutlabel/blob/main/img/sagemaker%20archtecture.jpg " ")

![alt text](https://github.com/pbdata/pbaboutlabel/blob/main/img/pb-api.gif " ")

b) Using Github and Github actions will do the the CI tests implemented in [this repo](https://github.com/pbdata/pbaboutlabel) and CD can update the Sagemaker Endpoint.

c) Using Mlflow Tracker server [here](http://mlflo-mlflo-kg1i011s8hid-60b8dc955cae2952.elb.us-east-1.amazonaws.com).  It's architecture is below.

![alt text](https://github.com/pbdata/pbaboutlabel/blob/main/img/mlflow%20architecture.JPG " ")

Multiple environments and experiments can be tracked in mlflow as shown below:

![alt text](https://github.com/pbdata/pbaboutlabel/blob/main/img/mlflow%20experiment.gif " ")

![alt text](https://github.com/pbdata/pbaboutlabel/blob/main/img/mlflow%20environments.gif " ")

d) Explained above
