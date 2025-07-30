# 📦 URL Shortener App – Part 1

## 📝 Project Overview

This is a simple serverless URL shortener using AWS.  
The user submits a long URL → receives a short ID → visiting the short link redirects to the original URL.

---

## ✅ AWS Services Used

| Component     | Service                     |
|---------------|-----------------------------|
| Frontend      | S3 (Static Website Hosting) |
| Backend       | Lambda Function URL         |
| Database      | DynamoDB                    |
| Communication | JavaScript + fetch + CORS   |

---

## 🚀 Step-by-Step Instructions

### 1. S3 – Static Website Hosting

- Created a bucket: `url-shortener-frontend-eyal-apple`
- Disabled **Block all public access**
- Enabled **Static website hosting** → index document: `index.html`
- Uploaded `index.html`
- Added public read permissions via bucket policy

### 2. DynamoDB Table

- Table name: `ShortUrls`
- Partition key: `id` (String)
- Fields stored:
  - `id`: Short ID
  - `url`: Original URL

### 3. AWS Lambda Function

- Name: `urlShortenerFunction`
- Runtime: Python 3.12
- Execution Role: `labrole` (existing role with DynamoDB access)
- Deployed via AWS Lambda Console

#### Functionality:

- `POST /shorten` → stores long URL in DynamoDB with generated ID
- `GET /{id}` → fetches and redirects to the original URL
- CORS is handled (OPTIONS requests + headers)

### 4. Lambda Function URL

- Enabled public Function URL
- Auth type: NONE
- Used it in frontend fetch requests

---

## 💻 Frontend Logic (`index.html`)

- Simple HTML with a text input and a button
- JavaScript fetches the short URL from Lambda:
  - Adds `https://` automatically if user forgets
  - Displays short link as clickable anchor

---

## 🧪 Testing

- Accessed S3 site: `http://url-shortener-frontend-eyal-apple.s3-website-us-west-2.amazonaws.com`
- Entered `google.com` → received short link
- Clicked short link → redirected successfully
- Verified data saved in DynamoDB
- Used browser console & CloudWatch logs for debugging

---

## 📸 Screenshots

- Lambda deployed with code
- DynamoDB table with entries
- Static S3 bucket with hosting enabled
- App in browser working end-to-end

---

## 📂 Project Files

- `index.html` – Frontend
- `lambda_function.py` – Backend (AWS Lambda)
- `README.md` – Documentation

---

## 🔗 Live Demo

Frontend:  
[`http://url-shortener-frontend-eyal-apple.s3-website-us-west-2.amazonaws.com`](http://url-shortener-frontend-eyal-apple.s3-website-us-west-2.amazonaws.com)

Example of shortened link:  
`https://km7vehlsi4gfvr6ejavlt376am0sathm.lambda-url.us-west-2.on.aws/PNFewD`

---

