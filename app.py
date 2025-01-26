from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def dashboard():
    # Sample data to display on the dashboard
    metrics = {
        'total_sales': 5000,
        'inventory_items': 120,
        'active_users': 15,
        'vendors': 20,
        'refunds': 50,
        'low_stock_items': 3,
        'total_transactions': 350,
        'pending_orders': 5,
        'daily_revenue': 500
    }
    return render_template('index.html', metrics=metrics)


@app.route('/inventory')
def inventory():
    return "<h2>Inventory Management</h2>"

@app.route('/sales')
def sales():
    return "<h2>Sales Data</h2>"

@app.route('/users')
def users():
    return "<h2>User Management</h2>"

@app.route('/reports')
def reports():
    return "<h2>Reports</h2>"

if __name__ == '__main__':
    app.run(debug=True)
