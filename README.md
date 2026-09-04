# Job Scraper & API

A Python-based job scraping application that collects job listings from multiple company job boards, stores them in a SQLite database, and exposes them through a FastAPI REST API with keyword and location filtering.

## Features

- Collects job listings from multiple companies
- Retrieves job data through company job board APIs
- Normalizes job data into a consistent format
- Stores job listings in a SQLite database
- Prevents duplicate listings using unique job links
- Provides a REST API using FastAPI
- Supports filtering jobs by keyword
- Supports filtering jobs by location
- Supports filtering by both keyword and location
- Returns job data as JSON

## Tech Stack

- **Python**
- **Requests**
- **SQLite**
- **FastAPI**

## How It Works

The application follows this general flow:

```text
Company Job Board APIs
        ↓
   HTTP Requests
        ↓
   Job Data (JSON)
        ↓
   Data Normalization
        ↓
    SQLite Database
        ↓
     FastAPI API
        ↓
   Filtered Job Data
```

## Running Locally

### 1. Clone the repository

```bash
git clone https://github.com/larugita/job-scraper.git
cd job-scraper
```

### 2. Install dependencies

```bash
pip install requests fastapi uvicorn
```

### 3. Run the scraper

```bash
python job_scraper.py
```

This will collect the available job listings and store them in `jobs.db`.

### 4. Start the API

```bash
uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

Interactive API documentation is available at:

```text
http://127.0.0.1:8000/docs
```

## Project Structure

```text
job-scraper/
├── job_scraper.py
├── main.py
└── jobs.db
```

### `job_scraper.py`

Responsible for:

- Requesting job listings from company APIs
- Processing and normalizing job data
- Inserting jobs into the SQLite database
- Preventing duplicate listings

### `main.py`

Contains the FastAPI application and API endpoints used to retrieve and filter jobs.

### `jobs.db`

SQLite database containing the collected job listings.

## API Endpoints

### Get all jobs

```text
GET /jobs
```

Returns all stored job listings.

### Filter by keyword

```text
GET /jobs?keyword=Python
```

Returns jobs whose titles contain the specified keyword.

### Filter by location

```text
GET /jobs?location=Toronto
```

Returns jobs whose locations contain the specified location.

### Filter by keyword and location

```text
GET /jobs?keyword=Software%20Engineer&location=Toronto
```

Returns jobs matching both the specified keyword and location.

## Current Companies

- Stripe
- DoorDash
- Reddit

## Future Improvements

- Add more companies and job boards
- Build a frontend for searching and browsing jobs
- Deploy the API
- Migrate from SQLite to PostgreSQL
- Add automated scheduled scraping
- Improve search and filtering capabilities
- Add additional job fields and sorting options

## Status

**In Progress**

This project is actively being developed as I continue expanding its functionality and improving its architecture.