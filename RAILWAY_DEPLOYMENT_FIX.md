# Railway Deployment Fix

## Issues Fixed

The deployment was failing with "Error creating build plan with Railpack" due to several configuration issues:

### Root Cause
Railway was trying to deploy from the root directory of your monorepo but couldn't find the necessary files to determine the deployment strategy. The error "Script start.sh not found" indicated that Railway was looking for deployment files at the root level.

### 1. Created Root-Level Configuration Files

**Root Level Files**:
- `railway.json`: Main Railway configuration pointing to backend service
- `start.sh`: Root-level start script that navigates to backend directory
- `nixpacks.toml`: Nixpacks configuration for Python detection
- `Procfile`: Alternative deployment method
- `requirements.txt`: Root-level requirements file that includes backend requirements

### 2. Updated Railway Configuration Files

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

## Latest Fix (Nixpacks Error)

**Issue**: `undefined variable 'pip'` error in Nixpacks configuration.

**Solution**: 
- Removed `nixpacks.toml` files that were causing conflicts
- Simplified Railway configuration to use `start.sh` script
- Added `runtime.txt` for Python version detection
- Let Railway auto-detect Python and handle pip installation

**Files Updated**:
- `railway.json`: Simplified to use start.sh script
- `runtime.txt`: Added for Python version detection
- Removed: `nixpacks.toml` and `backend/nixpacks.toml`

The deployment should now work without Nixpacks configuration conflicts!

## Healthcheck Fix

**Issue**: Build succeeded but healthcheck was failing - Django application not responding.

**Solution**:
- Updated healthcheck path from `/api/` to `/api/health/` (more specific endpoint)
- Enhanced start.sh script with better logging and error handling
- Added Django system check before starting server
- Improved Gunicorn configuration with proper logging
- Set DEBUG=False by default for production

**Files Updated**:
- `railway.json`: Updated healthcheck path to `/api/health/`
- `start.sh`: Added debugging, Django check, and better Gunicorn config
- `backend/ipswich_retail/settings.py`: Set DEBUG=False by default

The deployment should now start successfully and pass healthchecks!
