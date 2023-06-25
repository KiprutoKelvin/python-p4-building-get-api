import pdb
from app import app

# Set a breakpoint at the desired location in your code
pdb.set_trace()

# Run your Flask application
app.run(port=5555, debug=True)