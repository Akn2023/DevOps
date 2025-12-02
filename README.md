**Beginner’s Guide: Launching an AWS EC2 Instance Using Jenkins Pipeline + Python Boto3**
=========================================================================================

This guide is designed for beginners who want to automate EC2 instance creation using:

✅ **Jenkins** ✅ **GitHub**✅ **AWS CLI**✅ **Python + Boto3**

🎯 **What You Will Learn**

*   Install Jenkins on Ubuntu
    
*   Install Python, Pip, Virtual Environment
    
*   Install AWS CLI
    
*   Configure AWS Credentials
    
*   Write a simple Python boto3 script
    
*   Push code to GitHub
    
*   Create a Jenkins pipeline that launches EC2🟦 **1\. Install Jenkins on Ubuntu**
    

### **Step 1 — Update system**

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   sudo apt update  sudo apt install fontconfig openjdk-21-jre -y  java -version   `

### **Step 2 — Add Jenkins repo**

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   sudo wget -O /etc/apt/keyrings/jenkins-keyring.asc https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key  echo "deb [signed-by=/etc/apt/keyrings/jenkins-keyring.asc] \  https://pkg.jenkins.io/debian-stable binary/" | \  sudo tee /etc/apt/sources.list.d/jenkins.list > /dev/null  sudo apt update  sudo apt install jenkins -y   `

### **Step 3 — Open Jenkins Port in AWS SG**

Add **Inbound Rule**:

*   Port: **8080**
    
*   Type: Custom TCP
    
*   Source: 0.0.0.0/0 (for testing only)
    

🟩 **2\. Install Python, Pip, Virtual Environment & Boto3**

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   sudo apt update && sudo apt upgrade -y  sudo apt install python3-pip python3.12-venv -y  python3 -m venv venv  source venv/bin/activate  pip install boto3   `

🟧 **3\. Install AWS CLI**
==========================

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"  sudo apt install unzip -y  unzip awscliv2.zip  sudo ./aws/install  aws --version   `

🟪 **4\. Configure AWS Credentials**
====================================

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   aws configure   `

Enter:

FieldValueAWS Access Key IDYour keyAWS Secret KeyYour secretRegionap-south-1Outputjson

🟥 **5\. Python Script to Launch EC2 Instance**
===============================================

Create **create\_ec2.py**

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   import boto3  ec2 = boto3.client("ec2", region_name="ap-south-1")  response = ec2.run_instances(      ImageId="ami-0d176f79571d18a8f",      InstanceType="t3.micro",      MinCount=1,      MaxCount=1  )  print("Instance ID:", response["Instances"][0]["InstanceId"])   `

🟦 **6\. Push Code to GitHub**
==============================

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   echo "# demo" >> README.md  git init  git add .  git commit -m "first commit"  git branch -M main  git remote add origin https://github.com//demo.git  git push -u origin main   `

🟫 **7\. Configure Jenkins Credentials for AWS**
================================================

Jenkins Dashboard →**Manage Jenkins → Credentials → Global → Add Credentials**

Choose:

*   **Kind:** Secret Text
    
*   ID: AWS\_ACCESS\_KEY\_ID
    
*   Secret:
    

Add another:

*   **Kind:** Secret Text
    
*   ID: AWS\_SECRET\_ACCESS\_KEY
    
*   Secret:
    

🟩 **8\. Jenkins Pipeline (Beginner-Friendly)**

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   pipeline {      agent any      environment {          AWS_ACCESS_KEY_ID     = credentials('AWS_ACCESS_KEY_ID')          AWS_SECRET_ACCESS_KEY = credentials('AWS_SECRET_ACCESS_KEY')      }      stages {          stage('Clean Workspace') {              steps {                  cleanWs()              }          }          stage('Clone Repository') {              steps {                  git branch: 'main', url: 'https://github.com//demo.git'              }          }          stage('Run Python Script') {              steps {                  sh 'python3 create_ec2.py'              }          }      }      post {          success {              echo "EC2 Instance Launched Successfully!"          }          failure {              echo "Pipeline Failed!"          }      }  }   `

🖼 **9\. Architecture Diagram (Text Format)**
=============================================

Use this inside your documentation:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML  `GitHub Repo         |         v     Jenkins Pipeline         |         v   Python + Boto3 Script         |         v  AWS EC2 Instance Created`

🎉 **10\. Final Output**
========================

After pipeline completes:

✔ EC2 Instance launched✔ Instance ID printed✔ Jenkins pipeline shows SUCCESS
