resource "aws_instance" "cloud_status_instance" {
  ami           = "ami-0242293c1166ee926"  # Update this AMI based on your AWS region
  instance_type = "t2.micro"
  security_groups = [aws_security_group.cloud_status_sg.name]

  tags = {
    Name = "CloudStatusInstance"
  }

  # Optional: to bootstrap your instance, uncomment and provide a script
  # user_data = file("bootstrap.sh")
}

