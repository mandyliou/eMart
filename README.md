# eMart

## Table of Contents
1. [Introduction](#Introduction)
2. [Setup & Installation](#Setup-&-Installation)
3. [Key Features](#Key-Features)
4. [Technologies Used](#Technologies-Used)

## Introduction
At the intersection of innovation and convenience lies eMart, a pioneering e-commerce platform. Designed with a clear focus on streamlining digital transactions, eMart offers a tailored experience for buying, selling, uploading, and downloading digital files.

## Setup & Installation

_macOS/Linux Users_
```bash
python3 -m venv venv
source venv/bin/activate
venv/bin/python -m pip install pip pip-tools rav --upgrade
venv/bin/rav run installs
rav run freeze
cd src
python manage.py runserver
```


_Windows Users_
```powershell
c:\Python310\python.exe -m venv venv
.\venv\Scripts\activate
python -m pip install pip pip-tools rav --upgrade
rav run win_installs
rav run win_freeze
cd src
python manage.py runserver
```
## Key Features

### Innovative UI/UX:
- With the integration of TailwindCSS, users can navigate and make transactions effortlessly, redefining the digital shopping experience.

### Reliable Data Storage:
- By combining Neon's Serverless Postgres with Docker, eMart ensures scalable and dependable data storage. AWS S3 provides an additional layer of secure and vast storage for digital files, ensuring they are housed without compromise.

### Secure Transactions:
- The integration of Stripe ensures that all billing processes align with the highest e-commerce industry standards, safeguarding user's financial data.

### Enhanced Performance and Availability:
- With Akamai, eMart optimizes content delivery, ensuring faster load times and high availability even during traffic spikes.

## Technologies Used

### Backend:
- The core of eMart runs on Django, a high-level Python framework celebrated for its robustness and scalability.

### Frontend:
- The seamless and intuitive user interface is powered by TailwindCSS, lauded for its modularity and adaptability.

### Infrastructure:
- Docker ensures consistent and reproducible environments, making deployments swift and hassle-free.
- AWS S3 is utilized for its scalable and reliable cloud storage solutions.

### Performance:
- Akamai, a leader in content delivery, is employed to accelerate the platform's performance across the globe.

### Payments:
- Stripe, a global leader in online payments, is integrated to handle all transactional processes securely.
