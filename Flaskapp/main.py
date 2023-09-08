from flask import Flask, request, jsonify

app = Flask(__name__)

# Your user info
user_info = {
    "full_name_ddmmyyyy": "vamsi_nallapuneni_17092002",
    "email": "vamsikrishna_nallapueni@srmap.edu.in",
    "roll_number": "AP20110010735"
}

@app.route('/bfhl', methods=['GET', 'POST'])
def bfhl():
    if request.method == 'POST':
        data = request.get_json()
        if 'data' in data and isinstance(data['data'], list):
            numbers = [str(x) for x in data['data'] if isinstance(x, int) or (isinstance(x, str) and x.isdigit())]
            alphabets = [str(x) for x in data['data'] if isinstance(x, str) and x.isalpha()]
            highest_alphabet = [max(alphabets, key=lambda x: x.lower())] if alphabets else []

            response = {
                "is_success": True,
                "user_id": user_info["full_name_ddmmyyyy"],
                "email": user_info["email"],
                "roll_number": user_info["roll_number"],
                "numbers": numbers,
                "alphabets": alphabets,
                "highest_alphabet": highest_alphabet
            }
            return jsonify(response), 200
        else:
            return jsonify({"is_success": False, "message": "Invalid input data"}), 400
    elif request.method == 'GET':
        response = {"operation_code": 1}
        return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)