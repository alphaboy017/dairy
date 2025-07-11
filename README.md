# 🥛 Dairy Supply & Demand Forecasting

A comprehensive web application for forecasting dairy supply and demand, optimizing capacity utilization, and providing actionable insights for dairy plant operations.

## 📋 Project Overview

This application addresses the critical challenge of maximizing processing, packaging, and storage capacity utilization in dairy plants. It provides:

- **Real-time Analytics Dashboard**: Monitor key performance indicators
- **Advanced Forecasting Models**: Predict future demand using multiple ML algorithms
- **Capacity Optimization**: Identify bottlenecks and optimization opportunities
- **Interactive Visualizations**: Explore data patterns and trends

## 🚀 Features

### 📊 Dashboard
- Key performance metrics (supply, demand, capacity utilization)
- Time series analysis of supply vs demand
- Equipment downtime monitoring
- Product-wise demand and inventory analysis

### 🔮 Forecasting
- Multiple ML models (Random Forest, XGBoost, LightGBM, etc.)
- 30-day demand forecasting
- Model performance comparison
- Interactive forecast visualization

### ⚙️ Optimization
- Capacity utilization analysis
- Downtime impact assessment
- Seasonal demand patterns
- Actionable optimization recommendations

### 📈 Advanced Analytics
- Correlation analysis between variables
- Distribution analysis
- Statistical summaries
- Trend identification

## 🛠️ Technology Stack

- **Frontend**: Streamlit
- **Backend**: Python
- **Machine Learning**: Scikit-learn, XGBoost, LightGBM
- **Data Visualization**: Plotly, Matplotlib, Seaborn
- **Time Series**: Prophet, Statsmodels
- **Deployment**: Render

## 📦 Installation

### Local Development

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd dairy-forecasting
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run app.py
   ```

4. **Access the application**
   Open your browser and go to `http://localhost:8501`

### Docker Deployment

1. **Build the Docker image**
   ```bash
   docker build -t dairy-forecasting .
   ```

2. **Run the container**
   ```bash
   docker run -p 8501:8501 dairy-forecasting
   ```

## 🌐 Deployment on Render

### Prerequisites
- Render account
- GitHub repository with the project

### Deployment Steps

1. **Connect to Render**
   - Log in to Render dashboard
   - Click "New +" and select "Web Service"
   - Connect your GitHub repository

2. **Configure the service**
   - **Name**: `dairy-forecasting`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `streamlit run app.py --server.port $PORT --server.address 0.0.0.0`

3. **Environment Variables** (if needed)
   - Add any required environment variables in the Render dashboard

4. **Deploy**
   - Click "Create Web Service"
   - Render will automatically build and deploy your application

## 📊 Dataset

The application uses a comprehensive dairy dataset containing:
- **20,000+ records** of daily operations
- **Date range**: 2020-2024
- **Variables**:
  - Milk supply (liters)
  - Product demands (500ml milk, 1L milk, butter, cheese, yogurt)
  - Inventory levels
  - Equipment downtime
  - Derived efficiency metrics

## 🔧 Configuration

### Model Parameters
- **Forecast Period**: 30 days (configurable)
- **Test Split**: 20% for model validation
- **Models**: Random Forest, XGBoost, LightGBM, Gradient Boosting, Linear Regression

### Performance Metrics
- **MAE**: Mean Absolute Error
- **RMSE**: Root Mean Square Error
- **R²**: Coefficient of Determination

## 📈 Key Insights

### Capacity Utilization
- **Optimal Range**: 70-85%
- **Current Average**: Calculated from data
- **Improvement Opportunities**: Identified through analysis

### Demand Patterns
- **Seasonal Variations**: Monthly and quarterly patterns
- **Product Mix**: Relative demand for different products
- **Forecast Accuracy**: Model performance metrics

### Optimization Recommendations
- **Low Utilization**: Implement demand forecasting and flexible production
- **High Downtime**: Preventive maintenance and operator training
- **Demand Variability**: Safety stock strategies and flexible scheduling

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Support

For support and questions:
- Create an issue in the GitHub repository
- Contact the development team

## 🔄 Updates

### Version 1.0.0
- Initial release with core forecasting functionality
- Dashboard with key metrics
- Multiple ML model support
- Interactive visualizations
- Capacity optimization recommendations

---

**Built with ❤️ for the dairy industry** 