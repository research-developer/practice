"""Simple Flask API for the practice project."""

from flask import Flask, request, jsonify
from practice.calculator import calculate
from practice.utils import format_timestamp

app = Flask(__name__)


@app.route("/")
def home():
    """Home endpoint."""
    return jsonify({"message": "Practice API", "version": "0.1.0", "timestamp": format_timestamp()})


@app.route("/health")
def health():
    """Health check endpoint."""
    return jsonify({"status": "healthy", "timestamp": format_timestamp()})


@app.route("/calculate", methods=["POST"])
def calculate_endpoint():
    """Calculate endpoint for performing arithmetic operations.

    Expected JSON body:
    {
        "operation": "add|subtract|multiply|divide",
        "a": number,
        "b": number
    }
    """
    data = request.get_json()

    if not data:
        return jsonify({"error": "No JSON data provided"}), 400

    operation = data.get("operation")
    a = data.get("a")
    b = data.get("b")

    if not all([operation, a is not None, b is not None]):
        return jsonify({"error": "Missing required fields: operation, a, b"}), 400

    try:
        result = calculate(operation, a, b)
        return jsonify(
            {
                "operation": operation,
                "operands": {"a": a, "b": b},
                "result": result,
                "timestamp": format_timestamp(),
            }
        )
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": f"Internal error: {str(e)}"}), 500


@app.route("/operations")
def operations():
    """List available operations."""
    from practice.utils import list_operations

    return jsonify({"operations": list_operations(), "timestamp": format_timestamp()})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
