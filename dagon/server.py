"""
API server for Dagon AI
"""

from flask import Flask, request, jsonify
from dagon.enhanced import EnhancedDagonAI


app = Flask(__name__)
dagon = EnhancedDagonAI(model_name="gpt2")

# Configure personality
dagon.set_personality_trait("helpfulness", 0.95)
dagon.set_personality_trait("empathy", 0.85)


@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({"status": "healthy", "ai": "Dagon"})


@app.route('/chat', methods=['POST'])
def chat():
    """Chat endpoint"""
    try:
        data = request.get_json()
        user_input = data.get('message', '').strip()
        
        if not user_input:
            return jsonify({"error": "Message is required"}), 400
        
        response = dagon.chat(user_input)
        
        return jsonify({
            "success": True,
            "message": user_input,
            "response": response
        })
    
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


@app.route('/personality', methods=['GET'])
def get_personality():
    """Get personality profile"""
    return jsonify({
        "success": True,
        "personality": dagon.get_personality()
    })


@app.route('/personality', methods=['PUT'])
def set_personality():
    """Set personality trait"""
    try:
        data = request.get_json()
        trait = data.get('trait')
        value = data.get('value')
        
        if not trait or value is None:
            return jsonify({"error": "trait and value are required"}), 400
        
        dagon.set_personality_trait(trait, value)
        
        return jsonify({
            "success": True,
            "message": f"Set {trait} to {value}"
        })
    
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


@app.route('/statistics', methods=['GET'])
def get_statistics():
    """Get conversation statistics"""
    return jsonify({
        "success": True,
        "statistics": dagon.get_statistics()
    })


@app.route('/knowledge', methods=['POST'])
def add_knowledge():
    """Add knowledge to knowledge base"""
    try:
        data = request.get_json()
        domain = data.get('domain')
        key = data.get('key')
        value = data.get('value')
        
        if not all([domain, key, value]):
            return jsonify({"error": "domain, key, and value are required"}), 400
        
        dagon.add_knowledge(domain, key, value)
        
        return jsonify({
            "success": True,
            "message": "Knowledge added"
        })
    
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


@app.route('/memory', methods=['GET'])
def get_memories():
    """Get stored memories"""
    query = request.args.get('query')
    memories = dagon.recall_memories(query)
    
    return jsonify({
        "success": True,
        "memories": memories
    })


@app.route('/reset', methods=['POST'])
def reset_conversation():
    """Reset conversation"""
    dagon.reset_conversation()
    
    return jsonify({
        "success": True,
        "message": "Conversation reset"
    })


if __name__ == '__main__':
    app.run(debug=True, port=5000)
