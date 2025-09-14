# -Cloud-Status-Dashboard-Live-Monitoring-of-HTTP-Services-
A Flask-based microservice application that monitors uptime status of websites, deployed on AWS EC2 with Kubernetes, Dockerized, and automated using Terraform and CI/CD pipelines.
## Table of Contents
# Project Overview
This project provides a Cloud Status Dashboard, monitoring the availability of arbitrary HTTP websites. Built with Flask, containerized with Docker, deployed to Kubernetes on an AWS EC2 instance, and infrastructure managed by Terraform. A CI/CD pipeline automatically tests, builds, and deploys the service on code commits.

# Features
  - REST API exposing HTTP status information for specified websites.
  - Prometheus-compatible metrics endpoint for monitoring.
  - Containerized using Docker.
  - Deployed on Kubernetes running on an AWS EC2 instance.
  - Automated AWS infrastructure provisioning through Terraform.
  - CI/CD pipeline using GitHub Actions to automate build, test, and deployment.
    
#Architecture

![Architecture Diagram](images/Mermaid%20Chart%20-%20Create%20complex,%20visual%20diagrams%20with%20text.%20A%20smarter%20way%20of%20creating%20diagrams.-2025-09-14-100750.svg)





# Installation & Deployment
  # Prerequisites
  - AWS Account with permissions to create EC2 instances and manage security groups.
  - Terraform installed locally (https://www.terraform.io/downloads).
  - Docker installed locally or on the EC2 instance (https://docs.docker.com/get-docker/).
  - kubectl installed and configured to connect to your Kubernetes cluster.
  - SSH key pair to access your EC2 instance.
  - Git installed to clone the repository.

# Steps to Install and Deploy

  1. Clone the Repository
      - git clone https://github.com/yourusername/Cloud-Status-Dashboard.git
      - cd Cloud-Status-Dashboard
    
  2. Provision AWS Infrastructure Using Terraform
      -  cd terraform-cloud-status
      -  terraform init
      -  terraform apply
     Review the plan and approve with yes.
     Terraform will provision an EC2 instance and necessary security groups.

  3. Connect to the EC2 Instance
      -  ssh -i /path/to/your-key.pem ec2-user@<your-ec2-public-ip>
    
  4. Deploy the Flask Application
    Clone the repository or pull the latest code on the EC2 instance.
    Build and run the Docker container:
      -  docker build -t cloud-status-dashboard .
      -  docker run -d -p 5000:5000 cloud-status-dashboard
    
  5. (Optional) Deploy on Kubernetes
    Apply Kubernetes manifests for deployment and service:
      -  kubectl apply -f k8s/deployment.yaml
      -  kubectl apply -f k8s/service.yaml
    Verify pods and services are running:
      -  kubectl get pods
      -  kubectl get svc
    
  6. Continuous Integration and Deployment
      Push your changes to the main branch on GitHub.

GitHub Actions pipeline will automatically build, test, and deploy the updated Docker image to your Kubernetes cluster via SSH and kubectl.

-- Notes
  - Make sure your SSH key and Kubernetes config are accessible for deployment.

  - Adjust security group rules for HTTP, SSH, and app ports (default 5000).

  - Monitor logs using docker logs or kubectl logs for troubleshooting.

# Terraform Infrastructure
- Provisions a t2.micro EC2 instance.

- Sets security groups to allow SSH, HTTP, and app ports.

- Configuration stored in terraform-cloud-status.


# CI/CD Pipeline
- GitHub Actions workflows automate:

    - Linting and testing.

    - Docker build and push to container registry.

    - Deployment to EC2 Kubernetes cluster via SSH and kubectl.

# Future Enhancements
- Integrate SonarQube or SonarCloud static code analysis.

- Add Prometheus and Grafana for real-time monitoring.

- Extend Terraform with automated Kubernetes cluster provisioning.

- Support multi-node Kubernetes clusters or use AWS EKS.

## Note
This project was completed primarily to understand the core concepts of cloud infrastructure, containerization, infrastructure as code, and CI/CD automation, and to gain hands-on practical experience working with these technologies.

If you have any suggestions for improvements or additional features, please feel free to reach out or submit contributions. Feedback is highly appreciated to help enhance this project further.


