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
- Python 3.x
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

ContributingContributions are welcome! 
Please fork the repository and create a pull request with your changes.
License
This project is licensed under the MIT License. 
See the LICENSE file for details.
Feel free to modify this template based on additional specific details about your project.
incognito.
in case not:
<img width="625" alt="image" src="https://github.com/BoazHalter/PERIMETER81/assets/30419068/c8505ef9-58f9-4d66-b2ad-b5e83cf5a747">

chrome://flags/#unsafely-treat-insecure-origin-as-secure
