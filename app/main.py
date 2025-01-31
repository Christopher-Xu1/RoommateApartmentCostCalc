from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculate_rent():
    if request.method == 'POST':
        try:
            rent = float(request.form['rent'])
            totalsqft = float(request.form['totalsqft'])
            bedroomsqft = float(request.form['bedroomsqft'])
            roommates = int(request.form['roommates'])
            total_suitemates = int(request.form['total_suitemates'])
            
            price_per_sqft = rent / totalsqft
            communalsqft = totalsqft - bedroomsqft
            
            each_pays = rent * ((bedroomsqft / roommates + communalsqft) / (totalsqft * total_suitemates))
            
            return render_template('index.html', result=each_pays)
        except Exception as e:
            return render_template('index.html', error=str(e))
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
