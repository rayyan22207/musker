# Django-Tkinter Interface Project

## Overview

This project integrates the Django application from [musker](https://github.com/flatplanet/musker.git) with a custom-built Tkinter interface. The goal is to create a desktop-based GUI that interacts seamlessly with the Django backend, allowing users to access and manage the application features locally while utilizing the power of the web-based Django framework.

## Features

- **Django Backend**:
  - Built using the code from the `musker` repository.
  - Provides APIs and core application logic.
  - Supports token-based authentication with Django Rest Framework (DRF).

- **Tkinter Interface**:
  - A Python-based desktop GUI for user interaction.
  - Communicates with the Django backend through REST APIs.
  - Designed for simplicity and ease of use.

## Project Goals

1. Create a functional and interactive GUI using Tkinter.
2. Enable seamless interaction between the Tkinter interface and Django backend via REST APIs.
3. Leverage Django's features (authentication, database handling, etc.) in a desktop environment.

## Technologies

- **Backend**: Django, Django Rest Framework, Token Authentication.
- **Frontend**: Tkinter (Python GUI Library).

## Getting Started

### Prerequisites

- Python 3.x installed on your system.
- Required Python packages: 
  - `Django`
  - `djangorestframework`
  - `requests` (for API communication in Tkinter)

### Installation

1. Clone the `musker` repository:
   ```bash
   git clone https://github.com/flatplanet/musker.git
   cd musker
