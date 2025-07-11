# 🚀 Deployment Guide for Render

This guide will help you deploy the Dairy Supply & Demand Forecasting application on Render.
I am Vatsal
## 📋 Prerequisites

1. **GitHub Account**: You need a GitHub account to host your code
2. **Render Account**: Sign up at [render.com](https://render.com)
3. **Project Files**: Ensure all project files are in your GitHub repository

## 🔧 Step-by-Step Deployment

### Step 1: Prepare Your Repository

1. **Create a GitHub repository** (if you haven't already)
2. **Upload all project files** to your repository:
   ```
   dairy-forecasting/
   ├── app.py
   ├── requirements.txt
   ├── README.md
   ├── Dockerfile
   ├── .dockerignore
   ├── .gitignore
   ├── render.yaml
   ├── test_app.py
   └── Dairy_Supply_Demand_20000.csv
   ```

3. **Commit and push** your changes:
   ```bash
   git add .
   git commit -m "Initial commit: Dairy forecasting application"
   git push origin main
   ```

### Step 2: Deploy on Render

#### Option A: Using render.yaml (Recommended)

1. **Log in to Render Dashboard**
   - Go to [dashboard.render.com](https://dashboard.render.com)
   - Sign in with your account

2. **Create New Web Service**
   - Click "New +" button
   - Select "Web Service"
   - Connect your GitHub repository

3. **Configure the Service**
   - **Name**: `dairy-forecasting` (or your preferred name)
   - **Environment**: `Python 3`
   - **Region**: Choose closest to your users
   - **Branch**: `main` (or your default branch)
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `streamlit run app.py --server.port $PORT --server.address 0.0.0.0`

4. **Advanced Settings** (Optional)
   - **Auto-Deploy**: Enable for automatic deployments
   - **Health Check Path**: `/`
   - **Environment Variables**: Add if needed

5. **Create Service**
   - Click "Create Web Service"
   - Render will automatically build and deploy your application

#### Option B: Manual Configuration

If you prefer not to use `render.yaml`:

1. **Follow steps 1-2** from Option A
2. **Manual Configuration**:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `streamlit run app.py --server.port $PORT --server.address 0.0.0.0`
   - **Environment**: Python 3
   - **Plan**: Free (or choose paid plan for better performance)

### Step 3: Verify Deployment

1. **Monitor Build Process**
   - Watch the build logs in Render dashboard
   - Ensure all dependencies install successfully

2. **Test the Application**
   - Once deployed, click on your service URL
   - Verify all features work correctly:
     - Dashboard loads
     - Data visualizations display
     - Forecasting models train
     - Optimization recommendations show

3. **Check Logs**
   - Monitor application logs for any errors
   - Address any issues that arise

## 🔍 Troubleshooting

### Common Issues

#### 1. Build Failures
**Problem**: Build fails during dependency installation
**Solution**:
- Check `requirements.txt` for version conflicts
- Ensure all packages are compatible
- Try updating package versions

#### 2. Application Won't Start
**Problem**: Application fails to start after successful build
**Solution**:
- Check the start command is correct
- Verify `app.py` exists and is properly formatted
- Check application logs for specific errors

#### 3. Data Loading Issues
**Problem**: Application can't load the CSV file
**Solution**:
- Ensure `Dairy_Supply_Demand_20000.csv` is in the repository
- Check file permissions
- Verify file path in `app.py`

#### 4. Memory Issues
**Problem**: Application runs out of memory
**Solution**:
- Upgrade to a paid Render plan with more memory
- Optimize the application code
- Reduce dataset size if possible

### Performance Optimization

1. **Enable Caching**
   - The app already uses `@st.cache_data` for data loading
   - Consider additional caching for expensive computations

2. **Optimize Dependencies**
   - Remove unused packages from `requirements.txt`
   - Use lighter alternatives where possible

3. **Data Processing**
   - Consider preprocessing data before deployment
   - Use efficient data structures

## 🔄 Continuous Deployment

### Automatic Deployments
- Enable auto-deploy in Render settings
- Every push to main branch triggers deployment
- Monitor deployment status

### Manual Deployments
- Use "Manual Deploy" option for testing
- Deploy specific branches or commits
- Rollback to previous versions if needed

## 📊 Monitoring

### Health Checks
- Render automatically checks application health
- Monitor uptime and response times
- Set up alerts for downtime

### Logs
- Access application logs in Render dashboard
- Monitor for errors and performance issues
- Use logs for debugging

## 🔧 Environment Variables

If you need to add environment variables:

1. **In Render Dashboard**:
   - Go to your service settings
   - Add environment variables as needed
   - Common variables:
     - `PYTHON_VERSION`: `3.9.0`
     - `STREAMLIT_SERVER_PORT`: `$PORT`

2. **In Application**:
   ```python
   import os
   port = os.environ.get('PORT', 8501)
   ```

## 🚀 Scaling

### Free Plan Limitations
- 750 hours per month
- 512 MB RAM
- Shared CPU
- Sleep after 15 minutes of inactivity

### Upgrading
- Choose paid plan for better performance
- More RAM and CPU resources
- No sleep mode
- Custom domains

## 📞 Support

### Render Support
- [Render Documentation](https://render.com/docs)
- [Render Community](https://community.render.com)
- [Render Status](https://status.render.com)

### Application Issues
- Check application logs
- Review error messages
- Test locally first
- Create GitHub issues for bugs

## ✅ Deployment Checklist

- [ ] All files committed to GitHub
- [ ] `requirements.txt` includes all dependencies
- [ ] `app.py` runs locally without errors
- [ ] CSV file is in repository
- [ ] Render service created successfully
- [ ] Build completes without errors
- [ ] Application starts and loads correctly
- [ ] All features work as expected
- [ ] Health checks pass
- [ ] Application accessible via URL

## 🎉 Success!

Once deployed, your application will be available at:
```
https://your-app-name.onrender.com
```

Share this URL with stakeholders and start using your dairy forecasting application!

---

**Need Help?** Check the troubleshooting section or contact Render support. 