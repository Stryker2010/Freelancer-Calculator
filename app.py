from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Main Price Calculator endpoint
@app.route('/calculate-main-price', methods=['POST'])
def calculate_main_price():
    estimated_costs = float(request.form['estimated_costs'])
    hourly_rate = float(request.form['hourly_rate'])
    hours_worked = float(request.form['hours_worked'])
    profit_margin = float(request.form['profit_margin'])

    total_price = (estimated_costs + (hourly_rate * hours_worked)) * (1 + profit_margin / 100)
    return jsonify({"result": f"Total Price: {total_price:.2f}"})

# Hourly Rate Calculator endpoint
@app.route('/calculate-hourly-rate', methods=['POST'])
def calculate_hourly_rate():
    total_costs = float(request.form['total_costs'])
    desired_income = float(request.form['desired_income'])
    working_hours = float(request.form['working_hours'])

    hourly_rate = (total_costs + desired_income) / working_hours
    return jsonify({"result": f"Hourly Rate: {hourly_rate:.2f}"})

# Elasticity of Demand Calculator endpoint
@app.route('/calculate-elasticity', methods=['POST'])
def calculate_elasticity():
    old_price = float(request.form['old_price'])
    new_price = float(request.form['new_price'])
    old_quantity = float(request.form['old_quantity'])
    new_quantity = float(request.form['new_quantity'])

    price_elasticity = ((new_quantity - old_quantity) / old_quantity) / ((new_price - old_price) / old_price)
    return jsonify({"result": f"Price Elasticity of Demand: {price_elasticity:.2f}"})

if __name__ == '__main__':
    app.run(debug=True)
