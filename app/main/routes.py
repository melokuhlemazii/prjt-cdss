from flask import render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from app.main import bp

@bp.route('/')
def landing():
    return render_template("index.html")

@bp.route('/dashboard')
@login_required
def dashboard():
    return render_template("dashboard.html", user=current_user)

@bp.route('/admin_dashboard')
@login_required
def admin_dashboard():
    if current_user.role != 'admin':
        flash('Access denied: Admin only.', 'danger')
        return redirect(url_for('auth.login'))
    return render_template("admin_dashboard.html", user=current_user)

@bp.route('/staff_dashboard')
@login_required
def staff_dashboard():
    if current_user.role != 'staff':
        flash('Access denied: Staff only.', 'danger')
        return redirect(url_for('auth.login'))
    return render_template("staff_dashboard.html", user=current_user)



