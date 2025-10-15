# MediClinic - Advanced Mobile Clinic Recommendation System

A comprehensive healthcare management system designed for mobile clinic operations, providing intelligent clinical decision support and patient management capabilities.

## Features

### 🏥 Patient Management
- Comprehensive patient intake and registration system
- Vital signs recording and tracking
- Symptom tracking with intuitive interface
- Patient history and records management

### 🤖 AI Recommendations
- Intelligent clinical decision support system
- Evidence-based treatment recommendations
- Symptom analysis and diagnosis assistance
- Real-time clinical guidance based on patient data

### 📊 Analytics Dashboard
- Healthcare analytics and insights
- Trend monitoring and outcome tracking
- Data-driven decision making tools
- Performance metrics and reporting

### 👥 Role-Based Access Control
- Admin dashboard for clinic management
- Staff dashboard for healthcare professionals
- Secure authentication and authorization
- User role management (Admin/Staff)

## Technology Stack

- **Backend**: Flask (Python web framework)
- **Database**: SQLite with SQLAlchemy ORM
- **Authentication**: Flask-Login with bcrypt password hashing
- **Forms**: Flask-WTF with WTForms validation
- **Frontend**: HTML5, CSS3, responsive design
- **Architecture**: Blueprint-based modular structure

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd CDSS
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv cdss
   # On Windows:
   cdss\Scripts\activate
   # On macOS/Linux:
   source cdss/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the root directory:
   ```
   SECRET_KEY=your-secret-key-here
   DATABASE_URL=sqlite:///cdss.sqlite
   ```

5. **Initialize the database**
   ```bash
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```

## Running the Application

1. **Activate the virtual environment**
   ```bash
   cdss\Scripts\activate  # Windows
   source cdss/bin/activate  # macOS/Linux
   ```

2. **Run the application**
   ```bash
   python run.py
   ```

3. **Access the application**
   Open your web browser and navigate to `http://127.0.0.1:5000`

## Application Structure

```
CDSS/
├── app/
│   ├── __init__.py          # Application factory
│   ├── models.py            # Database models
│   ├── forms.py             # WTForms definitions
│   ├── auth/                # Authentication blueprint
│   │   ├── __init__.py
│   │   └── routes.py        # Auth routes (login, register, logout)
│   ├── main/                # Main application blueprint
│   │   ├── __init__.py
│   │   └── routes.py        # Main routes (dashboards, landing)
│   ├── static/              # Static files (CSS, JS, images)
│   │   ├── css/
│   │   ├── js/
│   │   └── images/
│   ├── templates/           # HTML templates
│   │   ├── base.html
│   │   ├── dashboard_base.html
│   │   ├── index.html
│   │   ├── login.html
│   │   ├── register.html
│   │   ├── admin_dashboard.html
│   │   └── staff_dashboard.html
│   └── database/            # Database utilities
├── tests/                   # Test files
├── instance/                # Instance folder (database file)
├── migrations/              # Database migrations
├── run.py                   # Application entry point
├── config.py               # Configuration settings
└── requirements.txt        # Python dependencies
```

## Usage

### User Registration
1. Navigate to the registration page
2. Fill in your name, email, password, and select your role (Admin/Staff)
3. Submit the form to create your account

### User Login
1. Go to the login page
2. Enter your email and password
3. You'll be redirected to the appropriate dashboard based on your role

### Admin Features
- Access to admin dashboard
- Staff management capabilities
- System oversight and monitoring
- Inventory management
- Operations control

### Staff Features
- Staff dashboard access
- Patient registration and management
- Medical records updates
- AI-powered clinical recommendations
- Patient data viewing and analysis

## API Routes

### Authentication Routes (Blueprint: `auth`)
- `GET/POST /auth/login` - User login
- `GET/POST /auth/register` - User registration  
- `POST /auth/logout` - User logout

### Main Application Routes (Blueprint: `main`)
- `GET /` - Landing page
- `GET /dashboard` - General dashboard
- `GET /admin_dashboard` - Admin dashboard (admin only)
- `GET /staff_dashboard` - Staff dashboard (staff only)

## Security Features

- Password hashing using bcrypt
- Session management with Flask-Login
- CSRF protection with Flask-WTF
- Role-based access control
- Form validation and sanitization

## Development

### Running Tests
```bash
pytest tests/
```

### Database Migrations
```bash
# Create migration
flask db migrate -m "Description of changes"

# Apply migration
flask db upgrade
```

### Adding New Features
1. Create appropriate routes in the relevant blueprint (`auth` or `main`)
2. Add corresponding templates in the `templates/` directory
3. Update models if database changes are needed
4. Add forms in `forms.py` if new forms are required
5. Write tests for new functionality

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support and questions, please open an issue in the repository or contact the development team.