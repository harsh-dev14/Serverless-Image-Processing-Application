# My Serverless Image Processing App

A serverless application built with AWS Lambda, API Gateway, S3, and DynamoDB for uploading and processing images using Python and Pillow.

## Table of Contents

- [Architecture](#architecture)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Setup and Deployment](#setup-and-deployment)
  - [Frontend](#frontend)
  - [Backend](#backend)
  - [Infrastructure](#infrastructure)

## Features

- **Image Upload:** Users can upload images via the frontend.
- **Image Processing:** Images are resized and thumbnails are generated using AWS Lambda with Pillow.
- **Storage:** Processed images and thumbnails are stored in Amazon S3.
- **Metadata Storage:** Image metadata is stored in DynamoDB.
- **CORS Enabled:** Frontend communicates seamlessly with the backend APIs.
