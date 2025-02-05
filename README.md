# Cloud Resume Challenge - [Your Name]

Welcome to my Cloud Resume Challenge repository! This project is a culmination of my journey into cloud computing, where I built a serverless resume website hosted on AWS. Below is an overview of the technologies and services I used to complete this challenge.

## Features

- **Frontend**: HTML, CSS, and JavaScript for the resume webpage.
- **Backend**: Python (boto3) for the Lambda function.
- **Database**: DynamoDB to store and retrieve the visitor counter.
- **API**: API Gateway and Lambda for serverless communication.
- **Infrastructure as Code**: AWS SAM template for defining and deploying resources.
- **CI/CD**: GitHub Actions for automated deployment of both frontend and backend.
- **HTTPS & DNS**: CloudFront for HTTPS and Route 53 for custom DNS.

## How It Works

1. The resume is hosted as a static website on Amazon S3.
2. A visitor counter is displayed on the webpage, which retrieves and updates the count from a DynamoDB table.
3. The JavaScript on the webpage communicates with an API Gateway endpoint, which triggers a Lambda function to interact with DynamoDB.
4. The entire infrastructure is defined using AWS SAM and deployed via GitHub Actions.

## Repository Structure

- `/frontend`: Contains the HTML, CSS, and JavaScript files for the resume website.
- `/backend`: Includes the AWS SAM template, Lambda function code, and Python tests.
- `.github/workflows`: GitHub Actions workflows for CI/CD.

## Live Demo

Check out my live resume website: [Your Custom Domain](<https://your-custom-domain.com>)

## Blog Post

I’ve written a blog post detailing my experience and learnings from this project. You can read it here: [Link to Blog Post]

## Acknowledgments

Special thanks to [Forrest Brazeal](<https://cloudresumechallenge.dev/>) for creating this amazing challenge!

