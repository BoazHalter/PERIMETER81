# PERIMETER81

This repository contains a project focused on network security and infrastructure management, utilizing technologies such as Terraform, Docker, and Python.

## Table of Contents
- [About](#about)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## About
This repo is designed to help manage and secure network infrastructure effectively. 
It leverages Terraform for infrastructure as code (IaC), Docker for containerization, and Python for server-side scripting.

## Features
- **Infrastructure as Code (IaC):** Manage infrastructure using Terraform.
- **Containerization:** Utilize Docker for deploying applications in isolated environments.
- **Python Server:** A Python-based server to handle requests and manage network operations.
- **HTML:** A index.html to deliver a web page content.
- **Helm:** A helm chart for deploying Kubernetes applications.
## Getting Started

### Prerequisites
- Docker
- Terraform
- Python
- Helm

### Installation
1. Clone the repository:
   ```
   bash
   git clone https://github.com/BoazHalter/PERIMETER81.git
   cd PERIMETER81
   ```
2. Set up the Docker environment:
   ```
   docker build -t perimeter81 
   ``` 
3. Initialize Terraform:
   ```
   cd terraform 
   terraform init 
   ```
4. UsageStart the Docker container:
   ```
   docker run -d -p 8080:8080 perimeter81 
   ```
5. Apply Terraform configurations:
   ```
   terraform apply
   ```
6. Access the server: 
Open a web browser and go to http://localhost:8080.

8. Contributing: <br>
   Contributions are welcome!.  <br>
   
### known issues:
Some features of the html are not working in regular chrome browser.<br>
Open chrome incognito.<br>
Browse to:<br>
```chrome://flags/#unsafely-treat-insecure-origin-as-secure```<br>
update: <br>
```http://a022f0fe0d6da4233a50d03ae09d8bd5-1555814403.eu-central-1.elb.amazonaws.com:8080```<br>


<img width="793" alt="image" src="https://github.com/BoazHalter/PERIMETER81/assets/30419068/d6813aea-ae53-477e-abcf-9c525ddbd97c"><br>
relaunch chrome chrome may generate a message regarding the use of unsupported flag<br>


http://a022f0fe0d6da4233a50d03ae09d8bd5-1555814403.eu-central-1.elb.amazonaws.com:8080/index.html
chrome://flags/#unsafely-treat-insecure-origin-as-secure

<img width="707" alt="image" src="https://github.com/BoazHalter/PERIMETER81/assets/30419068/b7ab42b0-8130-47d1-a239-44642a64ca30">

