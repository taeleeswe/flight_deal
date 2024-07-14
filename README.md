# Flight Deal Finder

## Overview
Flight Deal Finder is a Python-based application designed to help users find and receive notifications about the best flight deals. It leverages various APIs to search for flights and manage data.

## Features
- Search for flight deals based on specified criteria
- Manage and store flight data
- Notify users about the best deals

## Files
- `data_manager.py`: Handles data storage and management.
- `flight_data.py`: Manages flight data structures and operations.
- `flight_search.py`: Contains logic to search for flights using external APIs.
- `main.py`: Main entry point for the application.
- `notification_manager.py`: Manages notifications to users.

## APIs Used
- **Tequila API**: Used for searching flight deals.
- **Sheety API**: Used for managing and storing flight data.
- **Twilio API**: Used for sending notifications to users.

## Requirements
- Python 3.12
- Requests library

## Installation
1. Clone the repository:
   git clone https://github.com/taeleeswe/flight_deal.git
2. Navigate to the project directory:
   cd flight_deal
3. Install required packages:
   pip install -r requirements.txt
