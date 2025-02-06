from flask import Flask, request, jsonify
import logging

@app.route('/')
def home():
    return "Welcome to the LinkedIn AI Agent!"

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.route('/start-agent', methods=['POST'])
def start_agent():
    try:
        logging.info("Received request to start AI agent")
        # Here, you would start the AI agent process
        # For example, calling a function that starts the agent
        # start_ai_agent()
    return jsonify({"status": "AI agent started"}), 200    rn jsonify({"status": "AI agent started"}), 200
    
    except Exception as e:
        logging.er    return jsonify({"status": "AI agent started"}), 200(f"Error starting AI agent: {e}")
        return jsonify({"error": str(e)}), 500

@app.route('/log', methods=['GET'])
def get_log():
    try:
        logging.info("Received request for action log")
        # Here, you would retrieve the log entries
        # For example, reading from a log file or database
        # log_entries = get_log_entries()
        log_entries = ["Sample log entry 1", "Sample log entry 2"]
        return jsonify({"log": log_entries}), 200
    except Exception as e:
        logging.error(f"Error retrieving log: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
