import logging
from flask import Flask, request, render_template
import os

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/', defaults={'filename': 'file1.txt'}, methods=['GET'])
@app.route('/<filename>', methods=['GET'])
def read_file(filename):
    start_line = request.args.get('start', type=int)
    end_line = request.args.get('end', type=int)
    error_message = None

    try:
        file_path = os.path.join('files', filename)
        logger.info(f"Reading file: {file_path}")

        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File '{filename}' not found in the 'files' directory.")

        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            logger.info(f"Read {len(lines)} lines from file: {file_path}")
        
        if start_line is not None and end_line is not None:
            if start_line < 1 or end_line < 1:
                raise ValueError("start_line and end_line must be greater than or equal to 1.")
            elif start_line > len(lines) or end_line > len(lines):
                raise ValueError("start_line or end_line is greater than the number of lines in the file.")
            elif start_line > end_line:
                raise ValueError("start_line must be less than or equal to end_line.")
            
            lines = lines[start_line - 1:end_line]

        return render_template('display.html', content=''.join(lines), error_message=error_message)
    except (FileNotFoundError, ValueError) as e:
        error_message = str(e)
        logger.error(f"Error: {error_message}")
    except Exception as e:
        error_message = str(e)
        logger.exception(f"Unhandled exception: {error_message}")

    return render_template('error.html', error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True)
