# Tile and Carpet Solutions - QuickBooks Integration

This application provides automated QuickBooks integration for tile and carpet business operations.

## Features

- **Automated Banking**: Sync bank transfers, deposits, and payments
- **Sales Processing**: Record customer payments and Square transfers  
- **Financial Reporting**: Real-time sync of invoices and account balances
- **Loan Management**: Track business loan payments

## Deployment

### Vercel
1. Connect your GitHub repository to Vercel
2. Deploy with default settings
3. Add environment variables if needed

### Railway
1. Connect repository to Railway  
2. Deploy automatically with railway.json configuration
3. Health check available at `/health`

### Heroku
1. Create new Heroku app
2. Connect GitHub repository
3. Deploy from GitHub branch

## Required URLs for QuickBooks

- **Launch URL**: `https://your-domain.com/`
- **Privacy Policy**: `https://your-domain.com/privacy`
- **EULA**: `https://your-domain.com/eula`
- **OAuth Callback**: `https://your-domain.com/oauth/callback`
- **Disconnect URL**: `https://your-domain.com/disconnect`

## Environment Variables

- `SECRET_KEY`: Flask secret key for sessions
- `PORT`: Port number (automatically set by hosting platforms)

## Local Development

```bash
pip install -r requirements.txt
python app.py
```

Visit `http://localhost:5000` to view the application.

## Support

For technical support, contact: support@tilecarpetsolutions.com
