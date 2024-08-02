from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/bfhl', methods=['GET', 'POST'])
def bfhl():
    if request.method == 'POST':
        data = request.get_json()
        full_name = "john_doe"
        dob = "17091999"
        user_id = f"{full_name}_{dob}"

        input_data = data.get('data', [])
        numbers = [str(x) for x in input_data if str(x).isdigit()]
        alphabets = [str(x).upper() for x in input_data if str(x).isalpha()]

        highest_alphabet = max(alphabets) if alphabets else None

        response = {
            "is_success": True,
            "user_id": user_id,
            "email": "john@xyz.com",
            "roll_number": "ABCD123",
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_alphabet": [highest_alphabet] if highest_alphabet else []
        }
        return jsonify(response), 200

    elif request.method == 'GET':
        response = {
            "operation_code": 1
        }
        return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)
