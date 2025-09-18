# Railway Deployment Fix

## Issues Fixed

The deployment was failing with "Error creating build plan with Railpack" due to several configuration issues:

### 1. Updated Railway Configuration Files

**Backend (`backend/railway.json`)**:
- Fixed start command to use proper Django deployment with Gunicorn
- Updated healthcheck path to `/api/`
- Removed dependency on start.sh script

**Frontend (`frontend/railway.json`)**:
- Fixed start command to use `$PORT` environment variable
- Ensured proper build and serve process

### 2. Added Nixpacks Configuration

Created `nixpacks.toml` files for both backend and frontend to help Railway better detect and build the applications:

- **Backend**: Python 3.11, pip install, Django static files collection
- **Frontend**: Node.js, npm ci, build process

### 3. Added Procfile Support

Created `Procfile` files as an alternative deployment method:
- **Backend**: Django migrations, static files, sample data, Gunicorn
- **Frontend**: Build and serve with proper port handling

### 4. Fixed Start Script

Updated `backend/start.sh` to handle missing `$PORT` environment variable with a default fallback.

## Deployment Steps

1. **Commit and push these changes** to your repository
2. **Redeploy on Railway** - the build should now succeed
3. **Monitor the deployment logs** for any remaining issues

## Environment Variables

Make sure these are set in your Railway project:

**Backend**:
- `SECRET_KEY`: Django secret key
- `DEBUG`: Set to `False` for production
- `ALLOWED_HOSTS`: Include your Railway domain

**Frontend**:
- `VITE_API_URL`: Your backend API URL

## Troubleshooting

If deployment still fails:
1. Check Railway build logs for specific errors
2. Verify all environment variables are set
3. Ensure database migrations run successfully
4. Check that static files are collected properly

The deployment should now work with the improved configuration!
