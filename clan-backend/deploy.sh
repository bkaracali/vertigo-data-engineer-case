#!/bin/bash
set -e

PROJECT_ID="vertigo-case-488119"
REGION="europe-central2"
SERVICE_NAME="vertigo-case"
IMAGE_NAME="gcr.io/$PROJECT_ID/$SERVICE_NAME:latest"
DB_INSTANCE_CONNECTION_NAME="vertigo-case-488119:europe-central2:vertigo-db"
DB_USER="vertigo"
DB_PASSWORD="vertigo123"
DB_NAME="vertigo_db"

# 1️⃣ Build Docker image
echo "1️⃣ Building Docker image..."
docker build -t $IMAGE_NAME .

# 2️⃣ Push to GCR
echo "2️⃣ Pushing image to GCR..."
gcloud auth configure-docker
docker push $IMAGE_NAME

# 3️⃣ Deploy to Cloud Run
echo "3️⃣ Deploying to Cloud Run..."
gcloud run deploy $SERVICE_NAME \
    --image $IMAGE_NAME \
    --platform managed \
    --region $REGION \
    --allow-unauthenticated \
    --set-env-vars DATABASE_URL=postgresql+psycopg2://$DB_USER:$DB_PASSWORD@/$DB_NAME?host=/cloudsql/$DB_INSTANCE_CONNECTION_NAME

echo "✅ Deployment completed!"
gcloud run services describe $SERVICE_NAME --platform managed --region $REGION --format 'value(status.url)'


