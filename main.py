from flask import Flask


if __name__== "__main__":
  app = Flask(__name__)
  
  
  @app.route('/')
  def index():
      return 'Hello from Flask!'
  
  
  app.run(host='0.0.0.0', port=81)
