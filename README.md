The Great Wall of Photos 📸
A full-stack image gallery application demonstrating Cloud-Native Storage Patterns using Django, React, and LocalStack.

🚀 About The Project
This project moves beyond traditional file storage (saving files to a media/ folder on the server) and implements the S3 Direct Upload Pattern. By using Presigned URLs, the frontend uploads heavy image data directly to the storage layer, bypassing the backend server entirely.


This architecture ensures:

Scalability: The Django backend is not blocked by file uploads.

Security: Private S3 buckets are accessed via temporary signed tokens.

Cost-Efficiency: Developing locally with LocalStack simulates AWS without credit card usage.

🛠 Tech Stack
Infrastructure: LocalStack (Simulating AWS S3 via Docker)

Backend: Django, Django REST Framework, Boto3 (AWS SDK)

Frontend: React.js

Database: SQLite (Metadata storage)

🏗 Architecture Flow
Upload Authorization: React requests a "ticket" (Presigned URL) from Django.

Direct Upload: React uploads the binary file directly to LocalStack S3 using the ticket.

Metadata Sync: React sends the image title, description, and S3 Key to Django to be saved in the database.

Secure Retrieval: When viewing the gallery, Django generates temporary signed URLs for React to render the private images.

⚙️ Prerequisites
Docker (for running LocalStack)

Python 3.8+

Node.js & npm

AWS CLI or awslocal wrappe



📚 What I Learned
Infrastructure as Code: Setting up cloud resources locally using CLI tools.

Boto3 SDK: interacting with AWS services programmatically from Python.

Presigned URLs: Decoupling upload logic to improve backend performance.

CORS Management: Handling security headers between the browser, the API, and the Object Storage.
